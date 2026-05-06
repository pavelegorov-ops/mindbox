---
title: Массовый импорт пулов промокодов
slug: "bulk-import-promocode-pools-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-promocode-pools-v3"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:fcd6ebed7ce95d68376b978fd9b97ed9179f0be47937fa9de79c3671443aca19"
---

# Массовый импорт пулов промокодов

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PromoCodeTypes.Import&csvCodePage=65001&folderSystemName={системное имя папки}&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- folderSystemName - системное имя папки, в которую добавляются новые пулы промокодов
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| ExternalId | Идентификатор пула промодков |
| Name | Наименования пула промокода |
| IssueStartDateTimeUtc | Дата начала выдачи пула промокодов в часовом поясе UTC + 0. |
| IssueEndDateTimeUtc | Дата окончания выдачи пула промокодов в часовом поясе UTC + 0. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PromoCodeTypes.Import&csvCodePage=65001&folderSystemName={системное имя папки}

Authorization: SecretKey *******
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalId;Name;IssueStartDateTimeUtc;IssueEndDateTimeUtc
1;Новый пул промокодов;2017-11-11 13:30:00;2017-12-11 13:30:00
```
