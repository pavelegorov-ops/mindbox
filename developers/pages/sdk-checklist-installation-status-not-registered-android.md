---
title: У установки статус «приложение не зарегистрировано в системе отправки пушей»
slug: "sdk-checklist-installation-status-not-registered-android"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-installation-status-not-registered-android"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:9337572882a92486b9c579a991a6c08cd1bcfdb11145ce3cf48a0215290ff096"
---

# У установки статус «приложение не зарегистрировано в системе отправки пушей»

## Не реализована инструкция по работе с push-уведомлениями

### Как проверить

Убедитесь, что реализованы пункты из инструкции о [Firebase](firebase-send-push-notifications.md) и [Huawei](huawei-send-push-notifications.md).

### Как поправить

Реализуйте пункты из инструкций.

## Не был вызван метод передачи токена

### Как проверить

Убедитесь, что вызывается метод `Mindbox.updatePushToken`.

### Как поправить

Реализуйте пункты инструкции о [Firebase](firebase-send-push-notifications.md#2-передать-в-sdk-firebase-токен) и [Huawei](huawei-send-push-notifications.md#2-передать-в-sdk-firebase-токен).
