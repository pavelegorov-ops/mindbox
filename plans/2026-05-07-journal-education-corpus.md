# Журнал MindBox (раздел «Учебные материалы») как локальный корпус для агента

> Утверждён: 2026-05-07. Источник: `~/.claude/plans/abstract-growing-kurzweil.md`.

## Context

В проекте `mindBox` уже есть два локальных Markdown-зеркала документации
(`docs/` — help.mindbox.ru, `developers/` — developers.mindbox.ru),
которые поддерживают скрейперы `scripts/scrape_docs.py` и
`scripts/scrape_developers.py`. Они используются Claude как источник
правды при ответах на вопросы про MindBox.

Пользователь хочет добавить **третий корпус** — ~71 статью раздела
[mindbox.ru/journal/education/](https://mindbox.ru/journal/education/),
чтобы агент мог использовать их как источник вдохновения и контекста
по маркетинговым темам. Материал предназначен **именно для агента**:
человеку финальный ответ — это ссылка на оригинал, а тело статьи
читается локально, чтобы сформировать ответ дёшево и без сетевых
запросов.

Раздел `/journal/education/` выбран осознанно — пользователь ограничил
скоуп им (cases/news пока не нужны). Скрейпер закладываем
расширяемым через параметр `--section`, но в рантайме гоняем только
education.

## Подтверждённое разведкой

- В `https://mindbox.ru/sitemap.xml` лежит **71 URL** с подстрокой
  `/journal/education/` — это публичный канонический список, RSS нет.
- Каждая статья — **SSR**: `<article class="editor-article">` уже
  содержит готовый HTML с `<h1>` + `<h2>` + параграфами + изображениями.
  Достаточно `httpx` + `beautifulsoup4` + `markdownify`, как в
  `scripts/scrape_docs.py` (Playwright не нужен).
- Метаданные в `<meta>`-тегах:
  - `og:title`, `og:description`, `og:image`
  - `article:published_time` (например `2023-03-03 00:00:00`)
  - `article:modified_time`
  - `article:section` — у всех статей одинаковое `Учебные материалы`,
    как фильтр бесполезно
- Теги — внутри статьи в виде `<a href="/journal/tag/<tag-slug>/">`.
  Это естественная категоризация: «AB-тесты», «Маркетинг», «Лояльность»
  и т. п. Заменяет TOC-иерархию из `docs/`.
- URL → slug тривиально: `/journal/education/<slug>/` → файл
  `journal/pages/<slug>.md`.

## Решения, принятые с пользователем

1. **Scope**: только `/journal/education/` (~71 страница).
2. **Layout**: `journal/` в корне репо, без вложенного `education/`-каталога
   (один корпус — одна папка). Если потом появится `cases/`, заведём
   рядом `journal-cases/` или вложенную структуру тогда.
3. **Команды**: новый `scripts/scrape_journal.py` + регистрируется в
   `scripts/sync.py`, чтобы `/sync-docs` обновлял все три корпуса.
4. **Артефакты под агента** (выбираю сам, человек не читает):
   - `summaries.json` — обязательно, главный инструмент дешёвого
     Grep-триажа (proven в `docs/`, `developers/`).
   - `index/by-tag/<tag-slug>.md` — один файл на тег со списком статей.
     Заменяет section-индексы из `docs/`.
   - `INDEX.md` — линейный список всех статей, отсортированный по
     `published_at` от свежих к старым.
   - `manifest.json` — служебная инкрементальность.
   - `backlinks.json` **не делаем** — статьи журнала почти не
     перекрёстно ссылаются друг на друга.

## Выходная структура `journal/`

```
journal/
  CLAUDE.md           инструкция для агента (русский)
  INDEX.md            линейный, отсортирован по дате убыв.
  manifest.json       version=1, format_version=1, page_count, pages{slug:{...}}
  summaries.json      карточки для Grep-триажа
  pages/<slug>.md     71 статья — одна на файл
  index/
    by-tag/<tag-slug>.md   индекс по тегу: список статей
```

## Формат `journal/pages/<slug>.md`

```yaml
---
title: <og:title без хвоста " - Журнал Mindbox...">
slug: <последний сегмент URL>
source_url: https://mindbox.ru/journal/education/<slug>/
published_at: 2023-03-03
modified_at: 2024-10-22
description: <og:description>
tags: [ab-testyi, omnical-maillings, ...]
tag_titles: ["AB-тесты", "Омниканальные рассылки", ...]
fetched_at: 2026-05-07T...Z
content_hash: sha256:...
deprecation_hint: ["устарел", ...]   # опционально
---

# <h1>

<тело article, markdownify>
```

Дополнительные правила:

- `<aside class="glossary">` → блок-цитата.
- Изображения остаются абсолютными CDN-ссылками.
- Внутренние ссылки на другие статьи журнала переписываются в
  относительные `<slug2>.md`, если `<slug2>` есть в нашем корпусе.
- Ссылки на `/journal/tag/...` оставляем абсолютными.
- Авторский блок не вытаскиваем — он остаётся в теле.

## `summaries.json` — схема

Поля карточки: `slug`, `title`, `lead`, `headings`, `tags`,
`published_at`, `modified_at`, `source_url`, `deprecation_hint`.
`lead` — первый параграф `paragraph_lead`, обрезанный до ~280 символов
с границей по слову (через `_common.extract_lead`). `headings` — все
`<h2>` из `<article>`.

## `journal/CLAUDE.md` — содержание

1. Что это за корпус и для кого.
2. Workflow ответов: `Grep summaries.json` → `pages/<slug>.md` →
   `index/by-tag/<tag>.md`.
3. **Правило для человека**: 1-2 предложения сути + `source_url`,
   тело статьи не пересказывать.
4. Свежесть: `published_at` старше 2020 — проверь актуальность.
5. `deprecation_hint` — стандартный хук.
6. Обновление: `python scripts/scrape_journal.py` или `/sync-docs`.

## `scripts/scrape_journal.py` — конструкция

Использует хелперы из `scripts/_common.py`: `detect_deprecation`,
`extract_lead`, `load_manifest_strict`, `render_frontmatter`,
`redact_secrets`, `page_filename`, `compute_removed_slugs`,
`atomic_write_text`, `format_fetch_error`.

CLI:

```
python scripts/scrape_journal.py [--section education]
                                 [--out journal]
                                 [--concurrency 8]
                                 [--full] [--dry-run]
```

Фазы:

1. **Discovery**: GET `mindbox.ru/sitemap.xml`, фильтр `<loc>` по
   `/journal/<section>/`, формирует список slug-ов.
2. **Fetch**: `httpx.AsyncClient` + `Semaphore(concurrency)`,
   `verify=True`, таймаут `Timeout(30.0, connect=10.0)`. На каждую
   страницу — `BeautifulSoup`, извлечение `<article>`, og/article
   meta, теги. `markdownify(heading_style="ATX", bullets="-",
   escape_asterisks=False)`. `content_hash` по нормализованному телу.
3. **Build artifacts**: `pages/<slug>.md` пишется только при изменении
   `content_hash` (или `--full`). `summaries.json`, `INDEX.md`,
   `index/by-tag/*.md`, `manifest.json` пишутся всегда.
4. **Cleanup**: исчезнувшие slug-и удаляются из `pages/` через
   `compute_removed_slugs` (защита от транзитных HTTP-фейлов).
5. **Reporting**: `added / updated / unchanged / removed / failed /
   flagged`.

`--dry-run`: пропускаем `Path.write_text` и `unlink`.

## Изменения в существующих файлах

- `scripts/sync.py:37-40`: добавить запись
  `("mindbox.ru/journal", SCRIPTS_DIR / "scrape_journal.py")`.
- `CLAUDE.md` (корень): расширить раздел «Корпуса» и таблицу «Где
  искать ответ»; «обновляет три корпуса» в описании `/sync-docs`.
- `requirements.txt`: проверить `beautifulsoup4` (уже есть).
- `.gitignore`: проверить, что `journal/` не задет (не задет).

## Verification

1. `python scripts/scrape_journal.py --dry-run` → discovered 71,
   would write 71 pages + indexes, файлов нет.
2. `python scripts/scrape_journal.py --full` → ~71 файла в
   `journal/pages/`, валидный JSON в `summaries.json`/`manifest.json`.
3. Повтор без флагов → `unchanged: 71, updated: 0`, `git status` пусто.
4. Read одной статьи → frontmatter с published_at/tags/source_url,
   тело начинается с `# <title>`, изображения и `<h2>` на месте.
5. `Grep "AB" journal/summaries.json -B 1 -A 5` → карточка статьи.
6. Read tag-индекса → список статей с этим тегом.
7. `python scripts/sync.py --dry-run` → три секции `=== ... ===`.
