---
title: Получение общей суммы оплаченных заказов
slug: "get-total-paid-orders-amount"
source_url: "https://developers.mindbox.ru/docs/get-total-paid-orders-amount"
breadcrumb:
  - Заказы
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0670dcd127dcc0bde8ac8af5235fb8edc7692a1d6d82fce9ea21bb83dc6f7a7f"
---

# Получение общей суммы оплаченных заказов

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

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
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
  customer>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetCustomerRetailOrderStatistics

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
  <retailOrderStatistics>
    <totalPaidAmount>{Сумма оплаченных заказов}totalPaidAmount>
  retailOrderStatistics>
result>
```
