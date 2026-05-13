---
title: Получение информации о заказе
slug: "get-order-info"
source_url: "https://developers.mindbox.ru/docs/get-order-info"
breadcrumb:
  - Заказы
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:9ddddf39cacf9280297e79ad854bef0289639228127860c760a892577743c3d2"
---

# Получение информации о заказе

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

Метод соответствует операции с набором шагов "Заказ - Получить существующий заказ - Добавить в ответ операции данные - Информация о заказе".

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <order>
    <ids>
      <{название поля-идентификатора}>{Значение в поле-идентификаторе}
    ids>
  order>
operation>
```

В запросе передается один из идентификаторов заказа.

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetOrderInfo

Accept: application/xml
Content-Type: application/xml

<operation>
  <order>
    <ids>
      <webSiteId>1543webSiteId>
    ids>
  order>
operation>
```

## Ответ

```
<result>
    <status>Successstatus>
<order>
    <processingStatus>FoundprocessingStatus>
    <ids>
        <mindboxId>{ID заказа в Mindbox}mindboxId>
        <myWebSiteId>{ID заказа на сайте}myWebSiteId>
    ids>
    <lines>
        <line>
            <product>
                <ids>
                    <mindboxId>{ID товара в Mindbox}mindboxId>
                    <myWebSiteId>{ID товара на сайте}myWebSiteId>
                ids>
            product>
            <sku>
                <ids>
                    <mindboxId>{ID SKU в Mindbox}mindboxId>
                    <myWebSiteId>{ID SKU на сайте}myWebSiteId>
                ids>
            sku>
            <basePricePerItem>{Базовая цена за единицу товара}basePricePerItem>
            <priceOfLine>{Конечная цена за линию чека}priceOfLine>
            <quantity>{Количество}quantity>
            <status>
                <ids>
                    <externalId>{Статус покупки}externalId>
                ids>
            status>
            <appliedPromotions>
                <appliedPromotion>{Примененная промоакция к позиции заказа. Описание узла в отдельной таблице.}appliedPromotion>
            appliedPromotions>
        line>
    lines>
    <appliedPromotions>
        <appliedPromotion>{Примененная промоакция к заказу. Описание узла в отдельной таблице.}appliedPromotion>
    appliedPromotions>
    <payments>
        <payment>
            <type>{Идентификатор способ оплаты}type>
            <amount>{Размер платежа}amount>
        payment>
    payments>
    <bonusPointsInfoPerBalanceType>
        <bonusPointsInfo>
            <spentAmount>{Сумма потраченных баллов с конкретного балльного счета за заказ на настоящий момент времени}spentAmount>
            <earnedAmount>{Сумма начисленных баллов на конкретный балльный счет за заказ на настоящий момент времени}earnedAmount>
            <balanceType>
                <name>{Название балльного счета}name>
                <ids>
                    <systemName>{Системное имя балльного счета}systemName>
                ids>
            balanceType>
        bonusPointsInfo>
        <bonusPointsInfo>
            <spentAmount>{Сумма потраченных баллов с конкретного балльного счета за заказ на настоящий момент времени}spentAmount>
            <earnedAmount>{Сумма начисленных баллов на конкретный балльный счет за заказ на настоящий момент времени}earnedAmount>
            <balanceType>
                <name>{Название балльного счета}name>
                <ids>
                    <systemName>{Системное имя балльного счета}systemName>
                ids>
            balanceType>
        bonusPointsInfo>
    bonusPointsInfoPerBalanceType>
    <totalPrice>{Стоимость заказа с учетом скидок (после вычета отмененных и возвращенных позиций)}totalPrice>
order>
result>
```

## Примененные промоакции

В **appliedPromotions** в узле **type** указывается тип примененной промоакции.

Если с примененной акцией связан промокод, он вернется в ответе. При использовании внешних промокодов, процессинг которых не на стороне Майндбокс, узел **promotion** будет отсуствовать.

Поддерживаются следующие типы:

- **discount** — скидка, может применяться только к позиции заказа
- **deliveryDiscount** — скидка, может применяться только на заказ
- **earnedBonusPoints** — начисление бонусных баллов за заказов
- **spentBonusPoints** — списание бонусных баллов для оплаты заказа
- **issuedCoupon** — выданный купон за заказ
- **message** — сообщение покупателю

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
