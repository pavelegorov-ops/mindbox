---
title: xml
slug: prodactionxml
source_url: "https://developers.mindbox.ru/docs/prodactionxml"
breadcrumb:
  - Номенклатура
  - Действия с продуктами
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:027f41ff2590416dd564a9dc0b2d6f1b6fdb418995f5fecc3c32132e263c77a2"
---

# xml

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}
X-Customer-IP: {Ip адрес устройства клиента, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
    <email>{Емэйл клиента}email>
    <mobilePhone>{Мобильный телефон}mobilePhone>
  customer>
  <product>
    <ids>
      <webSiteId>{Идентификатор продукта на сайте}webSiteId>
    ids>
  product>
  <productGroup>
    <ids>
      <webSiteId>{Идентификатор продукта на сайте}webSiteId>
    ids>
  productGroup>  
operation>
```

## Примеры операций

#### Просмотр продукта авторизованным пользователем

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=ViewProduct

Accept: application/xml
Content-Type: application/xml

<operation>
<customer>
  <ids>
    <bitrixId>346257bitrixId>
  ids>
customer>
<product>
  <ids>
    <webSiteId>2453224webSiteId>
  ids>
product>
operation>
```

#### Просмотр продукта неавторизованным пользователем

#### Просмотр группы продуктов неавторизованным пользователем
