---
title: json
slug: "get-customer-data-json"
source_url: "https://developers.mindbox.ru/docs/get-customer-data-json"
breadcrumb:
  - Клиент
  - Получение данных клиента
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:a9bd002d6379d1978391162dad196fc283a9c4f7c63e01083386fbdc17250f01"
---

# json

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

{
  "customer": {
    "ids": {
      "webSiteUserId": "{Идентификатор клиента}"
    }
  }
}
```

- В ответе возвращаются только заполненные поля клиента

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=getCustomer

Accept: application/json
Content-Type: application/json
Authorization: SecretKey D061p764m85bklq

{
  "customer": {
    "ids": {
      "webSiteUserId": "5384275"
    }
  }
}
```

## Ответ

#### Клиент найден

```
{
    "status": "Success",
    "customer": {
        "processingStatus": "Found",
        "ids": {
            "mindboxId": "{ID клиента в БД mindbox}",
            "myWebSiteId": "{ID пользователя на сайте}"
        },
        "sex": "{пол - male/female}",
        "email": "{Емэйл клиента}",
        "isEmailInvalid": "{Емэйл клиента невалиден - true/false}",
        "isEmailConfirmed": "{Емэйл клиента подтвержден - true/false}",
        "pendingEmail": "{Емэйл, ожидающий подтверждения после смены}",
        "mobilePhone": "{Мобильный телефон}",
        "isMobilePhoneInvalid": "{Мобильный телефон невалиден - true/false}",
        "isMobilePhoneConfirmed": "{Мобильный телефон подтвержден - true/false}",
        "pendingMobilePhone": "{Мобильный телефон, ожидающий подтверждения после смены}",
        "lastName": "{Фамилия клиента}",
        "firstName": "{Имя клиента}",
        "birthDate": "{Дата рождения в формате YYYY-MM-DD}",
        "area": {
            "ids": {
                "externalId": "{Идентификатор географической зоны клиента}"
            },
            "name": "{Название географической зоны клиента}"
        },
        "subscriptions": [
            {
                "pointOfContact": "{Канал коммуникации Email/SMS/тд}",
                "topic": "{Тематика рассылок}",
                "isSubscribed": "{Статус подписки true/false}"
            }
        ],
        "customFields": {
            "Дополнительное поле": "{Значение дополнительного поля}"
        },
        "changeDateTimeUtc": "{Дата регистрации/редактирования в формате YYYY-MM-DD hh:mm:ss.fff}"
    }
}
```

#### Клиент не найден

Статус обработки/поиска клиента (`processingStatus`) может иметь различные значения для проверки наличия клиента:

- `Found` - клиент успешно найден
- `NotFound` - клиент не найден
