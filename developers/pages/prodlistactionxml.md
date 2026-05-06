---
title: xml
slug: prodlistactionxml
source_url: "https://developers.mindbox.ru/docs/prodlistactionxml"
breadcrumb:
  - Номенклатура
  - Действия со списками продуктов
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:df90f716d770b5313fc104b14c07a65719600811996173e7e14c3de1b61125f4"
---

# xml

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>      
      <WebSiteUserId>{Идентификатор клиента}WebSiteUserId>
    ids>
    <email>{Емэйл клиента}email>
    <mobilePhone>{Мобильный телефон}mobilePhone>
  customer>
  <productList>
    <productListItem>
      <product>
        <ids>
          <webSiteId>{Идентификатор продукта}webSiteId>
        ids>
        <sku>
          <ids>
            <webSiteId>{Номер SKU на сайте}webSiteId>
          ids>
        sku>
      product>
      <count>{Количество продуктов в корзине}count>
      <price>{Цена за количество единиц продукта}price>
    productListItem>
  productList>
operation>
```

## Примеры операций

#### Установка состава корзины авторизованным пользователем

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=SetCart

Accept: application/xml
Content-Type: application/xml

<operation>
<customer>
  <ids>
    <bitrixId>346257bitrixId>
  ids>
customer>
<productList>
  <productListItem>
    <product>
      <ids>
        <webSiteId>34562webSiteId>
      ids>
    product>
    <count>1count>
    <pricePerItem>150pricePerItem>
  productListItem>
  <productListItem>
    <product>
      <ids>
        <webSiteId>33962webSiteId>
      ids>
    product>
    <count>2count>
    <pricePerItem>450pricePerItem>
  productListItem>
productList>
operation>
```

#### Установка состава корзины неавторизованным пользователем

#### Добавление продукта в корзину

#### Удаление продукта из корзины

#### Установка количества продуктов в корзине

#### Очистка корзины
