---
title: "iOS | Настройка пуш-уведомлений"
slug: "ios-send-push-notifications-react-native"
source_url: "https://developers.mindbox.ru/docs/ios-send-push-notifications-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:72d01be684f0ed25f0c8ad58b4d0b4cc3fa98074f19ac338833218337c455140"
---

# iOS | Настройка пуш-уведомлений

# iOS | Настройка пуш-уведомлений

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md)
- [Добавление SDK в приложение](add-sdk-react-native.md)
- [Инициализация SDK](sdk-initialization-react-native.md)

### Результат шага «Отправка push-notifications»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).

[Пример реализации (Swift)](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp/ios)

## 1. Добавить работу с push-уведомлениями в настройках приложения

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/51f0ee2-Untitled_5.png)

1. Откройте настройки проекта;
2. Выберите основной target;
3. Перейдите на вкладку `Signing & Capabilities`;
4. Нажмите на кнопку «добавить» и выберите `Push Notifications` и `Background modes`;
5. В разделе Background Modes поставьте 3 галки:
   - Background fetch;
   - Remote notifications;
   - Background processing.

Передайте менеджеру проекта ключи для подключения к [Apple Push Notification service](apns-keys-setup.md#/) или добавьте ключи самостоятельно.

---

## 2. Настройка AppDelegate

### Расширьте класс с помощью UNUserNotificationCenterDelegate

```
import UserNotifications
import Mindbox
import MindboxSdk

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    
    var window: UIWindow?
    var bridge: RCTBridge!
...
```

### Сделайте начальную настройку

Зарегистрируйте устройство в APNS и подпишитесь на новый делегат, добавленный в 1 шаге.

```
...
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    
    var window: UIWindow?
    var bridge: RCTBridge!
    
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        
        UIApplication.shared.registerForRemoteNotifications()
        UNUserNotificationCenter.current().delegate = self
        registerForRemoteNotifications()
        
        return true
    }
...
```

### Отобразите разрешение на пуш-уведомление пользователю (опционально)

```
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
...
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        
        UIApplication.shared.registerForRemoteNotifications()
        UNUserNotificationCenter.current().delegate = self
        registerForRemoteNotifications()
        
        return true
    }
    
    func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        
        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
                print("Permission granted: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed: \(error.localizedDescription)")
                }
                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }
...
```

### Отобразите стандартные уведомления

```
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
...
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
    ) {
        completionHandler([.alert, .sound, .badge])
    }
...
```

### Передайте пуш токен в Mindbox

```
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
...
    func application(
         _ application: UIApplication,
         didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```

### Пример готового кода

```
import UserNotifications
import Mindbox
import MindboxSdk

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    
    var window: UIWindow?
    var bridge: RCTBridge!
    
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        
        UIApplication.shared.registerForRemoteNotifications()
        UNUserNotificationCenter.current().delegate = self
        registerForRemoteNotifications()
        
        return true
    }
    
    func registerForRemoteNotifications() {
        UNUserNotificationCenter.current().delegate = self
        
        DispatchQueue.main.async {
            UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
                print("Permission granted: \(granted)")
                if let error = error {
                    print("NotificationsRequestAuthorization failed: \(error.localizedDescription)")
                }
                Mindbox.shared.notificationsRequestAuthorization(granted: granted)
            }
        }
    }
    
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
    ) {
        completionHandler([.alert, .sound, .badge])
    }
    
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
    }
}
```

---

Если вы тестируете push-уведомления в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md#/)
