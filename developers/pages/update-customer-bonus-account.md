---
title: Изменение бонусного счета клиента
slug: "update-customer-bonus-account"
source_url: "https://developers.mindbox.ru/docs/update-customer-bonus-account"
breadcrumb:
  - Бонусный счет
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:c60037e973a99c3781824e338095cb7cce7f69f5e37f6d394fde15b3f5147eca"
---

# Изменение бонусного счета клиента

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
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
  customer>
  <balanceChanges>
    <balanceChange>
      <changeAmount>{Величина изменения баланса}changeAmount>
      <comment>{Комментарий}comment>
      <expirationDateTimeUtc>{Дата сгорания балов}expirationDateTimeUtc>
    balanceChange>
  balanceChanges>
operation>
```

## Примеры операций

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=chageCustomerBalance

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <webSiteUserId>5384275webSiteUserId>
    ids>
  customer>
  <balanceChanges>
    <balanceChange>
      <changeAmount>200changeAmount>
      <comment>За лайк в соц сетяхcomment>
      <expirationDateTimeUtc>2017-12-01 10:00:01.555expirationDateTimeUtc>
    balanceChange>
  balanceChanges>
operation>
```
