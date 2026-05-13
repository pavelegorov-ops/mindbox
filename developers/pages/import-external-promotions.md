---
title: Импорт внешних промоакций
slug: "import-external-promotions"
source_url: "https://developers.mindbox.ru/docs/import-external-promotions"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6c32a84762ebe9f0b16eddb7503b6507f9a7a178a6a3489ae23491d7625687ef"
---

# Импорт внешних промоакций

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Promotions.Import&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}

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
| ExternalId | Внешний идентификатор промоакции |
| Type | Тип промоакции. Поддерживается импорт только внешних промоакций с типом external. |
| Name | Наименование промоакции. |
| Description | Описание промоакции |
| StartDateTimeUtc | Дата начала действия промоакции в часовом поясе UTC+0. |
| EndDateTimeUtc | Дата окончания действия промоакции в часовом поясе UTC+0. |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Promotions.Import&csvCodePage=65001

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalId;Type;Name;Description;StartDateTimeUtc;EndDateTimeUtc
1;external;Скидки всем;Скидка всем 10 процентов;2016-08-08 17:34:00;2016-12-31 23:59:00
```
