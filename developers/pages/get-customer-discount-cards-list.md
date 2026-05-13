---
title: Получение списка дисконтных карт клиента
slug: "get-customer-discount-cards-list"
source_url: "https://developers.mindbox.ru/docs/get-customer-discount-cards-list"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8160361455b5dbde14c3410c15082593ad4390cb77dc0af88f6630b90c2e3ce8"
---

# Получение списка дисконтных карт клиента

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
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetCustomerDiscountCards

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
  <discountCards>
    <discountCard>
      <ids>
        <number>{Номер карты}number>
      ids>
      <status>
        <ids>
          <systemName>{Статус карты}systemName>
        ids>		
      status>
      <customFields>
        <Дополнительное поле>{Значение дополнительного поля}Дополнительное поле>
      customFields>
    discountCard>
  discountCards>
result>
```
