---
title: Получение истории изменений баланса клиента
slug: "get-customer-bonus-balance-history"
source_url: "https://developers.mindbox.ru/docs/get-customer-bonus-balance-history"
breadcrumb:
  - Бонусный счет
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:d7cbb903c7af2a41bc61e27a7b4191a3b1eb6683331cafa5ab6f1505fb5cd367"
---

# Получение истории изменений баланса клиента

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
  customer>
  <page>
    <sinceDateTimeUtc>{необязательный узел, дата, начиная с которой будут отображаться изменения баланса}sinceDateTimeUtc>
    <tillDateTimeUtc>{необязательный узел, дата по которую будут фильтроваться изменения баланса}tillDateTimeUtc>
    <pageNumber>{номер страницы}pageNumber>
    <itemsPerPage>{количество элементов на страницу}itemsPerPage>
  page>
operation>
```

- sinceDateTimeUtc и tillDateTimeUtc – необязательные поля для фильтрации изменений по дате.
- Страницы нумеруются с 1.
- Максимальное количество действий на страницу - 1000

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetBalanceAction

Accept: application/xml
Content-Type: application/xml

<operation>
  <customer>
    <ids>
      <webSiteUserId>5384275webSiteUserId>
    ids>
  customer>
  <page>
    <sinceDateTimeUtc>2017-08-22 10:00:00.000sinceDateTimeUtc>
    <tillDateTimeUtc>2017-08-22 11:00:00.000tillDateTimeUtc>
    <pageNumber>1pageNumber>
    <itemsPerPage>50itemsPerPage>
  page>
operation>
```

Запрос вернет первые 50 действий.

## Ответ

```
<result>
  <status>Successstatus>
  <customerActions>
    <customerAction>
      <ids>
        <mindboxId>{Идентификатор действия в Майндбокс}mindboxId>
        <externalId>{Внешний идентификатор действия}externalId>
      ids>
      <actionTemplate>
        <systemName>{Системное имя шаблона действия в Майндбоксе}systemName>
        <name>{Имя шаблона действия в Майндбоксе}name>
      actionTemplate>
      <dateTimeUtc>{Дата совершения действия клиентом}dateTimeUtc>
      <pointOfContact>
        <ids>
          <externalId>{Внешний идентификатор точки контакта}externalId>
        ids>
      pointOfContact>
      <customer>
        <ids>
          <mindboxId>{Идентификатор клиента в Майндбоксе}mindboxId>
          <webSiteId>{Идентификатор клиента}webSiteId>
        ids>
      customer>
      <customerBalanceChanges>
        <customerBalanceChange>
          <changeAmount>{Размер изменения баланса}changeAmount>
          <expirationDateTimeUtc>{Дата сгорания баллов}expirationDateTimeUtc>
          <isAvailable>{доступно ли изменение баланса для использования, true/false}isAvailable>
          <balanceChangeKind>
            <systemName>{Тип изменения баланса}systemName>
          balanceChangeKind>
        customerBalanceChange>
      customerBalanceChanges>
    customerAction>
  customerActions>
  <customerActionsCount>{Общее количество изменений баланса клиента}customerActionsCount>
result>
```

## Типы изменения баланса

| Бизнес смысл | Тип изменения |
| --- | --- |
| Бонус за розничный заказ | RetailOrderBonus |
| Оплата розничного заказа баллами | RetailOrderPayment |
| Прочее | Custom |
| Списание сгоревших баллов | Expired |
