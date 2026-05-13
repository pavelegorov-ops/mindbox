---
title: "iOS | Настройка гарантированной доставки"
slug: "ios-setup-background-tasks-flutter"
source_url: "https://developers.mindbox.ru/docs/ios-setup-background-tasks-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:bf976ff055182434fcdfcbd6ad94eb951c7c0353fc46312d026559ae69bbd729"
---

# iOS | Настройка гарантированной доставки

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)
- [Отправка push-notifications](ios-send-push-notifications-flutter.md)

## 1. Настройки в Xcode

Фоновые задачи нужны для работы механизма гарантированной доставки, чтобы SDK мог отправлять события при свернутом приложении.

Для их работы нужно добавить в `Info.plist` параметры:

- `Required background modes`:
  - App downloads content from the network;
  - App processes data in the background;
  - App downloads content in response to push notifications;
- `Permitted background task scheduler identifiers`:
  - `cloud.Mindbox.$(PRODUCT_BUNDLE_IDENTIFIER).GDAppRefresh`;
  - `cloud.Mindbox.$(PRODUCT_BUNDLE_IDENTIFIER).GDAppProcessing`;
  - `cloud.Mindbox.$(PRODUCT_BUNDLE_IDENTIFIER).DBCleanAppProcessing`.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/727f164-5507a51-Screenshot_2021-09-16_at_11.40.01.png)

---

## Регистрация фоновых задач

#### Быстрая настройка

Если ваш **`AppDelegate`** наследуется от **`MindboxFlutterAppDelegate`**, то никаких дополнительных изменений для гарантированной доставки не требуется.

#### Самостоятельная настройка
