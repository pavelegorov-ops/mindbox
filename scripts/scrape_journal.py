"""Scrape MindBox journal articles into a Markdown corpus for Claude Code.

Source: https://mindbox.ru/journal/<section>/ (default section: education).
Article discovery via the public sitemap at https://mindbox.ru/sitemap.xml.

Re-run anytime; only changed articles are rewritten thanks to content hashing.

Output layout (under --out, default `journal/`):
    CLAUDE.md                  Onboarding for Claude Code on how to use this corpus.
    INDEX.md                   Linear list of articles, newest first by publish date.
    manifest.json              Per-slug content hashes + timestamps for incremental sync.
    summaries.json             Per-article cards (title, lead, headings, tags) for grep triage.
    pages/<slug>.md            One Markdown file per article, with YAML frontmatter.
    index/by-tag/<tag>.md      One file per tag, listing articles tagged with it.

Internal links between journal articles are rewritten to local `<slug>.md` so
Claude can follow them via the Read tool.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
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
)

ORIGIN = "https://mindbox.ru"
SITEMAP_URL = f"{ORIGIN}/sitemap.xml"
USER_AGENT = "mindbox-journal-scraper/1.0 (+Claude Code knowledge sync)"
DEFAULT_CONCURRENCY = 8
TIMEOUT = httpx.Timeout(30.0, connect=10.0)

# Bump when the on-disk page file format changes — forces a full rewrite.
OUTPUT_FORMAT_VERSION = 1

# Title suffix that the site appends to every <og:title>; strip for cleaner frontmatter.
TITLE_SUFFIX_RE = re.compile(r"\s*[-—–]\s*Журнал Mindbox.*$", re.IGNORECASE)

# Internal mindbox.ru links inside an article body that point to other journal
# articles in the same section. Captured slug is the trailing path segment.
JOURNAL_LINK_RE_TEMPLATE = r'(href)=(["\'])(?:{origin})?/journal/{section}/([^"\'#?/]+)/?(\#[^"\']*)?\2'


class ArticleNotPresent(Exception):
    """Page exists at the URL but has no <article class='editor-article'>.

    Distinct from network failures (timeouts, 5xx) — these pages are valid
    HTML, just not real articles (e.g. test/placeholder URLs that ship in
    the public sitemap). They get reported as `skipped` and do NOT cause
    a non-zero exit code.
    """


@dataclass
class ArticleRef:
    slug: str
    url: str  # canonical URL with trailing slash


@dataclass
class FetchedArticle:
    ref: ArticleRef
    title: str
    description: str
    published_at: str  # ISO date "YYYY-MM-DD" or ""
    modified_at: str   # ISO date "YYYY-MM-DD" or ""
    tags: list[tuple[str, str]]  # [(slug, title), ...] — preserve order, deduped
    body_html: str  # contents of <article class="editor-article">, secrets redacted
    headings: list[str]  # all <h2> texts inside the article
    content_hash: str


@dataclass
class ArticleArtifacts:
    body_md: str
    hints: list[str]
    lead: str


@dataclass
class SyncStats:
    added: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)
    skipped: list[tuple[str, str]] = field(default_factory=list)
    deprecation_flagged: list[tuple[str, list[str]]] = field(default_factory=list)
    tag_indexes_written: int = 0
    tag_indexes_removed: list[str] = field(default_factory=list)


# ---------- discovery ----------

def parse_sitemap_for_section(xml_text: str, section: str) -> list[ArticleRef]:
    """Extract article URLs from sitemap.xml that match /journal/<section>/<slug>/."""
    pat = re.compile(
        rf"<loc>\s*({re.escape(ORIGIN)}/journal/{re.escape(section)}/([^/<\s]+)/?)\s*</loc>",
        re.IGNORECASE,
    )
    seen: dict[str, ArticleRef] = {}
    for m in pat.finditer(xml_text):
        url = m.group(1)
        slug = m.group(2)
        if not url.endswith("/"):
            url += "/"
        if slug not in seen:
            seen[slug] = ArticleRef(slug=slug, url=url)
    return list(seen.values())


# ---------- fetch + parse ----------

def _meta_content(soup: BeautifulSoup, **attrs) -> str:
    el = soup.find("meta", attrs=attrs)
    if el is None:
        return ""
    val = el.get("content", "")
    return val.strip() if isinstance(val, str) else ""


def _normalize_iso_date(raw: str) -> str:
    """`2023-03-03 00:00:00` or `2023-03-03T00:00:00+0000` → `2023-03-03`."""
    if not raw:
        return ""
    raw = raw.strip().replace("T", " ")
    return raw.split(" ", 1)[0]


def _slug_from_tag_href(href: str) -> str | None:
    """Extract <tag-slug> from an `/journal/tag/<slug>/` href."""
    if not isinstance(href, str):
        return None
    sp = urlsplit(href)
    path = sp.path or ""
    m = re.match(r"^/journal/tag/([^/]+)/?$", path)
    return m.group(1) if m else None


def parse_article(url: str, html_text: str) -> tuple[str, str, str, str, list[tuple[str, str]], str, list[str]]:
    """Pull title, desc, dates, tags, raw <article> HTML and h2 list out of a page.

    Returns: (title, description, published_at, modified_at, tags, body_html, headings).
    Raises ValueError if the page has no <article class="editor-article">.
    """
    soup = BeautifulSoup(html_text, "html.parser")

    article = soup.find("article", class_="editor-article")
    if article is None:
        raise ArticleNotPresent("no <article class='editor-article'> on page")

    raw_title = _meta_content(soup, property="og:title") or (soup.title.string if soup.title else "") or ""
    title = TITLE_SUFFIX_RE.sub("", raw_title).strip()
    description = _meta_content(soup, property="og:description") or _meta_content(soup, attrs={"name": "description"})
    published_at = _normalize_iso_date(_meta_content(soup, property="article:published_time"))
    modified_at = _normalize_iso_date(_meta_content(soup, property="article:modified_time"))

    # Tags: links inside the article whose href is /journal/tag/<slug>/
    tags: list[tuple[str, str]] = []
    seen_tag_slugs: set[str] = set()
    for a in article.find_all("a", href=True):
        slug = _slug_from_tag_href(a["href"])
        if slug and slug not in seen_tag_slugs:
            seen_tag_slugs.add(slug)
            tag_title = a.get_text(strip=True)
            tags.append((slug, tag_title or slug))

    # Strip the leading `<div class="lead lead_text">` that duplicates date+title;
    # we put title into frontmatter+H1 and date into frontmatter, so this would
    # be redundant noise in the body.
    for lead_div in article.select("div.lead.lead_text"):
        lead_div.decompose()
    # Strip the tag block at the end of the article (links to /journal/tag/...);
    # tags are in frontmatter, no need to keep the noisy paragraph at the bottom.
    for a in list(article.find_all("a", href=True)):
        slug = _slug_from_tag_href(a["href"])
        if slug:
            # Remove the closest <li>/<p>/<div> ancestor that wraps just tag links.
            anc = a.find_parent(["li", "p", "div"])
            if anc and all(_slug_from_tag_href(x.get("href", "")) for x in anc.find_all("a", href=True)):
                anc.decompose()
            else:
                a.decompose()

    headings = [h.get_text(" ", strip=True) for h in article.find_all("h2") if h.get_text(strip=True)]

    body_html = redact_secrets(str(article))
    return title, description, published_at, modified_at, tags, body_html, headings


def rewrite_internal_links(html_text: str, section: str, known_slugs: set[str]) -> str:
    """Rewrite `https://mindbox.ru/journal/<section>/<slug>/` (or path-only) hrefs to `<slug>.md`.

    Only when the target slug is in our local corpus. Other links — including
    /journal/tag/, /journal/cases/, external — stay absolute.
    """
    pat = re.compile(JOURNAL_LINK_RE_TEMPLATE.format(origin=re.escape(ORIGIN), section=re.escape(section)))

    def repl(m: re.Match) -> str:
        attr, sep, slug, anchor = m.group(1), m.group(2), m.group(3), (m.group(4) or "")
        if slug in known_slugs:
            return f'{attr}={sep}{slug}.md{anchor}{sep}'
        return m.group(0)

    return pat.sub(repl, html_text)


def html_to_markdown(body_html: str, section: str, known_slugs: set[str]) -> str:
    rewritten = rewrite_internal_links(body_html, section, known_slugs)
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


def slugify_tag(name: str) -> str:
    """Cyrillic-or-mixed tag slug → ASCII filename (lossy but stable)."""
    out: list[str] = []
    for ch in name.lower():
        if ch in RU_TO_LAT:
            out.append(RU_TO_LAT[ch])
        elif ch.isalnum() and ord(ch) < 128:
            out.append(ch)
        else:
            out.append("-")
    s = re.sub(r"-+", "-", "".join(out)).strip("-")
    return s or "tag"


# ---------- HTTP ----------

async def fetch_text(client: httpx.AsyncClient, url: str) -> str:
    r = await client.get(url, follow_redirects=True)
    r.raise_for_status()
    if r.encoding is None or r.encoding.lower() == "iso-8859-1":
        r.encoding = "utf-8"
    return r.text


async def fetch_article(client: httpx.AsyncClient, ref: ArticleRef) -> FetchedArticle:
    text = await fetch_text(client, ref.url)
    title, description, published_at, modified_at, tags, body_html, headings = parse_article(ref.url, text)
    content_hash = "sha256:" + hashlib.sha256(body_html.encode("utf-8")).hexdigest()
    return FetchedArticle(
        ref=ref,
        title=title,
        description=description,
        published_at=published_at,
        modified_at=modified_at,
        tags=tags,
        body_html=body_html,
        headings=headings,
        content_hash=content_hash,
    )


# ---------- writing artifacts ----------

def build_artifacts(article: FetchedArticle, body_md: str) -> ArticleArtifacts:
    hints = detect_deprecation(article.title + "\n" + body_md)
    lead = extract_lead(body_md, max_chars=280)
    return ArticleArtifacts(body_md=body_md, hints=hints, lead=lead)


def write_page_file(
    pages_dir: Path,
    article: FetchedArticle,
    fetched_at: str,
    artifacts: ArticleArtifacts,
) -> None:
    meta: dict = {
        "title": article.title,
        "slug": article.ref.slug,
        "source_url": article.ref.url,
    }
    if article.published_at:
        meta["published_at"] = article.published_at
    if article.modified_at:
        meta["modified_at"] = article.modified_at
    if article.description:
        meta["description"] = article.description
    if article.tags:
        meta["tags"] = [slug for slug, _ in article.tags]
        meta["tag_titles"] = [title for _, title in article.tags]
    meta["fetched_at"] = fetched_at
    meta["content_hash"] = article.content_hash
    if artifacts.hints:
        meta["deprecation_hint"] = artifacts.hints

    text = render_frontmatter(meta) + "\n# " + article.title + "\n\n" + artifacts.body_md
    (pages_dir / page_filename(article.ref.slug)).write_text(text, encoding="utf-8")


def write_summaries(out_dir: Path, summaries: dict[str, dict], *, generated_at: str, source: str) -> None:
    payload = {
        "generated_at": generated_at,
        "source": source,
        "page_count": len(summaries),
        "schema": {
            "fields": [
                "slug", "title", "lead", "headings", "tags",
                "published_at", "modified_at", "source_url", "deprecation_hint",
            ],
            "purpose": "lightweight per-article cards for topic triage; grep this before reading full pages",
        },
        "pages": dict(sorted(summaries.items())),
    }
    atomic_write_text(
        out_dir / "summaries.json",
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )


def render_main_index(articles: list[FetchedArticle], source: str) -> str:
    """Linear list of articles, newest first by published_at."""
    out: list[str] = [
        "# MindBox Journal — Index",
        "",
        f"Source: <{source}>",
        "",
        "Все статьи отсортированы по дате публикации (свежие сверху). Для",
        "тематического поиска используй `summaries.json` (грепом) или",
        "`index/by-tag/<тег>.md`.",
        "",
    ]
    sorted_articles = sorted(
        articles,
        key=lambda a: (a.published_at or "0000-00-00", a.ref.slug),
        reverse=True,
    )
    for a in sorted_articles:
        date = a.published_at or "—"
        tag_str = ", ".join(t for _, t in a.tags) if a.tags else ""
        line = f"- `{date}` — [{a.title}](pages/{page_filename(a.ref.slug)})"
        if tag_str:
            line += f" — _{tag_str}_"
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def render_tag_index(tag_slug: str, tag_title: str, articles: list[FetchedArticle], source: str) -> str:
    out: list[str] = [
        f"# Тег: {tag_title}",
        "",
        f"Все статьи раздела с этим тегом. Источник: <{source}>",
        "",
    ]
    sorted_articles = sorted(
        articles,
        key=lambda a: (a.published_at or "0000-00-00", a.ref.slug),
        reverse=True,
    )
    for a in sorted_articles:
        date = a.published_at or "—"
        out.append(f"## [{a.title}](../../pages/{page_filename(a.ref.slug)})")
        out.append("")
        meta_bits = [f"`{date}`"]
        if a.tags:
            other = [t for s, t in a.tags if s != tag_slug]
            if other:
                meta_bits.append("теги: " + ", ".join(other))
        out.append(" · ".join(meta_bits))
        out.append("")
        if a.description:
            out.append(a.description)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def write_tag_indexes(
    out_dir: Path,
    articles: list[FetchedArticle],
    source: str,
) -> tuple[list[str], list[str]]:
    """Write `index/by-tag/<tag-slug>.md` for each tag found across articles.

    Returns (written_filenames, removed_filenames).
    """
    by_tag_dir = out_dir / "index" / "by-tag"
    by_tag_dir.mkdir(parents=True, exist_ok=True)

    # Group articles by tag, preserving the human-readable title from the first
    # encounter (different articles may print the same tag with different casing).
    groups: dict[str, dict] = {}
    for a in articles:
        for tag_slug, tag_title in a.tags:
            entry = groups.setdefault(tag_slug, {"title": tag_title, "articles": []})
            entry["articles"].append(a)

    written: set[str] = set()
    used_filenames: dict[str, int] = {}
    for tag_slug, entry in groups.items():
        base = slugify_tag(tag_slug)
        n = used_filenames.get(base, 0)
        fname = f"{base}.md" if n == 0 else f"{base}-{n + 1}.md"
        used_filenames[base] = n + 1
        text = render_tag_index(tag_slug, entry["title"], entry["articles"], source)
        (by_tag_dir / fname).write_text(text, encoding="utf-8")
        written.add(fname)

    removed: list[str] = []
    for existing in by_tag_dir.glob("*.md"):
        if existing.name not in written:
            existing.unlink()
            removed.append(existing.name)
    return sorted(written), sorted(removed)


CLAUDE_MD = """# MindBox Journal — локальное зеркало (раздел «Учебные материалы»)

Эта папка — локальное Markdown-зеркало раздела
<https://mindbox.ru/journal/education/>, поддерживается скриптом
`scripts/scrape_journal.py` в репозитории.

Это **материал для агента, а не для маркетолога**. В отличие от
`docs/` и `developers/` (документация продукта), здесь лежат статьи
журнала: маркетинговые гайды, разборы кейсов, объяснения концепций.
Используй их как источник вдохновения, чтобы давать содержательные
ответы — но **не пересказывай тело статьи целиком** в ответе человеку.

## Правила ответа человеку

При ответах, опирающихся на этот корпус:

1. Сформулируй ответ своими словами в 1-3 предложениях.
2. Дай ссылку на оригинал (`source_url` из frontmatter, она же
   `https://mindbox.ru/journal/education/<slug>/`).
3. **Не вставляй больших фрагментов статьи**. У пользователя есть
   полный текст по ссылке — экономь его время и уважай авторские
   права журнала.
4. Если на вопрос отвечают несколько статей — перечисли 2-3 ссылки
   списком, по строке на каждую (с заголовком и датой).

Если вопрос не покрыт журналом — отвечай по `docs/` или `developers/`
(см. корневой `CLAUDE.md`). Журнал — дополнительный источник, не
основной.

## Структура

- `pages/<slug>.md` — одна статья на файл. Имя файла = последний
  сегмент URL: `https://mindbox.ru/journal/education/<slug>/` ↔
  `pages/<slug>.md`.
- `summaries.json` — карточки статей (title, lead, headings, tags,
  published_at). **Сначала grep его** при поиске темы — это в разы
  дешевле, чем читать несколько полных страниц.
- `index/by-tag/<tag-slug>.md` — индекс по тегу. Содержит список
  статей с этим тегом, отсортированный по дате убыв. Используй,
  когда нужен тематический обзор: «что есть про лояльность»,
  «статьи об AB-тестах».
- `INDEX.md` — линейный список всех статей по дате (свежие сверху).
  Удобен для вопросов «что нового», «есть ли свежее по X».
- `manifest.json` — служебка инкрементальной синхронизации
  (хеш контента и время выгрузки на каждую статью). Руками не править.

## Рекомендованный workflow поиска

Для вопросов «что в журнале говорят про X?»:

1. `Grep "X" journal/summaries.json -B 1 -A 5` → ранжированный список
   карточек с лидами и тегами, ~600 токенов в выходе.
2. Открыть самую релевантную `journal/pages/<slug>.md` целиком.
3. Ответить пользователю кратко + ссылкой `source_url` (см. правила выше).

Для тематического обзора («дай 3 статьи про сегментацию»):

1. Найти подходящий файл в `journal/index/by-tag/` (slug
   транслитерированный — `loyalty.md`, `metrics.md`, `marketing.md`).
2. Прочитать его — там уже отобраны статьи с этим тегом и их анонсы.
3. Если нужен полный текст конкретной статьи — открыть её
   `pages/<slug>.md`.

## Формат страницы

```yaml
---
title: <человекочитаемый заголовок>
slug: <последний сегмент URL>
source_url: https://mindbox.ru/journal/education/<slug>/
published_at: 2023-03-03            # дата публикации (опционально)
modified_at: 2024-10-22             # дата правки (опционально)
description: <короткий анонс из og:description>
tags: [ab-testyi, marketing, ...]   # slug'и тегов
tag_titles: ["AB-тесты", "Маркетинг", ...]   # человеко-читаемые подписи
fetched_at: 2026-05-07T...Z
content_hash: sha256:...
deprecation_hint: ["устарел", ...]   # ОПЦИОНАЛЬНО — см. ниже
---

# <заголовок>

<тело статьи в Markdown>
```

Тело — статья, отрендеренная через markdownify. Внутренние ссылки на
другие статьи журнала из этого же корпуса переписаны в относительные
`<slug>.md`. Изображения — абсолютными CDN-ссылками
(`https://image.mindbox.ru/...`); локально не сохраняются.

### Свежесть статей

У статей есть `published_at`. Журнал не такой динамичный, как
`docs/`, но статьи 2017-2020 годов могут описывать устаревшие
интерфейсы или практики. Если статья старше 2022 года и вопрос про
«как это сейчас работает» — добавь оговорку и предложи проверить
актуальность через `docs/` или сайт.

### `deprecation_hint`

Появляется, если в теле или заголовке найдены маркеры устарелости:
`устарел`, `устаревш`, `больше не работа`, `больше не поддержив`,
`не используется`, `старый интерфейс`, `старая версия`, `deprecated`,
`прекращ`, `снят с поддержки`, `архивн`. Если поле есть — добавь
оговорку в ответе.

## Обновление

```bash
python scripts/scrape_journal.py            # инкрементально (добавит/обновит изменившиеся)
python scripts/scrape_journal.py --full     # принудительно переписать каждый файл
python scripts/scrape_journal.py --dry-run  # показать, что изменится; ничего не пишет
```

(Запускать из корня репо — скрейпер пишет в `journal/` относительно
текущего каталога.)

Скрипт отчитывается: добавлено / обновлено / без изменений / удалено.
Удалённые статьи (slug'и, исчезнувшие из публичного sitemap)
удаляются из `pages/`; восстанавливай из git, если нужно.
"""


def save_manifest(path: Path, source: str, pages: dict[str, dict]) -> None:
    payload = {
        "version": 1,
        "format_version": OUTPUT_FORMAT_VERSION,
        "source": source,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "page_count": len(pages),
        "pages": dict(sorted(pages.items())),
    }
    atomic_write_text(
        path,
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )


# ---------- main pipeline ----------

async def run(args: argparse.Namespace) -> int:
    section = args.section
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

    section_source = f"{ORIGIN}/journal/{section}/"
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient(headers=headers, timeout=TIMEOUT, http2=False) as client:
        print(f"[1/3] Fetching sitemap: {SITEMAP_URL}", flush=True)
        sitemap_text = await fetch_text(client, SITEMAP_URL)
        refs = parse_sitemap_for_section(sitemap_text, section)
        if not refs:
            print(
                f"      sitemap had 0 URLs matching /journal/{section}/. "
                "Nothing to do.",
                file=sys.stderr,
            )
            return 1
        print(f"      sitemap parsed: {len(refs)} articles in /journal/{section}/.", flush=True)

        sem = asyncio.Semaphore(args.concurrency)
        stats = SyncStats()
        new_pages: dict[str, dict] = {}
        summaries: dict[str, dict] = {}
        successful_articles: list[FetchedArticle] = []
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        known_slugs: set[str] = {r.slug for r in refs}

        async def worker(ref: ArticleRef) -> None:
            async with sem:
                try:
                    article = await fetch_article(client, ref)
                except ArticleNotPresent as exc:
                    stats.skipped.append((ref.slug, str(exc)))
                    return
                except Exception as exc:  # noqa: BLE001
                    stats.failed.append((ref.slug, format_fetch_error(exc, url=ref.url)))
                    return

                old = old_pages.get(ref.slug)
                changed = (old is None) or (old.get("content_hash") != article.content_hash)
                target = pages_dir / page_filename(ref.slug)

                if old is None:
                    stats.added.append(ref.slug)
                elif changed:
                    stats.updated.append(ref.slug)
                else:
                    stats.unchanged.append(ref.slug)

                body_md = html_to_markdown(article.body_html, section, known_slugs)
                artifacts = build_artifacts(article, body_md)

                summaries[ref.slug] = {
                    "slug": ref.slug,
                    "title": article.title,
                    "lead": artifacts.lead,
                    "headings": article.headings,
                    "tags": [slug for slug, _ in article.tags],
                    "published_at": article.published_at,
                    "modified_at": article.modified_at,
                    "source_url": article.ref.url,
                    "deprecation_hint": artifacts.hints,
                }
                successful_articles.append(article)

                must_write = args.full or changed or not target.exists() or format_changed
                if must_write and not args.dry_run:
                    write_page_file(pages_dir, article, fetched_at, artifacts)
                if artifacts.hints:
                    stats.deprecation_flagged.append((ref.slug, artifacts.hints))

                entry = {
                    "title": article.title,
                    "source_url": article.ref.url,
                    "published_at": article.published_at,
                    "modified_at": article.modified_at,
                    "tags": [slug for slug, _ in article.tags],
                    "content_hash": article.content_hash,
                    "fetched_at": fetched_at if must_write else (old or {}).get("fetched_at", fetched_at),
                }
                if artifacts.hints:
                    entry["deprecation_hint"] = artifacts.hints
                new_pages[ref.slug] = entry

        print(f"[2/3] Fetching {len(refs)} articles (concurrency={args.concurrency})...", flush=True)
        await asyncio.gather(*(worker(r) for r in refs))

        # Skipped pages (no <article> upstream) are NOT removed from disk —
        # treat them like fetch failures for the on-disk file lifecycle so a
        # transient placeholder doesn't churn previously-known content.
        protected_slugs = {slug for slug, _ in stats.failed} | {slug for slug, _ in stats.skipped}
        removed_slugs, preserved_failed = compute_removed_slugs(
            old_slugs=set(old_pages),
            new_slugs=set(new_pages),
            failed_slugs=protected_slugs,
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
                "[3/3] Writing INDEX.md, index/by-tag/<tag>.md, summaries.json, "
                "CLAUDE.md, manifest.json...",
                flush=True,
            )
            (out_dir / "INDEX.md").write_text(
                render_main_index(successful_articles, section_source),
                encoding="utf-8",
            )
            (out_dir / "CLAUDE.md").write_text(CLAUDE_MD, encoding="utf-8")
            written, removed = write_tag_indexes(out_dir, successful_articles, section_source)
            stats.tag_indexes_written = len(written)
            stats.tag_indexes_removed = removed
            write_summaries(out_dir, summaries, generated_at=fetched_at, source=section_source)
            save_manifest(manifest_path, section_source, new_pages)
        else:
            print("[3/3] Dry run: skipping writes.", flush=True)

    print()
    print("Summary:")
    print(f"  added:     {len(stats.added)}")
    print(f"  updated:   {len(stats.updated)}")
    print(f"  unchanged: {len(stats.unchanged)}")
    print(f"  removed:   {len(stats.removed)}")
    print(f"  skipped:   {len(stats.skipped)}  (sitemap URL without <article>; not an error)")
    print(f"  failed:    {len(stats.failed)}")
    print(f"  flagged (deprecation_hint): {len(stats.deprecation_flagged)}")
    print(f"  tag indexes written: {stats.tag_indexes_written}")
    if stats.tag_indexes_removed:
        print(f"  tag indexes removed (stale): {len(stats.tag_indexes_removed)}")
        for n in stats.tag_indexes_removed:
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
    if stats.skipped:
        for slug, why in stats.skipped[:20]:
            print(f"    ? {slug}: {why}")
    if stats.failed:
        for slug, err in stats.failed[:20]:
            print(f"    ! {slug}: {err}")
        preserved_count = len(set(s for s, _ in stats.failed) & set(old_pages))
        if preserved_count:
            print(
                f"  preserved {preserved_count} previously-known article(s) "
                f"despite fetch failure (file kept on disk)."
            )

    return 1 if stats.failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--section",
        default="education",
        help="journal section under /journal/<section>/ (default: education)",
    )
    parser.add_argument("--out", default="journal", help="output directory (default: journal)")
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"parallel article fetches (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument("--full", action="store_true", help="rewrite every article even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing files")
    args = parser.parse_args()
    try:
        return asyncio.run(run(args))
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
