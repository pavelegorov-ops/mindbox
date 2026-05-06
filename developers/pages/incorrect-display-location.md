---
title: Некорректно выбрано место отображения
slug: "incorrect-display-location"
source_url: "https://developers.mindbox.ru/docs/incorrect-display-location"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - Механика не работает по тестовой ссылке
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0dcf9ffab3dcd6387a5683f0616a76da028c8a5b1403ca2a60c4c5400b6e78d7"
---

# Некорректно выбрано место отображения

**Как проверить**

1. Зайдите в настройки механики и посмотрите, какое выбрано место отображение

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/340bcac-image.png)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d1ceb6b-image.png)

2. Зайдите на страницу сайта, где должна работать механика
3. В консоли найдите селектор или div, которые указаны в настройках. Если они не находятся - место отображение выбрано некорректно.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/fb288c5-image.png)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/49bd367-image.png)

**Как исправить:**

Если хотите разместить виджет по селектору:

1. Выберите селектор [по инструкции](https://help.mindbox.ru/docs/ru/inline-block?highlight=%D0%9A%D0%B0%D0%BA%20%D0%B2%D1%8B%D0%B1%D1%80%D0%B0%D1%82%D1%8C%20%D1%81%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80)
2. Укажите его в настройках механики в разделе “место отображение”

Если хотите разместить виджет через div:

1. Скопируйте код из настроек механики
2. Поместите этот код в нужное место в шаблоне вашего сайта
