---
title: Подтверждение мобильного телефона и подписки на СМС
slug: "mobile-phone-verification"
source_url: "https://developers.mindbox.ru/docs/mobile-phone-verification"
breadcrumb:
  - Клиент
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:3aa36247245d269d6b066a63510e0518a8421dd93b67e4715f3f73e2de51153c"
---

# Подтверждение мобильного телефона и подписки на СМС

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
  <smsConfirmation>
    <code>{Код подтверждения}code>
  smsConfirmation>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=ConfirmMobilePhone

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <webSiteUserId>42webSiteUserId>
    ids>			
  customer>
  <smsConfirmation>
    <code>1234567code>
  smsConfirmation>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
  <smsConfirmation>
    <processingStatus>{Статус подтверждения}processingStatus>
  smsConfirmation>
result>
```

## Статус подтверждения

| Описание | Статус операции |
| --- | --- |
| Мобильный телефон и подписка на СМС успешно подтверждены. | SubscriptionAndMobilePhoneConfirmed |
| Подписка на СМС успешно подтверждена. Мобильный телефон уже подтвержден или не требует подтверждения. | SubscriptionConfirmed |
| Мобильный телефон успешно подтвержден. Подписка уже подтверждена, или не требует подтверждения. | MobilePhoneConfirmed |
| Мобильный телефон уже подтвержден или не требует подтверждения. >Подписка уже подтверждена, или не требует подтверждения. | AlreadyConfirmed |
| Некорректный код подтверждения | IncorrectConfirmationCode |
| В случае, если не найден потребитель | NotFound |
