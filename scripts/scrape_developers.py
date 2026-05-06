"""Scrape MindBox *developer* docs into a Markdown knowledge base for Claude Code.

Source: https://developers.mindbox.ru/docs/ (Zudoku-powered docs site).
Re-run anytime; only changed pages are rewritten thanks to content hashing.

Output layout (under --out, default `developers/`):
    CLAUDE.md          Onboarding for Claude Code on how to use this corpus.
    INDEX.md           Hierarchical index built from the per-page sidebar.
    manifest.json      Per-slug content hashes + timestamps for incremental sync.
    pages/<slug>.md    One Markdown file per documentation page, with frontmatter.
    summaries.json     Lightweight per-page cards for fast topic triage.
    backlinks.json     Reverse link index.
    index/<sect>.md    Per-section table of contents.

Discovery strategy: the site exposes pagefind, which already lists every page
and its anchors (h1/h2/h3). We download the gzipped meta + per-page fragment
files to enumerate all URLs without crawling. Each page is then fetched once
to grab the SSR'd HTML, the breadcrumb is read from the open chain in the
left sidebar, and the article body is converted to Markdown.

Internal links between pages are rewritten to local `<slug>.md` so Claude can
follow them via the Read tool.
"""

from __future__ import annotations

import argparse
import asyncio
import gzip
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
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Silence the noisy InsecureRequestWarning that httpx (via httpcore) emits
# when verify=False. The default is verify=False — see argparse below.
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
try:
    import urllib3  # type: ignore[import-not-found]

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except Exception:  # noqa: BLE001
    pass

ORIGIN = "https://developers.mindbox.ru"
BASE = f"{ORIGIN}/docs"
PAGEFIND_ENTRY = f"{ORIGIN}/pagefind/pagefind-entry.json"
USER_AGENT = "mindbox-developer-docs-scraper/1.0 (+Claude Code knowledge sync)"
DEFAULT_CONCURRENCY = 10
TIMEOUT = httpx.Timeout(30.0, connect=10.0)

OUTPUT_FORMAT_VERSION = 3

DEPRECATION_MARKERS = [
    "устарел",
    "устаревш",
    "больше не работа",
    "больше не поддержив",
    "не используется",
    "старый интерфейс",
    "старая версия",
    "deprecated",
    "прекращ",
    "снят с поддержки",
    "архивн",
]

RU_TO_LAT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}

# Internal link discovery (for the backlinks index): match both relative
# `/docs/<slug>` and absolute `https://developers.mindbox.ru/docs/<slug>` —
# Zudoku emits the latter for cross-page links with cyrillic (URL-encoded)
# slugs.
INTERNAL_LINK_RE = re.compile(
    r'(?:href|src)="(?:https?://developers\.mindbox\.ru)?/docs/([^"#?]+)(?:#[^"]*)?"',
)

PAGEFIND_MAGIC = b"pagefind_dcd"


@dataclass
class PageRef:
    slug: str
    pagefind_title: str  # title from pagefind meta (may differ from on-page <h1>)
    anchors: list[dict]  # raw anchor list from pagefind


@dataclass
class FetchedPage:
    ref: PageRef
    title: str  # from <title> tag
    body_html: str  # raw prose div, html-unescaped, with permalinks/svgs removed
    breadcrumb: list[str]  # section chain from open sidebar entries
    headings: list[dict]  # filtered anchor list from pagefind (h1-h3)
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


# ---------- pagefind discovery ----------

_TRANSIENT_EXC = (
    httpx.RemoteProtocolError,
    httpx.ReadTimeout,
    httpx.ConnectTimeout,
    httpx.ConnectError,
    httpx.ReadError,
    httpx.WriteError,
    httpx.PoolTimeout,
)


async def _request_with_retry(
    client: httpx.AsyncClient, url: str, *, attempts: int = 3
) -> httpx.Response:
    last_exc: Exception | None = None
    for i in range(attempts):
        try:
            r = await client.get(url, follow_redirects=True)
            r.raise_for_status()
            return r
        except _TRANSIENT_EXC as exc:
            last_exc = exc
            await asyncio.sleep(0.5 * (2 ** i))
        except httpx.HTTPStatusError:
            raise  # don't retry 4xx/5xx
    assert last_exc is not None
    raise last_exc


async def fetch_bytes(client: httpx.AsyncClient, url: str) -> bytes:
    r = await _request_with_retry(client, url)
    return r.content


async def fetch_text(client: httpx.AsyncClient, url: str) -> str:
    r = await _request_with_retry(client, url)
    if r.encoding is None or r.encoding.lower() == "iso-8859-1":
        r.encoding = "utf-8"
    return r.text


def gunzip(data: bytes) -> bytes:
    return gzip.decompress(data)


def parse_fragment(raw: bytes) -> dict:
    """Parse a pagefind .pf_fragment payload (gzipped, magic prefix + JSON)."""
    if not raw.startswith(PAGEFIND_MAGIC):
        raise ValueError("missing pagefind_dcd magic")
    payload = raw[len(PAGEFIND_MAGIC):]
    i = payload.index(b"{")
    return json.loads(payload[i:].decode("utf-8"))


async def discover_pages(client: httpx.AsyncClient, concurrency: int) -> list[PageRef]:
    """Use the pagefind index to enumerate every doc URL + title + headings."""
    entry = json.loads(await fetch_text(client, PAGEFIND_ENTRY))
    languages = entry.get("languages", {})
    if not languages:
        raise RuntimeError("pagefind-entry.json has no languages")
    # site is single-language ("en" container even though content is RU)
    lang_code, lang_info = next(iter(languages.items()))
    lang_hash = lang_info["hash"]
    print(f"      pagefind language: {lang_code} ({lang_hash}), {lang_info.get('page_count')} pages", flush=True)

    meta_url = f"{ORIGIN}/pagefind/pagefind.{lang_hash}.pf_meta"
    meta_blob = gunzip(await fetch_bytes(client, meta_url))
    # Fragment hashes look like en_xxxxxxx (7 hex)
    hash_prefix = lang_code + "_"
    hash_re = re.compile(rf"{re.escape(hash_prefix)}[0-9a-f]{{7}}".encode())
    raw_hashes = [h.decode("ascii") for h in hash_re.findall(meta_blob)]
    fragment_hashes = sorted(set(raw_hashes))
    print(f"      pagefind: {len(fragment_hashes)} unique fragment hashes", flush=True)

    sem = asyncio.Semaphore(concurrency)
    refs_by_slug: dict[str, PageRef] = {}
    skipped_fragments = 0

    async def fetch_one(h: str) -> None:
        nonlocal skipped_fragments
        async with sem:
            url = f"{ORIGIN}/pagefind/fragment/{h}.pf_fragment"
            try:
                blob = gunzip(await fetch_bytes(client, url))
                obj = parse_fragment(blob)
            except httpx.HTTPStatusError:
                # Pagefind's meta sometimes references shard hashes that aren't
                # served. Counting them is enough; per-hash logs are too noisy.
                skipped_fragments += 1
                return
            except Exception as exc:  # noqa: BLE001
                print(f"      ! fragment {h}: {exc!r}", flush=True)
                return
            page_url = obj.get("url") or ""
            if not page_url.startswith("/docs/"):
                return
            slug = page_url[len("/docs/"):].strip("/")
            if not slug or slug == "index":
                return
            # Take first occurrence per slug (pagefind may shard long pages
            # across multiple fragments; later ones cover the same URL).
            if slug in refs_by_slug:
                return
            meta = obj.get("meta") or {}
            title = (meta.get("title") or "").strip() or slug
            anchors = obj.get("anchors") or []
            refs_by_slug[slug] = PageRef(
                slug=slug,
                pagefind_title=title,
                anchors=anchors,
            )

    await asyncio.gather(*(fetch_one(h) for h in fragment_hashes))
    if skipped_fragments:
        print(f"      pagefind: {skipped_fragments} fragment hash(es) returned 404 (ignored)", flush=True)
    return sorted(refs_by_slug.values(), key=lambda r: r.slug)


# ---------- HTML extraction from a doc page ----------

# Permalink anchors next to headings: <a class="..." aria-label="Link to ...">...</a>
PERMALINK_ANCHOR_RE = re.compile(
    r'<a\b[^>]*\baria-label="Link to [^"]*"[^>]*>[\s\S]*?</a>',
)
# Strip all SVG icons (chevrons, copy/edit buttons)
SVG_RE = re.compile(r"<svg\b[\s\S]*?</svg>")
# The "Copy page" / dropdown button-group appearing right after <h1>
HEADER_BUTTON_GROUP_RE = re.compile(
    r'<div role="group"[^>]*data-slot="button-group"[^>]*>[\s\S]*?</header>',
)
# Last-modified row at the bottom of the article
LAST_MODIFIED_RE = re.compile(
    r'<div class="flex justify-between text-xs text-muted-foreground[\s\S]*?<time[\s\S]*?</div>\s*</div>\s*</div>',
)
# Prev/next link bar at the bottom (rendered as flex-wrap chips)
PREVNEXT_RE = re.compile(
    r'<div class="flex flex-wrap gap-2[^"]*"[^>]*data-pagefind-ignore="all"[^>]*>[\s\S]*?</div>\s*</div>',
)
# The horizontal divider after the last-modified line
HR_DIVIDER_RE = re.compile(
    r'<div class="h-px bg-border[^"]*"[^>]*></div>',
)
# Empty spacer divs that markdownify sometimes preserves as blank lines
EMPTY_SPACER_RE = re.compile(
    r'<div class="h-(?:8|16|24|px)[^"]*"[^>]*></div>',
)


def extract_main_html(html: str) -> str | None:
    """Return the innerHTML of <main data-pagefind-body="true">, or None."""
    m = re.search(r'<main\b[^>]*data-pagefind-body="true"[^>]*>', html)
    if not m:
        return None
    start = m.end()
    depth = 1
    i = start
    j = start
    while i < len(html) and depth > 0:
        nm = re.search(r'</?main\b', html[i:])
        if not nm:
            return None
        j = i + nm.start()
        if html[j : j + 5] == "<main":
            depth += 1
        else:
            depth -= 1
        i = j + nm.end() - nm.start()
    return html[start:j]


def extract_prose_html(main_html: str) -> str | None:
    """Return the inner content of the .prose article div, sliced before the right-hand sidecar."""
    m = re.search(r'<div\b[^>]*class="prose[^"]*\btypography\b[^"]*"[^>]*>', main_html)
    if not m:
        return None
    body = main_html[m.end():]
    # The prose div ends before the sidecar (right-hand on-this-page nav)
    end_m = re.search(r'<div class="hidden xl:block"', body)
    if end_m:
        body = body[: end_m.start()]
    # Trim trailing closing div(s) of prose
    return body


def extract_breadcrumb(html: str) -> list[str]:
    """Walk the SSR sidebar and return the chain of section names whose open
    collapsibles enclose the link with `aria-current="page"`.

    Sidebar shape (Radix Collapsible):

        <nav class="hidden ...">
            ...
            <div data-state="open">
                <button aria-expanded="true" data-state="open">
                    <div>...<div>SECTION_NAME</div>...</div>
                </button>
                <div data-state="open" id="..."><ul>... children ...</ul></div>
            </div>
            ...
        </nav>

    The current page is rendered as `<a aria-current="page" ...>`. We find that
    anchor, then walk up its ancestors collecting the visible label of every
    enclosing open collapsible header.
    """
    nav_start = html.find('<nav class="hidden')
    if nav_start == -1:
        return []
    end_m = re.search(r"</nav>", html[nav_start:])
    if not end_m:
        return []
    nav_html = html[nav_start : nav_start + end_m.start()] + "</nav>"

    soup = BeautifulSoup(nav_html, "html.parser")
    current = soup.find(attrs={"aria-current": "page"})
    if current is None:
        return []

    breadcrumb: list[str] = []
    # Each Radix Collapsible renders as:
    #     <div data-state="open">                    ← wrapper
    #         <a/button aria-expanded="true">LABEL</a/button>   ← header
    #         <div data-state="open" id="radix-..."><ul>...</ul></div>  ← body
    # The current page lives inside a body. Walk up through the wrappers and
    # for each one read the label from its header (a direct child element
    # with aria-expanded="true").
    for node in current.parents:
        attrs = getattr(node, "attrs", None) or {}
        if attrs.get("data-state") != "open":
            continue
        # Only act on the wrapper, not the body. Bodies have id="radix-..."
        # and contain a <ul>; wrappers contain the header element.
        if attrs.get("id", "").startswith("radix-"):
            continue
        # Find the header child with aria-expanded="true". `recursive=False`
        # to avoid descending into nested collapsibles.
        header = node.find(
            lambda tag: tag is not None
            and tag.has_attr("aria-expanded")
            and tag.get("aria-expanded") == "true",
            recursive=False,
        )
        if header is None:
            continue
        if header is current:
            continue  # current page's own header — title, not a breadcrumb step
        label = _label_for_header(header)
        if label:
            breadcrumb.append(label)

    breadcrumb.reverse()
    return breadcrumb


def _label_for_header(header) -> str:
    """Extract the visible section name from a Radix Collapsible header element.

    Two shapes occur in the wild:
      1. <button>...<div class="...truncate...">LABEL</div>...</button>
      2. <a href="..."><span title="LABEL">LABEL</span>...</a>  (page-and-section)
    """
    label_div = header.find("div", class_=lambda c: c and "truncate" in c)
    if label_div is not None:
        text = label_div.get_text(strip=True)
        if text:
            return text
    span = header.find("span", attrs={"title": True})
    if span is not None:
        text = span.get("title", "").strip() or span.get_text(strip=True)
        if text:
            return text
    return header.get_text(strip=True)


def extract_title(html: str) -> str:
    m = re.search(r"<title[^>]*>([\s\S]*?)</title>", html)
    if m:
        return htmlmod.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
    return ""


def filter_anchors(anchors: list[dict]) -> list[dict]:
    """Keep only h1-h3 from pagefind anchors, preserving order."""
    out: list[dict] = []
    for a in anchors:
        if not isinstance(a, dict):
            continue
        elem = a.get("element") or ""
        if elem in {"h1", "h2", "h3"}:
            text = (a.get("text") or "").strip()
            if text:
                out.append({"level": elem, "text": text})
    return out


def clean_prose_html(prose_html: str) -> str:
    """Strip Zudoku/Radix scaffolding so markdownify produces clean Markdown.

    Removed: header (h1 + breadcrumb chip + Copy-page button-group), prev/next
    nav at the bottom, last-modified line, decorative SVGs, in-heading
    permalink anchors, code-block toolbars (language label + copy button).
    Tab UI: tab triggers (the row of buttons) are dropped; each tabpanel has
    its label injected as a `### Label` heading so panels stay distinguishable
    once flattened.
    """
    s = prose_html
    # Cheap regex passes for whole-block removals
    s = re.sub(r"<header\b[^>]*>[\s\S]*?</header>", "", s, count=1)
    s = PREVNEXT_RE.sub("", s)
    s = LAST_MODIFIED_RE.sub("", s)
    s = HR_DIVIDER_RE.sub("", s)
    s = EMPTY_SPACER_RE.sub("", s)
    s = PERMALINK_ANCHOR_RE.sub("", s)
    s = SVG_RE.sub("", s)
    s = re.sub(
        r'<div class="text-sm font-semibold text-primary"[^>]*>[^<]*</div>',
        "",
        s,
    )

    # Structural cleanup with bs4 (tabs, code-block toolbars).
    soup = BeautifulSoup(s, "html.parser")

    # Tabs: collect trigger labels per tablist by aria-controls → label, then
    # drop the trigger row entirely and prepend each panel with its heading.
    triggers: dict[str, str] = {}
    for trig in soup.find_all(attrs={"role": "tab"}):
        controls = trig.get("aria-controls")
        if controls:
            label = trig.get_text(strip=True)
            if label:
                triggers[controls] = label
    for tablist in soup.find_all(attrs={"role": "tablist"}):
        tablist.decompose()
    for panel in soup.find_all(attrs={"role": "tabpanel"}):
        # Strip `hidden` so even inactive panels render in MD (we want the full
        # content surface for grep/Claude).
        if panel.has_attr("hidden"):
            del panel["hidden"]
        label = triggers.get(panel.get("id", ""))
        if label:
            new_h = soup.new_tag("h4")
            new_h.string = label
            panel.insert(0, new_h)

    # Code-block toolbar lives next to the <code> element. Zudoku wraps each
    # block as either:
    #   <pre><div><div>LABEL +copy</div><div><code>...</code></div></pre>
    # or:
    #   <pre><div>LABEL +copy</div><div><code>...</code></div></pre>
    # Find each <code>'s pre ancestor, and from that pre's descendants drop
    # the first sibling div that does NOT contain <code>.
    for pre in soup.find_all("pre"):
        code_el = pre.find("code")
        if code_el is None:
            continue
        # Toolbar = the deepest div that's a sibling of code's wrapper and
        # contains no <code>. We delete every such div under <pre>.
        for div in list(pre.find_all("div", recursive=True)):
            if div.find("code") is None and div.find_parent("pre") is pre:
                # Only delete leaves (no nested div with code) — safe because
                # any wrapper div that contains code would have div.find("code")
                # return non-None and be skipped.
                div.decompose()

    return str(soup)


# ---------- HTML → Markdown ----------

_ABS_DEV_DOCS_RE = re.compile(
    r'(href|src)=(["\'])(?:https?://developers\.mindbox\.ru)?/docs/([^"\']*)\2',
)
_DOC_REF_RE = re.compile(r'(href|src)=(["\'])doc:([^"\']*)\2')


def rewrite_internal_links(html: str, alias_to_slug: dict[str, str] | None = None) -> str:
    """Rewrite `/docs/<slug>` (relative or absolute) and `doc:<slug>` hrefs to
    `<slug>.md`.

    Slugs may be URL-encoded cyrillic (Zudoku rewrites cross-page links to
    %-encoded form when the slug contains non-ASCII). We unquote so the local
    filename matches the on-disk slug exactly. If `alias_to_slug` is provided,
    cyrillic-text aliases are mapped to their canonical (pagefind) slugs so
    cross-page links land on real files.
    """
    from urllib.parse import unquote

    aliases = alias_to_slug or {}

    def resolve(slug: str) -> str:
        return aliases.get(slug, slug)

    def _normalize_slug(s: str) -> str:
        s = unquote(s).strip("/")
        s = s.removesuffix(".html").removesuffix(".md")
        return s

    def repl_docs(match: re.Match) -> str:
        attr, sep, rest = match.group(1), match.group(2), match.group(3)
        slug_part, _, anchor = rest.partition("#")
        slug_part = _normalize_slug(slug_part)
        if not slug_part or slug_part == "index":
            target = "../INDEX.md"
        else:
            target = f"{resolve(slug_part)}.md"
        if anchor:
            target += f"#{unquote(anchor)}"
        return f"{attr}={sep}{target}{sep}"

    def repl_docref(match: re.Match) -> str:
        attr, sep, rest = match.group(1), match.group(2), match.group(3)
        slug_part, _, anchor = rest.partition("#")
        slug_part = _normalize_slug(slug_part)
        if not slug_part:
            return match.group(0)
        target = f"{resolve(slug_part)}.md"
        if anchor:
            target += f"#{unquote(anchor)}"
        return f"{attr}={sep}{target}{sep}"

    html = _ABS_DEV_DOCS_RE.sub(repl_docs, html)
    html = _DOC_REF_RE.sub(repl_docref, html)
    return html


def html_to_markdown(
    prose_html_unescaped: str,
    alias_to_slug: dict[str, str] | None = None,
) -> str:
    rewritten = rewrite_internal_links(prose_html_unescaped, alias_to_slug)
    text = md(
        rewritten,
        heading_style="ATX",
        bullets="-",
        code_language="",
        escape_underscores=False,
        escape_asterisks=False,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# ---------- summaries / leads / backlinks ----------

_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_MD_ITALIC_RE = re.compile(r"(?<!\w)[*_]([^*_\n]+)[*_](?!\w)")
_MD_CODE_RE = re.compile(r"`([^`]+)`")
_WS_RE = re.compile(r"\s+")


def _strip_markdown_inlines(s: str) -> str:
    s = _MD_IMAGE_RE.sub("", s)
    s = _MD_LINK_RE.sub(r"\1", s)
    s = _MD_BOLD_RE.sub(r"\1", s)
    s = _MD_ITALIC_RE.sub(r"\1", s)
    s = _MD_CODE_RE.sub(r"\1", s)
    return _WS_RE.sub(" ", s).strip()


def extract_lead(body_md: str, max_chars: int = 240) -> str:
    paragraphs: list[str] = []
    buf: list[str] = []
    for line in body_md.splitlines():
        if line.strip():
            buf.append(line)
        elif buf:
            paragraphs.append(" ".join(buf).strip())
            buf = []
    if buf:
        paragraphs.append(" ".join(buf).strip())

    for raw in paragraphs:
        if raw.startswith(("#", ">", "```", "- ", "* ", "+ ", "|")):
            continue
        clean = _strip_markdown_inlines(raw)
        if len(clean) < 20:
            continue
        if len(clean) <= max_chars:
            return clean
        cut = clean[:max_chars]
        sp = cut.rfind(" ")
        if sp > max_chars * 0.6:
            cut = cut[:sp]
        return cut.rstrip(" ,.;:—-") + "…"
    return ""


def detect_deprecation(text: str) -> list[str]:
    low = text.lower()
    return [m for m in DEPRECATION_MARKERS if m in low]


def extract_link_target_slugs(prose_html: str) -> set[str]:
    from urllib.parse import unquote

    slugs: set[str] = set()
    # Pull both `(href|src)="/docs/..."` (covered by INTERNAL_LINK_RE) and the
    # `doc:<slug>` short form Zudoku uses for cross-references.
    for m in INTERNAL_LINK_RE.finditer(prose_html):
        slugs.add(unquote(m.group(1).split("#", 1)[0]))
    for m in re.finditer(r'(?:href|src)="doc:([^"#?]+)', prose_html):
        slugs.add(unquote(m.group(1)))
    cleaned: set[str] = set()
    for slug in slugs:
        if slug.endswith(".html"):
            slug = slug[: -len(".html")]
        if slug.endswith(".md"):
            slug = slug[: -len(".md")]
        slug = slug.strip("/")
        if slug and slug != "index":
            cleaned.add(slug)
    return cleaned


# ---------- TOC tree (built bottom-up from breadcrumbs) ----------

@dataclass
class TocNode:
    name: str
    children: dict[str, "TocNode"] = field(default_factory=dict)
    pages: list[tuple[str, str]] = field(default_factory=list)  # (title, slug)


def build_toc(slug_to_breadcrumb: dict[str, list[str]], slug_to_title: dict[str, str]) -> TocNode:
    root = TocNode(name="")
    # Stable insertion order: alphabetic by slug ensures runs are deterministic.
    for slug in sorted(slug_to_breadcrumb.keys()):
        crumb = slug_to_breadcrumb[slug]
        node = root
        for part in crumb:
            child = node.children.get(part)
            if child is None:
                child = TocNode(name=part)
                node.children[part] = child
            node = child
        node.pages.append((slug_to_title.get(slug, slug), slug))
    # Sort pages alphabetically by title within each node.
    def sort_node(n: TocNode) -> None:
        n.pages.sort(key=lambda p: p[0].lower())
        for ch in n.children.values():
            sort_node(ch)
    sort_node(root)
    return root


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


def render_toc_tree(node: TocNode, *, depth: int, pages_prefix: str, out: list[str]) -> None:
    """Render TOC subtree to Markdown. depth 0 → '##', 1 → '###', 2+ → bullets."""
    for child_name in node.children:
        child = node.children[child_name]
        if depth <= 1:
            hashes = "#" * (depth + 2)
            out.append(f"{hashes} {child_name}")
            out.append("")
            for title, slug in child.pages:
                out.append(f"- [{title}]({pages_prefix}{page_filename(slug)})")
            if child.pages:
                out.append("")
            render_toc_tree(child, depth=depth + 1, pages_prefix=pages_prefix, out=out)
        else:
            indent = "  " * (depth - 2)
            out.append(f"{indent}- **{child_name}**")
            for title, slug in child.pages:
                out.append(f"{indent}  - [{title}]({pages_prefix}{page_filename(slug)})")
            render_toc_tree(child, depth=depth + 1, pages_prefix=pages_prefix, out=out)
    if depth == 0 and node.pages:
        # Top-level orphan pages (no breadcrumb) — list them under "Other"
        out.append("## (Без раздела)")
        out.append("")
        for title, slug in node.pages:
            out.append(f"- [{title}]({pages_prefix}{page_filename(slug)})")
        out.append("")


def render_index(toc: TocNode) -> str:
    out: list[str] = [
        "# MindBox Developers — Index",
        "",
        f"Source: <{BASE}/>",
        "",
        "Hierarchy is reconstructed from each page's left-sidebar breadcrumb",
        "(Zudoku reveals only the open chain, so the tree is the union of all",
        "fetched pages). Each leaf links to the local Markdown copy under `pages/`.",
        "",
        "Per-section indexes (lighter than this file) live in `index/`. Use",
        "`summaries.json` for fast, grep-based topic triage.",
        "",
    ]
    render_toc_tree(toc, depth=0, pages_prefix="pages/", out=out)
    return "\n".join(out).rstrip() + "\n"


def render_section_index(name: str, node: TocNode) -> str:
    out: list[str] = [
        f"# {name}",
        "",
        f"Section index — part of <{BASE}/>.",
        "Pages live under `../pages/`. Full TOC: [INDEX.md](../INDEX.md).",
        "",
    ]
    for title, slug in node.pages:
        out.append(f"- [{title}](../pages/{page_filename(slug)})")
    if node.pages:
        out.append("")
    render_toc_tree(node, depth=1, pages_prefix="../pages/", out=out)
    return "\n".join(out).rstrip() + "\n"


def write_section_indexes(out_dir: Path, toc: TocNode) -> tuple[list[str], list[str]]:
    index_dir = out_dir / "index"
    index_dir.mkdir(exist_ok=True)
    written: set[str] = set()
    used_slugs: dict[str, int] = {}
    for name, node in toc.children.items():
        base = slugify_section(name)
        n = used_slugs.get(base, 0)
        slug = base if n == 0 else f"{base}-{n + 1}"
        used_slugs[base] = n + 1
        text = render_section_index(name, node)
        (index_dir / f"{slug}.md").write_text(text, encoding="utf-8")
        written.add(f"{slug}.md")

    removed: list[str] = []
    for existing in index_dir.glob("*.md"):
        if existing.name not in written:
            existing.unlink()
            removed.append(existing.name)
    return sorted(written), sorted(removed)


# ---------- frontmatter / file IO ----------

def to_yaml_scalar(value: Any) -> str:
    if isinstance(value, str):
        if value == "" or re.search(r'[:#\-?&*!|>\'"%@`,\[\]\{\}\n]', value) or value.strip() != value:
            return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
        return value
    if isinstance(value, (int, float, bool)):
        return json.dumps(value)
    raise TypeError(f"unsupported scalar: {type(value)!r}")


def render_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {to_yaml_scalar(item)}")
        else:
            lines.append(f"{k}: {to_yaml_scalar(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def page_filename(slug: str) -> str:
    return slug.replace("/", "_").replace("\\", "_") + ".md"


def page_source_url(slug: str) -> str:
    return f"{BASE}/{slug}"


@dataclass
class PageArtifacts:
    body_md: str
    hints: list[str]
    lead: str
    headings_flat: list[str]
    outbound_slugs: list[str]


def build_artifacts(
    page: FetchedPage,
    known_slugs: set[str],
    alias_to_slug: dict[str, str] | None = None,
) -> PageArtifacts:
    cleaned = clean_prose_html(page.body_html)
    body_md = html_to_markdown(cleaned, alias_to_slug)
    hints = detect_deprecation(page.title + "\n" + body_md)
    lead = extract_lead(body_md)
    headings_flat = [h["text"] for h in page.headings if h["level"] in {"h1", "h2", "h3"}][:12]
    raw_outbound = extract_link_target_slugs(page.body_html)
    aliases = alias_to_slug or {}
    resolved = {aliases.get(s, s) for s in raw_outbound} & known_slugs
    resolved.discard(page.ref.slug)
    return PageArtifacts(
        body_md=body_md,
        hints=hints,
        lead=lead,
        headings_flat=headings_flat,
        outbound_slugs=sorted(resolved),
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
        "breadcrumb": page.breadcrumb,
        "fetched_at": fetched_at,
        "content_hash": page.content_hash,
    }
    if artifacts.hints:
        meta["deprecation_hint"] = artifacts.hints
    text = render_frontmatter(meta) + "\n# " + page.title + "\n\n" + artifacts.body_md
    (pages_dir / page_filename(page.ref.slug)).write_text(text, encoding="utf-8")


# ---------- summaries / backlinks / manifest ----------

def write_summaries(out_dir: Path, summaries: dict[str, dict], *, generated_at: str) -> None:
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


def write_backlinks(out_dir: Path, outbound_map: dict[str, list[str]], *, generated_at: str) -> None:
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


CLAUDE_MD = """# MindBox Developers — local mirror

This folder is a local Markdown mirror of <https://developers.mindbox.ru/docs/>,
maintained by `scrape_developers.py` at the repo root.

## Layout

- `pages/<slug>.md` — one file per docs page. Filename matches the canonical
  slug used by the upstream site, so you can guess paths from URLs:
  `https://developers.mindbox.ru/docs/<slug>` ↔ `pages/<slug>.md`.
- `summaries.json` — per-page cards (title, section, lead paragraph,
  headings, deprecation_hint). **Grep this first** when triaging a topic; it
  is far cheaper than reading multiple full pages.
- `index/<section-slug>.md` — per-section table of contents. Lighter than
  `INDEX.md`. Pick one when the user asks about a specific area
  (e.g. "сегментации", "промокоды", "карты").
- `INDEX.md` — full hierarchical table of contents reconstructed from
  per-page sidebars.
- `backlinks.json` — reverse link index: `<slug> → [slugs that link to it]`.
- `manifest.json` — bookkeeping for incremental sync (per-page content hash,
  fetched timestamp, breadcrumb). Don't edit manually.

## Scope

This corpus targets *integrators / engineers*. For product help (UI walk-throughs
for marketers, segments, campaigns), see the sibling `docs/` corpus mirroring
help.mindbox.ru.

## Recommended lookup workflow

For "how do I integrate X with the MindBox API?" questions:

1. `Grep "X" developers/summaries.json -B 1 -A 4` → ranked candidates with
   their leads and headings.
2. Read the most relevant `pages/<slug>.md` in full.
3. Optionally `Grep '"<slug>"' developers/backlinks.json -A 8` → related pages.

For "give me an overview of section Y":

1. Find the matching file in `developers/index/` (transliterated slug).
2. Read it directly — it's already scoped to that section.

## Per-page format

Every page begins with YAML frontmatter:

```yaml
---
title: <title from <title> tag>
slug: <stable upstream slug>
source_url: https://developers.mindbox.ru/docs/<slug>
breadcrumb: ["Section", "Subsection", ...]   # from sidebar open chain
fetched_at: 2026-05-04T...Z
content_hash: sha256:...
deprecation_hint: ["устарел", ...]   # OPTIONAL — see below
---
```

### `deprecation_hint`

Present **only** when the body or title contains substrings such as
`устарел`, `больше не работа`, `deprecated`, `прекращ`, etc.

**How to use:** add a brief caveat that the underlying feature may be
deprecated/legacy and link the user to the canonical `source_url`.

```bash
grep -l '^deprecation_hint:' developers/pages/*.md
```

## Refreshing

```bash
python scrape_developers.py            # incremental: re-fetches all, rewrites only changed
python scrape_developers.py --full     # force-rewrite every file
python scrape_developers.py --dry-run  # report what would change, write nothing
```
"""


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "pages": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"version": 1, "pages": {}}


def save_manifest(path: Path, pages: dict[str, dict]) -> None:
    payload = {
        "version": 1,
        "format_version": OUTPUT_FORMAT_VERSION,
        "source": BASE,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "page_count": len(pages),
        "pages": dict(sorted(pages.items())),
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


# ---------- per-page fetch & extract ----------

async def fetch_page(client: httpx.AsyncClient, ref: PageRef) -> FetchedPage:
    text = await fetch_text(client, page_source_url(ref.slug))
    main_html = extract_main_html(text)
    if main_html is None:
        raise ValueError("could not locate <main data-pagefind-body> in page")
    prose_html = extract_prose_html(main_html)
    if prose_html is None:
        raise ValueError("could not locate prose div in <main>")
    breadcrumb = extract_breadcrumb(text)
    title = extract_title(text) or ref.pagefind_title
    body_html = _redact_secrets(htmlmod.unescape(prose_html))
    headings = filter_anchors(ref.anchors)
    content_hash = "sha256:" + hashlib.sha256(body_html.encode("utf-8")).hexdigest()
    return FetchedPage(
        ref=ref,
        title=title,
        body_html=body_html,
        breadcrumb=breadcrumb,
        headings=headings,
        content_hash=content_hash,
    )


# ---------- secret redaction (see scrape_docs.py for rationale) ----------

_SECRET_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"shpat_[A-Za-z0-9]{20,}"), "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"shpss_[A-Fa-f0-9]{20,}"), "shpss_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"shppa_[A-Fa-f0-9]{20,}"), "shppa_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"),    "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
]


def _redact_secrets(text: str) -> str:
    for pat, repl in _SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text


# ---------- main run ----------

async def run(args: argparse.Namespace) -> int:
    out_dir = Path(args.out)
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    old_pages: dict[str, dict] = manifest.get("pages", {})
    old_format = manifest.get("format_version", 0)
    format_changed = old_format != OUTPUT_FORMAT_VERSION
    if format_changed and old_pages:
        print(
            f"      output format upgrade detected ({old_format} -> {OUTPUT_FORMAT_VERSION}); "
            "all pages will be rewritten.",
            flush=True,
        )

    headers = {"User-Agent": USER_AGENT}
    # developers.mindbox.ru serves an incomplete certificate chain (missing
    # intermediate); curl -k works but stdlib SSL fails. Default to verify=off
    # since this is fetching public docs content, but expose --verify for
    # users with a custom trust store.
    verify = args.verify
    async with httpx.AsyncClient(
        headers=headers, timeout=TIMEOUT, http2=False, verify=verify
    ) as client:
        print(f"[1/4] Discovering pages via pagefind: {PAGEFIND_ENTRY}", flush=True)
        refs = await discover_pages(client, args.concurrency)
        print(f"      discovered {len(refs)} unique pages.", flush=True)

        sem = asyncio.Semaphore(args.concurrency)
        stats = SyncStats()
        new_pages: dict[str, dict] = {}
        summaries: dict[str, dict] = {}
        outbound_map: dict[str, list[str]] = {}
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        slug_to_title: dict[str, str] = {}
        slug_to_breadcrumb: dict[str, list[str]] = {}
        known_slugs: set[str] = {r.slug for r in refs}
        fetched: dict[str, FetchedPage] = {}

        async def fetch_worker(ref: PageRef) -> None:
            async with sem:
                try:
                    page = await fetch_page(client, ref)
                except Exception as exc:  # noqa: BLE001
                    stats.failed.append((ref.slug, repr(exc)))
                    return
                fetched[ref.slug] = page

        print(f"[2/4] Fetching {len(refs)} pages (concurrency={args.concurrency})...", flush=True)
        await asyncio.gather(*(fetch_worker(r) for r in refs))

        # Phase 3: alias resolution. Each page can link to other pages by a
        # cyrillic-text slug (e.g. `интеграция-cardsmobileкошелек`). Zudoku
        # serves these aliases as a tiny meta-redirect:
        #   <!doctype html><script>window.location.href="/docs/<canonical>";</script>
        # We follow each unknown slug through up to a few hops to find the
        # canonical page, then rewrite cross-page links to land on real files.
        unknown_slugs: set[str] = set()
        for page in fetched.values():
            for s in extract_link_target_slugs(page.body_html):
                if s not in known_slugs:
                    unknown_slugs.add(s)

        alias_to_slug: dict[str, str] = {}
        unresolved_aliases: list[str] = []
        if unknown_slugs:
            print(
                f"[3/4] Resolving {len(unknown_slugs)} alias slug(s) via /docs redirects...",
                flush=True,
            )
            redirect_re = re.compile(
                r'window\.location\.href\s*=\s*["\'](?:https?://developers\.mindbox\.ru)?/docs/([^"\']+)["\']'
            )

            async def resolve_alias(alias: str) -> None:
                # Bounded redirect chain in case aliases hop more than once.
                seen: set[str] = {alias}
                current = alias
                for _ in range(5):
                    async with sem:
                        try:
                            text = await fetch_text(client, page_source_url(current))
                        except Exception:  # noqa: BLE001
                            return
                    if len(text) > 4096:
                        # Too big to be the redirect stub — this is the actual
                        # page (rare, but possible).
                        return
                    m = redirect_re.search(text)
                    if not m:
                        return
                    from urllib.parse import unquote
                    target = unquote(m.group(1)).split("#", 1)[0].strip("/")
                    if not target or target in seen:
                        return
                    if target in known_slugs:
                        if target != alias:
                            alias_to_slug[alias] = target
                        return
                    seen.add(target)
                    current = target

            await asyncio.gather(*(resolve_alias(a) for a in unknown_slugs))
            unresolved_aliases = sorted(unknown_slugs - set(alias_to_slug))
            print(
                f"      resolved {len(alias_to_slug)} alias(es); "
                f"{len(unresolved_aliases)} still unresolved.",
                flush=True,
            )
        else:
            print("[3/4] No alias slugs to resolve.", flush=True)

        # Phase 4: artifact generation + writing.
        for ref in refs:
            page = fetched.get(ref.slug)
            if page is None:
                continue
            slug_to_title[ref.slug] = page.title
            slug_to_breadcrumb[ref.slug] = page.breadcrumb
            old = old_pages.get(ref.slug)
            changed = (old is None) or (old.get("content_hash") != page.content_hash)
            target = pages_dir / page_filename(ref.slug)

            if old is None:
                stats.added.append(ref.slug)
            elif changed:
                stats.updated.append(ref.slug)
            else:
                stats.unchanged.append(ref.slug)

            artifacts = build_artifacts(page, known_slugs, alias_to_slug)
            outbound_map[ref.slug] = artifacts.outbound_slugs

            summaries[ref.slug] = {
                "slug": ref.slug,
                "title": page.title,
                "section": page.breadcrumb[0] if page.breadcrumb else "",
                "subsection": page.breadcrumb[1] if len(page.breadcrumb) > 1 else "",
                "lead": artifacts.lead,
                "headings": artifacts.headings_flat,
                "deprecation_hint": artifacts.hints,
            }

            must_write = args.full or changed or not target.exists() or format_changed
            if must_write and not args.dry_run:
                write_page_file(pages_dir, page, fetched_at, artifacts)
            if artifacts.hints:
                stats.deprecation_flagged.append((ref.slug, artifacts.hints))

            entry = {
                "title": page.title,
                "source_url": page_source_url(ref.slug),
                "breadcrumb": page.breadcrumb,
                "content_hash": page.content_hash,
                "fetched_at": fetched_at if must_write else (old or {}).get("fetched_at", fetched_at),
            }
            if artifacts.hints:
                entry["deprecation_hint"] = artifacts.hints
            new_pages[ref.slug] = entry

        # Detect removals
        removed_slugs = sorted(set(old_pages) - set(new_pages))
        for slug in removed_slugs:
            stats.removed.append(slug)
            target = pages_dir / page_filename(slug)
            if target.exists() and not args.dry_run:
                target.unlink()

        if not args.dry_run:
            print(
                "[4/4] Writing INDEX.md, index/<section>.md, summaries.json, "
                "backlinks.json, CLAUDE.md, manifest.json...",
                flush=True,
            )
            toc = build_toc(slug_to_breadcrumb, slug_to_title)
            (out_dir / "INDEX.md").write_text(render_index(toc), encoding="utf-8")
            (out_dir / "CLAUDE.md").write_text(CLAUDE_MD, encoding="utf-8")
            written, removed = write_section_indexes(out_dir, toc)
            stats.section_indexes_written = len(written)
            stats.section_indexes_removed = removed
            write_summaries(out_dir, summaries, generated_at=fetched_at)
            write_backlinks(out_dir, outbound_map, generated_at=fetched_at)
            save_manifest(manifest_path, new_pages)
        else:
            print("[4/4] Dry run: skipping writes.", flush=True)

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

    return 1 if stats.failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="developers", help="output directory (default: developers)")
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"parallel page fetches (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument("--full", action="store_true", help="rewrite every page even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing files")
    parser.add_argument(
        "--verify",
        action="store_true",
        help="verify TLS certs (off by default: developers.mindbox.ru ships an incomplete chain)",
    )
    args = parser.parse_args()
    try:
        return asyncio.run(run(args))
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
