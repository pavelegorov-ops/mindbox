# Эволюция YAML-схемы сценариев

`private/<тенант>/scenarios/src/<id>.yaml` → `scripts/render_scenarios.py` →
`private/<тенант>/scenarios/rendered/<id>.md` + INDEX/dependencies/issues.

Реализовано в задаче S-1 первоначального backlog'а.

## Принцип

YAML — единый источник правды, рендер — детерминированный (идемпотентный).
Схема расширялась по мере встречи с реальными сценариями.

**Правило при описании нового сценария:** если конструкция из MindBox UI
не выражается текущей схемой — расширить валидатор и схему, а не
«сжимать» сценарий в существующее. Каркас бери из `scenarios/template.yaml`,
справочник полей — `scenarios/schema.md`.

## Расширения, появившиеся при описании первого реального сценария (`Sc_Calendar_HealthLover_AF1`)

### 1. `trigger.schedule` — подобъект расписания

```yaml
schedule:
  mode: daily | weekly | monthly
  time: "HH:MM"
  timezone: Europe/Moscow      # IANA
  weekdays: [mon, tue, ...]    # для weekly
  days: [1, 15]                # для monthly
  day_of_month: 1              # альтернатива days для monthly
```

Раньше был только заглушкой.

### 2. `trigger.pre_filters` — стал объектом

Теперь `{summary: str, detail?: list}`, а не `list[str]`. Реальные
фильтры MindBox («Подписан в бренде X в канале Y в тематике Z», нескольких
уровней AND/OR) не укладываются в плоский список меток. `summary`
обязателен, multiline. `detail` — для будущих структурных представлений.

### 3. `block.name` (опц.)

Имя блока из MindBox UI (типа `Trg_Calendar_HealthLover_S1_AF1`). Не
валидируется, рендерится в карточку. ID блока остаётся коротким (`B1`,
`B2`...) для читаемости диаграмм.

### 4. `condition.filters_detail` — стал гибче

Принимает либо `list[str]` (построчно как в UI), либо `list[dict]`
произвольной формы. Раньше требовал жёсткий `{field, op, value}` —
реальные фильтры в этот shape не уложились.

### 5. `dependencies` дополнены тремя категориями

- `excludes_scenarios` — кросс-сценарные исключения («Не проходил
  сценарий X»).
- `product_categories` — категории продуктов с ID, формат
  `"Health (1147)"`.
- `brands` — бренды из условий подписки/сегментов.
- Также добавлены `push_templates`, `viber_templates`, `wallet_templates` —
  раньше упоминались в `STEP_KIND_TO_DEPS`, но не входили в
  `_REQUIRED_DEP_KEYS` (баг — push-шаблоны не попадали в обратный индекс).

## Полезные факты про корпус сценариев Usmall

- **Naming convention:** `Trg_<TriggerType>_<Audience>_<Stage>_<Variant>`
  (`Trg_Calendar_HealthLover_S1_AF1`). Один и тот же базовый id
  используется и для имени блока в Mindbox, и для имени email-шаблона;
  для push-шаблонов добавляется `_IOS` или `_Android`.
- **Архетип каскада:** многоступенчатый nurture с проверкой
  «Оплаченный заказ до сих пор один?» между ступенями (если докупил —
  выход в `stop_purchased`); в каждой ступени — email + iOS push +
  Android push с проверками платформы.
- **Контексты условий:** `customer` (большинство), реже `action` (для
  проверок «было открытие письма»).
