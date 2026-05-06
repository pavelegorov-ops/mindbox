---
title: Массовый импорт карт и клиентов
slug: "bulk-import-cards-clients"
source_url: "https://developers.mindbox.ru/docs/bulk-import-cards-clients"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:6df6e7772960e0c4aab32e542046b9dc4509debe6e4ac521aab8efeb90a5d8b9"
---

# Массовый импорт карт и клиентов

### В инструкции описаны примеры POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса и набор принимаемых полей настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Customers.ImportCards&newCardCreationAllowed=true&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

**Параметры запроса**

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- endpointId - точка доступа, из которой будут взяты настройки интеграции. Значение настраивается в системе.
- newCardCreationAllowed - разрешение создавать новые карты. По умолчанию создание новых карт запрещено.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.
- поддерживается формат gzip. Для этого веб-сервер должен вернуть заголовок Content-Encoding: gzip. При этом файл нужно прикрепить в бинарном виде (например, binary в postman)

## Описание полей данных импорта

| Заголовок | Описание |
| --- | --- |
| MobilePhone | Мобильный телефон |
| Email | Емейл клиента |
| IsSubscribed | Статус подписки true/false |
| Дополнительное поле клиента | Значение дополнительного поля клиента |
| ExternalIdentityWebsiteID | Идентификатор во внешней системе WebsiteID |
| StatusChangeDateTimeUtc | Дата изменения статуса дисконтной карты в UTC в формате "yyyy-MM-dd hh:mm" |
| Status | Текущий статус карты:  - Inactive — Не активирована - Activated — Активирована - Blocked — Заблокирована |
| CardNumber | Номер дисконтной карты |
| CardType | Тип карты, применяется только для новых карт. Для существующих игнорируется. |

Все принимаемые поля описаны тут [https://{системное_имя_проекта}.mindbox.ru/customers/import](https://%7B%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D0%BE%D0%B5_%D0%B8%D0%BC%D1%8F_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%7D.mindbox.ru/customers/import)

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Customers.ImportCards&newCardCreationAllowed=true&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ExternalIdentityWebsiteID;Email;StatusChangeDateTimeUtc;CardNumber;Status
1212121;test@gmail.com;16.10.2022 21:00;99999;Activated
```
