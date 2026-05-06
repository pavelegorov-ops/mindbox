---
title: json
slug: "userredjson-1"
source_url: "https://developers.mindbox.ru/docs/userredjson-1"
breadcrumb:
  - Клиент
  - Редактирование данных клиента
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:48121d48820bcc869350aae34644168055a06574a74ba9b799f53d556c05f1a2"
---

# json

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

{
    "customer": {
        "authenticationTicket": "{Секретный тикет}",
        "ids": {
            "webSiteUserId": "{Идентификатор клиента}"
        },
        "email": "{Емэйл клиента}",
        "mobilePhone": "{Мобильный телефон}",
        "lastName": "{Фамилия клиента}",
        "firstName": "{Имя клиента}",
        "birthDate": "{Дата рождения в формате YYYY-MM-DD}",
        "password": "{Пароль}",
        "subscriptions": [
            {
                "pointOfContact": "{Канал коммуникации Email/SMS/тд}",
                "topic": "{Тематика рассылок}",
                "isSubscribed": "{Статус подписки true/false}"
            }
        ],
        "customFields": {
            "Дополнительное поле": "{Значение дополнительного поля}"
        }
    }
}
```

Секретный тикет нужен, если сервис вызывается без секретного ключа напрямую с клиента. Его можно сформировать самостоятельно по алгоритму описанному [здесь](website-authorization-ticket.md)  
Также он может понадобится, если потребитель не аутентифицирован и переходит из письма по секретной ссылке. Тогда тикет берется из ссылки.

Чтобы затереть поле, надо передать значение `%CLEAR%`. Например: `"mobilePhone": "%CLEAR%"`

## Примеры операций

#### Редактирование данных в личном кабинете

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=EditCustomer

Accept: application/json
Content-Type: application/json
Authorization: SecretKey D061p764m85bklq

{
    "customer": {
        "ids": {
            "bitrixId": "346257"
        },
        "email": "pivan@mindbox.ru",
        "mobilePhone": 79374134389,
        "lastName": "Петров",
        "firstName": "Иван",
        "password": "Qwerty",
        "customFields": {
            "city": "Mосква",
            "b2b": true
        },
        "subscriptions": [
            {
                "pointOfContact": "Sms",
                "topic": "Recommendation",
                "isSubscribed": false
            },
            {
                "pointOfContact": "Email",
                "topic": "Recommendation",
                "isSubscribed": true
            }
        ]
    }
}
```

#### Редактирование данных с аутентификацией по тикету

#### Замена пароля на новый с помощью секретной ссылки

#### Очистка данных клиента
