---
title: Получение RuStore ключей
slug: "rustore-get-keys"
source_url: "https://developers.mindbox.ru/docs/rustore-get-keys"
breadcrumb:
  - Мобильные приложения
  - Android SDK
  - Получение ключей провайдеров пушей
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:2237deb2f9d79cb7e253145335de923a91a1dd522b46632fb5b53024926c5d75"
---

# Получение RuStore ключей

### Убедитесь, что выполнена

[Настройка точек интеграции для Android приложения](add-android-integration.md)

### Результаты выполнения данного шага:

- Получены креды для мобильного приложения
- Внесены данные в форму «Настройка отправки мобильных push-уведомлений Android» для нужной точки интеграции

Для отправки мобильных push-уведомлений через RuStore нужно указать в системе:

- Project ID (ID проекта)
- Service Token (Сервисный токен)

### Для подключения провайдера RuStore необязательно публиковать своё приложение в RuStore

Для получения Project ID и Service Token:

1. Откройте [RuStore Console](https://console.rustore.ru/apps)
2. Перейдите во вкладку «Инструменты» и выберите то приложение, которое интегрируете с Mindbox

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/679930a535e9545b9754fcd759de12b534048a81d37ca00925f770c4b2d4c086-image.png)

3. Перейдите в раздел «Push-уведомления» → «Проекты» → выберите нужный проект и скопируйте значения, обозначенные на скриншоте

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ef43241c3e8446aafdbff3db3425cde8e869a45fba7b6a2bd68e2bb8e2bc062e-RuStore_Keys.png)

4. В [интеграции](mobile-app-integrations.md#интеграции) с Android-приложением включите тоггл RuStore и вставьте ID проекта в поле Project ID и сервисный токен — в Service Token. Нажмите «Сохранить».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/28a513cb8601a72685f92a291a33f0d8a5f94d18eadf32ecab58a6f4c0cb3ba8-image.png)

5. Нажмите «Сохранить изменения» наверху страницы точки интеграции.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a1d58726c4bde922d5087a97f43b8226e32e480048b6f99c4e40eaf0ecff234f-__2025-02-25__20.35.16.png)
