# MindBox Developers — local mirror

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
