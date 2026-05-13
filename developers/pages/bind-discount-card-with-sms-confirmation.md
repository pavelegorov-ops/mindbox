---
title: "Выдача дисконтной карты клиенту с смс-подтверждением"
slug: "bind-discount-card-with-sms-confirmation"
source_url: "https://developers.mindbox.ru/docs/bind-discount-card-with-sms-confirmation"
breadcrumb:
  - Карты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:259a5ff3678f40ac7fbef30ad39ab05b248d8b39d5a0cd0d1ae98164f447248a"
---

# Выдача дисконтной карты клиенту с смс-подтверждением

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <mobilePhone>{мобильный телефон клиента}mobilePhone>
  customer>
  <discountCard>
    <ids>
      <number>{Номер карты}number>
    ids>
  discountCard>
  <authentificationCode>{Код подтверждения}authentificationCode>
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
    <mobilePhone>71234567890mobilePhone>
  customer>
  <discountCard>
    <ids>
      <number>231534554262number>
    ids>
  discountCard>
  <authentificationCode>1234authentificationCode>
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
| Уже привязана к текущему потребителю | AlreadyBoundToCurrentCustomer |
| Уже привязана к другому потребителю | AlreadyBoundToAnotherCustomer |
| Карта с таким номером не найдена | NotFound |
| В случае если не удалось найти потребителя | NotProcessed |
