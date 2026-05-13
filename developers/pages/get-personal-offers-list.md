---
title: Получение персональных предложений
slug: "get-personal-offers-list"
source_url: "https://developers.mindbox.ru/docs/get-personal-offers-list"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:9d09e127c8f2bce966a08561827b025dcbb04c592db7ef4f305629e760bd0a52"
---

# Получение персональных предложений

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

## Запрос

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <mindboxId>{Id клиента в Mindbox}mindboxId>
    ids>
  customer>
operation>
```

## Ответ

```
<result>
  <status>{Результат выполнения запроса: Success в случае успеха, ValidationError в случае ошибки пользователя, ProtocolError в случае ошибки интеграции, InternalServerError в случае недоступности сервера.}status>
  <personalOffers>
    <personalOfferItem>
      <product>
        <ids>
          <mindboxId>{Идентификатор Mindbox}mindboxId>
        ids>
      product>
      <benefit>
        <amount>
          <value>{Размер скидки. Применимо к скидочной и к бальной промоакции}value>
          <type>{Тип скидки. Возможные значения Price (стоимость продукта), Percent (значение скидки в процентах), Absolute (абсолютное значение скидки)}type>
        amount>
        <limit>
          <period>{Тип периода для лимита. Возможные значения FixedDays, FixedWeeks, FixedMonths}period>
          <amount>
            <value>{Значение лимита}value>
            <type>{Тип лимита. Возможные значения Quantity}type>
          amount>
          <used>{Использовано лимита}used>
        limit>
      benefit>
      <startDateTimeUtc>{Дата начала действия предложения}startDateTimeUtc>
      <endDateTimeUtc>{Дата окончания действия предложения}endDateTimeUtc>
    personalOfferItem>
  personalOffers>
result>
```
