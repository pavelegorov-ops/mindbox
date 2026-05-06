---
title: Получение баланса клиента
slug: "get-customer-bonus-balance"
source_url: "https://developers.mindbox.ru/docs/get-customer-bonus-balance"
breadcrumb:
  - Бонусный счет
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:3663fb666e3946dbf52b81c7155af532b1b5e401a4ae85854419ada80de67743"
---

# Получение баланса клиента

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
operation>
```

## Примеры операций

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=giveCustomerBalance

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <webSiteUserId>5384275webSiteUserId>
    ids>
  customer>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
  <balances>
    <balance>
      <totalValue>{Сумма баллов, накопленных за все время программы}totalValue>
      <availableValue>{Сумма баллов, доступная к трате}availableValue>
      <blockedValue>{Сумма баллов, недоступная к трате}blockedValue>
      <balanceType>
        <ids>
          <systemName>{Системное имя балльного счёта}systemName>
        ids>
        <name>{Название балльного счёта}name>
      balanceType>
    balance>
  balances>
result>
```

Порядок элементов в массиве `balances` не гарантирован и может меняться. Если на проекте более двух балльных счетов, при обработке ответа полагайтесь не на порядок в массиве, а на системное имя балльного счета (`systemName`).
