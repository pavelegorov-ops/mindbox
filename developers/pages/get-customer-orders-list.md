---
title: Получение списка заказов клиента v2.1
slug: "get-customer-orders-list"
source_url: "https://developers.mindbox.ru/docs/get-customer-orders-list"
breadcrumb:
  - Заказы
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8f8559797f779d27453a4605b8488bc12f9a2eced14dc9ee10736d76c042ccd3"
---

# Получение списка заказов клиента v2.1

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью GET-запроса. Название операции настраивается в системе Майндбокс.

```
GET https://project-services.mindbox.ru/v2.1/orders/by-customer?operation=DirectCrm.V21CustomerOrderListOperation&startingIndex={Порядковый номер заказа, начиная с которого будет сформирован список заказов}&countToReturn={Максимальное количество заказов для возврата}&website={Идентификатор клиента}&orderLineStatuses={Статусы заказов для возврата через запятую}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}
```

## Пример операции

```
GET https://mindbox-services.mindbox.ru/v2.1/orders/by-customer?operation=DirectCrm.V21CustomerOrderListOperation&startingIndex=0&countToReturn=10&mindbox=123321&orderLineStatuses=Delivered

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey we4fTqwe52R
```

## Ответ

```
<result>
  <orders>
    <totalCount>{Общее количество заказов клиента}totalCount>
    <order>
      <ids>
        <mindbox>{Идентификатор заказа в Майндбоксе}mindbox>
        <Внешняя система>{Идентификатор заказа во внешней системе}Внешняя система>
      ids>
      <createdPointOfContact>{Идентификатор точки контакта сайт/магазин/термионал/т.п.}createdPointOfContact>
      <createdDateTimeUtc>{Дата и время создания заказа в UTC в формате yyyy-MM-dd HH:mm:ss}createdDateTimeUtc>
      <discountedTotalPrice>{Стоимость заказа с учетом скидок}discountedTotalPrice>
      <appliedDiscounts>
        <appliedDiscount>
          <type>promoActiontype>
          <id>{Идентификатор промоакции}id>
          <amount>{Размер скидки, примененной к заказу}amount>
        appliedDiscount>
        <appliedDiscount>
          <type>balancetype>
          <amount>{Размер скидки, примененной к заказу}amount>
        appliedDiscount>
        <appliedDiscount>
          <type>promoCodetype>
          <amount>{Размер скидки, примененной к заказу}amount>
        appliedDiscount>
        <appliedDiscount>
          <type>giftcardtype>
          <amount>{Размер скидки, примененной к заказу}amount>
        appliedDiscount>
        <appliedDiscount>
          <type>externalPromoActiontype>
          <id>{Идентификатор промоакции}id>
          <amount>{Размер скидки по внешней акции}amount>
        appliedDiscount>
      appliedDiscounts>
      <lines>
        <line>
          <sku>
            <productId>{Идентификатор продукта}productId>
          sku>
          <appliedDiscounts>
            <appliedDiscount>
              <type>promoActiontype>
              <id>{Идентификатор промоакции}id>
              <amount>{Размер скидки, примененной к линии чека}amount>
            appliedDiscount>
            <appliedDiscount>
              <type>balancetype>
              <amount>{Размер скидки, примененной к линии чека}amount>
            appliedDiscount>
            <appliedDiscount>
              <type>promoCodetype>
              <amount>{Размер скидки, примененной к линии чека}amount>
            appliedDiscount>
            <appliedDiscount>
              <type>giftcardtype>
              <amount>{Размер скидки, примененной к линии чека}amount>
            appliedDiscount>
            <appliedDiscount>
              <type>externalPromoActiontype>
              <id>{Идентификатор промоакции}id>
              <amount>{Размер скидки по внешней акции}amount>
            appliedDiscount>
          appliedDiscounts>
          <basePricePerItem>{Цена с учетом скидки за линию}basePricePerItem>
          <quantity>{Количество единиц продукта}quantity>
          <status>{Идентификатор статуса заказа}status>
        line>
      lines>
  		<totalAcquiredBalanceChange>{Количество баллов, которое было начислено за заказ}totalAcquiredBalanceChange>
    order>
  orders>
result>
```
