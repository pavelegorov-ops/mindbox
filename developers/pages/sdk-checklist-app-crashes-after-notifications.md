---
title: После отправки уведомлений приложение падает
slug: "sdk-checklist-app-crashes-after-notifications"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-app-crashes-after-notifications"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:c96d985f7ba3a3c14ccdb8257f04f55f569830bd0fabdbc8ac42c8f228ee9b41"
---

# После отправки уведомлений приложение падает

## Класс месседжинг-сервиса находится не там, где ожидается

### Как проверить

Проверьте структуру папок и android manifest.

### Как поправить

Перенесите файл с месседжинг-сервисом рядом с файлом main activity и проверьте, что этот же адрес файла указан в android manifest.
