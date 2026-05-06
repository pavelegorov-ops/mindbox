# Схема YAML для триггерных сценариев MindBox

Документация полей для людей. Не JSON Schema.

YAML-файл живёт в `private/<тенант>/scenarios/src/<id>.yaml`. После
редактирования запускай `python scripts/render_scenarios.py` (из корня
репо) — скрипт валидирует исходники и генерит Markdown-карточки, INDEX,
обратный индекс зависимостей и список варнингов в
`private/<тенант>/scenarios/rendered/`.

**Источник правды по типам блоков** —
[`docs/index/scenarii.md`](../docs/index/scenarii.md).

## Соглашение по языку ключей

- Технические ключи и enum-значения — латиница: `type`, `edges`, `kind: email`,
  `mode: regular`, `context: customer`.
- Свободный текст и UI-метки веток — русский: `title`, `notes`, `summary`,
  `до_лимита`/`после_лимита` для `limit`-блока.

Это сознательное решение: метки веток приходят с UI MindBox, переводить
их — путать пользователя.

## Корневые поля

| Поле | Обязательно | Тип | Описание |
|---|---|---|---|
| `id` | да | string | Уникален среди всех файлов в `src/`. Латиница, цифры, дефисы. Совпадает с именем файла без расширения. |
| `title` | да | string | Человекочитаемое название (из MindBox UI). |
| `folder` | да | string | Папка в дереве сценариев MindBox, например `/welcome`. |
| `status` | да | enum | `enabled` \| `draft` \| `stopped` |
| `notes` | нет | string | Свободный текст: контекст, история изменений, ссылка на задачу. |
| `trigger` | да | map | См. ниже. |
| `blocks` | да | list | Минимум 1 элемент. См. ниже. |
| `ends` | да | map | Локальный словарь концевых узлов: `<id>: <человеческое описание>`. |
| `dependencies` | да | map | Объявляются для обратного индекса. Все 7 категорий обязательны как ключи (можно пустыми списками). |

## `trigger`

| Поле | Обязательно | Описание |
|---|---|---|
| `type` | да | `event` \| `schedule` |
| `event` | да при `type=event` | ID события из доки MindBox (например `customer_registered`). |
| `schedule` | да при `type=schedule` | Объект, см. ниже. |
| `pre_filters` | нет | Объект `{summary, detail?}`, см. ниже. |
| `frequency_per_customer` | нет | `once` \| `every` \| `per_period` |
| `per_period` | да при `frequency_per_customer=per_period` | Мапа с `every: <duration>`. |
| `frequency_per_order` | нет | те же значения или `null`. |

### `trigger.schedule`

Обязателен при `trigger.type: schedule`.

| Поле | Обязательно | Описание |
|---|---|---|
| `mode` | да | `daily` \| `weekly` \| `monthly` |
| `time` | да | Строка `HH:MM`, например `"14:10"`. |
| `timezone` | да | IANA-id, например `Europe/Moscow`. |
| `weekdays` | да при `mode=weekly` | Список из `mon, tue, wed, thu, fri, sat, sun` (≥1). |
| `days` | да при `mode=monthly` (или `day_of_month`) | Список целых, например `[1, 15]`. |
| `day_of_month` | альтернатива `days` | Произвольная метка, например `last`. |

```yaml
trigger:
  type: schedule
  schedule:
    mode: daily
    time: "14:10"
    timezone: "Europe/Moscow"
```

### `trigger.pre_filters`

Описывает условия отбора клиентов на запуске сценария (раздел «Клиенты» в
MindBox UI). Объект:

| Поле | Обязательно | Описание |
|---|---|---|
| `summary` | да | Многострочная человекочитаемая текстовка дерева фильтров. По одной строке на узел/группу. |
| `detail` | нет | Список любой формы — структурный дамп если нужно (валидатор не интерпретирует). |

```yaml
pre_filters:
  summary: |
    Email заполнен и валидный
    Подписан на канал Email в тематике Триггерные письма
    Заказ ≥1 шт со статусом Доставлен
```

Структурное дерево с AND/OR-группами и квантифицированными подфильтрами
сейчас НЕ типизировано — пиши в `summary` свободно. Если потом понадобится
машинная обработка — добавим типизированный формат отдельной задачей.

## `blocks`

Список блоков. Каждый блок:

| Поле | Обязательно | Описание |
|---|---|---|
| `id` | да | Уникален в пределах файла. По соглашению — `B1`, `B2`, ... |
| `type` | да | См. таблицу ниже. |
| `name` | нет | Имя блока в UI MindBox (например `Trg_Calendar_HealthLover_S1_AF1`). Используется для трассируемости — рендерится в карточку блока. |
| `edges` | да | Куда ведут стрелки. Структура зависит от `type`. |

Можно добавлять любые произвольные поля сверху минимально-обязательных —
валидатор их не трогает.

### Поддерживаемые типы блоков

| `type` | Обязательные поля | `edges` |
|---|---|---|
| `condition` | `mode` (`regular`\|`multibranch`), `context`, `summary` | regular: `{yes, no}`; multibranch: произвольные ключи + опц. `other` |
| `steps` | `actuality`, `steps` (>=1) | `{next}` обязателен; `{on_fail}` опционален |
| `delay` | `mode` (`fixed`\|`interval`\|`dynamic`); fixed→`duration`; dynamic→`source`+`field_name`+`offset` | `{next}` обязателен; `exit_window` опц. на корне блока |
| `splitter` | `branches` (>=2, каждая с `weight` и `next`) | формируется из branches |
| `ab_test` | `hypothesis`, `primary_metric`, `variants` (>=2, каждая с `share` и `next`) | формируется из variants |
| `limit` | `quantity`, `period`; `notify_threshold` опц. | `{до_лимита, после_лимита}` обе обязательны |

### `condition` — `summary` и `filters_detail`

Каждый condition обязан иметь `summary: "..."` — человекочитаемую строку
(заголовок блока в UI MindBox).

Опционально можно добавить `filters_detail`. Принимаются две формы:

**Строки — построчно как в UI MindBox** (рекомендуется для сложных фильтров,
которые не укладываются в `field/op/value`):

```yaml
filters_detail:
  - "Email заполнен и валидный"
  - "Подписан в бренде Usmall в канале Email в тематике Триггерные письма"
```

**Структурированно** — для критичных условий, где нужна точность:

```yaml
filters_detail:
  - { field: email.subscribed, op: "=", value: true }
  - { field: email.valid,      op: "=", value: true }
```

Можно смешивать строки и словари в одном списке. Если в словаре есть все
три ключа `field`, `op`, `value` — рендерится как `\`field\` \`op\` \`value\``;
иначе как `key1=v1, key2=v2`.

### `steps[]` — минимально-обязательные поля по `kind`

| `kind` | Required | Куда попадает в `dependencies` |
|---|---|---|
| `email` | `template` | `email_templates` |
| `sms` | `template`, `pool` | `sms_templates` + `promo_pools` |
| `viber` | `template` | `viber_templates` (если объявлен) |
| `push` | `template` | `push_templates` (если объявлен) |
| `wallet` | `template` | `wallet_templates` (если объявлен) |
| `webhook` | `url` | `webhooks` |
| `edit_customer` | `set` (мапа) | ключи `set` идут в `custom_fields` |
| `change_balance` | `amount` | — |

Неизвестный `kind` — warning «Unknown step kind: X» в `issues.md`, но не
error.

### `on_fail`

Поддерживают только блоки `steps` (и шаг `kind: webhook` внутри `steps`,
неявно через сам блок). Для `delay`, `limit`, `condition`, `splitter`,
`ab_test` — error.

## `ends`

```yaml
ends:
  done_ok:            "Каскад завершён"
  stop_no_email:      "Email затёрли"
```

Валидатор проверяет двунаправленную связность:

- каждый ключ из `ends` должен встретиться хотя бы в одном `edges.*`;
- каждое значение в `edges`, не являющееся ID блока, должно быть объявлено
  в `ends`.

## `dependencies`

Все тринадцать категорий обязательны как ключи (можно пустыми):

```yaml
dependencies:
  email_templates:    []           # шаблоны рассылок: email
  sms_templates:      []           # шаблоны рассылок: sms
  push_templates:     []           # шаблоны мобильных пушей
  viber_templates:    []           # шаблоны Viber
  wallet_templates:   []           # шаблоны Wallet (Apple/Google)
  action_templates:   []           # шаблоны действий (action)
  segments:           []           # сегменты клиентов
  promo_pools:        []           # пулы промокодов
  webhooks:           []           # вебхуки (URL)
  custom_fields:      []           # доп. поля клиента/заказа
  excludes_scenarios: []           # сценарии, после которых клиент сюда НЕ заходит
  product_categories: []           # категории продуктов, формат свободный, напр. "Health (1147)"
  brands:             []           # бренды, упомянутые в условиях подписки/сегментах
```

Это даёт обратный индекс «что сломается, если удалить шаблон/сегмент/пул X»
в `rendered/dependencies.md`. Все значения — строки; для категорий продуктов
и брендов записывай человекочитаемо («Health (1147)», «Usmall»).

## Что проверяет валидатор

**Errors (рендер сценария НЕ создаётся, exit code 1):**

- Дубликаты `id` сценария между файлами.
- Дубликаты `id` блока внутри файла.
- Битые `edges` — ссылка на несуществующий блок или ключ из `ends`.
- Неизвестные значения в enum-полях.
- Не выполнены обязательные поля по типу блока.
- Блоки без входящих ссылок (мёртвые), кроме первого блока.
- Концевые узлы из `ends` без использования в `edges`, и наоборот.
- `on_fail` на типе блока, который его не поддерживает.
- `frequency_per_customer: per_period` без `per_period.every`.

**Warnings (рендер создаётся, попадают в `rendered/issues.md`):**

- АБ-тест с разной длиной задержки в ветках.
- `condition` между `ab_test` и его `steps` (искажает чистоту замера).
- `delay.duration` >30d без `exit_window`.
- Неизвестный `kind` в `steps[]`.
- Cross-check с `docs/summaries.json` (помечен `[CROSS]`):
  - Событие из `trigger.event` не найдено в локальном корпусе MindBox docs.
  - Использование функции с `deprecation_hint` на странице доки.

## Как добавить новый сценарий

1. Скопируй `scenarios/template.yaml` (общий шаблон в корне репо) в
   `private/<тенант>/scenarios/src/<id>.yaml`.
2. Заполни поля. Минимально нужны: `id`, `title`, `folder`, `status`,
   `trigger`, `blocks` (>=1), `ends`, `dependencies`.
3. Запусти `python scripts/render_scenarios.py` (из корня репо).
4. Проверь `private/<тенант>/scenarios/rendered/<id>.md` и
   `private/<тенант>/scenarios/rendered/issues.md`.
5. Закоммить и `src/<id>.yaml`, и весь `rendered/` в приватный репо
   тенанта — PR-review должен видеть и YAML, и сгенерированный Markdown.

## Как запустить рендер

```bash
python scripts/render_scenarios.py             # инкрементально: только изменённые файлы
python scripts/render_scenarios.py --full      # переписать всё принудительно
python scripts/render_scenarios.py --dry-run   # отчёт без записи
```

Idempotency: повторный запуск без изменений YAML не должен переписать ни
байта в `rendered/`.
