---
title: Аутентификация по секретному коду
slug: "secret-code-authentication"
source_url: "https://developers.mindbox.ru/docs/secret-code-authentication"
breadcrumb:
  - Клиент
  - Аутентификация
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:92313d9d9ca1f8c112160890017cf30fcaeff39b7a5884ce9eb9cf7b1b7d4d68"
---

# Аутентификация по секретному коду

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
  customer>
  <authentificationCode>{Секретный код}authentificationCode>
operation>
```

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=AuthenticateBySecretCode

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
  	<mobilePhone>79001234567mobilePhone>
  customer>
  <authentificationCode>1234authentificationCode>
operation>
```

## Ответ

#### Если код верен

```
<result>
  <status>Successstatus>
result>
```

#### Если код не верен
