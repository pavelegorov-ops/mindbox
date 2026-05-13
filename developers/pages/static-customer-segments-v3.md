---
title: Массовый импорт статических сегментаций клиентов
slug: "static-customer-segments-v3"
source_url: "https://developers.mindbox.ru/docs/static-customer-segments-v3"
breadcrumb:
  - Сегментации
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f7ce5cd25d941589c7bbfa0fcee1ab81e5c10a4f3d76cc1b8707e7b103e483a6"
---

# Массовый импорт статических сегментаций клиентов

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Адрес и параметры запроса настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.StaticCustomerSegments.Import&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

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

При вызове достаточно передать одно любое поле, с помощью которого можно идентифицировать клиента, и идентификаторы сегментации и сегмента.

| Название колонки | Описание |
| --- | --- |
| CustomerEmail | Email |
| CustomerMobilePhone | Мобильный телефон |
| DiscountCard | Номер дисконтной карты |
| CustomerMindboxId | Идентификатор клиента в базе Mindbox |
| CustomerExternalIdentityClientCustomIdentity | Идентификатор клиента - дополнительное поле |
| SegmentationExternalId | Внешний идентификатор сегментации |
| SegmentExternalId | Внешний идентификатор сегмента. Если он не указан, клиент выводится из сегментации. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.StaticCustomerSegments.Import&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

CustomerExternalIdentityClientCustomIdentity;SegmentationExternalId;SegmentExternalId
customer-in-segment;customerVerifiedSegmentation;customerVerifiedSegment
customer-not-in-segment;customerVerifiedSegmentation;
another-customer-in-segment;customerVerifiedSegmentation;customerVerifiedSegment
```

Важно передавать данные о принадлежности клиента к сегментации только одной записью.
