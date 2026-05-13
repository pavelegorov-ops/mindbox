---
title: Настройка гарантированной доставки
slug: "ios-guarantee-delivery-setup"
source_url: "https://developers.mindbox.ru/docs/ios-guarantee-delivery-setup"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:081f4e4d0f6e96e66a629155fa0daab80279e220286788ffb5eb7c12a6bde878"
---

# Настройка гарантированной доставки

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для iOS приложения](add-ios-integration.md)
- [Добавление SDK в приложение](add-sdk-to-app.md#/)
- [Инициализация SDK](ios-sdk-initialization.md#/)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md#/)
- [Настройка push-notifications](ios-quick-setup-push-notifications.md#/)

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

Если ваш **AppDelegate** наследуется от **MindboxAppDelegate**, то никаких дополнительных изменений для гарантированной доставки не требуется.

#### Самостоятельная настройка
