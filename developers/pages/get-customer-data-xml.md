---
title: xml
slug: "get-customer-data-xml"
source_url: "https://developers.mindbox.ru/docs/get-customer-data-xml"
breadcrumb:
  - Клиент
  - Получение данных клиента
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:1d5e44f16fb9570a2d762b146ba3e7ab701e4c2de8dcdf552da8700c8881af0b"
---

# xml

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

- В ответе возвращаются только заполненные поля клиента

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=getCustomer

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

#### Клиент найден

```
<result>
  <status>Successstatus>
  <customer>
    <processingStatus>FoundprocessingStatus>
    <ids>
      <mindboxId>{ID клиента в БД mindbox}mindboxId>
      <myWebSiteId>{ID пользователя на сайте}myWebSiteId>
    ids>
    <sex>{пол - male/female}sex>
    <email>{Емэйл клиента}email>
    <isEmailInvalid>{Емэйл клиента невалиден - true/false}isEmailInvalid>
    <isEmailConfirmed>{Емэйл клиента подтвержден - true/false}isEmailConfirmed>
    <pendingEmail>{Емэйл, ожидающий подтверждения после смены}pendingEmail>
    <mobilePhone>{Мобильный телефон}mobilePhone>
    <isMobilePhoneInvalid>{Мобильный телефон невалиден - true/false}isMobilePhoneInvalid>
    <isMobilePhoneConfirmed>{Мобильный телефон подтвержден - true/false}isMobilePhoneConfirmed>
    <pendingMobilePhone>{Мобильный телефон, ожидающий подтверждения после смены}pendingMobilePhone>
    <lastName>{Имя клиента}lastName>
    <firstName>{Фамилия клиента}firstName>
    <birthDate>{Дата рождения в формате YYYY-MM-DD}birthDate>
    <area>
      <ids>
        <externalId>{Идентификатор географической зоны клиента}externalId>
      ids>
      <name>{Название географической зоны клиента}name>
    area>
    <subscriptions>
      <subscription>
        <pointOfContact>{Канал коммуникации Email/SMS/тд}pointOfContact>
        <topic>{Тематика рассылок}topic>
        <isSubscribed>{Статус подписки true/false}isSubscribed>        
      subscription>
    subscriptions>
    <customFields>
      <Дополнительное поле>{Значение дополнительного поля}Дополнительное поле>
    customFields>
    <changeDateTimeUtc>{Дата регистрации/редактирования в формате YYYY-MM-DD hh:mm:ss.fff}changeDateTimeUtc>
  customer>
result>
```

#### Клиент не найден

Статус обработки/поиска клиента () может иметь различные значения для проверки наличия клиента:

- `Found` - клиент успешно найден
- `NotFound` - клиент не найден
