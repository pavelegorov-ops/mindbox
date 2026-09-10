# Write-контракты редактирования сценариев MindBox (REST)

Как программно менять триггерный сценарий в админке MindBox. Разведено на
сценарии 250838 (`cooling_abandoned_basket`, usmall.mindbox.ru) в режиме
edit. Метод — перехват клиентского кода + read-only реплей; **ни одна
запись не выполнялась**, поэтому write-контракты ниже восстановлены из
загруженного JS и read-снимков, а НЕ из перехваченных POST-запросов.

## Главный вывод

Основное редактирование сценария идёт через **REST, не GraphQL**. База —
`https://scenarios.g.mindbox.ru`. GraphQL используется только для чтения
(см. ниже). Отдельной GraphQL-mutation публикации/сохранения графа/блока
**не обнаружено**.

## Контракты записи (из клиентского кода, НЕ выполнены)

Все изменения — `POST`, JSON-тело, без `queryName`.

| Назначение | Endpoint | Тело |
|---|---|---|
| Создание сценария | `/scenario/{folderInternalId}/createNew` | аргументы после удаления folderInternalId; UI передаёт brandExternalId; shouldOpenBlockEditor удаляется моделью |
| Сохранение графа/черновика | `/scenario/{id}?versionNumber={n}` | объект сценария: blockIdToBlocksViewModel, connections, rowVersion, метаданные |
| Сохранение condition/блока | `/scenario/saveBlock/{id}?versionNumber={n}` | `{block:{...settings,name,coordinates},repeatSettings?,rowVersion}` |
| Стартовый блок | `/scenario/saveStartBlock/{id}?versionNumber={n}` | тот же wrapper; выбор endpoint зависит от типа блока |
| Новый черновик | `/scenario/{id}/draft/new?versionNumber={n}` | `{rowVersion,adminSiteMetricsTransaction?}` |
| Запуск версии | `/scenario/{id}/launch?versionNumber={n}` | `{rowVersion,adminSiteMetricsTransaction?}` |
| Проверка готовности | `/scenario/{id}/version/ready-for-execution?versionNumber={n}` | `{rowVersion}` — POST со сменой статуса, НЕ read-only |
| Импорт структуры | `/scenario/{id}/import?versionNumber={n}` | `structure`; полная форма не установлена |

## Структура saveScenario (граф/черновик)

Mapper включает: `id`, `folderInternalId`, `brandExternalId`, `name`,
`blockIdToBlocksViewModel`, `connections`, `rowVersion`, `status`,
`versionNumber`, `editedByStaffDateTimeUtc`, `statusPlannedDateTimeUtc`,
`isVersionCloning`, `folderSegmentExternalId`, `scenarioProcessingType`,
`mode`.

API удаляет перед отправкой: `warnings`, `throttlingStatus`,
`potentialTransactionalInfo`, `throttledInfo`.

**Connections** сериализуются как `{id, inputId: targetPortId, outputId:
sourcePortId}` — это НЕ React Flow edges напрямую.

## Condition-блок

- Чтение: `GET /scenario/250838/{blockId}?versionNumber=1` → HTTP 200,
  тип `fullCondition`, вложенный `condition.$type = filterConditionViewModel`.
- Дерево фильтра: `condition.filter.filterViewModel`; в save-wrapper это
  `block.condition.filter.filterViewModel`.
- Блок содержит полный `settings`, `name`, `coordinates`; `rowVersion`
  берётся со сценария.
- Формат filterViewModel — вложенные `innerConditions` с узлами
  `{entityType, filterFactory, value:{mode:"concrete", value:...}}` и
  `aggregationStrategyViewModel.$discriminator` ∈ {any, none}. Живой пример
  снят в `condition_read_replay.json` (в артефактах разведки).

## Автосохранение (опасно при наблюдении)

Клиент сохраняет **немедленно** при `createNode` и с **debounce 750 мс**
при `updateNode/removeNode/createEdge/updateEdge/removeEdge`, с проверкой
readonly/status. У block settings — собственный save effect. Поэтому даже
«подвинуть блок ради перехвата» уже есть запись. Новый черновик при
существующей development-версии может предварительно удалить её — этот
UI-handler не вызывать в разведке.

## GraphQL — только чтение

- `ScenariosLoadInfoByIdsQuery` — `POST .../graphql?queryName=...`,
  переменные `{scenarioIds:[250838], sortOptions, tenant:"Usmall"}`.
  Реплей read-only с `credentials: omit` → HTTP 200, `errors: []`.
- `ScenarioMailingStepsQuery` — типы AST: `scenarioId: Int!`,
  `versionNumber: Int!`.
- `AIAssistantConsentQuery` — на `ai-assistant-rnd.g.mindbox.ru`, к
  сохранению сценария не относится.

GraphQL-mutations сценария (только статический AST, не перехвачены):
- `ScenarioVersionCreateCommentMutation` / `...Update...` / `...Delete...`
  — комментарии канвы, НЕ бизнес-блоки/условия.
- `SaveScenarioSummaryReportMetricsMutation`, `NotificationSettingsMutation`
  — отчётность/уведомления, не граф.

## Транспорт и авторизация

- GraphQL: `POST <service>/graphql?queryName=<имя>`, JSON
  `{operationName, variables, query}` (query целиком из перехвата, с fragments).
- Заголовки: `authorization: Bearer ...`, `accept: application/json`,
  `content-type: application/json`, `accept-language: ru-RU`,
  `x-product-feature: Scenarios`.
- Read-реплей GraphQL и REST GET работают с `credentials: omit` → cookies
  для чтения не требуются (write-endpoint'ы не проверялись).
- Токен: `window[Symbol.for('__mindbox_authToken')].Token`.
- JWT живёт **300 секунд**; клиент обновляет при остатке <60с.
- Получение токена: `GET /token?t=<Date.now()>` на usmall.mindbox.ru
  (`same-origin`, `no-store`, `redirect: manual`). Если логин истёк —
  входит пользователь, агент вход не обходит.

## Как реплеить сохранение (порядок)

1. Согласовать тестовый сценарий/версию и точное изменение.
2. Включить Network до санкционированного сохранения; захватить реальный
   REST POST (тело + ответ). Без wire-образца payload собирается по коду.
3. Прочитать свежие GET сценария и блока → актуальный `versionNumber` и
   `rowVersion` (не брать устаревший).
4. Взять свежий Bearer из страницы.
5. Для condition менять только согласованную часть
   `block.condition.filter.filterViewModel`, сохранить остальные поля
   wrapper и идентификаторы. Для графа использовать backend
   map/connections, не React Flow nodes/edges.
6. Выполнить `fetch` абсолютного REST endpoint, `POST`, JSON-тело, Bearer.
   Не подменять выдуманной GraphQL-mutation; не запускать launch авто.
7. Проверить HTTP и бизнес-ответ `status`/`validationMessages`/
   `blockContentValidationMessages`. При `ChangeConflict` — остановиться и
   перечитать, не затирать.
8. После записи прочитать тот же target через GET и проверить изменение,
   rowVersion, status, отсутствие посторонних правок.

## Снимок сценария 250838 на момент разведки

- id 250838, versionNumber 1, developmentVersionNumber 1.
- status `ReadyForExecution`, mode Default, brandExternalId 1.
- folderInternalId `e17df97c-b420-4ba0-b777-a971d675a74b`.
- endpointExternalId `IE-Usmall-Usmall`.
- rowVersion `22waHA==` (на 2026-09-08; конкурентный токен, перед записью
  читать заново).
- 4 блока: 2 condition + 1 inboundEvent + 1 operation; 3 connection.

## Что НЕ установлено

- Реальные сетевые payload/ответы при изменении/сохранении/создании/
  публикации (запись не инициировалась).
- Успешность write-replay, серверные обязательные поля, все input/enum
  схемы, идемпотентность, обязательность telemetry-поля.
- Полный список запросов первоначального открытия (позднее подключение CDP).
- Server schema/introspection (не запрашивался).

## Артефакты разведки

`C:/Users/user/AppData/Local/Temp/mindbox_edit_recon/`:
- `report.md` — полный отчёт (источник этой заметки).
- `scenario_read.json` — GET сценария + списка версий.
- `condition_read_replay.json` — полный формат condition-фильтра.
- `graphql_read_replay.json` — реплей ScenariosLoadInfoByIdsQuery.
- `captures.jsonl` — реальные запросы (заголовки очищены).
- `static_operations.json` — извлечённые AST.
- `script_63.js` (REST API слой, base client), `script_62.js` (block save,
  graph mapper, auto-save), `script_50.js` (comments mutations, create UI).
