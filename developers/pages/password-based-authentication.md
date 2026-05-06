---
title: Аутентификация по паролю
slug: "password-based-authentication"
source_url: "https://developers.mindbox.ru/docs/password-based-authentication"
breadcrumb:
  - Клиент
  - Аутентификация
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:2fccda772acff18ce9aed705104168c8033334e28401ee61dcf6d3165801aed8"
---

# Аутентификация по паролю

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

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
    <password>{Пароль}password>
  customer>
operation>
```

## Пример операции

#### Аутентификация по email и паролю

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=AuthenticateByPassword

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <email>test@mail.ruemail>
    <password>Qwertypassword>
  customer>
operation>
```

#### Аутентификация по мобильному телефону и паролю

## Ответ

#### Если пароль верен

```
<result>
  <status>Successstatus>
  <customer>
    <processingStatus>AuthenticationSucceededprocessingStatus>
  customer>
result>
```

#### Если пароль не верен

#### Если потребителя не найден
