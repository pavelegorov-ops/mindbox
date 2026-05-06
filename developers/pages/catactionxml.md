---
title: xml
slug: catactionxml
source_url: "https://developers.mindbox.ru/docs/catactionxml"
breadcrumb:
  - Номенклатура
  - Действия с категориями
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:c4f67c2d41352f11dee9bab404c88aec6d584dcf27f2688b9e410b6763df06d8"
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
  <productCategory>
    <ids>
      <webSiteId>{Идентификатор категории продукта}webSiteId>
    ids>
  productCategory>
operation>
```

## Примеры операций

#### Просмотр категории авторизованным пользователем

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=viewCategory

Accept: application/xml
Content-Type: application/xml

<operation>
<customer>
  <ids>
    <bitrixId>346257bitrixId>
  ids>
customer>
<productCategory>
  <ids>
    <webSiteId>504webSiteId>
  ids>
productCategory>
operation>
```

#### Просмотр категории неавторизованным пользователем
