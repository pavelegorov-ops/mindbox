---
title: Изменение статуса позиции заказа
slug: "update-order-line-status"
source_url: "https://developers.mindbox.ru/docs/update-order-line-status"
breadcrumb:
  - Заказы
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:1b71160b017619db7adadfc888dd96b94493ad65443e0b9f4944281ad59da4c1"
---

# Изменение статуса позиции заказа

## Описание метода

## Набор шагов

| Шаг | Описание |
| --- | --- |
| Заказ - Обновить cтатус позиции заказа | Предназначен для того, чтобы обновить данные по линии в заказе. |

Метод работает в двух режимах: обновляет статус у всех позиций заказа через значение поля orderLinesStatus или обновляет статус у переданных позиций в массиве lines.

Для поиска позиций нужно передавать либо идентификатор позиции (lineId), либо порядковый номер позиции (lineNumber), либо id продукта и стоимость возвращенной позиции.  
При необходимости Майндбокс самостоятельно разобьет позицию на две (например, при частичном возврате одной позиции).  
Если при изменении статуса произошел возврат денег, информация об этом дополнительно передается в узле returnedPayments.

Если заказа еще не было в системе, вернется ошибка 400.  
Секретный ключ обязателен для данной операции.

Рекомендуется вызывать сервис асинхронно, чтобы не влиять на работу кассового ПО или сайта.

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ}

<operation>
  <order>
    <ids>
      <webSiteId>{Идентификатор заказа во внешней системе}webSiteId>
    ids>
    <customFields>
      <Дополнительное поле заказа>{Значение дополнительного поля}Дополнительное поле заказа>
    customFields>
    <returnedPayments>
      <returnedPayment>
        <type>{Способ оплаты (Card)}type>
        <amount>{Размер возвращенного платежа}amount>
        <creditCard>
          <hash>{Хеш банковской карты}hash>
        creditCard>
      returnedPayment>
    returnedPayments>
    <lines>
      <line>
        <lineId>{Идентификатор позиции. Обязательно передавать либо идентификатор позиции, либо ее порядковый номер.}lineId>
        <lineNumber>{Порядковый номер позиции. Обязательно передавать либо идентификатор позиции, либо ее порядковый номер.}lineNumber>
        <quantity>{Количество товаров в позиции}quantity>
        <status>{Статус позиции}status>
        <product>
          <ids>
            <websiteID>{Id Product в NewWebsiteID}websiteID>
          ids>
        product>
        <customFields>
          <Дополнительное поле линии>{Значение дополнительного поля}Дополнительное поле линии>
        customFields>
      line>
    lines>
    <email>{Email}email>
    <mobilePhone>{Номер мобильного телефона без форматирования}mobilePhone>
  order>
  <orderLinesStatus>{Новый статус для всех линий заказа}orderLinesStatus>
  <executionDateTimeUtc>{Дата и время выполнения (можно использовать для выполнения запроса задним числом)}executionDateTimeUtc>
operation>
```

#### JSON

#### JSON, заказ

#### JSON, линии (lineNumber)

#### JSON, линии (productId)

#### JSON, линии (lineId)

## Описание ответа

#### Успешный ответ, заказ (xml)

```
</spanxml version="1.0" encoding="utf-8"?>
<result>  
  <status>Successstatus>
result>
```

#### Успешный ответ, заказ (json)

#### Успешный ответ, линии (xml)

#### Успешный ответ, линии (json)

## Примененные промоакции в ответе

В узле type указывает тип примененной промоакции.

Если с примененной акцией связан промокод, он вернется в ответе. При использовании внешних промокодов, процессинг которых не на стороне Майндбокс, узел promotion будет отсуствовать.

Поддерживаются следующие типы:

1. discount — скидка, может применяться только к позиции заказа
2. deliveryDiscount — скидка, может применяться только на заказ
3. earnedBonusPoints — начисление бонусных баллов за заказов
4. spentBonusPoints — списание бонусных баллов для оплаты заказа
5. issuedCoupon — выданный купон за заказ
6. message — сообщение покупателю

#### discount

```
<appliedPromotion>
  <type>discounttype>
  <coupon>
    <ids>
      <code>{Промокод}code>
    ids>
    <pool>
      <ids>
        <mindboxId>{Идентификатор Mindbox}mindboxId>
        <externalId>{Внешний идентификатор пула промокодов}externalId>
      ids>
      <name>{Наименование пула промокодов}name>
      <description>{Описание пула промокодов}description>
    pool>
  coupon>
  <promotion>
    <ids>
      <mindboxId>{Идентификатор Mindbox}mindboxId>
      <externalId>{Внешний идентификатор промоакции}externalId>
    ids>
    <name>{Наименование промоакции}name>
    <type>{Тип промоакции}type>
  promotion>
  <amount>{Размер скидки}amount>
appliedPromotion>
```

#### deliveryDiscount

#### earnedBonusPoints

#### spentBonusPoints

#### issuedCoupon

#### message
