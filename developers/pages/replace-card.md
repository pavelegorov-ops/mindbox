---
title: Замена дисконтной карты
slug: "replace-card"
source_url: "https://developers.mindbox.ru/docs/replace-card"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:907dd03d5257de4953289645f2eed4840df6243d2d89992201935ff52a3e6cfc"
---

# Замена дисконтной карты

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <oldDiscountCard>
    <ids>
      <number>{Номер старой карты}number>
    ids>
  oldDiscountCard>
 	<newDiscountCard>
    <ids>
      <number>{Номер новой карты}number>
    ids>
  newDiscountCard>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=ReplaceCard

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <oldDiscountCard>
    <ids>
      <number>421432234321number>
    ids>
  oldDiscountCard>
 	<newDiscountCard>
    <ids>
      <number>421432234334number>
    ids>
  newDiscountCard>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
  <oldDiscountCard>
    <processingStatus>{Системное имя статуса для старой карты}processingStatus>
  oldDiscountCard>
  <newDiscountCard>
    <processingStatus>{Системное имя статуса для новой карты}processingStatus>
  newDiscountCard>
result>
```

## Статус операции для старой карты

| Описание | Статус операции |
| --- | --- |
| Статус карты изменен | Changed |
| У карты уже установлен такой статус | NotChanged |
| Карта не привязана к клиенту. Нельзя менять у нее статус. | NotBoundToCustomer |
| Карта с таким номером не найдена | NotFound |

## Статус операции для новой карты

| Описание | Статус операции |
| --- | --- |
| Карта успешно привязана | Bound |
| В случае если не удалось найти старую карту или она не привязана к клиенту. | NotProcessed |
| Уже привязана к текущему клиенту | AlreadyBoundToCurrentCustomer |
| Уже привязана к другому клиенту | AlreadyBoundToAnotherCustomer |
| Карта с таким номером не найдена | NotFound |
