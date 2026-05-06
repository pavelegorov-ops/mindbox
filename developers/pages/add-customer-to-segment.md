---
title: Включение в сегмент
slug: "add-customer-to-segment"
source_url: "https://developers.mindbox.ru/docs/add-customer-to-segment"
breadcrumb:
  - Сегментации
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8ea856b77fc14617fbce94f0dec789dd02fcbe93131e9fa8d106b72e0b3d2c03"
---

# Включение в сегмент

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
    <websiteId>{Идентификатор клиента на сайте}websiteId>
  customer>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=AddCustomerToSegment

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <websiteId>{Идентификатор клиента на сайте}websiteId>				
  customer>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
result>
```
