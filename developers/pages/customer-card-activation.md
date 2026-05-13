---
title: Выдача дисконтной карты клиенту
slug: "customer-card-activation"
source_url: "https://developers.mindbox.ru/docs/customer-card-activation"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c9bb08cab9aa1b238e40b282fb643c2e1de7eb1165b686dd2b6f6a5443e926a1"
---

# Выдача дисконтной карты клиенту

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteId>{ID пользователя на сайте}webSiteId>
    ids>
  customer>
  <discountCard>
    <ids>
      <number>{Номер карты}number>
    ids>
  discountCard>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=RegCard

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <webSiteId>52367webSiteId>
    ids>
  customer>
  <discountCard>
    <ids>
      <number>231534554262number>
    ids>
  discountCard>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
  <customer>
  	<processingStatus>{Found/NotFound}processingStatus>
  customer>
  <discountCard>
  	<processingStatus>{Статус обработки карты}processingStatus>
  discountCard>
result>
```

## Статус обработки карты

| Описание | Статус операции |
| --- | --- |
| Карта успешно привязана | Bound |
| Уже привязана к текущему клиенту | AlreadyBoundToCurrentCustomer |
| Уже привязана к другому клиенту | AlreadyBoundToAnotherCustomer |
| Карта с таким номером не найдена | NotFound |
| В случае если не удалось найти клиента | NotProcessed |
