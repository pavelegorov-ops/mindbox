---
title: Массовый импорт статусов дисконтных карт
slug: "bulk-import-discount-card-statuses-v3"
source_url: "https://developers.mindbox.ru/docs/bulk-import-discount-card-statuses-v3"
breadcrumb:
  - Карты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:63c07cf3bbe9a59661e64ddbe9fa3753e6c4f64d4734e34dcf700e592a564573"
---

# Массовый импорт статусов дисконтных карт

## Описание метода

Осуществляется с помощью POST-запроса. Адрес и параметры запроса настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Customers.ImportCards&csvCodePage=65001&newCardCreationAllowed=true&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- newCardCreationAllowed - разрешение создания новых карт в рамках задачи импорта. По умолчанию создание новых карт запрещено.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей файла

| Заголовок | Описание |
| --- | --- |
| CardNumber | Номер карты |
| Status | Текущий статус карты  - Inactive — Не активирована - Activated — Активирована - Blocked — Заблокирована |
| StatusChangeDateTimeUtc | Дата изменения статуса дисконтной карты в UTC в формате "yyyy-MM-dd hh:mm" |
| CardType | Тип карты, применяется только для новых карт. Для существующих игнорируется. |
| Идентификатор | Укажите идентификатор клиента, которые необходимо использовать для импорта. Это может быть Email, MobilePhone или какой-то свой внешний идентификатор |
| PointOfContact | Точка контакта выдачи/блокировки карты, например "Сайт" или "Магазин на Тверской" |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Customers.ImportCards&csvCodePage=65001&newCardCreationAllowed=true

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

CardNumber;Status;StatusChangeDateTimeUtc;PointOfContact
4359487117524;Activated;2014-9-17 12:35:21.31;MagazinVMoskve
```
