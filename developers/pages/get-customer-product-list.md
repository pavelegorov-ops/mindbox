---
title: Получение списка продуктов клиента
slug: "get-customer-product-list"
source_url: "https://developers.mindbox.ru/docs/get-customer-product-list"
breadcrumb:
  - Номенклатура
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:4ed496f241526b208b662e9a72cb459e43f17c33b88f4e0de698b4a6cf108c3c"
---

# Получение списка продуктов клиента

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointid={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

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
POST https://api.mindbox.ru/v3/operations/sync?endpointid=MindboxRu&operation=GetSegments

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

```
<result>
  <status>Successstatus>
  <productList>
    <productListItem>
      <product>	
        <ids>
          <webSiteId>{Идентификатор продукта на сайте}webSiteId>
        ids>
      product>
      <count>{Количество продуктов в корзине}count>
      <price>{Цена продукта}price>
    productListItem>
  productList>
result>
```
