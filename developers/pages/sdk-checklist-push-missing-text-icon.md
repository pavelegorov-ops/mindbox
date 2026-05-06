---
title: "Уведомления приходят, но в них не отображаются текст, иконка или вообще ничего"
slug: "sdk-checklist-push-missing-text-icon"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-push-missing-text-icon"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:9c139778a2c4ee898169b364c2536b1633ce2d17310caf524f363d0a33341121"
---

# Уведомления приходят, но в них не отображаются текст, иконка или вообще ничего

## Отрисовка сообщения реализована с ошибкой

### Как проверить

Проверьте метод `onMessageReceived`. Убедитесь, что он совпадает с тем, что описано в инструкциях о [Firebase](firebase-send-push-notifications.md#3-реализовать-отображение--уведомлений) и [Huawei](huawei-send-push-notifications.md#3-реализовать-отображение--уведомлений).

Если нет вызова `Mindbox.handleRemoteMessage`, значит, push-уведомление отрисовывается не нашей функций, это нужно дебажить на вашей стороне.

### Как поправить

Реализуйте пункты в соответствии с инструкциями выше.
