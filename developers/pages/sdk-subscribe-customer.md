---
title: Создание клиента в Mindbox
slug: "sdk-subscribe-customer"
source_url: "https://developers.mindbox.ru/docs/sdk-subscribe-customer"
breadcrumb:
  - Мобильные приложения
  - Справочное
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7e5b4174c82383fffa8b542596883aadcc7762bc27a73058fe28cda20646c8fd"
---

# Создание клиента в Mindbox

Пользователь может появиться не сразу после инициализации, а в течение нескольких минут.

После завершения инициализации, в консоли вы должны увидеть значение deviceUUID вашего устройства — cкопируйте его.

Перейдите в mindbox.

**Укажите deviceUUID в фильтре «Устройство - GUID устройства» на странице клиентов, нажмите «Применить»**:

![1134](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/2c2eda5-1.png "1.png")

Подождите некоторе время, пока ваш пользователь появится в системе. Чтобы проверить, появился ли клиент надо перезагружать результат фильтров (нажать кнопку «Применить» или обновить страницу).

Когда клиент появился, откройте его страницу с подробной информацией — для этого кликните по ссылке в поле «Клиент»:

![1111](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/48e2f5f-2.png "2.png")

И далее — «Все устройства»:

![1369](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c0adeaa-3.png "3.png")

Вы должны увидеть следующее:

![1072](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/4bce2f5-4.png "4.png")

Статус разрешения на уведомления (Notifications permission status): **Запрещены (Forbidden)**

Статус устройства (Device status): **Деактивировано (Deactivated)**

Причина деактивации (Deactivation reason): **Устройство не зарегистрировано в системе рассылки пушей (The device is not registered in the push mailing system)**
