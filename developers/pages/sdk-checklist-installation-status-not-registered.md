---
title: У установки статус «приложение не зарегистрировано в системе отправки пушей»
slug: "sdk-checklist-installation-status-not-registered"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-installation-status-not-registered"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0ab99b17f750abecdc1cf07a3aa18df4825e92cbcb746f7522bb31f5e96596cc"
---

# У установки статус «приложение не зарегистрировано в системе отправки пушей»

Ошибка возникает, когда приложение запустилось, клиент есть в админке, но не пришел токен от приложения.

## Не был вызван метод передачи токена

### Как проверить

Проверьте вызов метода `Mindbox.shared.apnsTokenUpdate`.

### Как поправить

Если ошибка возникла, значит, у вас собственная реализация делегата Mindbox. Проверьте метод [в этой инструкции](ios-quick-setup-push-notifications.md#самостоятельная-настройка) — у вас должен быть идентичный.
