---
title: Получение списка рекомендаций
slug: "get-popular-products"
source_url: "https://developers.mindbox.ru/docs/get-popular-products"
breadcrumb:
  - Рекомендации
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:1c197b9fddb7e38c12e5fa996997bd15197569eaf53f3693025464cc04144343"
---

# Получение списка рекомендаций

## Описание метода

Осуществляется с помощью POST-запроса. Название операции можно получить в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).  
Также возможен синхронный вызов с [Javascript SDK](javascript-sdk.md)

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={UUID устройства}

Content-Type: application/xml; charset=utf-8
Accept: application/xml
User-Agent: {User-Agent устройства клиента}
X-Customer-IP: {IP адрес клиента}

<operation>
  <recommendation>
    <limit>{Максимальное количество результатов}limit>
    <area>
      <ids>
        <externalId>{Внешний идентификатор зоны}externalId>
      ids>
    area>
  recommendation>
operation>
```

- Максимальное количество результатов - 30
- **Area** необязательна. Если не указана, выбираются продукты из зоны клиента, либо общего фида, если зона клиента не определена.
- **deviceUUID** может быть необязательным параметром в зависимости от настроек операции
- В запросе на рекомендации товар к товару (Похожие, Сопутствующие и т.д.) необходимо передавать только **offer_id**.

## Пример запроса операции

#### Популярные товары в категории

```
POST https://api.mindbox.cloud/v3/operations/sync?endpointId=Mindboxru&operation=Categorypopularproducts&deviceUUID=c0acc2bc-c52f-4157-9a26-9703825e7f7a

Accept: application/xml
Content-Type: application/xml

<operation>
<recommendation>
  <limit>50limit>
  <area>
    <ids>
      <externalId>34572externalId>
    ids>
  area>
  <productCategory>
    <ids>
      <demowebsite>78demowebsite>
    ids>
  productCategory>
recommendation>
operation>
```

#### Персональные рекомендации

#### Сопутствующие товары

#### Популярные товары

#### Похожие товары

## Ответ

```
<result>
  <status>Successstatus>
  <recommendations>
    <recommendation>
      <name>Drink (297533)name>
      <description>aH2Ffdescription>
      <displayName>IcecreamdisplayName>
      <url>http://oyfuhgss.com/igrgspxuu?yqhtfk=avrXU&amp;nbrhtst=53Lnurl>
      <pictureUrl>http://udlwf.com/heca?ezjbvy=VAzJ&amp;bheca=AsFGApictureUrl>
      <price>13572156.48price>
      <oldPrice>2688629.14oldPrice>
      <ids>
        <mindboxId>996849070mindboxId>
        <demowebsite>761954132demowebsite>
      ids>
      <manufacturer>
        <name>4eTCNaDXGuVname>
      manufacturer>
    recommendation>
    <recommendation>
      <name>Drink (297533)name>
      <description>aH2Ffdescription>
      <displayName>IcecreamdisplayName>
      <url>http://oyfuhgss.com/igrgspxuu?yqhtfk=avrXU&amp;nbrhtst=53Lnurl>
      <pictureUrl>http://udlwf.com/heca?ezjbvy=VAzJ&amp;bheca=AsFGApictureUrl>
      <price>13572156.48price>
      <oldPrice>2688629.14oldPrice>
      <ids>
        <mindboxId>996849070mindboxId>
        <demowebsite>761954132demowebsite>
      ids>
      <manufacturer>
        <name>4eTCNaDXGuVname>
      manufacturer>
    recommendation>
  recommendations>
result>
```

- **name** - технический параметр для совместимости. Для отображения названия товара используйте **displayName**
