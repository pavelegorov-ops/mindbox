---
title: xml
slug: tranletterxml
source_url: "https://developers.mindbox.ru/docs/tranletterxml"
breadcrumb:
  - Рассылки
  - Отправка рассылок по API
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:110c0bb3f9802e14efc7a7ebe95f14a777a2b6ddec9f3432133703de7f20c515"
---

# xml

## Описание метода

Осуществляется с помощью POST-запроса. Событие для отправки письма определяется на стороне клиента. Название операции и набор принимаемых полей настраиваются в системе Mindbox. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}&{transactionId}={Id транзакции в вашей системе}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customer>
    <email>{Email}email>
  customer>
  <emailMailing>
    <customParameters>
      <{Имя параметра}>{Значение параметра}
    customParameters>
    <attachments>
      <attachment>
        <fileName>{Имя прикрепляемого файла}fileName>
        <body>
          <fileId>{Идентификатор прикрепляемого файла}fileId>
        body>
      attachment>
    attachments>
  emailMailing>
  <executionDateTimeUtc>{Дата и время выполнения (можно использовать для выполнения запроса задним числом)}executionDateTimeUtc>
operation>
```

### Параметры запроса

- `customer/email` — может быть любой другой идентификатор клиента, зависит от настроек операции.
- `emailMailing` — объект для передачи дополнительных параметров при их наличии. Может меняться на `smsMailing/viberMailing/mobilePushMailing/webPushMailing` в зависимости от канала рассылок.
- `customParameters` — объект для передачи [пользовательских параметров](https://help.mindbox.ru/docs/custom-parameters-operation) при их наличии.
- `attachments` — массив для передачи [вложений](https://help.mindbox.ru/docs/email-with-attachment) при их наличии.

**transactionId** — это ключ идемпотентности, который используется как уникальный идентификатор транзакции отправки письма в вашей системе (необязательный параметр).

[Подробнее о ключе идемпотентности.](https://help.mindbox.ru/docs/idempotentnost#kak-sozdat-klyuch-idempotentnosti)

По этому идентификатору можно узнать статус рассылки: была ли доставлена, открыта и т.п. Если в Mindbox уже зарегистрирована транзакция с таким `transactionId`, то повторно рассылка не будет отправлена и в логе запроса будет сообщение **Transaction already processed**. Если в случае ошибки вы вызываете операцию повторно, то `transactionId` передавать обязательно. Иначе рассылка может отправиться одному и тому же человеку несколько раз.

Отправка Email в режиме `sync` не поддерживает использование `transactionId` — сообщения уйдут клиенту дважды. Для отправки письма используйте режим `async`.

Если все же необходимо настроить операцию в синхронном режиме с использованием ключа идемпотентности, обратитесь к менеджеру вашего проекта.

## Примеры операций

#### Приветственное письмо

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=sendWelcome

Accept: application/xml
Content-Type: application/xml

<operation>
<customer>
  <email>pivan@mindbox.ruemail>
customer>
operation>
```

#### Востановление пароля

#### Письмо с товарным блоком

#### Отправка СМС сообщения

#### Отправка сообщения в Viber
