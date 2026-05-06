---
title: При отправке уведомления ошибка с текстом «wrong token» или «все токены доступа некорректны»
slug: "sdk-checklist-wrong-token-or-invalid-tokens"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-wrong-token-or-invalid-tokens"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:5ce2ddb8b8e887150c07ec5d5a8ec0b56c17db6429bda1f4b562e7257f24b79e"
---

# При отправке уведомления ошибка с текстом «wrong token» или «все токены доступа некорректны»

## Прописаны некорректные ключи для подключения

### Как проверить

Проверьте соответствие ваших ключей в [Firebase Server key](firebase-key-setup.md) или в [Huawei Push Kit](huawei-get-keys.md) и в точке интеграции в админке проекта.

### Как поправить

Прописать корректные ключи в настройках точки интеграции в админке проекта.
