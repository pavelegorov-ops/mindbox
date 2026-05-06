---
title: Android SDK
slug: "android-sdk"
source_url: "https://developers.mindbox.ru/docs/android-sdk"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:4439e81f9e548d7357fa2ced31d955f2e0e7aea765dcd076e7101af12d2e9a21"
---

# Android SDK

### В результате этой интеграции вы сможете:

- собирать подписчиков из приложения;
- отправлять подписчикам как обычные push-уведомления, так и rich-push;
- передавать клики по мобильным push-уведомлениям в CDP mindbox;
- передавать переходы в приложение в CDP mindbox;
- настроить гарантированную доставку действий пользователя в приложении, даже если оно работает в фоновом режиме;
- передавать действия из приложения — просмотры, корзины, заказы и другие действия.

[Пример приложения с использованием Mindbox SDK](https://github.com/mindbox-cloud/android-sdk/tree/develop/example)

## Что нужно сделать:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- Рекомендуем подключить всех провайдеров:

  - [Получение Firebase ключей для Android-приложения](firebase-key-setup.md)
  - [Получение Huawei ключей для Android-приложения](huawei-get-keys.md)
  - [Получение RuStore ключей](rustore-get-keys.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)
- Рекомендуем настроить отправку через всех провайдеров:

  - [Отправка push-notifications через Firebase](firebase-send-push-notifications.md)
  - [Отправка push-notifications через Huawei](huawei-send-push-notifications.md)
  - [Отправка push-notifications через RuStore](rustore-send-push-notifications.md)
- [Получение кликов на мобильные push-уведомления](android-get-click.md)
- [Настройка отслеживания источников установки приложения](android-app-start-tracking.md)
- [Интеграция действий в приложении](android-integration-of-actions.md)
