---
title: "[iOS] Самостоятельная настройка пушей"
slug: "ios-push-notifications-setup-advanced"
source_url: "https://developers.mindbox.ru/docs/ios-push-notifications-setup-advanced"
breadcrumb: []
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:d0745d051c44296fdb44f34934102cab92a8a23f5b6b1f1ae6288482ba2f1696"
---

# [iOS] Самостоятельная настройка пушей

## Регистрация устройства в APNS

В файле AppDelegate.swift нужно найти и реализовать функцию registerForRemoteNotifications и вызвать в ней Mindbox.shared.notificationsRequestAuthorization.

```
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        UIApplication.shared.registerForRemoteNotifications()
        registerForRemoteNotifications()
        
        ...
        
        return true
    }
```

## Передача статус разрешения в Mindbox

Запрашиваем разрешение у пользователя и передаем в Mindbox

```
private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(options: [ .alert, .sound, .badge]) { granted, error in
                print("Permission granted: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }
                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }
```

## Настройка отображения пушей

Настраиваем пуш уведомления, чтобы они отображались когда приложение в foreground

```
func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.alert, .badge, .sound])
    }
```

## Передача токена

Передаем токен в Mindbox, чтобы можно SDK знало куда отправлять пуш уведомление

```
func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
            Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```

## Пример готового кода

```
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        UIApplication.shared.registerForRemoteNotifications()
        registerForRemoteNotifications()
        
        ...
        
        return true
    }
    
    private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(options: [ .alert, .sound, .badge]) { granted, error in
                print("Permission granted: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }
                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }
    
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.alert, .badge, .sound])
    }
    
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
            Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```
