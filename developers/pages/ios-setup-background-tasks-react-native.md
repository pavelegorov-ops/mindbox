---
title: "iOS | Настройка гарантированной доставки"
slug: "ios-setup-background-tasks-react-native"
source_url: "https://developers.mindbox.ru/docs/ios-setup-background-tasks-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:b7da05ebc4fd672317dece46f5ef7f9920b9933a743923aaa9ddbfcf55d7f85f"
---

# iOS | Настройка гарантированной доставки

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-ios-integration.md)
- [Добавление SDK в приложение](add-sdk-react-native.md)
- [Инициализация SDK](sdk-initialization-react-native.md)

[Пример реализации](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/ios/AppDelegate.swift#L40)

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

## 2. Регистрация фоновых задач

Чтобы фоновые задачи работали, их нужно зарегистрировать в файле `AppDelegate.swift`.

```
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {

    // ...

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {

        if #available(iOS 13.0, *) {
            Mindbox.shared.registerBGTasks()
        }

        UIApplication.shared.setMinimumBackgroundFetchInterval(
            UIApplication.backgroundFetchIntervalMinimum
        )

        return true
    }

    func application(
        _ application: UIApplication,
        didReceiveRemoteNotification userInfo: [AnyHashable: Any],
        fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
    ) {
        Mindbox.shared.application(
            application,
            performFetchWithCompletionHandler: completionHandler
        )
    }
}
```
