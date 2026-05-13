---
title: Массовый импорт пула подарочных карт
slug: "bulk-import-gift-card-pool-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-gift-card-pool-v3"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:2a7cd406f8d95a1eef53c7e90f59f65709796a91f2a502d288f73ad884207d53"
---

# Массовый импорт пула подарочных карт

## Описание метода

Осуществляется с помощью POST-запроса. Адрес и параметры запроса настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=ImportGiftCards.OnlyNew&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

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
| Number | Номер подарочной карты |
| Amount | Количество баллов на карте |
| ProductId{ExternalSystem} | Id продукта, с которым связанна подарочная карта. Название поля уточняйте у менеджера. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=ImportGiftCards.OnlyNew&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

Number;Amount;ProductIdWebSite
6768953;5000;21533674
```
