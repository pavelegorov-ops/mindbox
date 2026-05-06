---
title: Отправка кода подтверждения
slug: "send-confirmation-code"
source_url: "https://developers.mindbox.ru/docs/send-confirmation-code"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:f2ac0b09b8487eccfe25dfd4c28814add899909a7c85db101310ba4c52b07fc6"
---

# Отправка кода подтверждения

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
    <mobilePhone>{мобильный телефон клиента}mobilePhone>			
  customer>
operation>
```

## Пример операции

```
```xml
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=SendConfirmationCode

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customer>
    <mobilePhone>71234567890mobilePhone>				
  customer>
operation>
```

## Ответ

```
```xml
<result>
  <status>Successstatus>
result>
```
