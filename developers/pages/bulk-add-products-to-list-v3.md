---
title: Массовое добавление продуктов в список
slug: "bulk-add-products-to-list-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-add-products-to-list-v3"
breadcrumb:
  - Номенклатура
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:077cad690f5cf6a6a00108eb998d6fe97590b3f66ad565ba50314fabf36ee848"
---

# Массовое добавление продуктов в список

## Описание метода

Осуществляется с помощью POST-запроса. Сервис добавляет в список к существующим продуктам новые. Адрес запроса и набор принимаемых полей настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId=`{уникальный идентификатор сайта и т.п.}`&operation=AddToPersonalProductList&pointOfContact=`{Точка контакта}`&personalProductListSystemName=`{Системное имя списка продуктов}`&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22&transactionId=`{Значение ключа идемпотентности в формате GUID}`

Authorization: SecretKey `{Секретный ключ}`
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- endpointId - точка доступа, из которой будут взяты настройки интеграции. Значение настраивается в системе.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| Customer | Идентификатор клиента на сайте |
| Product | Идентификатор продукта на сайте |
| Quantity | Количество |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId=`{уникальный идентификатор сайта и т.п.}`&operation=AddToPersonalProductList&pointOfContact=`{Точка контакта}`&personalProductListSystemName=`{Системное имя списка продуктов}`&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22

Authorization: SecretKey `{Секретный ключ}`
Accept: application/json
Content-Type: text/csv;charset=utf-8

CustomerWebsiteid;ProductWebsiteid;Quantity
21324;268;1
21324;270;1
21324;1574;1
```
