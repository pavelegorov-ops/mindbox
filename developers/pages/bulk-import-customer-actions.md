---
title: Массовый импорт действий клиентов
slug: "bulk-import-customer-actions"
source_url: "https://developers.mindbox.ru/docs/bulk-import-customer-actions"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:55fd7dcb63abb3d74e46a751d93fcfc12f1cef85bbd53fdd11ba4e125cd62967"
---

# Массовый импорт действий клиентов

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса и набор принимаемых полей настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=CustomerActionsImport&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22&actionTemplate={системное имя шаблона действия}&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

**Параметры запроса**

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- endpointId - точка доступа, из которой будут взяты настройки интеграции. Значение настраивается в системе.
- actionTemplate - системное имя шаблона действия. Например, "RedaktirovanieKlientaVOperaciiRedaktirovat". Значение настраивается в системе.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.
- поддерживается формат gzip. Для этого веб-сервер должен вернуть заголовок Content-Encoding: gzip. При этом файл нужно прикрепить в бинарном виде (например, binary в postman)

## Описание полей данных импорта

| Заголовок | Описание |
| --- | --- |
| CustomerWebsiteid | Идентификатор клиента на сайте |
| CustomerMindboxId | Id клиента в Mindbox |
| CustomerMobilePhone | Мобильный телефон |
| CustomerEmail | Емэйл клиента |
| ActionDateTimeUtc | Дата регистрации в формате yyyy-MM-dd HH:mm по UTC |
| PointOfContact | Точка контакта регистрации, например "Сайт" или "Магазин на Тверской" |
| ProductWebsiteid | Идентификатор продукта на сайте |
| ProductGroupWebsiteid | Идентификатор группы продукта на сайте |

Все принимаемые поля описаны тут https://{системное*имя*проекта}.mindbox.ru/bulkoperations?operationKindName=AddCustomerActions

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=CustomerActionsImport&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22&actionTemplate=ZaregistrirovalsyaVLoyalnosti

Authorization: SecretKey {Секретный ключ}
Accept: application/json
Content-Type: text/csv;charset=utf-8

ActionDateTimeUtc;PointOfContact;CustomerMindboxId
16.04.2016 21:00;727;1
16.04.2016 21:00;727;1
```
