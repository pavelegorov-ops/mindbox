---
title: Ошибка с текстом «неправильное окружение / Все токены доступа невалидны»
slug: "sdk-checklist-wrong-environment-all-tokens-invalid"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-wrong-environment-all-tokens-invalid"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c6a5a359f104e7bc176af5c44cd7c8da733f7f0f8a1149dfc310aad6355b122b"
---

# Ошибка с текстом «неправильное окружение / Все токены доступа невалидны»

## Рассылка production отправляется в sandbox-окружение или рассылка sandbox отправляется в окружение production

### Как проверить

Если клиент только интегрируется и тестирует пуши, то проверить, стоит ли галочка "Тестовое сообщение sandbox" в профиле рассылки «Вручную». Подробнее [тут](sandbox-integration-setup.md#/)

### Как поправить

Проставить/снять галочку "Тестовое сообщение sandbox" в профиле рассылки “Вручную” в зависимости от окружения, куда отправляются пуши
