# Проект mindBox

Локальная база знаний для Claude Code, состоящая из двух частей:

- **Универсальный движок** — открытые скрейперы документации MindBox,
  генератор сценариев, slash-команды. Один и тот же для любого тенанта.
- **Бизнес-данные тенанта** — приватные данные конкретной компании
  (например, Usmall): описания триггерных сценариев, справочник параметров
  шаблонов рассылок. Лежат в `private/<имя>/` и приходят отдельным
  `git clone` приватного репозитория.

## Корпуса документации MindBox (общие)

Движок поддерживает два локальных Markdown-зеркала:

- **Help** (для маркетологов) с <https://help.mindbox.ru/docs/>
- **Developers** (для интеграторов) с <https://developers.mindbox.ru/docs/>

Зеркала лежат в `docs/` и `developers/`, читаются всеми тенантами одинаково.

## Структура проекта

- `scripts/` — все исполняемые файлы движка (Python-скрейперы, генератор
  сценариев, лаунчеры для Windows и macOS/Linux). Подробности ниже.
- `requirements.txt` — Python-зависимости (`httpx`, `markdownify`,
  `beautifulsoup4`, `pyyaml`). Лежит в корне, потому что `.venv/` тоже
  в корне.
- `.claude/commands/` — slash-команды для Claude Code:
  - `/sync-docs` — обновить корпуса доков (вызывает `scripts/mindbox.bat`
    на Windows и `scripts/sync.sh` на macOS/Linux).
  - `/bootstrap` — первичная настройка среды: venv + проверки + smoke-test.
  - `/обнови-данные`, `/отправь-данные` — повседневные команды
    маркетолога: `git pull` / `git push` сразу в обоих репо.
- `docs/` — корпус Help. **Перед ответом на вопросы маркетолога читай
  `docs/CLAUDE.md`.**
- `developers/` — корпус Developers. **Перед ответом на интеграционные /
  API-вопросы читай `developers/CLAUDE.md`.**
- `private/<имя>/` — данные конкретного тенанта (см. ниже).
- `notes/` — приёмы и грабли, которые невозможно вывести из кода. См.
  раздел «Дополнительные приёмы».
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
- `scripts/render_scenarios.py` — валидатор + генератор Markdown-карточек
  сценариев по YAML-источникам активного тенанта. Подробности — в
  разделе «Сценарии».

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
| Поля шаблонов рассылок и сценариев активного тенанта (`Order.X`, `Recipient.Y`, `CustomField.*`) | `private/<активный>/mailing-parameters/` (см. `private/<активный>/mailing-parameters/CLAUDE.md`) |
| Конкретные триггерные сценарии тенанта | `private/<активный>/scenarios/` |

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
4. **Проверяй свежесть.** `generated_at` в `<corpus>/manifest.json` —
   когда зеркало обновлялось последний раз. Если вопрос про что-то, что
   могло недавно измениться, предложи `/sync-docs`.

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
  python scripts/render_scenarios.py --tenant usmall # явный выбор (нужен при нескольких тенантах)
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
