---
title: Массовый импорт точек контакта
slug: "bulk-import-touchpoints-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-touchpoints-v3"
breadcrumb:
  - "Точки контакта, магазины, зоны"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:635ef0696e1c055785d1c507b0f96a8db0cf02d61a4d3299e0bc9e8953da5279"
---

# Массовый импорт точек контакта

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PointsOfContacts.Import&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

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
| ExternalId | Идентификатор точки контакта (магазин, сайт и т.д.).Например, "ShopTverskaya9" |
| Name | Название точки контакта.Например, "Магазин на Тверской, 9" |
| Comment | Описание точки контакта |
| ParentChannelExternalId | Идентификатор канала, к которому относится точка контакта. Канал используется для создание иерархии, например регион → город → магазин. |
| CustomFieldAddress | Дополнительное поля к точке контакта.Название и количество дополнительных полей свое на каждом проекте. Уточняйте у менеджера Mindbox. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.PointsOfContacts.Import&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalId;Name;Comment;ParentChannelExternalId;CustomFieldAddress
ShopTverskaya9;Магазин на Тверской, 9;Первый магазин в Москве!;15;Москва, ул. Тверская, д. 9
```
