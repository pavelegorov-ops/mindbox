---
title: Импорт возможных значений дополнительных полей
slug: "import-field-values"
source_url: "https://developers.mindbox.ru/docs/import-field-values"
breadcrumb:
  - Разное
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:14a101526a74290b595ee1fa15aabcea0806423c55df41e9859628c1373d8bf2"
---

# Импорт возможных значений дополнительных полей

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.CustomFieldEnumValues.Import&customFieldKindSystemName={системное имя поля}&customFieldKindEntityType={сущность дополнительного поля}&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}
HTTP/1.1

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- customFieldKindSystemName - системное имя дополнительного поля
- customFieldKindEntityType - сущность дополнительного поля. Возможные значения:  
  — `HC` - клиент  
  — `ProductInfo` - продукт  
  — `AR` - зона  
  — `DC` - дисконтная карта  
  — `CA` - действие  
  — `RO` - заказ  
  — `RP` - позиция заказа  
  — `RLP` - линия списка продуктов  
  — `POC` - точка контакта
- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| ExternalId | Идентификатор варианта значения перечисления |
| Value | Вариант значения перечисления |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.CustomFieldEnumValues.Import&customFieldKindSystemName=CustomStatus&suppressAllWarnings=true&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalId;Value
SilverStatus;Серебряный статус
GoldStatus;Золотой статус
```
