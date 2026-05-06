---
title: Подтверждение мобильного телефона на стороне заказчика
slug: "phone-verification-client-side"
source_url: "https://developers.mindbox.ru/docs/phone-verification-client-side"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:79385f5826b302d98c85310b01b391f2b3b38742fa3e46299f1f1172db1059fb"
---

# Подтверждение мобильного телефона на стороне заказчика

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}

Content-Type: application/xml; charset=utf-8
Accept: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <mindboxId>{Id клиента в Mindbox}mindboxId>
    ids>
    <mobilePhone>{Мобильный телефон}mobilePhone>
  customer>
  <executionDateTimeUtc>{Дата и время выполнения (для выполнения запроса задним числом)}executionDateTimeUtc>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=ConfirmMobilePhone

Content-Type: application/xml; charset=utf-8
Accept: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <mindboxId>1135935890mindboxId>
    ids>
    <mobilePhone>79001234567mobilePhone>
  customer>
  <executionDateTimeUtc>2018-12-19 20:01:58.095executionDateTimeUtc>
operation>
```

## Ответ

```
<result>
  <status>Successstatus>
  <mobilePhoneConfirmation>
    <processingStatus>{Статус подтверждения}processingStatus>
  mobilePhoneConfirmation>
result>
```

## Статус подтверждения

| Описание | Статус операции |
| --- | --- |
| Мобильный телефон подтвержден | MobilePhoneConfirmed |
| Мобильный телефон уже подтвержден | MobilePhoneAlreadyConfirmed |
| Потребитель не найден | NotFound |
