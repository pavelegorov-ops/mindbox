---
title: Формат пуш уведомления iOS
slug: "ios-push-notification-format"
source_url: "https://developers.mindbox.ru/docs/ios-push-notification-format"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:e03ead99244f0d42a16cf840aefcfbea8047dd2823b2960d93a49c6945158b13"
---

# Формат пуш уведомления iOS

Mindbox отправляет пуши через Apple Push Notification System - APNS. У всех пушей по дефолту стоит флаг: `mutable-content 1`. Это значит, что все пуши запускают Notification Service Extension, где вы должны настроить скачивание картинки, обработку кнопок и отправку информации о полученном пуше.

### Описание полей

`body` , `clickUrl` заполняются всегда

`title` - необязательный ключ

`imageUrl` и `payload` - могут быть пустыми

`buttons` - массив кнопок. Может содержать от 0 до 3 элементов

```
{
    "aps": {
        "alert": {
            "title": "<Заголовок сообщения>",
            "body": "<Текст сообщения>"
        },
        "sound": "default",
        "mutable-content": 1,
        "content-available":0
    },
    "clickUrl": "<Ссылка с тела пуша>",
    "imageUrl": "<Ссылка на картинку>",
    "payload": "<Любой дополнительный JSON>",
    "buttons": [
        {
            "text": "<Текст кнопки 1>",
            "url": "<Ссылка с кнопки 1>",
            "uniqueKey": "<Гуид кнопки 1>"
        },
        {
            "text": "<Текст кнопки 2>",
            "url": "<Ссылка с кнопки 2>",
            "uniqueKey": "<Гуид кнопки 2>"
        },
        {
            "text": "<Текст кнопки 3>",
            "url": "<Ссылка с кнопки 3>",
            "uniqueKey": "<Гуид кнопки 3>"
        }
    ],
    "uniqueKey": "<Гуид сообщения>"
}
```

### Можно ли отправить silent push через Mindbox?

**Нет**, Mindbox всегда отправляет только стандартные пуш-уведомления, предназначенные для маркетинговых коммуникаций. По дефолту во всех пушах стоит флаг `content-available 0`.
