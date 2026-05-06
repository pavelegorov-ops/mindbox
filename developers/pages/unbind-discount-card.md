---
title: Открепление дисконтной карты
slug: "unbind-discount-card"
source_url: "https://developers.mindbox.ru/docs/unbind-discount-card"
breadcrumb:
  - Карты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8adbe7f8070f2961ab7cccdfbe37b630d0213a32b6be563c1feed3229efa57a3"
---

# Открепление дисконтной карты

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
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
  discountCard>
result>
```

## Статус операции

| Описание | Статус операции |
| --- | --- |
| Карта откреплена | Processed |
| Карты уже ни к кому не прикреплена | NotChanged |
| Карта с таким номером не найдена | NotFound |
