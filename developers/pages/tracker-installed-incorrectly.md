---
title: Трекер Mindbox установлен некорректно
slug: "tracker-installed-incorrectly"
source_url: "https://developers.mindbox.ru/docs/tracker-installed-incorrectly"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - Механика не работает по тестовой ссылке
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:458823938b3f3aba2aed00e0cdd1828eea9e5868efcc96c2a1ef41372150685e"
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
