---
title: xml
slug: userredxml
source_url: "https://developers.mindbox.ru/docs/userredxml"
breadcrumb:
  - Клиент
  - Редактирование данных клиента
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:33797d556bceb0ebe413a1cc742402f6ae7b5e04c04796b583f3a186c9b06835"
---

# xml

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <authenticationTicket>{Секретный тикет}authenticationTicket>
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
    <email>{Емэйл клиента}email>
    <mobilePhone>{Мобильный телефон}mobilePhone>
    <lastName>{Фамилия клиента}lastName>
    <firstName>{Имя клиента}firstName>
    <birthDate>{Дата рождения в формате YYYY-MM-DD}birthDate>
    <password>{Пароль}password>
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
  customer>
operation>
```

Секретный тикет нужен, если сервис дергается без секретного ключа напрямую с клиента. Его можно сформировать самостоятельно по алгоритму описанному [здесь](website-authorization-ticket.md)  
Также он может понадобится, если потребитель не аутентифицирован и переходит из письма по секретной ссылке. Тогда тикет берется из ссылки.

Чтобы затереть поле, надо передать тег с атрибутом `clear`. Например:

## Примеры операций

#### Редактирование данных в личном кабинете

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=EditCustomer

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <bitrixId>346257bitrixId>
    ids>
    <email>pivan@mindbox.ruemail>
    <mobilePhone>79374134389mobilePhone>
    <lastName>ПетровlastName>
    <firstName>ИванfirstName>
    <password>Qwertypassword>
    <customFields>
      <city>Mоскваcity>
      <b2b>trueb2b>
    customFields>
    <subscriptions>
      <subscription>
        <pointOfContact>SmspointOfContact>
        <topic>Recommendationtopic>
        <isSubscribed>falseisSubscribed>
      subscription>
      <subscription>
        <pointOfContact>EmailpointOfContact>
        <topic>Recommendationtopic>
        <isSubscribed>trueisSubscribed>
      subscription>
    subscriptions>
  customer>
operation>
```

#### Редактирование данных с аутентификацией по тикету

#### Замена пароля на новый с помощью секретной ссылки

#### Очистка данных клиента
