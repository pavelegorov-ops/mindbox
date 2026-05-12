# План: обогащение journal-корпуса для агента (A + B + C)

## Контекст

Сейчас корпус `journal/` (492 кейса + 383 учебных статьи) индексируется
плоским `summaries.json`, в котором `lead` — это `og:description` со
страницы. На практике это часто мусор уровня «1001 DRESS — российский
производитель платьев»: при триаже агент промахивается и читает не ту
статью.

Помимо этого есть три выявленные дыры:

1. **Лексический gap RU↔EN и морфология.** Запрос «удержание» не
   матчится на статью со словом «retention»; теги-транслит
   (`broshennaya-korzina`) не гриплются от русскоязычного запроса.
2. **Похороненные факты в кейсах.** «У кого retention вырос на 30%?»
   — цифра в теле статьи, не в `summaries`. Сейчас приходится читать
   десятки страниц.
3. **Кросс-синтез по кейсам.** «Какие механики чаще всего применяют
   fashion-ритейлеры?» требует читать 20+ статей.

Цель — **снизить токен-стоимость и повысить точность** ответов агента
по журналу. Никакой внешней инфраструктуры (vector store, embedding
сервисов). Всё derived data, регенерируется из `pages/*.md`,
коммитится в репо, чтобы изменения было видно при `git diff`.

## Подход — три слоя, все производные

### Слой A — обогащённые `summaries.json`

Заменить бесполезный `lead` на LLM-сгенерированный `summary_ru`
(1–2 предложения «о чём статья и что доказывает/учит») и
`key_points` (3–5 буллетов). Добавить `tag_titles_ru` уже в саму
запись summary (сейчас они в frontmatter страницы, но не в
`summaries.json`) — чтобы grep по «лояльность» матчился.

**Поля схемы `summaries.json` после изменений:**
```
slug, title, summary_ru, key_points[], headings, tags, tag_titles_ru,
published_at, modified_at, source_url, deprecation_hint
```

Поле `lead` удаляется (пользователей у него нет, кроме самого
скрипта). Все обращения в коде — пересмотреть.

### Слой B — fact-index для cases

Новый файл `journal/cases/fact_index.json` со структурированным
извлечением из каждого кейса:

```json
{
  "1001-dress": {
    "industry": "odezhda-i-obuv",
    "client_size_hint": "142000 клиентов в базе",
    "mechanics": ["welcome-chain", "broshennaya-korzina", "ab-testing", "email-newsletter-builder"],
    "kpis": [
      {"name": "open_rate", "delta_pp": 2, "period": "2 месяца"},
      {"name": "click_rate", "delta_pp": 1, "period": "2 месяца"}
    ],
    "operational_results": [
      {"name": "время на верстку", "before": "2 дня", "after": "2 часа"},
      {"name": "стоимость верстки", "before": "5000 ₽/письмо", "after": "0 ₽"}
    ],
    "time_to_value": "4 месяца",
    "channels": ["email"]
  }
}
```

Производные индексы:
- `journal/cases/index/by-mechanic/<mechanic>.md` — список кейсов на
  механику (`welcome-chain.md`, `broshennaya-korzina.md`, …).
- `journal/cases/index/by-industry/<industry>.md` — то же по нишам.
- `journal/cases/index/by-kpi/<kpi-name>.md` — кейсы, где есть метрика
  (для запросов «у кого вырос conversion»).

Извлечение строгое JSON-schema через Claude API; температура 0; если
кейс не содержит KPI — массив пустой (не выдумываем).

### Слой C — BM25-индекс по абзацам

Полнотекстовый поиск по чанкам обоих корпусов с RU-стеммингом.

- **Чанкование:** один абзац = один чанк, плюс инкорпорируем `slug`
  ближайшего H2/H3 как `section_title` для контекста сниппета.
- **Стеммер:** `pymorphy3` (RU-нормализация лемм), `Snowball` для
  EN. Фильтр стоп-слов RU+EN.
- **Алгоритм:** `rank-bm25` (чистый Python, без C-расширений → не
  усложняет setup на Windows).
- **Хранение:** `journal/<section>/search_index.pkl` — pickled
  `BM25Okapi` + `chunks.jsonl` с позициями чанков.
- **CLI:** `python scripts/journal_search.py "запрос" [--section
  cases|education] [--top 10]` → JSON `[{slug, source_url,
  section_title, snippet, score}]`. Агент вызывает через Bash, когда
  summaries-триаж не дал ответа.

## Изменения по файлам

### Новые скрипты (`scripts/`)

- `scripts/enrich_journal.py` — основной инструмент Слоёв A и B.
  CLI: `--section education|cases`, `--full`, `--dry-run`,
  `--limit N` для отладки. Идемпотентен: использует `content_hash`
  из `manifest.json` для пропуска неизменённых статей. Пишет в
  отдельный `enrichment_manifest.json`, чтобы не путать с
  scrape-манифестом.
- `scripts/build_bm25.py` — Слой C. Перестраивает индекс из всех
  `pages/*.md`. Бежит ~секунды на весь корпус.
- `scripts/journal_search.py` — query CLI поверх индекса.
  STDOUT — JSON-массив (для парсинга агентом и людьми).
- `scripts/_llm.py` — общий хелпер: инициализация Anthropic клиента,
  retry/backoff, structured output через
  `tool_use`/`response_format`. Не дублировать в каждом скрипте.

### Обновления существующего

- `scripts/sync.py` — после скрейпа двух секций оркестрировать:
  1. `enrich_journal.py --section education`
  2. `enrich_journal.py --section cases`
  3. `build_bm25.py` (обе секции)
  
  Если `ANTHROPIC_API_KEY` не задан — Слои A и B пропускаются с
  предупреждением, Слой C всё равно строится (он офлайн).

- `scripts/scrape_journal.py:293` (`build_artifacts`) и `:328`
  (`write_summaries`) — убрать `lead` из схемы. Сам скрейпер больше
  не отвечает за summary; он только пишет `pages/<slug>.md` и
  скелет `summaries.json` без `summary_ru` (заполнит
  `enrich_journal.py`).

- `scripts/_common.py` — `extract_lead` остаётся для других
  скрейперов (`scrape_docs.py`, `scrape_developers.py`), не трогаем.

- `requirements.txt` — добавить:
  ```
  anthropic>=0.40
  rank-bm25>=0.2
  pymorphy3>=2.0
  pymorphy3-dicts-ru>=2.4
  nltk>=3.8        # Snowball EN stemmer
  ```

- `journal/CLAUDE.md` — обновить раздел «Рекомендованный workflow
  поиска»: новый шаг 0 «глянуть `summary_ru` + `key_points` в
  `summaries.json`», новый шаг 3 «если не нашёл — `python
  scripts/journal_search.py "<запрос>"`», и описать
  `cases/fact_index.json` + `by-mechanic/`/`by-industry/`/`by-kpi/`.

- `CLAUDE.md` (корневой) — таблица «Где искать ответ»: расширить
  строку про cases, добавить упоминание `fact_index.json` и
  `journal_search.py`.

### Существующие функции для переиспользования

- `_common.atomic_write_text` — для записи всех новых JSON/MD.
- `_common.compute_removed_slugs` — управление жизненным циклом
  записей в `enrichment_manifest.json` (если статья удалена из
  `pages/`, удалить из обогащений).
- `scrape_journal.slugify_tag` — для создания slug'ов
  `by-mechanic/<mechanic>.md`.
- Шаблон `manifest.json` (формат `version`, `generated_at`,
  `pages: {slug: {content_hash, fetched_at}}`) — повторить структуру
  для `enrichment_manifest.json`, чтобы паттерн был узнаваемый.

## Стоимость и режимы работы

- **Полный enrichment** одного корпуса (875 статей):
  - Claude Haiku 4.5: вход ~5K токенов × 875 статей × ($0.80/M вход
    + $4/M выход @ ~500 токенов) ≈ **~$5–7 разовый** на оба корпуса.
- **Инкрементальный** запуск (после `sync.py`): обогащаются только
  статьи, у которых в `manifest.json` изменился `content_hash`.
  Обычно — единицы статей в день, копейки.
- **BM25-индекс** офлайн, ноль стоимости. Перестройка ~секунды.

## Этапы реализации (порядок)

1. **Каркас**: `scripts/_llm.py` + минимальный `enrich_journal.py`
   (только `summary_ru` + `key_points`), `enrichment_manifest.json`.
   Прогон на `--limit 10`, проверить качество вывода руками.
2. **Слой A полностью**: убрать `lead`, добавить `tag_titles_ru` в
   `summaries.json`, прогнать на оба корпуса, ревью diff в git.
   Обновить `journal/CLAUDE.md`.
3. **Слой B**: расширить `enrich_journal.py` для cases —
   `fact_index.json` + `by-mechanic/`/`by-industry/`/`by-kpi/`. Снова
   прогон на `--limit 10`, проверить, что схема стабильно
   соблюдается.
4. **Слой C**: `build_bm25.py` + `journal_search.py`. Тесты на
   нескольких реальных запросах из дыр №2 и №3.
5. **Интеграция**: `sync.py` оркестрирует всё; `requirements.txt`,
   docs, BOOTSTRAP про `ANTHROPIC_API_KEY`.

## Верификация

- **Слой A:**
  - `python scripts/enrich_journal.py --section cases --limit 5
    --dry-run` → распечатать 5 примеров `summary_ru`. Глазами
    проверить, что summary отвечает на «о чём» и «что доказывает».
  - `git diff journal/cases/summaries.json` после полного прогона —
    глазами выборочно посмотреть 10 случайных статей.
- **Слой B:**
  - `cat journal/cases/fact_index.json | jq '.["1001-dress"]'` —
    сверить с реальным содержимым статьи (KPI и operational_results
    должны совпасть с цифрами в теле).
  - Spot-check 10 случайных кейсов: 0 hallucinated KPI (если в теле
    нет цифр — массив пустой).
  - `ls journal/cases/index/by-mechanic/ | wc -l` ≈ 30–60 (разумно).
- **Слой C:**
  - `python scripts/journal_search.py "удержание клиентов" --section
    cases --top 5` — топ-результаты должны включать статьи про
    retention/lifetime/churn (тест на RU↔EN gap).
  - `python scripts/journal_search.py "open rate выросла на 30%"
    --section cases --top 5` — должно поднять кейсы с конкретными
    KPI (тест на похороненные факты).
- **Интеграция:**
  - `python scripts/sync.py` без `ANTHROPIC_API_KEY` — должен
    выполниться, скрейпинг и BM25 OK, A/B пропущены с warning.
  - `python scripts/sync.py` с ключом и без изменений в источнике —
    должен пропустить enrichment (0 LLM-вызовов), BM25
    переиндексирует за секунды.

## Риски и оговорки

- **Недетерминизм LLM-вывода.** Mitigate: `temperature=0`,
  structured output через `tool_use`. Drift всё равно возможен —
  поэтому `enrichment_manifest.json` хранит хеш входа (content +
  prompt version), и без изменений мы не пере-вызываем модель.
- **`pymorphy3` на Windows.** Имеет pre-built wheels, но проверить
  на этапе 1; если упрётся — fallback на простой `re.split` без
  стемминга (хуже качество, но работает).
- **Размер репо.** Pickled BM25-индекс по 26 MB корпуса → ~10 MB
  каждый. `journal/<section>/search_index.pkl` коммитится: при
  каждом scrape он перезаписывается, git его упакует в pack
  нормально, но репо подрастёт. Альтернатива — добавить в
  `.gitignore` и регенерировать локально (тогда первый запуск у
  нового пользователя занимает +30 секунд). **Рекомендация:
  добавить в `.gitignore`** — индекс полностью производный и быстрый
  в сборке.
- **Privacy кейсов.** Тела кейсов отправляются в Anthropic API. Это
  публичные статьи `mindbox.ru/journal/`, ничего конфиденциального.
  OK.
