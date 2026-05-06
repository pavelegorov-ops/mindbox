---
title: Получение сегментов клиента
slug: "get-customer-segments"
source_url: "https://developers.mindbox.ru/docs/get-customer-segments"
breadcrumb:
  - Сегментации
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:13bcb93235e9ba0d612866d063fbade318a2df890b72778ed89606f7f7c81c50"
---

# Получение сегментов клиента

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Mindbox. Подробней про вызов метода можно прочитать [здесь](v3.md).

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательно уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
  customer>
operation>
```

#### JSON

#### JavaScript

Сегментации, которые нужно получить, можно:

- либо передавать в запросе явно
- либо настроить в операции (тогда узел `segmentations` передавать не надо)

## Пример операции

#### По Id клиента (XML)

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetSegments

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq
Content-Length: 123

<operation>
  <customer>
    <ids>
      <webSiteUserId>5384275webSiteUserId>
    ids>
  customer>
operation>
```

#### Получение по DeviceUUID (JSON)

#### Получение по DeviceUUID, сегментации передаются в запросе (JavaScript)

## Ответ

#### XML

```
<result>
  <status>Successstatus>
  <customerSegmentations>
    <customerSegmentation>
      <segmentation>
        <ids>
          <externalId>{Внешний идентификатор сегментации}externalId>
        ids>
        <name>{Имя сегментации}name>
      segmentation>
      <segment>
        <ids>
          <externalId>{Внешний идентификатор сегмента}externalId>
        ids>
        <name>{Имя сегмента}name>
      segment>
    customerSegmentation>
    <customerSegmentation>
      <segmentation>
        <ids>
          <externalId>{Внешний идентификатор сегментации}externalId>
        ids>
        <name>{Имя сегментации}name>
      segmentation>
    customerSegmentation>
  customerSegmentations>
result>
```

#### JSON

Отсутствующий `segment` означает, что клиент не входит в сегментацию.  
Отсутствующий `customerSegmentations` означает, что клиент не был найден по переданному идентификатору.
