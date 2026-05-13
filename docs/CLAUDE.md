# MindBox Help — local mirror

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
