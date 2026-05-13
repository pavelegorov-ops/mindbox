---
title: xml
slug: userregxml
source_url: "https://developers.mindbox.ru/docs/userregxml"
breadcrumb:
  - Клиент
  - "Регистрация, формы подписки, трекинг входа на сайт"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:1a05510db6092f6db419030fadbb9589a8ad5063a8c493cb6e56104d52cc8790"
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
    <ids>
      <webSiteUserId>{Идентификатор клиента}webSiteUserId>
    ids>
    <email>{Емэйл клиента}email>
    <mobilePhone>{Мобильный телефон}mobilePhone>
    <lastName>{Фамилия клиента}lastName>
    <firstName>{Имя клиента}firstName>
    <birthDate>{Дата рождения в формате YYYY-MM-DD}birthDate>
    <password>{Пароль}password>
    <area>
      <ids>
        <externalId>{Идентификатор географической зоны клиента}externalId>
      ids>
    area>
    <subscriptions>
      <subscription>
        <pointOfContact>{Канал коммуникации Email/SMS/тд}pointOfContact>
        <topic>{Тематика рассылок}topic>
      subscription>
    subscriptions>
    <customFields>
      <Дополнительное поле>{Значение дополнительного поля}Дополнительное поле>
      <Дополнительное поле со множеством значений>
        <value>{Значение дополнительного поля}value>
        <value>{Значение дополнительного поля}value>        
      Дополнительное поле со множеством значений>
    customFields>
  customer>
operation>
```

## Примеры операций

#### Регистрация на сайте

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=registartion

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <bitrixId>346257bitrixId>
    ids>
    <email>test@mindbox.ruemail>
    <mobilePhone>79374134389mobilePhone>
    <fullName>Петров ИванfullName>
    <password>Qwertypassword>
    <area>
      <ids>
        <externalId>MoscowexternalId>
      ids>
    area>
    <subscriptions>
      <subscription>
        <pointOfContact>SmspointOfContact>
        <topic>Newstopic>
      subscription>
      <subscription>
        <pointOfContact>EmailpointOfContact>
        <topic>Digesttopic>
      subscription>
    subscriptions>
    <customFields>
      <b2b>trueb2b>
      <childrenNames>
        <value>Петяvalue>
        <value>Машаvalue>
      childrenNames>
    customFields>
  customer>
operation>
```

#### Трекинг входа на сайт

#### Заказ обратного звонка

#### Попап подписки

#### Регистрация по реферальному коду

#### Регистрация в мобильном приложении

## Ответ

#### Успешная регистрация нового потребителя

```
<result>
    <status>Successstatus>
result>
```

#### Если такой потребитель уже есть

В зависимости от настроек операции при повторной регистрации мы можем либо редактировать потребителя, либо возвращать валидационную ошибку. Валидационная ошибка может возникать из-за повторной регистрации с уникальным идентификатором, который уже есть в системе или из-за повторной регистрации контактов с доступом к аккаунту. Подробнее можно прочитать [здесь](https://help.mindbox.ru/docs/%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D0%B2%D0%BE%D0%B7%D0%BD%D0%B8%D0%BA%D0%B0%D0%B5%D1%82-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B0-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-id-%D0%B4%D0%BE%D0%BB%D0%B6%D0%BD%D1%8B-%D0%B1%D1%8B%D1%82%D1%8C-%D1%83%D0%BD%D0%B8%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B-%D1%83%D0%B1%D0%B5%D0%B4%D0%B8%D1%82%D0%B5%D1%81%D1%8C-%D1%87%D1%82%D0%BE-%D0%B2%D1%8B-%D0%BD%D0%B5-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D1%82%D0%B5-%D0%BE%D0%B4%D0%B8%D0%BD-%D0%B8-) и [здесь](https://help.mindbox.ru/docs/%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D0%B2%D0%BE%D0%B7%D0%BD%D0%B8%D0%BA%D0%B0%D0%B5%D1%82-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B0-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-%D1%81-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D0%BE%D0%BC-%D1%83%D0%B6%D0%B5-%D0%B7%D0%B0%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD-%D0%B2%D0%B2%D0%B5%D0%B4%D0%B8%D1%82%D0%B5-%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B9-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C) .
