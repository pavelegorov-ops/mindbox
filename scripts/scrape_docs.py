"""Scrape MindBox help docs into a Markdown knowledge base for Claude Code.

Source: https://help.mindbox.ru/docs/ (Diplodoc Platform).
Re-run anytime; only changed pages are rewritten thanks to content hashing.

Output layout (under --out, default `docs/`):
    CLAUDE.md          Onboarding for Claude Code on how to use this corpus.
    INDEX.md           Hierarchical index built from the site's TOC.
    manifest.json      Per-slug content hashes + timestamps for incremental sync.
    pages/<slug>.md    One Markdown file per documentation page, with frontmatter.

Internal links between pages are rewritten to local `<slug>.md` so Claude can
follow them via the Read tool.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import html as htmlmod
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx
from markdownify import markdownify as md

# Allow running this script directly (`python scripts/scrape_docs.py`) as well
# as via the sync.py orchestrator — _common lives next to it.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    DEPRECATION_MARKERS,
    RU_TO_LAT,
    atomic_write_text,
    compute_removed_slugs,
    detect_deprecation,
    extract_lead,
    format_fetch_error,
    load_manifest_strict,
    page_filename,
    redact_secrets,
    render_frontmatter,
    to_yaml_scalar,
)

BASE = "https://help.mindbox.ru/docs"
TOC_URL = f"{BASE}/toc.js"
USER_AGENT = "mindbox-docs-scraper/1.0 (+Claude Code knowledge sync)"
DEFAULT_CONCURRENCY = 10
TIMEOUT = httpx.Timeout(30.0, connect=10.0)

# Bump when the on-disk page file format changes. A mismatch with manifest's
# stored value forces a rewrite of every page so older files pick up new
# frontmatter fields even when upstream content_hash hasn't changed.
OUTPUT_FORMAT_VERSION = 2

# Pattern for extracting internal-link targets *before* the rewrite step.
# Captures both `/docs/<slug>` (absolute) and bare `<slug>.html` (relative).
INTERNAL_LINK_RE = re.compile(
    r'(?:href|src)="(?:/docs/([^"#]+)|((?!https?:|mailto:|tel:|#|/)[^"]+\.html))(?:#[^"]*)?"',
)

DIPLODOC_STATE_RE = re.compile(
    r'<script type="application/json" id="diplodoc-state">(.*?)</script>',
    re.DOTALL,
)
TOC_ASSIGN_RE = re.compile(
    r"window\.__DATA__\.data\.toc\s*=\s*(.*);\s*$", re.DOTALL
)
# Diplodoc prepends a permalink <a class="yfm-anchor">...</a> inside every heading,
# duplicating the heading text. Strip these before Markdown conversion.
YFM_ANCHOR_RE = re.compile(
    r'<a\b[^>]*\bclass="yfm-anchor"[^>]*>.*?</a>',
    re.DOTALL,
)


@dataclass
class PageRef:
    slug: str
    toc_title: str
    toc_path: list[str]


@dataclass
class FetchedPage:
    ref: PageRef
    title: str
    body_html: str  # raw, html-unescaped
    headings: list[dict]
    vcs_path: str | None
    content_hash: str


@dataclass
class SyncStats:
    added: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)
    deprecation_flagged: list[tuple[str, list[str]]] = field(default_factory=list)
    section_indexes_written: int = 0
    section_indexes_removed: list[str] = field(default_factory=list)


def parse_toc(js_text: str) -> dict:
    m = TOC_ASSIGN_RE.search(js_text)
    if not m:
        raise ValueError("toc.js: assignment 'window.__DATA__.data.toc = ...' not found")
    return json.loads(m.group(1))


def collect_pages(toc: dict) -> list[PageRef]:
    """Walk the TOC tree and return a deduplicated list of page references.

    Breadcrumb is the chain of `name` fields of ancestor groups. The same page
    can appear under several groups (TOC cross-links); we keep the first path.
    """
    seen: dict[str, PageRef] = {}

    def walk(node: Any, breadcrumb: list[str]) -> None:
        if isinstance(node, dict):
            href = node.get("href")
            name = node.get("name") or node.get("title")
            if isinstance(href, str) and not href.startswith(("http://", "https://", "mailto:", "tel:")):
                slug_part = href.split("#", 1)[0]
                if slug_part.endswith(".html"):
                    slug = slug_part[: -len(".html")]
                else:
                    slug = slug_part
                slug = slug.strip("/")
                if slug and slug != "index" and slug not in seen:
                    seen[slug] = PageRef(slug=slug, toc_title=name or slug, toc_path=list(breadcrumb))
            child_breadcrumb = breadcrumb + [name] if name else breadcrumb
            items = node.get("items")
            if isinstance(items, list):
                walk(items, child_breadcrumb)
        elif isinstance(node, list):
            for child in node:
                walk(child, breadcrumb)

    walk(toc.get("items", []), [])
    return list(seen.values())


def extract_state(html_text: str) -> dict:
    m = DIPLODOC_STATE_RE.search(html_text)
    if not m:
        raise ValueError("diplodoc-state script tag not found")
    return json.loads(m.group(1))


def rewrite_internal_links(html_text: str) -> str:
    """Rewrite `/docs/<slug>` and `<slug>.html` hrefs to `<slug>.md` for local navigation."""

    def repl_abs(match: re.Match) -> str:
        attr, sep, rest = match.group(1), match.group(2), match.group(3)
        # rest is everything after `/docs/` up to the closing quote (matched by re)
        slug_part, _, anchor = rest.partition("#")
        slug_part = slug_part.removesuffix(".html").strip("/")
        if not slug_part or slug_part == "index":
            target = "../INDEX.md"
        else:
            target = f"{slug_part}.md"
        if anchor:
            target += f"#{anchor}"
        return f'{attr}={sep}{target}{sep}'

    # absolute /docs/... links
    html_text = re.sub(
        r'(href|src)=(["\'])/docs/([^"\']*)\2',
        repl_abs,
        html_text,
    )

    def repl_rel(match: re.Match) -> str:
        attr, sep, rest = match.group(1), match.group(2), match.group(3)
        slug_part, _, anchor = rest.partition("#")
        slug_part = slug_part.removesuffix(".html").strip("/")
        if not slug_part:
            return match.group(0)
        target = f"{slug_part}.md"
        if anchor:
            target += f"#{anchor}"
        return f'{attr}={sep}{target}{sep}'

    # bare relative `<slug>.html` (no scheme, no leading slash)
    html_text = re.sub(
        r'(href)=(["\'])(?!https?:|mailto:|tel:|#|/)([^"\']+\.html(?:#[^"\']*)?)\2',
        repl_rel,
        html_text,
    )
    return html_text


def html_to_markdown(body_html_unescaped: str) -> str:
    cleaned = YFM_ANCHOR_RE.sub("", body_html_unescaped)
    rewritten = rewrite_internal_links(cleaned)
    text = md(
        rewritten,
        heading_style="ATX",
        bullets="-",
        code_language="",
        escape_underscores=False,
        escape_asterisks=False,
    )
    # collapse 3+ blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def flatten_headings(headings_tree: list, max_depth: int = 2, limit: int = 12) -> list[str]:
    """Flatten Diplodoc's headings tree to a list of titles, capped at max_depth/limit."""
    out: list[str] = []

    def walk(items: list, depth: int) -> None:
        for h in items or []:
            if not isinstance(h, dict) or len(out) >= limit:
                return
            title = (h.get("title") or "").strip()
            if title:
                out.append(title)
            if depth < max_depth:
                walk(h.get("items") or [], depth + 1)

    walk(headings_tree or [], 1)
    return out


def slugify_section(name: str) -> str:
    out: list[str] = []
    for ch in name.lower():
        if ch in RU_TO_LAT:
            out.append(RU_TO_LAT[ch])
        elif ch.isalnum() and ord(ch) < 128:
            out.append(ch)
        else:
            out.append("-")
    s = re.sub(r"-+", "-", "".join(out)).strip("-")
    return s or "section"


def extract_link_target_slugs(body_html_unescaped: str) -> set[str]:
    """Find all internal doc slugs this page links to (before link rewrite)."""
    slugs: set[str] = set()
    for m in INTERNAL_LINK_RE.finditer(body_html_unescaped):
        raw = m.group(1) or m.group(2) or ""
        slug = raw.split("#", 1)[0]
        if slug.endswith(".html"):
            slug = slug[: -len(".html")]
        slug = slug.strip("/")
        if slug and slug != "index":
            slugs.add(slug)
    return slugs


@dataclass
class PageArtifacts:
    body_md: str
    hints: list[str]
    lead: str
    headings_flat: list[str]
    outbound_slugs: list[str]


def build_artifacts(page: "FetchedPage", known_slugs: set[str]) -> PageArtifacts:
    body_md = html_to_markdown(page.body_html)
    hints = detect_deprecation(page.title + "\n" + body_md)
    lead = extract_lead(body_md)
    headings_flat = flatten_headings(page.headings)
    outbound = extract_link_target_slugs(page.body_html) & known_slugs
    outbound.discard(page.ref.slug)
    return PageArtifacts(
        body_md=body_md,
        hints=hints,
        lead=lead,
        headings_flat=headings_flat,
        outbound_slugs=sorted(outbound),
    )


def page_source_url(slug: str) -> str:
    return f"{BASE}/{slug}"


async def fetch_text(client: httpx.AsyncClient, url: str) -> str:
    r = await client.get(url, follow_redirects=True)
    r.raise_for_status()
    # Diplodoc serves UTF-8; httpx may guess latin-1 if charset is missing
    if r.encoding is None or r.encoding.lower() == "iso-8859-1":
        r.encoding = "utf-8"
    return r.text


async def fetch_page(client: httpx.AsyncClient, ref: PageRef) -> FetchedPage:
    text = await fetch_text(client, page_source_url(ref.slug))
    state = extract_state(text)
    data = state.get("data", {})
    raw_body = data.get("html", "") or ""
    body_html = redact_secrets(htmlmod.unescape(raw_body))
    title = data.get("title") or ref.toc_title
    headings = data.get("headings") or []
    vcs_path = (data.get("meta") or {}).get("vcsPath")
    content_hash = "sha256:" + hashlib.sha256(body_html.encode("utf-8")).hexdigest()
    return FetchedPage(
        ref=ref,
        title=title,
        body_html=body_html,
        headings=headings,
        vcs_path=vcs_path,
        content_hash=content_hash,
    )


def write_page_file(
    pages_dir: Path,
    page: FetchedPage,
    fetched_at: str,
    artifacts: PageArtifacts,
) -> None:
    meta = {
        "title": page.title,
        "slug": page.ref.slug,
        "source_url": page_source_url(page.ref.slug),
        "vcs_path": page.vcs_path or "",
        "toc_path": page.ref.toc_path,
        "fetched_at": fetched_at,
        "content_hash": page.content_hash,
    }
    if artifacts.hints:
        meta["deprecation_hint"] = artifacts.hints
    text = render_frontmatter(meta) + "\n# " + page.title + "\n\n" + artifacts.body_md
    (pages_dir / page_filename(page.ref.slug)).write_text(text, encoding="utf-8")


def _slug_from_href(href: Any) -> str | None:
    if not isinstance(href, str) or href.startswith(("http://", "https://", "mailto:", "tel:")):
        return None
    s = href.split("#", 1)[0]
    if s.endswith(".html"):
        s = s[: -len(".html")]
    s = s.strip("/")
    return s if s and s != "index" else None


def _render_tree_items(
    items: list,
    slug_to_title: dict[str, str],
    *,
    pages_prefix: str,
    out: list[str],
) -> None:
    """Shared TOC subtree renderer. depth 0 → '##', depth 1 → '###', deeper → bullets."""

    def render_node(node: dict, depth: int) -> None:
        name = node.get("name") or node.get("title") or ""
        slug = _slug_from_href(node.get("href"))
        children = node.get("items") if isinstance(node.get("items"), list) else []

        if depth <= 1 and children:
            hashes = "#" * (depth + 2)
            if slug:
                title = slug_to_title.get(slug, name) or slug
                out.append(f"{hashes} [{title}]({pages_prefix}{page_filename(slug)})")
            elif name:
                out.append(f"{hashes} {name}")
            out.append("")
            for child in children:
                if isinstance(child, dict):
                    render_node(child, depth + 1)
            out.append("")
            return

        indent = "  " * max(0, depth - 2)
        if slug:
            title = slug_to_title.get(slug, name) or slug
            out.append(f"{indent}- [{title}]({pages_prefix}{page_filename(slug)})")
        elif name:
            out.append(f"{indent}- **{name}**")
        for child in children:
            if isinstance(child, dict):
                render_node(child, depth + 1)

    for top in items or []:
        if isinstance(top, dict):
            render_node(top, 0)


def render_index(toc: dict, slug_to_title: dict[str, str]) -> str:
    """Render INDEX.md preserving the TOC hierarchy.

    Top-level groups become `##`, second-level groups become `###`, deeper
    groups appear as bold bullet items, leaf pages are bullet links. Hybrid
    nodes (group with their own page) render as a linked heading.
    """
    out: list[str] = [
        "# MindBox Help — Index",
        "",
        f"Source: <{BASE}/>",
        "",
        "Hierarchy mirrors the official site navigation. Each leaf links to the",
        "local Markdown copy under `pages/`.",
        "",
        "Per-section indexes (lighter than this file) live in `index/`. Use",
        "`summaries.json` for fast, grep-based topic triage.",
        "",
    ]
    _render_tree_items(toc.get("items", []), slug_to_title, pages_prefix="pages/", out=out)
    return "\n".join(out).rstrip() + "\n"


def render_section_index(
    section_node: dict,
    slug_to_title: dict[str, str],
) -> str:
    """Render a single top-level TOC section as a standalone Markdown index."""
    name = section_node.get("name") or section_node.get("title") or "Section"
    out: list[str] = [
        f"# {name}",
        "",
        f"Section index — part of <{BASE}/>.",
        f"Pages live under `../pages/`. Full TOC: [INDEX.md](../INDEX.md).",
        "",
    ]
    _render_tree_items(
        section_node.get("items") or [],
        slug_to_title,
        pages_prefix="../pages/",
        out=out,
    )
    return "\n".join(out).rstrip() + "\n"


def write_section_indexes(
    out_dir: Path,
    toc: dict,
    slug_to_title: dict[str, str],
) -> tuple[list[str], list[str]]:
    """Write `docs/index/<section-slug>.md` for each top-level TOC group.

    Returns (written_filenames, removed_filenames).
    """
    index_dir = out_dir / "index"
    index_dir.mkdir(exist_ok=True)
    written: set[str] = set()
    used_slugs: dict[str, int] = {}
    for section in toc.get("items", []):
        if not isinstance(section, dict):
            continue
        name = section.get("name") or section.get("title") or "section"
        base_slug = slugify_section(name)
        # Disambiguate identical slugs across sections.
        n = used_slugs.get(base_slug, 0)
        slug = base_slug if n == 0 else f"{base_slug}-{n + 1}"
        used_slugs[base_slug] = n + 1
        text = render_section_index(section, slug_to_title)
        (index_dir / f"{slug}.md").write_text(text, encoding="utf-8")
        written.add(f"{slug}.md")

    # Clean up stale section files.
    removed: list[str] = []
    for existing in index_dir.glob("*.md"):
        if existing.name not in written:
            existing.unlink()
            removed.append(existing.name)
    return sorted(written), sorted(removed)


def write_summaries(
    out_dir: Path,
    summaries: dict[str, dict],
    *,
    generated_at: str,
) -> None:
    payload = {
        "generated_at": generated_at,
        "source": BASE,
        "page_count": len(summaries),
        "schema": {
            "fields": ["slug", "title", "section", "subsection", "lead", "headings", "deprecation_hint"],
            "purpose": "lightweight per-page cards for topic triage; grep this before reading full pages",
        },
        "pages": dict(sorted(summaries.items())),
    }
    (out_dir / "summaries.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_backlinks(
    out_dir: Path,
    outbound_map: dict[str, list[str]],
    *,
    generated_at: str,
) -> None:
    backlinks: dict[str, list[str]] = {}
    for src, targets in outbound_map.items():
        for tgt in targets:
            backlinks.setdefault(tgt, []).append(src)
    backlinks = {k: sorted(set(v)) for k, v in backlinks.items()}
    payload = {
        "generated_at": generated_at,
        "source": BASE,
        "page_count": len(backlinks),
        "schema": {
            "purpose": "reverse link index: which pages link to a given slug",
            "format": "<slug>: [<slug_that_links_to_it>, ...]",
        },
        "backlinks": dict(sorted(backlinks.items())),
    }
    (out_dir / "backlinks.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


CLAUDE_MD = """# MindBox Help — local mirror

This folder is a local Markdown mirror of <https://help.mindbox.ru/docs/>,
maintained by `scrape_docs.py` at the repo root.

## Layout

- `pages/<slug>.md` — one file per docs page. Filename matches the canonical
  slug used by the upstream site, so you can guess paths from URLs:
  `https://help.mindbox.ru/docs/<slug>` ↔ `pages/<slug>.md`.
- `summaries.json` — per-page cards (title, section, lead paragraph,
  headings, deprecation_hint). **Grep this first** when triaging a topic; it
  is far cheaper than reading multiple full pages.
- `index/<section-slug>.md` — per-section table of contents. Lighter than
  `INDEX.md` (~5 KB vs ~100 KB). Pick one when the user asks about a
  specific area (e.g. "сегменты", "лояльность").
- `INDEX.md` — full hierarchical table of contents. Useful when you really
  need the whole tree, but expensive in tokens — prefer `index/` or
  `summaries.json` for most lookups.
- `backlinks.json` — reverse link index: `<slug> → [slugs that link to it]`.
  Use to find related pages without grepping the whole corpus.
- `manifest.json` — bookkeeping for incremental sync (per-page content hash,
  fetched timestamp). Don't edit manually.

## Recommended lookup workflow

For "what does MindBox say about X?" questions:

1. `Grep "X" docs/summaries.json -B 1 -A 4` → ranked candidates with their
   leads and headings, ~600 tokens output.
2. Read the most relevant `pages/<slug>.md` in full.
3. Optionally `Grep '"<slug>"' docs/backlinks.json -A 8` → related pages.

For "give me an overview of section Y":

1. Find the matching file in `docs/index/` (transliterated slug, e.g.
   `segmenty.md`, `loyalnost-i-akcii.md`).
2. Read it directly — it's already scoped to that section.

## Per-page format

Every page begins with YAML frontmatter:

```yaml
---
title: <human-readable title>
slug: <stable upstream slug>
source_url: https://help.mindbox.ru/docs/<slug>
vcs_path: <slug>.md             # path of the original Markdown in MindBox's repo
toc_path: ["Section", "Subsection", ...]
fetched_at: 2026-05-04T...Z
content_hash: sha256:...
deprecation_hint: ["устарел", ...]   # OPTIONAL — see below
---
```

Body is the article rendered to Markdown. Internal links between docs are
rewritten to relative `<slug>.md`, so `Read` works for navigation.

### `deprecation_hint`

Present **only** when the page body contains substrings such as `устарел`,
`устаревш`, `больше не работа`, `больше не поддержив`, `не используется`,
`старый интерфейс`, `старая версия`, `deprecated`, `прекращ`, `снят с
поддержки`, or `архивн`. The value is the list of matched markers in the
order they appear in the detection list.

**How to use:** when answering from a page that has `deprecation_hint`, add a
brief caveat that the underlying feature may be deprecated/legacy and link
the user to the canonical `source_url` for confirmation. To list all flagged
pages quickly:

```bash
grep -l '^deprecation_hint:' docs/pages/*.md
```

## How to use as a knowledge source

- **Topic search**: `Grep` over `pages/*.md`. Filenames are slugs, often
  descriptive enough to narrow with `Glob` first
  (e.g. `pages/*segment*.md`).
- **Browse by area**: open `INDEX.md` and follow links.
- **Cite back to canonical source**: the `source_url` in frontmatter is the
  live page on help.mindbox.ru.
- **Freshness**: check `fetched_at` in frontmatter, or the top-level
  `generated_at` in `manifest.json`. Re-run `python scrape_docs.py` to refresh.

## Refreshing

```bash
python scrape_docs.py            # incremental: re-fetches all, rewrites only changed
python scrape_docs.py --full     # force-rewrite every file
python scrape_docs.py --dry-run  # report what would change, write nothing
```

The script reports added / updated / unchanged / removed pages on each run.
Removed pages (slugs that disappeared from the upstream TOC) are deleted from
`pages/`; recover from git if needed.
"""


def save_manifest(path: Path, toc_hash: str, pages: dict[str, dict]) -> None:
    payload = {
        "version": 1,
        "format_version": OUTPUT_FORMAT_VERSION,
        "source": BASE,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "toc_hash": toc_hash,
        "page_count": len(pages),
        "pages": dict(sorted(pages.items())),
    }
    atomic_write_text(
        path,
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )


async def run(args: argparse.Namespace) -> int:
    out_dir = Path(args.out)
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    manifest = load_manifest_strict(manifest_path)
    old_pages: dict[str, dict] = manifest.get("pages", {})
    old_format = manifest.get("format_version", 1)
    format_changed = old_format != OUTPUT_FORMAT_VERSION
    if format_changed and old_pages:
        print(
            f"      output format upgrade detected ({old_format} -> {OUTPUT_FORMAT_VERSION}); "
            "all pages will be rewritten.",
            flush=True,
        )

    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient(headers=headers, timeout=TIMEOUT, http2=False) as client:
        print(f"[1/3] Fetching TOC: {TOC_URL}", flush=True)
        toc_js = await fetch_text(client, TOC_URL)
        toc = parse_toc(toc_js)
        toc_hash = "sha256:" + hashlib.sha256(toc_js.encode("utf-8")).hexdigest()

        refs = collect_pages(toc)
        print(f"      TOC parsed: {len(refs)} pages.", flush=True)

        sem = asyncio.Semaphore(args.concurrency)
        stats = SyncStats()
        new_pages: dict[str, dict] = {}
        summaries: dict[str, dict] = {}
        outbound_map: dict[str, list[str]] = {}
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        slug_to_title: dict[str, str] = {}
        known_slugs: set[str] = {r.slug for r in refs}

        async def worker(ref: PageRef) -> None:
            async with sem:
                try:
                    page = await fetch_page(client, ref)
                except Exception as exc:  # noqa: BLE001
                    stats.failed.append(
                        (ref.slug, format_fetch_error(exc, url=page_source_url(ref.slug)))
                    )
                    return
                slug_to_title[ref.slug] = page.title
                old = old_pages.get(ref.slug)
                changed = (old is None) or (old.get("content_hash") != page.content_hash)
                target = pages_dir / page_filename(ref.slug)

                if old is None:
                    stats.added.append(ref.slug)
                elif changed:
                    stats.updated.append(ref.slug)
                else:
                    stats.unchanged.append(ref.slug)

                artifacts = build_artifacts(page, known_slugs)
                outbound_map[ref.slug] = artifacts.outbound_slugs

                summaries[ref.slug] = {
                    "slug": ref.slug,
                    "title": page.title,
                    "section": ref.toc_path[0] if ref.toc_path else "",
                    "subsection": ref.toc_path[1] if len(ref.toc_path) > 1 else "",
                    "lead": artifacts.lead,
                    "headings": artifacts.headings_flat,
                    "deprecation_hint": artifacts.hints,
                }

                # Always (re)write on --full or when changed, or when target file
                # is missing (manifest may have drifted from disk), or when the
                # output format version changed.
                must_write = args.full or changed or not target.exists() or format_changed
                if must_write and not args.dry_run:
                    write_page_file(pages_dir, page, fetched_at, artifacts)
                if artifacts.hints:
                    stats.deprecation_flagged.append((ref.slug, artifacts.hints))

                entry = {
                    "title": page.title,
                    "source_url": page_source_url(ref.slug),
                    "vcs_path": page.vcs_path or "",
                    "toc_path": ref.toc_path,
                    "content_hash": page.content_hash,
                    "fetched_at": fetched_at if must_write else (old or {}).get("fetched_at", fetched_at),
                }
                if artifacts.hints:
                    entry["deprecation_hint"] = artifacts.hints
                new_pages[ref.slug] = entry

        print(f"[2/3] Fetching {len(refs)} pages (concurrency={args.concurrency})...", flush=True)
        await asyncio.gather(*(worker(r) for r in refs))

        # Detect removals. See compute_removed_slugs for the why — short
        # version: a failed fetch must NOT cause file deletion.
        removed_slugs, preserved_failed = compute_removed_slugs(
            old_slugs=set(old_pages),
            new_slugs=set(new_pages),
            failed_slugs={slug for slug, _ in stats.failed},
        )
        for slug in removed_slugs:
            stats.removed.append(slug)
            target = pages_dir / page_filename(slug)
            if target.exists() and not args.dry_run:
                target.unlink()
        for slug in preserved_failed:
            new_pages[slug] = old_pages[slug]

        if not args.dry_run:
            print(
                "[3/3] Writing INDEX.md, index/<section>.md, summaries.json, "
                "backlinks.json, CLAUDE.md, manifest.json...",
                flush=True,
            )
            (out_dir / "INDEX.md").write_text(render_index(toc, slug_to_title), encoding="utf-8")
            (out_dir / "CLAUDE.md").write_text(CLAUDE_MD, encoding="utf-8")
            written, removed = write_section_indexes(out_dir, toc, slug_to_title)
            stats.section_indexes_written = len(written)
            stats.section_indexes_removed = removed
            write_summaries(out_dir, summaries, generated_at=fetched_at)
            write_backlinks(out_dir, outbound_map, generated_at=fetched_at)
            save_manifest(manifest_path, toc_hash, new_pages)
        else:
            print("[3/3] Dry run: skipping writes.", flush=True)

    print()
    print("Summary:")
    print(f"  added:     {len(stats.added)}")
    print(f"  updated:   {len(stats.updated)}")
    print(f"  unchanged: {len(stats.unchanged)}")
    print(f"  removed:   {len(stats.removed)}")
    print(f"  failed:    {len(stats.failed)}")
    print(f"  flagged (deprecation_hint): {len(stats.deprecation_flagged)}")
    print(f"  section indexes written: {stats.section_indexes_written}")
    if stats.section_indexes_removed:
        print(f"  section indexes removed (stale): {len(stats.section_indexes_removed)}")
        for n in stats.section_indexes_removed:
            print(f"    - {n}")
    if stats.added:
        for s in stats.added[:20]:
            print(f"    + {s}")
        if len(stats.added) > 20:
            print(f"    ... and {len(stats.added) - 20} more")
    if stats.updated:
        for s in stats.updated[:20]:
            print(f"    ~ {s}")
        if len(stats.updated) > 20:
            print(f"    ... and {len(stats.updated) - 20} more")
    if stats.removed:
        for s in stats.removed:
            print(f"    - {s}")
    if stats.failed:
        for slug, err in stats.failed[:20]:
            print(f"    ! {slug}: {err}")
        preserved_count = len(set(s for s, _ in stats.failed) & set(old_pages))
        if preserved_count:
            print(
                f"  preserved {preserved_count} previously-known page(s) "
                f"despite fetch failure (file kept on disk)."
            )

    return 1 if stats.failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="docs", help="output directory (default: docs)")
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"parallel page fetches (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument("--full", action="store_true", help="rewrite every page even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing files")
    args = parser.parse_args()
    try:
        return asyncio.run(run(args))
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
