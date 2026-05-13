---
title: У установки статус «приложение не зарегистрировано в системе отправки пушей»
slug: "sdk-checklist-installation-status-not-registered"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-installation-status-not-registered"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c6411328a957b25531efd6d7bfd97f34c6a24ca604fb6e5e31ce7c6a37c90307"
---

# У установки статус «приложение не зарегистрировано в системе отправки пушей»

Ошибка возникает, когда приложение запустилось, клиент есть в админке, но не пришел токен от приложения.

## Не был вызван метод передачи токена

### Как проверить

Проверьте вызов метода `Mindbox.shared.apnsTokenUpdate`.

### Как поправить

Если ошибка возникла, значит, у вас собственная реализация делегата Mindbox. Проверьте метод [в этой инструкции](ios-quick-setup-push-notifications.md#самостоятельная-настройка) — у вас должен быть идентичный.
