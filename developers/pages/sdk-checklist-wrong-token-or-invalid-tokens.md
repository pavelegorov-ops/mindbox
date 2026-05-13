---
title: При отправке уведомления ошибка с текстом «wrong token» или «все токены доступа некорректны»
slug: "sdk-checklist-wrong-token-or-invalid-tokens"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-wrong-token-or-invalid-tokens"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f6ade9f892d6cb854fc845b65ca47f9a9c357e77f8195de2f5251b697040d5e5"
---

# При отправке уведомления ошибка с текстом «wrong token» или «все токены доступа некорректны»

## Прописаны некорректные ключи для подключения

### Как проверить

Проверьте соответствие ваших ключей в [Firebase Server key](firebase-key-setup.md) или в [Huawei Push Kit](huawei-get-keys.md) и в точке интеграции в админке проекта.

### Как поправить

Прописать корректные ключи в настройках точки интеграции в админке проекта.
