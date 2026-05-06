---
title: Flutter SDK
slug: "flutter-sdk"
source_url: "https://developers.mindbox.ru/docs/flutter-sdk"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:c8b93d86016fc307dedcd24058b46cd4b98b6763f52941e3005ec17a5f569d40"
---

# Flutter SDK

## Что получим в результате?

### В результате этой интеграции вы сможете:

- собирать подписчиков из приложения;
- отправлять подписчикам как обычные push-уведомления, так и rich-push;
- передавать клики по мобильным push-уведомлениям в CDP mindbox;
- передавать переходы в приложение в CDP mindbox;
- настроить гарантированную доставку действий пользователя в приложении, даже если оно работает в фоновом режиме;
- передавать действия из приложения — просмотры, корзины, заказы и другие действия.

[Пример приложения с использованием Mindbox SDK](https://github.com/mindbox-cloud/flutter-sdk/tree/develop/example/flutter_example#example-app-for-mindbox-sdk-for-flutter)

  

## Что нужно сделать:

- [Настройка точек интеграции](flutter-new-integration-setup.md#/)
- [Получение ключей для пуш-уведомлений](flutter-get-push-keys.md#/)
- [Добавление SDK в приложение](add-sdk-flutter.md#/)
- [Инициализация SDK](flutter-sdk-initialization.md#/)
- Настройка пуш-уведомлений
  - [iOS](ios-send-push-notifications-flutter.md#/)
  - [Android](flutter-android-push-notifications-setup.md#/)
- [iOS | Настройка Rich-push уведомлений](flutter-ios-rich-push-notifications.md#/) (Опционально)
- [Передача кликов по push-уведомлениям](ios-get-click-flutter.md#/) (Опционально)
- [Навигация по клику на push-уведомление](flutter-push-navigation.md#/) (Опционально)
- [Настройка гарантированной доставки](ios-setup-background-tasks-flutter.md#/)
- [Получение источника установки мобильного приложения](ios-app-start-tracking-flutter.md#/) (Опционально)
