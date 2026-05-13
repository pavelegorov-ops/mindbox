---
title: Проверка наличия клиента в БД
slug: "customer-existence-database-check"
source_url: "https://developers.mindbox.ru/docs/customer-existence-database-check"
breadcrumb:
  - Клиент
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f82255f8031c93ee9b1a40f1c0d432cb8926d1437311a1fdb93e4ea8092c3c4e"
---

# Проверка наличия клиента в БД

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
  customer>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=CheckExists

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <webSiteUserId>5384275webSiteUserId>
    ids>
  customer>
operation>
```

## Ответ

#### Ответ, если клиент есть

```
<result>
  <status>Successstatus>
  <customer>
    <processingStatus>FoundprocessingStatus>
  customer>
result>
```

#### Ответ, если клиента нет

Статус обработки клиента (`processingStatus`) может иметь различные значения для проверки наличия клиента:

- `Found` - клиент успешно найден
- `NotFound` - клиент не найден
