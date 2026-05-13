---
title: Смена статуса дисконтной карты в личном кабинете
slug: "change-card-status-in-account"
source_url: "https://developers.mindbox.ru/docs/change-card-status-in-account"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8e6e928b3343133143c033458569d988e966fb56ae339d23f59c6998306948b7"
---

# Смена статуса дисконтной карты в личном кабинете

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
      <webSiteId>{ID клиента на сайте}webSiteId>
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
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=ChangeStatus

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
 		<ids>
			<webSiteId>412434webSiteId>
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
  <discountCard>
    <processingStatus>{Статус операции}processingStatus>
    <ids>
			<number>{Номер карты}number>
    ids>
    <status>
      <ids>
        <systemName>{Системное имя статуса карты}systemName>
      ids>
    status>
    <type>
      <ids>
        <externalId>{Внешний идентификатор типа карты}externalId>
      ids>
      <name>{Название типа карты}name>
    type>
    <customFields>
      <Дополнительное поле>{Значение дополнительного поля}Дополнительное поле>
    customFields>
  discountCard>
result>
result>
```

## Статус операции

| Описание | Статус операции |
| --- | --- |
| Статус изменен | Changed |
| У карты уже установлен такой статус | NotChanged |
| Карта не привязана к клиенту. Нельзя менять у нее статус. | NotBoundToCustomer |
| Карта привязана к другому клиенту. Текущий клиент не может изменить ее статус. | BoundToAnotherCustomer |
| Карта с таким номером не найдена | NotFound |
