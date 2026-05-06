---
title: Изменение заказа
slug: "update-order"
source_url: "https://developers.mindbox.ru/docs/update-order"
breadcrumb:
  - Заказы
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:066482a1a29d34251b8a54e8e709bee37fff35f961a285aeeb9a6c0b601c1220"
---

# Изменение заказа

## Описание метода

## Набор шагов

| Шаг | Описание |
| --- | --- |
| Клиент - Авторизованный - Получить существующего, ищем по... | Предназначен для поиска клиента в базе данных Mindbox. Поиск может происходить по различным (одному или нескольким) параметрам, которые выбираются из выпадающего списка. |
| Заказ (без процессинга) - Обновить данные заказа | Предназначен для того, чтобы обновить данные в заказе. |

Обновляет заказ в системе Майндбокс. Если заказа еще не было в системе, он будет создан. Секретный ключ обязателен для данной операции.

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ}

<operation>
  <executionDateTimeUtc>{Дата и время изменения заказа в UTC+0}executionDateTimeUtc>
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
        <status>{Статус покупки}status>
      line>
    lines>
    <payments>
      <payment>
      	<type>{Идентификатор способ оплаты}type>
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
      <mindboxId>{Идентификатор заказа в Mindbox}mindboxId>
      <webSiteId>{Идентификатор заказа во внешней системе}webSiteId>
    ids>
    <email>{Email-адрес для транзакционных сообщений по заказу}email>
    <mobilePhone>{Мобильный телефон для транзакционных сообщений по заказу}mobilePhone>
  order>
operation>
```

#### JSON

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
