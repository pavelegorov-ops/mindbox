---
title: После отправки уведомлений приложение падает
slug: "sdk-checklist-app-crashes-after-notifications"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-app-crashes-after-notifications"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:7a7a81ab8dc2d358f732e1491db56d8282f12992d2a79f12f69c9cee697d722a"
---

# После отправки уведомлений приложение падает

## Класс месседжинг-сервиса находится не там, где ожидается

### Как проверить

Проверьте структуру папок и android manifest.

### Как поправить

Перенесите файл с месседжинг-сервисом рядом с файлом main activity и проверьте, что этот же адрес файла указан в android manifest.
