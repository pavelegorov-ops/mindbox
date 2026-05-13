---
title: Оформление заказа
slug: "order-checkout"
source_url: "https://developers.mindbox.ru/docs/order-checkout"
breadcrumb:
  - Заказы
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:ffa144279e8000a6346a584c4f779f7c017290e26a4418b900658297d5f9306a"
---

# Оформление заказа

## Описание метода

| Шаг | Описание |
| --- | --- |
| Клиент - Авторизованный - Получить существующего, ищем по... | Предназначен для поиска клиента в базе данных Mindbox. Поиск может происходить по различным (одному или нескольким) параметрам, которые выбираются из выпадающего списка. |
| Заказ (без процессинга) - Оформление заказа | Предназначен для того, чтобы создать в системе заказ без процессинга. |

Создает новый заказ в системе Mindbox. Если такой заказ уже существует, вернется ошибка 400.

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ}

<operation>
  <customer>
    <ids>
    	<webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
    <email>{Email}email>
    <mobilePhone>{Мобильный телефон}mobilePhone>
  customer>
  <order>
    <deliveryCost>{Стоимость доставки заказа}deliveryCost>
    <totalPrice>{Итоговая сумма, полученная от пользователя. Должна учитывать возвраты и отмены. Используется для подсчета среднего чека.}totalPrice>
     "ids": {
      "mindboxId": "<Идентификатор заказа в Mindbox>",
      "testId": "<Идентификатор заказа TestId>",
      "testID2": "<Идентификатор заказа testID2>"
    
    <lines>
      <line>
        <lineId>{Идентификатор позиции}lineId>
        <product>
          <ids>
            <websiteId>{Идентификатор продукта на сайте}websiteId>
          ids>
        product>
        <basePricePerItem>{Базовая цена за единицу товара}basePricePerItem>
        <costPricePerItem>{Себестоимость за единицу продукта}costPricePerItem>
        <quantity>{Количество товара в линии}quantity>
        <customFields>
          <Дополнительное поле линии>{Значение дополнительного поля}Дополнительное поле линии>
        customFields>
        <discounts>
          <discount>
            <type>externalPromoActiontype>
            <externalPromoAction>
              <ids>
                <externalId>{Идентификатор промоакции}externalId>
              ids>
            externalPromoAction>
            <amount>{Размер скидки в рублях}amount>
          discount>
          <discount>
            <type>promoCodetype>
            <promoCode>
              <ids>
                <code>{Промокод}code>
              ids>
            promoCode>
            <amount>{Размер скидки в рублях}amount>
          discount>
        discounts>
      line>
    lines>
    <payments>
      <payment>
      	<type>{Идентификатор способа оплаты}type>
     	 	<amount>{Размер платежа}amount>
	    payment>
    payments>
    <customFields>
      <Дополнительное поле заказа>{Значение дополнительного поля}Дополнительное поле заказа>
    customFields>
    <area>
      <ids>
        <externalId>{Идентификатор зоны (региона)}externalId>
      ids>
    area>
    <ids>
      <webSiteId>{Идентификатор заказа во внешней системе}webSiteId>
    ids>
    <email>{Email-адрес для транзакционных сообщений по заказу}email>
    <mobilePhone>{Мобильный телефон для транзакционных сообщений по заказу}mobilePhone>
  order>
operation>
```

#### JSON

#### JavascriptSDK

  

## Описание ответа

#### Успешный ответ (xml)

```
</spanxml version="1.0" encoding="utf-8"?>
<result>  
  <status>Successstatus>
result>
```

#### Успешный ответ (json)

#### Ошибка (xml)

#### Ошибка (json)
