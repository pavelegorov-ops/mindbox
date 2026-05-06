---
title: Не установлен трекер Mindbox
slug: "tracker-not-installed"
source_url: "https://developers.mindbox.ru/docs/tracker-not-installed"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - Механика не работает по тестовой ссылке
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:5826664fd6932fdbd2bc3c1c0051b82dbb945662c381505312b62c8b51f7ede0"
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
