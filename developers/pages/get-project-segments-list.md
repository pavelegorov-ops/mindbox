---
title: Получение списка сегментаций
slug: "get-project-segments-list"
source_url: "https://developers.mindbox.ru/docs/get-project-segments-list"
breadcrumb:
  - Сегментации
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:57d5867b33259a1486b4646c94983e11cb5fd25cce50949180668aeb4501d46f"
---

# Получение списка сегментаций

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса настраивается в системе Майндбокс.

#### XML

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}
HTTP/1.1

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}
```

#### JSON

## Пример запроса

#### XML

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetSegmentationsForCustomers
HTTP/1.1

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq
```

#### JSON

## Пример ответа

#### XML

```
<result>
  <status>Successstatus>
  <segmentations>
    <segmentation>
      <ids>
        <externalId>{Внешний идентификатор сегментации}externalId>
      ids>
      <name>{Имя сегментации}name>
      <segments>
        <segment>
          <ids>
            <externalId>{Внешний идентификатор сегмента}externalId>
          ids>
          <name>{Имя сегмента}name>
          <count>{Количество сущностей в сегменте}count>
        segment>
        <segment>
          <ids>
            <externalId>{Внешний идентификатор сегмента}externalId>
          ids>
          <name>{Имя сегмента}name>
          <count>{Количество сущностей в сегменте}count>
        segment>
      segments>
    segmentation>
    <segmentation>
      <ids>
        <externalId>{Внешний идентификатор сегментации}externalId>
      ids>
      <name>{Имя сегментации}name>
      <segments>
        <segment>
          <ids>
            <externalId>{Внешний идентификатор сегмента}externalId>
          ids>
          <name>{Имя сегмента}name>
          <count>{Количество сущностей в сегменте}count>
        segment>
        <segment>
          <ids>
            <externalId>{Внешний идентификатор сегмента}externalId>
          ids>
          <name>{Имя сегмента}name>
          <count>{Количество сущностей в сегменте}count>
        segment>
      segments>
    segmentation>
  segmentations>
result>
```

#### JSON
