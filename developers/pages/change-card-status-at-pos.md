---
title: Смена статуса дисконтной карты на кассе
slug: "change-card-status-at-pos"
source_url: "https://developers.mindbox.ru/docs/change-card-status-at-pos"
breadcrumb:
  - Карты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:89e943d6b9848b83e5f0e257f36679ebd20245822c249cc8e307acce08bf6b25"
---

# Смена статуса дисконтной карты на кассе

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

## Статус операции

| Описание | Статус операции |
| --- | --- |
| Статус изменен | Changed |
| У карты уже установлен такой статус | NotChanged |
| Карта не привязана к клиенту. Нельзя менять у нее статус. | NotBoundToCustomer |
| Карта с таким номером не найдена | NotFound |
