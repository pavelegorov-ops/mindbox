---
title: "[iOS] Быстрая настройка пушей"
slug: "ios-push-notifications-setup"
source_url: "https://developers.mindbox.ru/docs/ios-push-notifications-setup"
breadcrumb: []
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:9417b96e4b0976d39864ed925acd89e682d39c8a25113d7f7e18fa44b890ca04"
---

# [iOS] Быстрая настройка пушей

## Наследование от MindboxAppDelegate

Mindbox SDK предоставляет готовый AppDelegate, с готовыми настройками, чтобы надо было меньше настраивать.

```
final class AppDelegate: MindboxAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        super.application(application, didFinishLaunchingWithOptions: launchOptions)
        
        registerForRemoteNotifications()
        
        return true
    }
```

## Запрос авторизации

Создаем метод для запроса разрешения на пуши у пользователя, и передаем статус в Mindbox

```
private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        DispatchQueue.main.async {
            UIApplication.shared.registerForRemoteNotifications()
            UNUserNotificationCenter.current().requestAuthorization(options: [ .alert, .sound, .badge]) { granted, error in
                print("Permission granted to allow local and remote notifications for your app: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }
                Mindbox.shared.refreshNotificationPermissionStatus()
            }
        }
    }
```

## Вызов метода

Добавьте метод `registerForRemoteNotifications` в `didFinishLaunchingWithOptions`.

```
override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        super.application(application, didFinishLaunchingWithOptions: launchOptions)
        
        registerForRemoteNotifications()
        
        return true
    }
```

## Отображение пуш уведомления

Для того чтоб пуш-уведомление отображалось, нужно выставить соответствующие настройки в методе 'willPresent'

```
func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.list, .badge, .sound, .banner])
    }
}
```

## Пример готового кода

```
final class AppDelegate: MindboxAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        super.application(application, didFinishLaunchingWithOptions: launchOptions)
        
        registerForRemoteNotifications()
        
        return true
    }
    
    private func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        DispatchQueue.main.async {
            UIApplication.shared.registerForRemoteNotifications()
            UNUserNotificationCenter.current().requestAuthorization(options: [ .alert, .sound, .badge]) { granted, error in
                print("Permission granted to allow local and remote notifications for your app: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed with error: \(error.localizedDescription)")
                }
                Mindbox.shared.refreshNotificationPermissionStatus()
            }
        }
    }
    
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.list, .badge, .sound, .banner])
    }
}
```
