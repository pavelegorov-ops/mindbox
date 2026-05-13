---
title: Получение Huawei ключей
slug: "huawei-get-keys"
source_url: "https://developers.mindbox.ru/docs/huawei-get-keys"
breadcrumb:
  - Мобильные приложения
  - Android SDK
  - Получение ключей провайдеров пушей
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c4105e1f27d390c8e6384768840389974c9b657f73c974528b83ff5b56900d62"
---

# Получение Huawei ключей

### Убедитесь, что выполнена

[Настройка точек интеграции для Android приложения](add-android-integration.md)

### Результаты выполнения данного шага:

- Получены креды для мобильного приложения
- Внесены данные в форму "Настройка отправки мобильных push-уведомлений Android" для нужной точки интеграции

Для отправки мобильных push-уведомлений через Huawei Push Kit нужно указать в системе:

- ID клиента
- Секрет клиента

Для получения этих данных:

1. Откройте Push Kit
2. Выберите то приложение, которое интегрируете с Mindbox
3. Перейдите в настройки
4. Внизу экрана выберите нужное приложение и скопируйте значение, обозначенные на картинке

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/175fa99-Screenshot_2022-03-10_at_19.12.34.png "Screenshot 2022-03-10 at 19.12.34.png")

Если вы выбрали в подписи приложения в AppGallary 1 способ, то не забудьте добавить сгенерированный AppGallary отпечаток в пункте 4

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/86e03cf-image.png)

5. Вставьте ID клиента в поле Client ID и секрет клиента - в Client Secret в [интеграции](mobile-app-integrations.md#интеграции) с Android-приложением.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/74ecee7-__2024-07-23__15.43.03.png)
