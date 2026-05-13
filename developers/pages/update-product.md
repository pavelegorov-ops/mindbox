---
title: Обновление информации о продукте
slug: "update-product"
source_url: "https://developers.mindbox.ru/docs/update-product"
breadcrumb:
  - Номенклатура
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:12d37ef92d27093d8b7641bdae64e622bf4e619134751b2e9378d5b67895a23c"
---

# Обновление информации о продукте

## Описание работы метода

При вызове метода происходит обновление данных о продукте, переданных в методе.  
Если ранее не было информации о продукте, то создается новый продукт с данными переданными в методе.

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
  <ids>
    <{Наименование идентификатора}>{Идентификатор продукта в системе }
  ids>
  <categories>
    <category>
      <ids>
        <{Наименование идентификатора}>{Идентификатор категории в системе }
      ids>
    category>
  categories>
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
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=SaveProduct

  Accept: application/xml
  Content-Type: application/xml
  Authorization: SecretKey D061p764m85bklq

  <operation>
    <product>
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
