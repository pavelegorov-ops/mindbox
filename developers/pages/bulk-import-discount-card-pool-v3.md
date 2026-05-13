---
title: Массовый импорт пула дисконтных карт
slug: "bulk-import-discount-card-pool-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-discount-card-pool-v3"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:2048c697ce76e009ec9194b7d2910a882592e028e884267684e031b0a1780ed3"
---

# Массовый импорт пула дисконтных карт

## Описание метода

Осуществляется с помощью POST-запроса. Адрес и параметры запроса настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.DiscountCards.ImportCards&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

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
| Number | Номер дисконтной карты |
| Type | Тип дисконтной карты |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.DiscountCards.ImportCards&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

Number;Type
6768953;loyal10
```
