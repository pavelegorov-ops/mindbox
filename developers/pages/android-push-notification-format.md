---
title: Формат пуш уведомления Android
slug: "android-push-notification-format"
source_url: "https://developers.mindbox.ru/docs/android-push-notification-format"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:bfe2b054af4f795ba579e3c2c49353630913f5266c1ac3670ca8da931f9cfc5d"
---

# Формат пуш уведомления Android

Mindbox отправляет пуши через Firebase. У всех уведомлений есть только поле `data`, чтобы вы могли в приложении обработать получение и отрисовку уведомления

Это приводит к тому, что в методе `onMessageRecieved` надо явно реализовать отображение уведомления.

### Описание полей

`message` , `clickUrl` заполняются всегда

`title` - необязательный ключ

`imageUrl` и `payload` - могут быть пустыми

`buttons` - строка, может содержать от 0 до 3 объектов

```
{
  "data": {
    "title": "<Заголовок сообщения>",
    "message": "<Текст сообщения>",
    "clickUrl": "<Ссылка с тела пуша>",
    "imageUrl": "<Ссылка на картинку>",
    "payload": "<Любой дополнительный JSON>",
    "buttons": "[{\"text\":\"<Текст кнопки 1>\",\"url\":\"<Ссылка с кнопки 1>\",\"uniqueKey\":\"<Гуид кнопки 1>\"},{\"text\":\"<Текст кнопки 2>\",\"url\":\"<Ссылка с кнопки 2>\",\"uniqueKey\":\"<Гуид кнопки 2>\"},{\"text\":\"<Текст кнопки 3>\",\"url\":\"<Ссылка с кнопки 3>\",\"uniqueKey\":\"<Гуид кнопки 3>\"}]",
    "uniqueKey": "<Гуид сообщения>"
  }
}
```
