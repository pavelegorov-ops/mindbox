---
title: Не установлен трекер Mindbox
slug: "tracker-not-installed"
source_url: "https://developers.mindbox.ru/docs/tracker-not-installed"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - Механика не работает по тестовой ссылке
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:67ad483e2274f3cb44d0eee6a311a79bd3f2033422fa9746f0d2541945bce6b8"
---

# Не установлен трекер Mindbox

**Как проверить**

1. Откройте сайт, где должна работать механика персонализации
2. Откройте вкладку “Console” в инструментах разработчика
3. В поиске введите `mindbox`
4. Если в результатах будет `Uncaught ReferenceError: mindbox is not defined`- скрипт не инициализируется

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c8e87f5-image.png)

**Как поправить**

Установите трекер по [инструкции](javascript-sdk.md)
