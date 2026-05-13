---
title: xml
slug: catactionxml
source_url: "https://developers.mindbox.ru/docs/catactionxml"
breadcrumb:
  - Номенклатура
  - Действия с категориями
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:391ad4a79562454bce734f377c621f51094a53d12078921a34db4972efa1652c"
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
