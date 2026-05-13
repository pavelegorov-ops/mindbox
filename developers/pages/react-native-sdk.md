---
title: React Native SDK
slug: "react-native-sdk"
source_url: "https://developers.mindbox.ru/docs/react-native-sdk"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:e7fd282a15cd94c703f1bf9bdae06ff9b3771f7fe67faa25649da485b38996bb"
---

# React Native SDK

## Что получим в результате?

### В результате этой интеграции вы сможете:

- собирать подписчиков из приложения;
- отправлять подписчикам как обычные push-уведомления, так и rich-push;
- передавать клики по мобильным push-уведомлениям в CDP mindbox;
- передавать переходы в приложение в CDP mindbox;
- настроить гарантированную доставку действий пользователя в приложении, даже если оно работает в фоновом режиме;
- передавать действия из приложения — просмотры, корзины, заказы и другие действия.

[Пример приложения с использованием Mindbox SDK](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp)

---

  

## Что нужно сделать:

- [Настройка точек интеграции](add-integration-rn.md#/)
- [Получение ключей для пуш-уведомлений](rn-get-push-keys.md#/)
- [Добавление SDK в приложение](add-sdk-react-native.md#/)
- [Инициализация SDK](sdk-initialization-react-native.md#/)
- Настройка пуш-уведомлений
  - [iOS](ios-send-push-notifications-react-native.md#/)
  - [Android](rn-push-notifications-setup.md#/)
- [Настройка гарантированной доставки](ios-setup-background-tasks-react-native.md#/)
- [iOS | Настройка Rich-push уведомлений](rn-ios-rich-push-notifications.md#/) (Опционально)
- Передача кликов по push-уведомлениям (Опционально)
  - [iOS](ios-get-click-react-native.md#/)
  - [Android](android-get-click-react-native.md#/)
- [Навигация по клику на push-уведомление](flutter-push-navigation-react-native.md#/) (Опционально)
- [Получение источника установки мобильного приложения](ios-app-start-tracking-react-native.md#/) (Опционально)
