---
title: Массовый импорт каналов
slug: "bulk-import-channels-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-channels-v3"
breadcrumb:
  - "Точки контакта, магазины, зоны"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0652c3ab06cb99e3018d528c8a3ff0afb4ff6fb1cfb9164cc808586a03cd996d"
---

# Массовый импорт каналов

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Channels.Import&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| ExternalId | Идентификатор канала. Например, "15" |
| Name | Название канала. Например, "Москва" |
| Comment | Описание канала |
| ParentChannelExternalId | Идентификатор родительского канала. Родительский канал используется для создание иерархии, например регион → город → магазин. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Channels.Import&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalId;Name;Comment;ParentChannelExternalId
15;Москва;Столица;1
1;Центральный регион;Тут Москва;
```
