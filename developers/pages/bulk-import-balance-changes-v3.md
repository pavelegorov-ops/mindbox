---
title: Массовый импорт изменений баланса
slug: "bulk-import-balance-changes-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-balance-changes-v3"
breadcrumb:
  - Бонусный счет
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:80b97958b78e44b880921cc282f41cffec85e8b17e4310042d02673b17fe1c9c"
---

# Массовый импорт изменений баланса

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.CreateCustomerBalanceChangeOperation&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
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
| PointOfContactSystemName | Идентификатор сайта/магазина, в котором произошло изменение баланса |
| CustomerIdentity | Идентификатор клиента во внешней системе. Обязателен только один из параметров **CustomerIdentity** или **DiscountCard**. |
| DiscountCard | Номер карты клиента. Обязателен только один из параметров **CustomerIdentity** или **DiscountCard**. |
| ChangeAmount | Размер изменения баланса. Для списаний нужно передавать отрицательный размер. |
| Comments | Комментарий к изменению баланса |
| AdminSiteComments | Комменатрий в административном интерфейсе к изменению баланса |
| ExpirationDateTimeUtc | Дата и время сгорания баллов UTC. Актуально только для начислений. У списаний даты не может быть. |
| BalanceSystemName | Системное имя балльного счета |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.CreateCustomerBalanceChangeOperation

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

PointOfContactSystemName;CustomerIdentity;Comments;AdminSiteComments;ChangeAmount;ExpirationDateTimeUtc
15;1821602785;2015-06-20 16:23:44.681;;;13964201.48
```
