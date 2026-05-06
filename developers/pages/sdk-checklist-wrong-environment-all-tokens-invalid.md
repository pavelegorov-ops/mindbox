---
title: Ошибка с текстом «неправильное окружение / Все токены доступа невалидны»
slug: "sdk-checklist-wrong-environment-all-tokens-invalid"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-wrong-environment-all-tokens-invalid"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:055bcad544106960836633debbd46c8d6dea7983ff97b20a842a7a1c2ae489c5"
---

# Ошибка с текстом «неправильное окружение / Все токены доступа невалидны»

## Рассылка production отправляется в sandbox-окружение или рассылка sandbox отправляется в окружение production

### Как проверить

Если клиент только интегрируется и тестирует пуши, то проверить, стоит ли галочка "Тестовое сообщение sandbox" в профиле рассылки «Вручную». Подробнее [тут](sandbox-integration-setup.md#/)

### Как поправить

Проставить/снять галочку "Тестовое сообщение sandbox" в профиле рассылки “Вручную” в зависимости от окружения, куда отправляются пуши
