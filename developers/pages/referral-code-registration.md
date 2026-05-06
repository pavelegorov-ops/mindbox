---
title: Реферальная программа
slug: "referral-code-registration"
source_url: "https://developers.mindbox.ru/docs/referral-code-registration"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:66841a8437023bec7d1eb80d6648bd6bb97445d532155fec579af03709d0a4c2"
---

# Реферальная программа

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Mindbox. Подробней про вызов метода можно прочитать [здесь](v3.md). Настройки реферальной программы описаны в [статьях](https://help.mindbox.ru/docs/%D1%80%D0%B5%D1%84%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <ids>
      <webSiteUserId>{Идентификатор приглашенного клиента}webSiteUserId>
      <referralCode>{Реферальный код, который позже приглашенный потребитель сможет слать своим друзьям}referralCode>
    ids>
    <email>{Емэйл приглашенного клиента}email>
    <mobilePhone>{Мобильный телефон приглашенного клиента}mobilePhone>
    <lastName>{Фамилия клиента приглашенного клиента}lastName>
    <firstName>{Имя клиента приглашенного клиента}firstName>
    <birthDate>{Дата рождения приглашенного клиента в формате YYYY-MM-DD}birthDate>
    <area>
      <ids>
        <externalId>{Идентификатор региона приглашенного клиента}externalId>
      ids>
    area>
    <subscriptions>
      <subscription>
        <pointOfContact>{Канал коммуникации Email/SMS/тд}pointOfContact>
        <topic>{Тематика рассылок}topic>
        <isSubscribed>{Статус подписки true/false}isSubscribed>
        <valueByDefault>{Значение поля подписки по умолчанию true/falsevalueByDefault>
      subscription>
    subscriptions>
    <customFields>
      <Дополнительное поле>{Значение дополнительного поля}Дополнительное поле>
    customFields>
  customer>
  <referencedCustomer>
    <ids>
      <referralCode>{Реферальный код клиента, который пригласил друга}referralCode>
      <mindboxId>{Id клиента, который пригласил друга}mindboxId>
      <webSiteUserId>{Идентификатор на сайте клиента, который пригласил друга}webSiteUserId>
    ids>
    <email>{Емэйл клиента, который пригласил друга}email>
    <mobilePhone>{Мобильный телефон клиента, который пригласил друга}mobilePhone>
  referencedCustomer>
operation>
```

В `referencedCustomer` надо передавать потребителя, который уже есть в системе. В `customer` передаем потребителя, которого хотим добавить. Не важно сам он регистрируется, или его приглашает друг.  
За генерацию реферальных кодов отвечает клиент. Нужно просто передавать реферальный код при регистрации потребителя. В качестве кода можно использовать любой идентификатор потребителя или даже его контакт.

## Примеры операции

#### Регистрация по реферальному коду

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=RegistartionByReferrealCode

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <ids>
      <referralCode>ASDFGreferralCode>
    ids>
    <email>pivan@mindbox.ruemail>
    <mobilePhone>79374134389mobilePhone>
    <lastName>ПетровlastName>
    <firstName>ИванfirstName>
  customer>
  <referencedCustomer>
    <ids>
      <referralCode>QWERTYreferralCode>
    ids>
  referencedCustomer>
operation>
```

#### Приглашение друга

## Ответ

#### В случае успешной регистрации (приглашения)

```
<result>
    <status>Successstatus>
    <customer>
    	<processingStatus>CreatedprocessingStatus>
    customer>
    <referencedCustomer>
    	<processingStatus>FoundprocessingStatus>
    referencedCustomer>
result>
```

#### Если реферальный код (приглашающий потребитель) не найден
