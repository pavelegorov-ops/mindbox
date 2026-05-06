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

## Подтверждение применимости

Применено в `Sc_Winback_CF1` (id=220216 в кабинете usmall.mindbox.ru):
123 ноды + 164 edges были извлечены одним JS-вызовом, 14 уникальных
filter-текстов прочитаны через 14 navigate'ов вместо 53.
