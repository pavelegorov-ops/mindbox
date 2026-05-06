---
title: Обновление региональных данных продукта
slug: "save-product-regional-info"
source_url: "https://developers.mindbox.ru/docs/save-product-regional-info"
breadcrumb:
  - Номенклатура
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:99c26ea6d2be9b4370c27d839389e9f562b0f05ab5676040f8e926b813b47202"
---

# Обновление региональных данных продукта

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
<product>
  <area>
    <ids>
      <externalId>{Внешний идентификатор зоны}externalId>
    ids>
  area>
  <ids>
    <{Наименование идентификатора}>{Идентификатор продукта в системе }
  ids>
  <category>
    <ids>
      <{Наименование идентификатора}>{Идентификатор категории в системе }
    ids>
  category>
  <name>{Наименование продукта}name>
  <description>{Описание SKU}description>
  <isAvailable>{Доступность продукта: true/false}isAvailable>
  <price>{Текущая цена}price>
  <oldPrice>{Старая цена}oldPrice>
  <shelfLife>{Срок годности продукта (количество дней)}shelfLife>
  <url>{Ссылка на страницу продукта}url>
  <pictureUrl>{Ссылка на картинку продукта}pictureUrl>
  <customFields>
    <{Дополнительное поле продукта}>{Значение доп. поля продукта}
  customFields>
product>
operation>
```

#### JSON

## Пример операции

#### Пример вызова XML

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=SaveRegionalProductData

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <product>
    <area>
      <ids>
        <externalId>1externalId>
      ids>
    area>    
    <ids>
      <webSiteId>1webSiteId>
    ids>
    <category>
      <ids>
        <webSiteId>1webSiteId>
      ids>
    category>
    <name>Продукт 1name>
    <description>Описаниеdescription>
    <isAvailable>trueisAvailable>
    <price>1000price>
    <oldPrice>800oldPrice>
    <shelfLife>90shelfLife>
    <url>https://mindbox.ruurl>
    <pictureUrl>https://mindbox.rupictureUrl>
    <customFields>
      <customField1>1customField1>
    customFields>
  product>
operation>
```

#### Пример вызова JSON

## Ответ

#### XML

```
<result>
<status>Successstatus>
result>
```

#### JSON
