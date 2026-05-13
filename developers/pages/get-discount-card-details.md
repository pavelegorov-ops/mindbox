---
title: Получение данных дисконтной карты
slug: "get-discount-card-details"
source_url: "https://developers.mindbox.ru/docs/get-discount-card-details"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:db722688c27727ada444f91515f7f7e46968a2708b1b41ac9158b169d041f8b1"
---

# Получение данных дисконтной карты

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

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
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=GetDiscountCard

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
    <processingStatus>{Found/NotFound}processingStatus>
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
```

## Статусы карт

По умолчанию, на проекте заведено 3 статуса карт. Словарь статусов карт, расширяется в системе Майндбокс.

| Статус карты | Системное имя статуса карты |
| --- | --- |
| Не выдана (в пуле) | NotIssued |
| Выдана (в пуле, но точный статус неизвестен) | Issued |
| Не активирована | Inactive |
| Активирована | Activated |
| Заблокирована | Blocked |
