# Проект mindBox

Локальная база знаний для Claude Code, состоящая из двух частей:

- **Универсальный движок** — открытые скрейперы документации MindBox,
  генератор сценариев, slash-команды. Один и тот же для любого тенанта.
- **Бизнес-данные тенанта** — приватные данные конкретного тенанта
  (например, Usmall): описания триггерных сценариев, справочник параметров
  шаблонов рассылок. Лежат в `private/<имя>/` и приходят отдельным
  `git clone` приватного репозитория.

> **Терминология.** Везде в этой документации, slash-командах и путях
> `private/<имя>/` слово **«тенант»** означает один конкретный экземпляр
> MindBox у компании-клиента (Usmall, ACME, …). Слова «проект» и
> «компания» в этом значении не используются — это всегда «тенант».
> «Проект» — это сам репозиторий-движок (`mindBox`).

## Приветствие новых пользователей

Если пользователь впервые знакомится с проектом — спрашивает «что это
за проект?», «расскажи про проект», «как он работает?», «что внутри?»,
«с чего начать?» или похожее общее вводное — **прочитай `WELCOME.md`
в корне репо и ответь на основе его содержимого**, адаптировав под
чат (можно сократить, но обязательно сохрани раздел «Шаг 2 — настрой
среду» с предложением запустить `/bootstrap`).

Не используй WELCOME.md для конкретных предметных вопросов
(«как настроить сегмент…», «формат payload у webhook…») — на них
отвечай по корпусам `docs/` / `developers/` как обычно.

## Корпуса документации MindBox (общие)

Движок поддерживает три локальных Markdown-зеркала:

- **Help** (для маркетологов) с <https://help.mindbox.ru/docs/> →
  лежит в `docs/`.
- **Developers** (для интеграторов) с
  <https://developers.mindbox.ru/docs/> → лежит в `developers/`.
- **Journal** (для агента) с <https://mindbox.ru/journal/> → лежит в
  `journal/`, разделён на подкорпуса по секциям сайта:
  - `journal/education/` — учебные материалы (гайды, объяснения
    концепций).
  - `journal/cases/` — кейсы клиентов (что внедряли, какой результат).

  **Journal качается по запросу, а не всегда.** В дефолтный `/sync-docs`
  он не входит: пока за кейсами и статьями не пришли, держать их локально
  незачем (это ~950 страниц). Попросили — выгружаю сам
  (`/sync-docs --journal`, или одну секцию: `--journal cases`) и работаю
  с ними в `journal/<секция>/`. Отсутствие корпуса — норма, а не поломка:
  `check_freshness.py` показывает по нему `SKIP`, а не `MISSING`.

Зеркала читаются всеми тенантами одинаково. **Journal — материал для
тебя, агента**: при ответе человеку давай суть своими словами и
ссылку `source_url`, не пересказывай тело статьи. Подробные правила —
включая разные рамки для education и cases — в `journal/CLAUDE.md`.

## Структура проекта

- `scripts/` — все исполняемые файлы движка (Python-скрейперы, генератор
  сценариев, лаунчеры для Windows и macOS/Linux). Подробности ниже.
- `requirements.txt` — Python-зависимости (`httpx`, `markdownify`,
  `beautifulsoup4`, `pyyaml`). Лежит в корне, потому что `.venv/` тоже
  в корне.
- `.claude/commands/` — slash-команды для Claude Code:
  - `/sync-docs` — обновить базовые корпуса (`docs/`, `developers/`);
    журнал — только с флагом `--journal [education|cases]`. Вызывает
    `scripts/mindbox.bat` на Windows и `scripts/sync.sh` на macOS/Linux.
  - `/bootstrap` — первичная настройка среды: venv + проверки + smoke-test.
  - `/обнови-данные`, `/отправь-данные` — повседневные команды
    маркетолога: `git pull` / `git push` сразу в обоих репо.
- `docs/` — корпус Help. **Перед ответом на вопросы маркетолога читай
  `docs/CLAUDE.md`.**
- `developers/` — корпус Developers. **Перед ответом на интеграционные /
  API-вопросы читай `developers/CLAUDE.md`.**
- `journal/` — корпус Journal, разделённый на подкорпуса
  `journal/education/` (учебные материалы) и `journal/cases/` (кейсы
  клиентов). **Перед использованием читай `journal/CLAUDE.md`** —
  там правила: `summaries.json` для триажа в каждой секции, ответ
  человеку всегда с `source_url`, для education коротко (1–3
  предложения), для cases чуть подробнее (контекст + механики +
  результат), без пересказа тела статьи.
- `private/<имя>/` — данные конкретного тенанта (см. ниже).
- `notes/` — приёмы и грабли, которые невозможно вывести из кода. См.
  раздел «Дополнительные приёмы».
- `plans/` — утверждённые пользователем планы работ
  (`YYYY-MM-DD-описание.md`) с реестром в `plans/INDEX.md`.
- `scenarios/template.yaml`, `scenarios/schema.md` — общий шаблон и
  спецификация YAML-схемы сценариев (общие для всех тенантов).

### Скрипты в `scripts/`

Все вызывай **из корня репо** — пути в скриптах рассчитаны на это:

- `scripts/mindbox.bat` — **консольная команда** для маркетолога на
  Windows. Первый запуск: создаёт `.venv/` в корне репо, ставит
  `requirements.txt`, скачивает оба зеркала. Дальше — инкрементальное
  обновление. Прокидывает `--full` и `--dry-run` в оба скрейпера.
- `scripts/sync.sh` — то же для macOS/Linux.
- `scripts/sync.py` — оркестратор, который запускают launcher'ы. Можно
  вызывать напрямую, если зависимости уже стоят:
  `python scripts/sync.py [--full|--dry-run]`.
- `scripts/scrape_docs.py` — скрейпер `help.mindbox.ru` (Diplodoc). Флаги:
  `python scripts/scrape_docs.py [--full|--dry-run]`.
- `scripts/scrape_developers.py` — скрейпер `developers.mindbox.ru`
  (Zudoku). Те же флаги. По умолчанию `verify=False`, потому что у
  dev-сайта неполная TLS-цепочка; `--verify` — если есть свой trust store.
- `scripts/scrape_journal.py` — скрейпер журнала `mindbox.ru/journal/`.
  Источник — публичный `sitemap.xml`. Параметризуется секцией:
  `--section education` или `--section cases`; пишет в
  `journal/<section>/`. Те же флаги (`--full`, `--dry-run`).
  Оркестратор `sync.py` запускает обе секции автоматически.
- `scripts/enrich_journal.py` — LLM-обогащение journal-корпуса.
  Перезаписывает `summary_ru` + `key_points` в `summaries.json` обеих
  секций; для `cases` дополнительно строит `fact_index.json` и
  faceted-индексы `index/by-{mechanic,industry,kpi}/`. Требует
  `ANTHROPIC_API_KEY`. Идемпотентен: пропускает статьи с неизменённым
  `content_hash`. CLI: `--section cases|education`, `--full`,
  `--dry-run`, `--limit N` для отладки.
- `scripts/build_bm25.py` — собирает BM25-индекс по абзацам в
  `journal/<section>/search_index.pkl` (RU-лемматизация через
  `pymorphy3`, EN-стемминг через `nltk`). Офлайн, секунды на весь
  корпус. Файл индекса не коммитится (см. `.gitignore`).
- `scripts/journal_search.py` — query CLI поверх BM25-индекса,
  возвращает JSON для агента. Используй, когда грепа `summaries.json`
  и faceted-индексов мало (похороненные факты, RU↔EN gap). Пример:
  `python scripts/journal_search.py "удержание клиентов" --top 5`.
- `scripts/render_scenarios.py` — валидатор + генератор Markdown-карточек
  сценариев по YAML-источникам активного тенанта. Подробности — в
  разделе «Сценарии».
- `scripts/check_freshness.py` — проверка свежести корпусов: печатает
  OK/WARN/MISSING по базовым зеркалам (`docs`/`developers`) и `SKIP` по
  не выгруженному журналу (он по запросу), всегда выходит с кодом 0. Прогоняй из корня репо перед ответом из
  корпуса (см. правило 4 ниже). Чистый stdlib, fail-open.

## Тенанты

Бизнес-данные каждого тенанта живут в `private/<имя>/` и **не входят
в публичный репозиторий движка** (см. `.gitignore`). Каждый тенант — это
отдельный приватный git-репозиторий, склонированный в `private/<имя>/`.

Структура одного тенанта:

```
private/<имя>/
  engine.txt                         минимальная совместимая версия движка
  mailing-parameters/                справочник полей рассылок (с админки)
  scenarios/
    src/<id>.yaml                    сценарии — источник правды (YAML)
    rendered/                        Markdown-карточки, сгенерированные из YAML
  emails/transactional/              (опционально) HTML-снапшоты активных транзакционных писем + README-реестр
  emails/transfer_mailings/          (опционально) каскадные письма внутри сценариев (welcome, реактивация) + README-реестр
  mob_push/transactional/            (опционально) тексты активных транзакционных пушей (IOS+Android) + README-реестр
  mob_push/transfer_push/            (опционально) каскадные пуши внутри сценариев (IOS+Android) + README-реестр
  personalization/                   (опционально) формы персонализации (поп-апы, встроенные блоки, in-app): README-реестр + карточки + HTML-снапшоты
  backlog/                           (опционально) рабочие записки
```

`private/_template/` — публичный скелет нового тенанта; движок его
игнорирует (не считает активным).

**Активный тенант определяется автоматически**: если в `private/` лежит
ровно один подкаталог (кроме `_template/`), `scripts/render_scenarios.py`
берёт его. Если их несколько — нужен явный флаг `--tenant <имя>`. Если
ни одного — движок отчитывается «бизнес-данных нет» и не падает.

Подробнее, как добавить нового тенанта, — в `private/_template/README.md`.

## Где искать ответ

| Пользователь спрашивает про… | Куда смотреть |
| --- | --- |
| UI-проводки, сегменты, кампании, программу лояльности, маркетинговые фичи | `docs/` (Help) |
| HTTP API, SDK (JS/iOS/Android/Flutter/RN), POS-адаптеры, схемы импорта данных, вебхуки, push | `developers/` (Developers) |
| Кросс-концепт («что такое клиент / сегмент в MindBox») | Сначала `docs/summaries.json`, при отсутствии — `developers/summaries.json` |
| Маркетинговые подходы, концепции, идеи для механик (для вдохновения, не как продуктовая истина) | `journal/education/summaries.json` для триажа (`summary_ru`/`key_points`/`tag_titles_ru`), ответ кратко + `source_url` |
| Реальные истории клиентов: «кто внедрял такую механику», «какой получили результат» | `journal/cases/summaries.json` для триажа; `journal/cases/fact_index.json` + `index/by-mechanic\|industry\|kpi/` для запросов вида «у кого retention +30%»; ответ с контекстом + механиками + результатом + `source_url` |
| Похороненный в теле статьи факт; русский запрос про английский термин («удержание» ↔ «retention») | `python scripts/journal_search.py "<запрос>" [--section cases\|education]` — BM25 по абзацам с RU-лемматизацией |
| Поля шаблонов рассылок и сценариев активного тенанта (`Order.X`, `Recipient.Y`, `CustomField.*`) | `private/<активный>/mailing-parameters/` (см. `private/<активный>/mailing-parameters/CLAUDE.md`) |
| Конкретные триггерные сценарии тенанта | `private/<активный>/scenarios/` |
| Активные транзакционные email-рассылки тенанта (тема, прехедер, тело письма, история правок) | `private/<активный>/emails/transactional/README.md` — реестр; HTML-снапшоты рядом |
| Активные транзакционные мобильные пуши тенанта (заголовок, тело, deeplink, IOS/Android-пары) | `private/<активный>/mob_push/transactional/README.md` — реестр; тексты пар в `*_IOS.md` / `*_Android.md` |
| Каскадные email-рассылки тенанта (welcome, реактивация и т.п. — письма внутри триггерных сценариев) | `private/<активный>/emails/transfer_mailings/README.md` — реестр с привязкой к сценариям и аудиториям; HTML-снапшоты рядом |
| Каскадные мобильные пуши тенанта (внутри триггерных сценариев, IOS/Android-пары) | `private/<активный>/mob_push/transfer_push/README.md` — реестр с привязкой к сценариям; тексты пар в `*_IOS.md` / `*_Android.md` |
| Формы персонализации тенанта (поп-апы, встроенные блоки, in-app): настройки показа, таргетинг, условия, что выдаёт | `private/<активный>/personalization/README.md` — реестр; карточки форм в `popups/` (+ HTML-снапшоты) |

## Правила ответа на вопросы про MindBox

1. **Источник правды — локальный корпус, а не живой сайт.**
   `<corpus>/pages/*.md` — ground truth. Поле `source_url` во frontmatter —
   каноническая ссылка для цитаты пользователю.
2. **Сначала grep `<corpus>/summaries.json`, потом полные страницы.** В
   summaries есть title, section, лид-параграф и заголовки каждой страницы —
   это самый дешёвый способ выбрать кандидата.
3. **Уважай `deprecation_hint`.** Если у страницы во frontmatter есть это
   поле — добавь оговорку, что фича может быть устаревшей, и дай ссылку
   на `source_url` для подтверждения.
4. **Проверяй свежесть — и обновляй сам, не «предлагай».** `generated_at`
   в `<corpus>/manifest.json` — когда зеркало обновлялось последний раз.
   Перед ответом из корпуса прогони `python scripts/check_freshness.py`
   (из корня репо) — он печатает OK/WARN/MISSING по каждому корпусу и
   всегда выходит с кодом 0. Если по нужному корпусу WARN или MISSING —
   **запусти обновление сам** (`/sync-docs`, вручную —
   `scripts/mindbox.bat` на Windows / `scripts/sync.sh` на POSIX,
   инкрементально ~1–2 минуты) и отчитайся цифрами. Это read-only забор
   публичной документации — разрешения на него не спрашивают.
5. **Нет страницы в корпусе — сначала синк, потом веб** (для журнала —
   сначала вообще его выгрузить: `/sync-docs --journal`). Пустой результат
   поиска не доказывает, что материала нет: зеркало могло отстать (новая
   статья) или ты искал не тем инструментом (корпуса gitignored, обычный
   `grep`/ripgrep их не видит — нужен прямой путь или `rg --no-ignore`).
   Порядок: прямой путь `<corpus>/pages/<slug>.md` → grep по
   `<corpus>/summaries.json` → **обновить зеркало** → искать снова. Уход в
   веб — только после этого и с явной оговоркой пользователю.

## Сценарии (YAML → Markdown)

В этом репо лежит документация триггерных сценариев активного тенанта.
Источник правды — YAML, Markdown генерируется.

- `private/<активный>/scenarios/src/<id>.yaml` — один файл на сценарий,
  редактируется руками. Схема описана в корневом `scenarios/schema.md`,
  пустой шаблон — в `scenarios/template.yaml`.
- `private/<активный>/scenarios/rendered/` — выход `scripts/render_scenarios.py`:
  карточки сценариев (`<id>.md` с frontmatter, Mermaid-схемой и таблицами
  зависимостей), `INDEX.md` со списком, `dependencies.md` с обратным
  индексом «актив → сценарии», и `issues.md` с предупреждениями
  валидатора (включая кросс-проверки `[CROSS]` против `docs/summaries.json`).
- `scripts/render_scenarios.py` — валидатор + генератор. CLI (вызывать
  из корня репо):

  ```bash
  python scripts/render_scenarios.py                 # инкрементально для активного тенанта
  python scripts/render_scenarios.py --tenant usmall-mindbox # явный выбор (нужен при нескольких тенантах)
  python scripts/render_scenarios.py --full          # переписать все файлы
  python scripts/render_scenarios.py --dry-run       # показать, что изменится; ничего не пишет
  ```

  Идемпотентен: повторный запуск без изменений в YAML переписывает 0
  файлов. Возвращает код выхода `1`, если хоть один сценарий не прошёл
  валидацию.

**Когда что-то меняется в админке MindBox:** правишь YAML в
`private/<активный>/scenarios/src/`, запускаешь
`python scripts/render_scenarios.py`, коммитишь и `src/`, и `rendered/`
в приватный репо тенанта (или пользуешься `/отправь-данные`) — ревьюер
видит исходник и сгенерированный Markdown рядом.

## Дополнительные приёмы

- [notes/react-flow-extraction.md](notes/react-flow-extraction.md) — как
  вытащить nodes/edges/filters сценария из админки MindBox через React
  fiber и DOM. Почему `pushState` не работает (нужен `navigate`).
- [notes/personalization-extraction.md](notes/personalization-extraction.md) —
  как быстро (3 вызова) снять конфиг формы-персонализации (поп-ап
  PopMechanic): `get_page_text` + fiber (internalId сегментов из Redux) +
  `screenshot` (оффер-баннер); HTML тела в обход фильтра и тупики.
- [notes/customer-profile-extraction.md](notes/customer-profile-extraction.md) —
  как снять карточку клиента (`newcustomers/<id>`): быстрый обзор через
  `get_page_text` vs полный проверяемый дамп реплеем именованных
  GraphQL-операций (`POST /graphql?queryName=<Op>`, Bearer). Обнаружение
  операций через `performance` (не угадывать), скрытые internalId сегментов,
  история переходов с причиной, лента как журнал «на момент события»,
  правила полноты (пагинация/словари/errors/маскирование), аудит «почему
  получил/не получил коммуникацию», грабли перехвата и тупики.
- [notes/customer-filter-grammar.md](notes/customer-filter-grammar.md) — как
  **собрать** любой фильтр по клиентам (`newcustomers/customers/?filter=…`):
  конструктор зеркалит дерево условий в URL. Базовый цикл «собрать условие →
  Применить → прочитать URL», каркас языка (`and`/`or`/вложенность, скаляр
  `field(cv()filter-mode())`, коллекция `f(and())aggregate()`, сегмент `sid`),
  грабли (ИЛИ из UI ненадёжно попадает в URL — проверять счётчиком). Полная
  грамматика — в `../knowledge/reference/mindbox-фильтр-клиентов.md`.
- [notes/operations-extraction.md](notes/operations-extraction.md) — как
  снять список операций тенанта (Операции v3) и конфиг каждой: инвентарь
  через реплей `CustomerOperationsListQuery` (GraphQL, Bearer живёт ~5 мин),
  конфиг из скрытого `OperationTypeViewModel.JsonViewModel` (читать после
  React-гидрации, не из сырого HTML), спека запрос/ответ с `/help`. Две
  админки (`/newcampaigns/operations` SPA vs легаси `/campaigns/.../edit`),
  `id`≠`internalId`. Безопасность: `SecretKey`/`endpointId` в репо
  редактируем. Грабли `javascript_tool` (лимит вывода ~1000 симв.,
  биндинги REPL, async-IIFE) и фан-аут по вкладкам.
- [notes/ui-quirks.md](notes/ui-quirks.md) — известные глюки UI MindBox
  (например, «некорректное значение» в condition-фильтрах = ошибка
  отрисовки, надо перезагрузить страницу).
- [notes/yaml-schema-evolution.md](notes/yaml-schema-evolution.md) —
  история расширений YAML-схемы сценариев (что добавилось при
  описании первого реального сценария и почему).
- [notes/claude-behavior.md](notes/claude-behavior.md) — поведенческие
  правила для Claude в этом проекте (зеркало feedback-памяти из
  `~/.claude/projects/<проект>/memory/`). Все правила вида «коммить и
  пуш в обоих репо», «дублируй поведение в notes/» и т.п. живут здесь.

---

> Общие принципы кодинга (Karpathy) — в корневом `../CLAUDE.md` и `../.claude/behavior/`. Здесь не дублируем.
