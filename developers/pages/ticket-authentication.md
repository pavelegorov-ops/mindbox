---
title: Аутентификация по ссылке из рассылки
slug: "ticket-authentication"
source_url: "https://developers.mindbox.ru/docs/ticket-authentication"
breadcrumb:
  - Клиент
  - Аутентификация
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:67950523675ec3001046613c178c31fda8eb1d26e8205acd572cfd5531f23dc3"
---

# Аутентификация по ссылке из рассылки

# Аутентификация по ссылке из рассылки

## Описание метода

Метод позволяет автоматически авторизовать клиента на сайте при переходе по персональной ссылке из рассылки.

Как это работает:

- В рассылке формируется персональная ссылка с [тикетом аутентификации](https://help.mindbox.ru/docs/%D1%82%D0%B8%D0%BA%D0%B5%D1%82)
- Клиент переходит по ссылке на сайт
- Сайт извлекает тикет из URL и отправляет запрос в Mindbox API
- Mindbox проверяет тикет и возвращает данные клиента, если тикет корректен
- Сайт авторизует клиента на основе полученных данных

Настройка авторизации через ссылку в чат-боте описана в [статье](chatbot-authorization.md).

## Предварительная настройка

Перед началом интеграции убедитесь, что:

1. Создана операция в Mindbox со следующими шагами:

   - Клиент — Авторизованный — Получить существующего по тикету
   - Клиент — Получить данные по текущему клиенту (настройте нужные поля для возврата)

   [Подробнее о создании операций](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F).
2. Настроена ссылка перехода в рассылки с использованием тикета. Например универсальный тикет на 5 минут:
   `https://example.com/auth?ticket=${Ticket.UniversalAuthenticationCustomizableTimeTicket(5)}`

## Формат запроса

### URL и параметры

`POST https://api.mindbox.ru/v3/operations/sync?endpointId={Идентификатор точки интеграции}&operation={Название операции}&deviceUUID={Уникальный идентификатор устройства}`

Подробнее о работе с V3 API, URL запросов и заголовках: [Документация V3 API](v3.md)

### Заголовки

| Заголовок | Значение JSON | Значение XML |
| --- | --- | --- |
| Authorization | SecretKey {секретный_ключ_точки_интеграции} | |
| Content-Type | application/json; charset=utf-8 | application/xml; charset=utf-8 |
| Accept | application/json | application/xml |

### Тело запроса

#### JSON

```
{
  "customer": {
    "authenticationTicket": "<Тикет аутентификации клиента из ссылки>"
  }
}
```

#### XML

## Пример запроса

#### JSON

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=AuthenticateByTicket&deviceUUID=550e8400-e29b-41d4-a716-446655440000

Content-Type: application/json; charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}

{
  "customer": {
    "authenticationTicket": "YwQzgwMDY5Q0IwNEE5RDNFRDAyMzRBQTE4NTZCMkVENzAyNzE1MCIgc2lnbmF0dXJlPSJFREVEMkE2NzNDQjAwMEY1MTNGQzBGN0Q0NkY0NTY2MjRGMThCNjVCRUE5REM4MDMxRUJDNTZBOTJBODdGN0JBOTZBOTJBQzk3NjRBNjBGRURCNjYwRjAzRkY0NDgyMzkxMjI5MkI4NDhENEZGQTUwRDExODA2NjAwMkVCOTlBMSIgLz"
  }
}
```

#### XML

## Пример ответа

### Состав параметров

Параметры в узле `customer` зависят от полей, выбранных в шаге операции «Клиент — Получить данные по текущему клиенту». Уточните список у менеджера проекта или посмотрите в описании операции.

### Корректный тикет

При передаче валидного тикета API возвращает данные клиента:

#### JSON

```
{
  "status": "Success",
  "customer": {
      "firstName": "Иван",
      "lastName": "Петров",
      "email": "test@example.com",
      "isEmailInvalid": false,
      "mobilePhone": 79991234567,
      "isMobilePhoneInvalid": false,
      "ids": {
        "mindboxId": 12345,
        "websiteID": "user-67890"
      },
      "changeDateTimeUtc": "2026-02-19T08:21:29.54Z"
  }
}
```

#### XML

### Некорректный или просроченный тикет

При передаче невалидного тикета API возвращает ответ без данных клиента:

#### JSON

```
{
  "status": "Success"
}
```

#### XML

### Полный список возможных параметров ответа

## Обработка ошибок

### ProtocolError

Ошибка возникает при передаче пустого значения `authenticationTicket`:

#### JSON

```
{
  "status": "ProtocolError",
  "errorMessage": "/customer/authenticationTicket: Поле должно быть заполнено.",
  "errorId": "<Идентификатор ошибки. Может отсутствовать>",
  "httpStatusCode": 400
}
```

#### XML

## Обработка результата на сайте

После получения ответа от API:

1. Проверьте статус ответа (`status`)
2. Проверьте наличие узла `customer` в ответе
3. Если данные клиента **получены** — авторизуйте клиента на сайте
4. Если данные клиента **отсутствуют** — перенаправьте на страницу входа

Конкретная реализация зависит от особенностей вашей интеграции.

## Связанные материалы

- [Аутентификация по паролю](password-based-authentication.md)
- [Аутентификация по секретному коду](secret-code-authentication.md)
- [Типы тикетов аутентификации](https://help.mindbox.ru/docs/%D1%82%D0%B8%D0%BA%D0%B5%D1%82)
