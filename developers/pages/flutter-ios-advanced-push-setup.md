---
title: "[Flutter] [iOS] Самостоятельная настройка пуш-уведомлений"
slug: "flutter-ios-advanced-push-setup"
source_url: "https://developers.mindbox.ru/docs/flutter-ios-advanced-push-setup"
breadcrumb: []
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8e025dc5ed8ace86d1a5ae59a72f033cfdf15f0fed783b506a19913cd713bf51"
---

# [Flutter] [iOS] Самостоятельная настройка пуш-уведомлений

## Скорректируйте файл Podfile

В **`Podfile`** укажите **Mindbox iOS SDK**.

```
target 'Runner' do
  use_frameworks!
  use_modular_headers!

  pod 'Mindbox'
  flutter_install_all_ios_pods File.dirname(File.realpath(__FILE__))
end
```

## Импорт нативной библиотеки

Добавьте импорт Mindbox в AppDelegate.

```
import UIKit
import Flutter
import Mindbox

@UIApplicationMain
...
```

## Регистрация устройства в APNS

Чтобы устройство получило APNS токен, его нужно зарегистрировать в didFinishLaunchingWithOptions

```
...
@objc class AppDelegate: FlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
				// ...
        UIApplication.shared.registerForRemoteNotifications()
   	    registerForRemoteNotifications()
				// ...

        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
...
```

## Запрос разрешения у пользователя

Чтобы устройство могло получить пуш уведомления, нужно запросить разрешение у пользователя

```
...
@objc class AppDelegate: FlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
				// ...
        UIApplication.shared.registerForRemoteNotifications()
   	    registerForRemoteNotifications()
				// ...

        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

    // MARK: - Register for Remote Notifications
    private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self

        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(
                options: [.alert, .sound, .badge]
            ) { granted, error in
                print("Permission granted: \(granted)")

                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }

                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }
...
```

## Настройка отображения пуш-уведомлений

Чтобы пуш-уведомления корректно отображались, нужно настроить их в методе willPresent

```
...
    override func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
    ) {
        completionHandler([.alert, .badge, .sound])
    }
...
```

## Передача APNS токена в Mindbox

Чтобы можно было передать пуш-уведомление через Mindbox, нужно передать APNS токен в систему.

```
...
   override func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```

## Пример готового кода

```
import UIKit
import Flutter
import Mindbox

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
				// ...
        UIApplication.shared.registerForRemoteNotifications()
   	    registerForRemoteNotifications()
				// ...

        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

    // MARK: - Register for Remote Notifications
    private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self

        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(
                options: [.alert, .sound, .badge]
            ) { granted, error in
                print("Permission granted: \(granted)")

                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }

                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }

    override func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
    ) {
        completionHandler([.alert, .badge, .sound])
    }

    override func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```
