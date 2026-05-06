---
title: Трекер Mindbox установлен некорректно
slug: "tracker-installed-incorrectly"
source_url: "https://developers.mindbox.ru/docs/tracker-installed-incorrectly"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - Механика не работает по тестовой ссылке
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:1fde98e05a4ebba72ee97c262ddf14ccb15dc672a58505dbe76f9a9652f6888e"
---

# Трекер Mindbox установлен некорректно

**Как проверить**

1. Откройте сайт, где должна работать механика персонализации
2. Откройте вкладку “Elements” в инструментах разработчика
3. В поиске введите `tracker`

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7ef1895-image.png)

4. Сравните, соответствует ли скрипт одному из вариантов:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/37050e7-image.png)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/b8c2b5b-image.png)

5. Если скрипт не соответствует одному из вариантов - трекер установлен некорректно

**Как поправить**

Установите трекер по [инструкции](javascript-sdk.md)
