# Извлечение графа сценария из MindBox UI

Как достать полный список nodes/edges сценария из React Flow state и как
читать `filters_detail` для condition-блоков, не открывая каждый блок
кликом.

## Где находится state

Страница `https://<тенант>.mindbox.ru/scenarios/<id>/view` — это React Flow
поверх React 16 (на DOM-элементах висят ключи вида
`__reactInternalInstance$<key>`).

- На любом `.react-flow__node` ищи fiber-key `__reactInternalInstance$...`,
  поднимайся вверх по `f.return` и собирай `f.memoizedProps`.
- На глубине ~15 от ноды лежат `props.nodes` (≈все ноды сценария) и
  `props.edges` (≈все рёбра). React Flow **виртуализирует** ноды — в DOM
  рендерятся только видимые, в state есть все.

## Что лежит в `node.data.node`

- `id`, `name`, `type` ∈ {`schedule`, `operation`, `condition`, `delay`},
  `position {x, y}`, `attributes.hasMailingStep` (bool).
- Для `condition`: `data.conditionPreview = {entityDataPartType, id}` —
  **только id фильтра, не текст**. `entityDataPartType` маппится на
  `condition.context`: `Customer → customer`, нет = `action`
  (вебхук-условия).
- Для `delay`: `settings.initialDelayStrategySettings = {periodType: "Days",
  periodValue: N}`.
- Для `operation`: имя содержательное (`name`), но содержимое шага (имя
  email/push-шаблона, URL вебхука, имя сегмента) **в state НЕ хранится** —
  нужно открывать панель.

## Что лежит в `edges`

`{id, source, target, sourceHandle, targetHandle, label}`. Для condition
`label ∈ {"Да", "Нет"}`, для остальных `label = null`.

## Подгрузка `filters_detail`

При `?blockId=<uuid>` в URL правая панель открывается и подгружает фильтр
через React-фасад без отдельного REST-вызова (фильтры приходят с initial
scenario data + рендерятся фронтом). Подгрузка занимает **15–25 секунд**
при cold reload (загружается федеративный модуль `frontend_filters_v2`).

⚠️ Через `pushState + popstate` панель НЕ перерисовывается — нужен полный
`navigate` на новый URL.

## Как читать filter-текст из DOM

```js
const t = document.body.innerText;
const s = t.indexOf('Проверка выполнения условия');
const e = t.indexOf('Добавить фильтр', s);
const lines = t.slice(s, e).split('\n').map(l => l.trim()).filter(Boolean);
// lines[0] = "Проверка выполнения условия"
// lines[1] = context label ("По клиенту" / "По ответу вебхука" / ...)
// lines[2] = "Eще"  (всегда)
// lines[3..] = строки фильтра до "Добавить фильтр"
```

## Идентификация уникальных фильтров

В одном сценарии condition-блоки с одинаковым `name` обычно имеют
**разные** `conditionPreview.id`, но текст фильтра идентичен (это копии).
Безопасная эвристика: проверить один представитель каждого уникального
`name`, остальные — мапить на тот же текст. Это снижает количество
navigate-кликов с 50+ до 10–15.

## Pre-filters / раздел «Клиенты»

На schedule-сценариях ВИДНЫ в `/view`, если открыть панель schedule-блока
через `?blockId=<schedule-uuid>` — секция «Условия запуска» / «Клиенты /
Выбранные клиенты» показывает дерево фильтров с тем же
`Eще / Добавить фильтр / Сбросить фильтр` интерфейсом. Парсится через
тот же приём `slice('Клиенты\nВыбранные клиенты' .. 'Редактировать')`.
Для event-триггеров пре-фильтры могут быть в другом месте — пока не
проверял.

## Folder сценария

В URL `/scenarios/<id>/view` папки нет — она видна только в дереве на
`/scenarios`. У Usmall все триггерные сценарии лежат в одной папке
`Триггерные рассылки`.

## Режим `edit` vs `view`: отличия структуры нод

Всё вышеописанное проверялось на `/scenarios/<id>/view`. В режиме
`/scenarios/<id>/edit?version=draft` структура ноды **другая**, учти:

- Узел по-прежнему ищется по fiber-ключу `__reactInternalInstance$…` и
  `props.nodes` / `props.edges` лежат на той же глубине ~15 от ноды. Но
  **React Flow в edit-режиме держит в state только видимые ноды** —
  виртуализация агрессивнее, чем в view. Для больших сценариев полный
  список одним `props.nodes` не достать: нужно скроллить canvas и
  собирать инкрементально, либо искать исходный граф в
  `memoizedState`-хуках родительского компонента (обход всего дерева от
  корня через `.child`/`.sibling`, искать массивы с ключами
  `source`/`target` у edges и `data.node` у nodes).
- `node.data.node.type` в edit дополнен типом `comment` — это служебные
  комментарии на канве (`data: {comment: "1", x, y, ...}`), НЕ
  бизнес-логика. Фильтруй их (по `type === "comment"`) перед описанием
  сценария.
- Для `condition` текст фильтра лежит не в state, а читается из DOM
  открытой панели. Панель открывается навигацией на
  `?blockId=<node-uuid>` (id НОДЫ, не `conditionPreview.id`). Текст
  фильтра — между строкой `Eще` и `Добавить фильтр` (в view это было
  между `Проверка выполнения условия` и `Добавить фильтр`); ниже по
  панели идёт шум от AI-ассистента, его не парсить.
- Данные триггера (`inboundEvent`) лежат в `data.node.event` (например
  `{eventTypeSystemName: "SessionEnded", productLists: [{name:"Корзина"}]}`),
  операция (`operation`) — в `data.node.attributes.hasMailingStep`.

## Грабли чтения фильтров (выстраданы на сценарии 192495, view-режим)

Самые коварные затыки — не про React, а про сравнение строк и гонку
загрузки. Один раз перечитай, чтобы не переоткрывать заново:

- **«Еще» с ЛАТИНСКОЙ E.** Маркер строки — `Eще`, где первая буква —
  латинская `E` (char code **69**), а не кириллическая `Е` (**1045**).
  Сравнивай через `ord(line[0]) in (69, 1045)`, иначе barrier никогда не
  сработает и процесс молча зависнет в ожидании уже отрендеренного тела.
- **Барьер загрузки обязателен.** Без него читаешь DOM *предыдущей*
  страницы (все N фильтров вернут один и тот же текст первого). Жди все
  три условия сразу: (1) `location.href` содержит новый `blockId`,
  (2) `document.readyState === 'complete'`, (3) в `innerText` появилось
  тело фильтра (строка `Eще`). Холодный релоад федеративного модуля
  `frontend_filters_v2` — **до 59 сек**, ставь generous таймаут.
- **Webhook-условие без маркера.** Блок вида «Есть ответ от вебхука»
  (`entityDataPartType` отсутствует) НЕ имеет строки «Добавить фильтр» —
  у него другая панель («Условия» / «Статус ответа»). Снимать отдельным
  slice, не тем же парсером.
- **schedule / split в view не отдают содержимое.** У этих типов `name` и
  `event` в `props.nodes` приходят `null` — в state лежат только
  координаты. Содержимое (триггер, ветки, веса) надо снимать через
  панель `?blockId=` или из `memoizedState`-обхода, а не из `props.nodes`.
- **conditionPreview в view на уровень глубже.** В view-режиме фильтр-id
  лежит в `node.data.node.data.conditionPreview.id` (а не
  `node.data.node.data.conditionPreview`, как читает первый наивный
  clean). Снимай через полный `data.node.data.conditionPreview`.

## Подтверждение применимости

Применено в `Sc_Winback_CF1` (id=220216 в кабинете usmall.mindbox.ru):
123 ноды + 164 edges были извлечены одним JS-вызовом, 14 уникальных
filter-текстов прочитаны через 14 navigate'ов вместо 53.

Применено в `cooling_abandoned_basket` (id=250838, режим edit):
8 нод (4 логических + 4 comment) + 3 edges извлечены одним JS-вызовом,
2 condition-фильтра прочитаны через 2 навигации `?blockId=`. Сценарий
маленький — виртуализация не помешала.

Применено в `192495` (view-режим, 77 нод / 90 рёбер / 52 condition):
полный граф одним `Runtime.evaluate` за ~0.1с, все 52 filter-текста
прочитаны (поштучно, не по эвристике «имя=фильтр» — 52 уникальных
filter-id). Выстраданы 5 граблей выше (Latin-E, барьер загрузки,
webhook-без-маркера, schedule/split-null, глубина conditionPreview).
Чтение 52 фильтров заняло ~40 мин из-за 10–59с на холодную подгрузку
модуля фильтров на каждую навигацию.
