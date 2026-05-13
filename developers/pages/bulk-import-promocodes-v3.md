---
title: Массовый импорт промокодов
slug: "bulk-import-promocodes-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-promocodes-v3"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:e44d9b78218a5b50ff5f942b627f3cab90269e2c32ce620632f085f172cd15b5"
---

# Массовый импорт промокодов

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PromoCodes.Import&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- `csvCodePage` - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- `csvColumnDelimiter` - символ, использующийся для разделения колонок в CSV-файле.
- `csvTextQualifier` - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- `transactionId` - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Обязательность | Описание |
| --- | --- | --- |
| Code | ✅ | Значение промокода |
| CodeType | ❌ | Внешний идентификатор пула промокодов |
| UsedPointOfContact | ❌ | Внешний идентификатор [точки контакта](https://help.mindbox.ru/docs/point-of-contact-add), в которой погашен код. Заполнять только для погашенных кодов |
| AvailableFromDateTimeUtc | ❌ | Дата старта возможности использования |
| AvailableTillDateTimeUtc | ❌ | Дата окончания возможности использования |
| IssueStartDateTimeUtc | ❌ | Дата старта выдачи |
| IssueEndDateTimeUtc | ❌ | Дата окончания выдачи |
| UsedDateTimeUtc | ❌ | Дата использования |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PromoCodes.Import&csvCodePage=65001

Authorization: SecretKey **************
Accept: application/json
Content-Type: text/csv;charset=utf-8

Code;AvailableFromDateTimeUtc;AvailableTillDateTimeUtc;CodeType;IssueStartDateTimeUtc;IssueEndDateTimeUtc
e55be6785;2021-06-22 16:18:29.510;2021-06-25 16:18:29.510;promo-code-pool-5;2021-06-22 16:18:29.510;2021-06-27 16:18:29.510
```
