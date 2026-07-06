"""Enrich the journal corpus with LLM-derived metadata for agent retrieval.

Two layers, both written from `journal/<section>/pages/*.md`:

- **Layer A (both sections)**: replace the useless og:description-derived
  `lead` in `summaries.json` with a 1-2 sentence `summary_ru` ("what is
  this about and what does it teach/prove?") plus 3-5 `key_points`
  bullets. Also lifts `tag_titles_ru` from the page frontmatter into
  the summary entry so a Russian-language grep (e.g. "лояльность")
  matches even if the tag slug is transliterated (`loyalty`).

- **Layer B (cases only)**: build `journal/cases/fact_index.json` with
  structured fields per case (industry, mechanics, KPIs, operational
  results, time_to_value), then render faceted indexes
  `index/by-mechanic/`, `index/by-industry/`, `index/by-kpi/`.

Both layers are idempotent: enrichment is keyed on `content_hash` from
the scrape manifest (+ a prompt-version sentinel), so re-runs over an
unchanged corpus produce zero LLM calls.

Graceful degradation: if `ANTHROPIC_API_KEY` isn't set or the SDK isn't
installed, the script prints a warning and exits 0 — the rest of
sync.py keeps working.

CLI (run from the repo root):

    python scripts/enrich_journal.py --section education
    python scripts/enrich_journal.py --section cases
    python scripts/enrich_journal.py --section cases --limit 5 --dry-run
    python scripts/enrich_journal.py --section cases --full       # re-enrich every page
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import atomic_write_text, load_manifest_strict, page_filename, RU_TO_LAT  # noqa: E402
from _llm import LLMUnavailable, get_client  # noqa: E402


# Bump when the prompt or schema changes — forces re-enrichment of all
# pages on next run. Stored in enrichment_manifest.json next to the
# content_hash so we can decide skip vs. re-call per page.
PROMPT_VERSION = 1

# How aggressively to truncate article body before sending to the model.
# Most articles fit; the cap is for outliers (huge longreads). Cuts at a
# paragraph boundary near the limit so we don't slice mid-sentence.
MAX_BODY_CHARS = 16000


# ---------- frontmatter parsing ----------

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_page(path: Path) -> tuple[dict, str]:
    """Read a page file → (frontmatter dict, body markdown without H1).

    Lightweight parser — only handles the fields our scraper writes.
    Avoids pulling in pyyaml just for this read path.
    """
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f"no YAML frontmatter in {path}")
    fm_text = m.group(1)
    body = text[m.end():]
    # Drop the leading `# Title` H1 — duplicates frontmatter title.
    body = re.sub(r"^#\s+[^\n]+\n+", "", body, count=1)

    fm: dict = {}
    current_key: str | None = None
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_key is None:
                continue
            # An empty-valued key (`tags:`) was seeded as None above; a
            # following `  - ` item means it's actually a list — promote it.
            if not isinstance(fm.get(current_key), list):
                fm[current_key] = []
            fm[current_key].append(_unquote_yaml_scalar(line[4:].strip()))
        elif ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "" or val == "[]":
                fm[key] = [] if val == "[]" else None
                current_key = key
            else:
                fm[key] = _unquote_yaml_scalar(val)
                current_key = key
    return fm, body


def _unquote_yaml_scalar(s: str) -> str:
    """Strip surrounding quotes our `_common.to_yaml_scalar` produces."""
    if len(s) >= 2 and s[0] == s[-1] and s[0] in {'"', "'"}:
        return s[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return s


# ---------- body trimming ----------

def trim_body(body: str, max_chars: int = MAX_BODY_CHARS) -> str:
    """Return body truncated at a paragraph boundary near max_chars."""
    if len(body) <= max_chars:
        return body
    cut = body[:max_chars]
    para_end = cut.rfind("\n\n")
    if para_end > max_chars * 0.6:
        cut = cut[:para_end]
    return cut.rstrip() + "\n\n…"


# ---------- enrichment manifest ----------

def manifest_key(content_hash: str) -> str:
    """Cache key combines page content_hash with prompt version."""
    return f"{content_hash}@v{PROMPT_VERSION}"


def load_enrichment_manifest(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "prompt_version": PROMPT_VERSION, "pages": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_enrichment_manifest(path: Path, source: str, pages: dict[str, dict]) -> None:
    payload = {
        "version": 1,
        "prompt_version": PROMPT_VERSION,
        "source": source,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "page_count": len(pages),
        "pages": dict(sorted(pages.items())),
    }
    atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


# ---------- Layer A: summary + key_points ----------

LAYER_A_SYSTEM = (
    "Ты помогаешь маркетологу-агенту триажить статьи MindBox Journal. "
    "Получаешь заголовок, теги и тело статьи. Возвращаешь два поля: "
    "summary_ru (1–2 предложения по-русски, отвечающие на «о чём статья» "
    "и «что она доказывает или чему учит»; БЕЗ воды вроде «эта статья "
    "рассказывает о...») и key_points (3–5 коротких буллетов, каждый — "
    "одно предложение, конкретный факт/тезис из статьи). "
    "Если в статье есть конкретные цифры результатов — обязательно "
    "включи их в key_points. Не выдумывай, опирайся только на текст."
)

LAYER_A_TOOL_SCHEMA = {
    "type": "object",
    "properties": {
        "summary_ru": {
            "type": "string",
            "description": "1-2 sentence Russian summary: что в статье и что она доказывает/учит.",
        },
        "key_points": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 5,
            "description": "3-5 single-sentence bullets с конкретными тезисами/цифрами.",
        },
    },
    "required": ["summary_ru", "key_points"],
}


def build_layer_a_user_prompt(*, title: str, tags_ru: list[str], body: str) -> str:
    tag_line = ", ".join(tags_ru) if tags_ru else "(нет тегов)"
    return (
        f"Заголовок: {title}\n"
        f"Теги: {tag_line}\n\n"
        f"Тело статьи:\n\n{trim_body(body)}"
    )


# ---------- Layer B: cases fact extraction ----------

LAYER_B_SYSTEM = (
    "Ты извлекаешь структурированные факты из кейса MindBox для индекса. "
    "Получаешь заголовок, теги и тело кейса. Возвращаешь только то, что "
    "ЯВНО есть в тексте. Если поля нет — оставляй массив пустым или "
    "строку пустой. Не выдумывай цифры. "
    "Поля: industry (одна ниша slug-ом), client_size_hint (свободный "
    "текст вроде '142000 клиентов в базе' или ''), mechanics (нормализованные "
    "slug-и применённых маркетинговых механик: welcome-chain, brand-zone, "
    "broshennaya-korzina, ab-testing, segmentation, loyalty-program, "
    "popup, push, sms, email-newsletter-builder, product-recommendations, "
    "review-collection, customer-data-platform — выбирай из этого списка, "
    "и расширяй только при крайней необходимости новым slug-ом), kpis "
    "(массив объектов с измеримыми маркетинговыми метриками: name — "
    "open_rate/click_rate/conversion/revenue/retention/ltv/roi/arpu/aov/ctr/cr/dau и т.п.), "
    "operational_results (массив объектов 'было → стало' для нефинансовых "
    "результатов: время на задачу, нагрузка на персонал и т.п.), "
    "time_to_value (свободный текст вроде '4 месяца' или ''), "
    "channels (slug-и каналов: email, sms, push, web, mobile-app, voice)."
)

LAYER_B_TOOL_SCHEMA = {
    "type": "object",
    "properties": {
        "industry": {"type": "string", "description": "Slug отрасли клиента или ''."},
        "client_size_hint": {"type": "string", "description": "Размер клиентской базы/бизнеса свободным текстом или ''."},
        "mechanics": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Slug-и применённых механик.",
        },
        "kpis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Имя метрики (open_rate, conversion, retention, ...)."},
                    "delta_pct": {"type": "number", "description": "Относительный прирост в %, если указан."},
                    "delta_pp": {"type": "number", "description": "Прирост в процентных пунктах, если указан."},
                    "before": {"type": "string", "description": "Значение до изменения, если есть."},
                    "after": {"type": "string", "description": "Значение после, если есть."},
                    "absolute": {"type": "string", "description": "Абсолютное число (выручка, ROI), если оно — единственное в статье."},
                    "period": {"type": "string", "description": "За какой период измерено."},
                },
                "required": ["name"],
            },
        },
        "operational_results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "before": {"type": "string"},
                    "after": {"type": "string"},
                },
                "required": ["name"],
            },
        },
        "time_to_value": {"type": "string", "description": "Срок до результата свободным текстом или ''."},
        "channels": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Slug-и использованных каналов.",
        },
    },
    "required": ["industry", "client_size_hint", "mechanics", "kpis", "operational_results", "time_to_value", "channels"],
}


def build_layer_b_user_prompt(*, title: str, tags_ru: list[str], body: str) -> str:
    tag_line = ", ".join(tags_ru) if tags_ru else "(нет тегов)"
    return (
        f"Кейс: {title}\n"
        f"Теги: {tag_line}\n\n"
        f"Тело кейса:\n\n{trim_body(body)}"
    )


# ---------- summaries.json patch ----------

def patch_summaries(summaries_path: Path, enrichments: dict[str, dict], page_fm: dict[str, dict]) -> None:
    """Merge `summary_ru`, `key_points`, `tag_titles_ru` into summaries.json.

    We don't rebuild summaries.json from scratch — we patch the existing
    file the scraper just wrote, so summaries stays the canonical record
    of what Claude should grep.
    """
    payload = json.loads(summaries_path.read_text(encoding="utf-8"))
    pages = payload.get("pages", {})
    for slug, entry in pages.items():
        enrichment = enrichments.get(slug)
        if enrichment:
            entry["summary_ru"] = enrichment.get("summary_ru", "")
            entry["key_points"] = enrichment.get("key_points", [])
        # tag_titles_ru lifted from page frontmatter (no LLM needed).
        fm = page_fm.get(slug, {})
        tag_titles = fm.get("tag_titles") or []
        if tag_titles:
            entry["tag_titles_ru"] = tag_titles
        # Drop legacy `lead` once we have a real summary; keep it as
        # fallback if enrichment hasn't run for this page yet.
        if "summary_ru" in entry and entry.get("summary_ru"):
            entry.pop("lead", None)

    schema = payload.setdefault("schema", {})
    schema["fields"] = [
        "slug", "title", "summary_ru", "key_points", "headings",
        "tags", "tag_titles_ru", "published_at", "modified_at",
        "source_url", "deprecation_hint",
    ]
    schema["purpose"] = (
        "lightweight per-article cards for topic triage; grep this "
        "before reading full pages. summary_ru/key_points are LLM-"
        "generated, regenerated only when the page's content_hash changes."
    )

    atomic_write_text(
        summaries_path,
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )


# ---------- Layer B: faceted indexes ----------

def slugify_facet(name: str) -> str:
    """Cyrillic/mixed → ASCII filename slug. Stable, lossy."""
    out: list[str] = []
    for ch in name.lower():
        if ch in RU_TO_LAT:
            out.append(RU_TO_LAT[ch])
        elif ch.isalnum() and ord(ch) < 128:
            out.append(ch)
        else:
            out.append("-")
    s = re.sub(r"-+", "-", "".join(out)).strip("-")
    return s or "facet"


def render_facet_index(facet_kind: str, facet_value: str, entries: list[dict]) -> str:
    """One Markdown file listing all cases with this facet value.

    `entries` are facet entries: [{slug, title, source_url, summary_ru,
    published_at, kpis (optional), context (optional)}, ...].
    """
    out: list[str] = [
        f"# Кейсы по {facet_kind}: `{facet_value}`",
        "",
        f"Все кейсы из `journal/cases/`, помеченные `{facet_kind} = {facet_value}`. "
        f"Источник фактов — `journal/cases/fact_index.json`.",
        "",
    ]
    sorted_entries = sorted(
        entries,
        key=lambda e: (e.get("published_at") or "0000-00-00", e.get("slug") or ""),
        reverse=True,
    )
    for e in sorted_entries:
        date = e.get("published_at") or "—"
        title = e.get("title") or e["slug"]
        out.append(f"## [{title}](../../pages/{page_filename(e['slug'])})")
        out.append("")
        out.append(f"`{date}` · <{e['source_url']}>")
        out.append("")
        if e.get("summary_ru"):
            out.append(e["summary_ru"])
            out.append("")
        if e.get("context"):
            out.append(f"_{e['context']}_")
            out.append("")
        for kpi in e.get("kpis") or []:
            out.append(f"- {format_kpi_line(kpi)}")
        if e.get("kpis"):
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def format_kpi_line(kpi: dict) -> str:
    """Compact one-liner for a single KPI row in a facet index."""
    parts: list[str] = [f"**{kpi['name']}**"]
    if kpi.get("before") and kpi.get("after"):
        parts.append(f"{kpi['before']} → {kpi['after']}")
    if kpi.get("delta_pct") is not None:
        parts.append(f"+{kpi['delta_pct']}%")
    if kpi.get("delta_pp") is not None:
        parts.append(f"+{kpi['delta_pp']} п.п.")
    if kpi.get("absolute"):
        parts.append(kpi["absolute"])
    if kpi.get("period"):
        parts.append(f"({kpi['period']})")
    return " · ".join(parts)


def write_facet_indexes(
    cases_dir: Path,
    fact_index: dict[str, dict],
    page_fm: dict[str, dict],
    summaries: dict[str, dict],
) -> tuple[int, int, int]:
    """Build by-mechanic / by-industry / by-kpi indexes from fact_index."""
    by_mechanic: dict[str, list[dict]] = {}
    by_industry: dict[str, list[dict]] = {}
    by_kpi: dict[str, list[dict]] = {}

    for slug, facts in fact_index.items():
        fm = page_fm.get(slug, {})
        sm = summaries.get(slug, {})
        entry_base = {
            "slug": slug,
            "title": fm.get("title") or sm.get("title") or slug,
            "source_url": fm.get("source_url") or sm.get("source_url") or "",
            "published_at": fm.get("published_at") or sm.get("published_at") or "",
            "summary_ru": sm.get("summary_ru") or "",
            "context": facts.get("client_size_hint") or "",
            "kpis": facts.get("kpis") or [],
        }
        for mech in facts.get("mechanics") or []:
            by_mechanic.setdefault(mech, []).append(entry_base)
        if facts.get("industry"):
            by_industry.setdefault(facts["industry"], []).append(entry_base)
        for kpi in facts.get("kpis") or []:
            name = kpi.get("name")
            if name:
                # Per-KPI entry should highlight ONLY this KPI in its kpis list,
                # so the facet page reads cleanly.
                by_kpi.setdefault(name, []).append({**entry_base, "kpis": [kpi]})

    def _write_group(kind: str, groups: dict[str, list[dict]]) -> int:
        out_dir = cases_dir / "index" / f"by-{kind}"
        out_dir.mkdir(parents=True, exist_ok=True)
        written: set[str] = set()
        for value, entries in groups.items():
            fname = slugify_facet(value) + ".md"
            (out_dir / fname).write_text(
                render_facet_index(kind, value, entries),
                encoding="utf-8",
            )
            written.add(fname)
        # Drop stale facet files we no longer produce.
        for existing in out_dir.glob("*.md"):
            if existing.name not in written:
                existing.unlink()
        return len(written)

    return (
        _write_group("mechanic", by_mechanic),
        _write_group("industry", by_industry),
        _write_group("kpi", by_kpi),
    )


# ---------- main pipeline ----------

def run(args: argparse.Namespace) -> int:
    section = args.section
    section_dir = Path(args.out) / section
    pages_dir = section_dir / "pages"
    summaries_path = section_dir / "summaries.json"
    scrape_manifest_path = section_dir / "manifest.json"
    enrichment_manifest_path = section_dir / "enrichment_manifest.json"
    fact_index_path = section_dir / "fact_index.json"

    if not summaries_path.exists() or not scrape_manifest_path.exists():
        print(
            f"[enrich] {section}: scrape outputs missing in {section_dir}. "
            f"Run `python scripts/scrape_journal.py --section {section}` first.",
            file=sys.stderr,
        )
        return 1

    try:
        llm = get_client()
    except LLMUnavailable as exc:
        print(f"[enrich] {section}: skipping — {exc}", file=sys.stderr)
        return 0  # not an error: degrade gracefully

    scrape_manifest = load_manifest_strict(scrape_manifest_path)
    scrape_pages: dict[str, dict] = scrape_manifest.get("pages", {})
    enrichment_manifest = load_enrichment_manifest(enrichment_manifest_path)
    cached: dict[str, dict] = enrichment_manifest.get("pages", {})
    cached_prompt_version = enrichment_manifest.get("prompt_version", 0)
    if cached_prompt_version != PROMPT_VERSION:
        print(
            f"[enrich] {section}: prompt version bump "
            f"({cached_prompt_version} → {PROMPT_VERSION}); re-enriching all pages.",
            flush=True,
        )

    # Read every page's frontmatter + body. Cheap (875 small files), and we
    # need the body for any page we end up enriching anyway.
    page_fm: dict[str, dict] = {}
    page_body: dict[str, str] = {}
    for slug in scrape_pages:
        page_path = pages_dir / page_filename(slug)
        if not page_path.exists():
            continue
        try:
            fm, body = parse_page(page_path)
        except ValueError as exc:
            print(f"[enrich] {section}: skipping {slug}: {exc}", file=sys.stderr)
            continue
        page_fm[slug] = fm
        page_body[slug] = body

    # Decide which slugs need a fresh LLM call.
    targets: list[str] = []
    for slug, page_meta in scrape_pages.items():
        if slug not in page_fm:
            continue
        ch = page_meta.get("content_hash") or ""
        cached_entry = cached.get(slug)
        cached_fresh = (
            cached_entry is not None
            and cached_entry.get("content_hash") == ch
            and cached_prompt_version == PROMPT_VERSION
            and "summary_ru" in cached_entry
            and (section != "cases" or "facts" in cached_entry)
        )
        if not args.full and cached_fresh:
            continue
        targets.append(slug)

    if args.limit is not None:
        targets = targets[: args.limit]

    print(
        f"[enrich] {section}: {len(targets)} page(s) to enrich "
        f"(cached: {len(cached)}, total: {len(scrape_pages)}, full={args.full}, dry_run={args.dry_run}).",
        flush=True,
    )

    new_cached: dict[str, dict] = dict(cached)
    enriched_summaries: dict[str, dict] = {}
    fact_index: dict[str, dict] = {}

    # Seed fact_index with cached values for pages we're skipping (cases only).
    if section == "cases":
        for slug, entry in cached.items():
            if slug in page_fm and "facts" in entry:
                fact_index[slug] = entry["facts"]
        for slug, entry in cached.items():
            if slug in page_fm and "summary_ru" in entry:
                enriched_summaries[slug] = {
                    "summary_ru": entry.get("summary_ru", ""),
                    "key_points": entry.get("key_points", []),
                }
    else:
        for slug, entry in cached.items():
            if slug in page_fm and "summary_ru" in entry:
                enriched_summaries[slug] = {
                    "summary_ru": entry.get("summary_ru", ""),
                    "key_points": entry.get("key_points", []),
                }

    started = time.monotonic()
    failed: list[tuple[str, str]] = []

    for i, slug in enumerate(targets, 1):
        fm = page_fm[slug]
        body = page_body[slug]
        title = fm.get("title") or slug
        tags_ru = fm.get("tag_titles") or []

        if args.dry_run:
            print(f"  [{i}/{len(targets)}] would enrich {slug} (title: {title!r})")
            continue

        try:
            layer_a = llm.call_structured(
                system=LAYER_A_SYSTEM,
                user=build_layer_a_user_prompt(title=title, tags_ru=tags_ru, body=body),
                tool_name="record_summary",
                tool_description="Record a 1-2 sentence Russian summary and 3-5 key bullet points.",
                tool_schema=LAYER_A_TOOL_SCHEMA,
                max_tokens=1024,
            )
        except Exception as exc:  # noqa: BLE001
            failed.append((slug, f"layer A: {type(exc).__name__}: {exc}"))
            continue

        entry: dict = {
            "content_hash": scrape_pages[slug].get("content_hash", ""),
            "summary_ru": layer_a.get("summary_ru", ""),
            "key_points": layer_a.get("key_points") or [],
            "enriched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        enriched_summaries[slug] = {
            "summary_ru": entry["summary_ru"],
            "key_points": entry["key_points"],
        }

        if section == "cases":
            try:
                layer_b = llm.call_structured(
                    system=LAYER_B_SYSTEM,
                    user=build_layer_b_user_prompt(title=title, tags_ru=tags_ru, body=body),
                    tool_name="record_case_facts",
                    tool_description="Record structured facts extracted from a MindBox case study.",
                    tool_schema=LAYER_B_TOOL_SCHEMA,
                    max_tokens=2048,
                )
            except Exception as exc:  # noqa: BLE001
                failed.append((slug, f"layer B: {type(exc).__name__}: {exc}"))
                # Keep the layer-A enrichment we already got — partial progress
                # is better than dropping the page entirely.
                new_cached[slug] = entry
                continue
            entry["facts"] = layer_b
            fact_index[slug] = layer_b

        new_cached[slug] = entry
        print(f"  [{i}/{len(targets)}] {slug}", flush=True)

    # Drop manifest entries whose pages disappeared from disk.
    for slug in list(new_cached):
        if slug not in scrape_pages:
            new_cached.pop(slug)
            fact_index.pop(slug, None)
            enriched_summaries.pop(slug, None)

    elapsed = time.monotonic() - started

    if not args.dry_run:
        # Patch summaries.json with what we have (enriched + cached).
        # `enriched_summaries` already contains both fresh and cached entries.
        patch_summaries(summaries_path, enriched_summaries, page_fm)

        if section == "cases":
            atomic_write_text(
                fact_index_path,
                json.dumps(
                    {
                        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "source": "https://mindbox.ru/journal/cases/",
                        "page_count": len(fact_index),
                        "schema": {
                            "fields": [
                                "industry", "client_size_hint", "mechanics",
                                "kpis", "operational_results", "time_to_value", "channels",
                            ],
                            "purpose": (
                                "structured facts per case for queries like "
                                "'кейсы из fashion с email и retention >30%'"
                            ),
                        },
                        "pages": dict(sorted(fact_index.items())),
                    },
                    ensure_ascii=False,
                    indent=2,
                ) + "\n",
            )
            # Reload summaries we just patched, so by-* indexes can show summary_ru.
            patched_summaries = json.loads(summaries_path.read_text(encoding="utf-8")).get("pages", {})
            n_mech, n_ind, n_kpi = write_facet_indexes(
                section_dir, fact_index, page_fm, patched_summaries
            )
            print(
                f"[enrich] {section}: facet indexes written — "
                f"by-mechanic: {n_mech}, by-industry: {n_ind}, by-kpi: {n_kpi}.",
                flush=True,
            )

        save_enrichment_manifest(
            enrichment_manifest_path,
            f"https://mindbox.ru/journal/{section}/",
            new_cached,
        )

    print()
    print(f"[enrich] {section} done in {elapsed:.1f}s.")
    print(f"  enriched (LLM calls): {len(targets) - len(failed)}")
    print(f"  cached (skipped):     {len(cached) if not args.full else 0}")
    print(f"  failed:               {len(failed)}")
    if failed:
        for slug, why in failed[:20]:
            print(f"    ! {slug}: {why}", file=sys.stderr)
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--section", required=True, choices=["education", "cases"])
    parser.add_argument("--out", default="journal", help="parent journal directory (default: journal)")
    parser.add_argument("--full", action="store_true", help="re-enrich every page even if cached")
    parser.add_argument("--dry-run", action="store_true", help="report which pages would be enriched; no LLM calls, no writes")
    parser.add_argument("--limit", type=int, default=None, help="cap LLM calls for debugging")
    args = parser.parse_args()
    try:
        return run(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
