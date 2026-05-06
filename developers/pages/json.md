---
title: json
slug: json
source_url: "https://developers.mindbox.ru/docs/json"
breadcrumb:
  - Клиент
  - "Регистрация, формы подписки, трекинг входа на сайт"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:6b5e4e06e648bcf5aa0d3ba2853bbc8df4a993da4915f2ed05861b6a23918557"
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
    "ids": {
      "<Идентификатор>": "<Значение идентификатора>",
    },
    "lastName": "<Фамилия клиента>",
    "firstName": "<Имя клиента>",
    "middleName": "<Отчество клиента>",
    "mobilePhone": "<Мобильный телефон клиента>",
    "email": "<Емэйл клиента>",
    "password": "<Пароль>",
    "area": {
      "ids": {
        "externalId": "<Идентификатор региона клиента>"
      }
    },
    "customFields": {
      "<Дополнительное поле>": "<Значение дополнительного поля>",
      "<Дополнительное поле со множеством значений>": [
      "<Значение дополнительного поля>",
      "<Значение дополнительного поля>"
      ],
    },
    "subscriptions": [
      {
        "pointOfContact": "<Канал коммуникации Email/SMS/тд>",
        "topic": "<Тематика рассылок>",
      }
    ]
  }
}
```

## Примеры операций

#### Регистрация

```
POST https://api.mindbox.ru/v3/operations/async?endpointId=MindboxRu&operation=registration

Accept: application/json
Content-Type: application/json
Authorization: SecretKey D061p764m85bklq

{
  "customer": {
    "ids": {
      "bitrixId": "346257"
    },
    "mobilePhone": 79374134389,
    "fullName": "Петров Иван",
    "email": "test@mindbox.ru",
    "password": "Qwerty",
    "customFields": {
      "city": "Mосква",
      "b2b": true,
      "childrenNames": [
        "Маша",
        "Петя"
      ]
    },
    "subscriptions": [
      {
        "pointOfContact": "Sms",
        "topic": "News"
      },
      {
        "pointOfContact": "Email",
        "topic": "Digest"
      }
    ]
  }
}
```

#### Трекинг входа на сайт

#### Заказ обратного звонка

#### Попап подписки

## Ответ

#### Успешная регистрация нового потребителя

```
{
  status: "Success"
}
```

#### Если такой потребитель уже есть
