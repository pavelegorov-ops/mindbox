---
title: "[Flutter] [iOS] Быстрая настройка пуш-уведомлений"
slug: "ios-mindboxflutterappdelegate"
source_url: "https://developers.mindbox.ru/docs/ios-mindboxflutterappdelegate"
breadcrumb: []
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:fc5ebf9bb9e76d2f4e053d15c74288d1fc65b54660877aa4ac260ba27c876d61"
---

# [Flutter] [iOS] Быстрая настройка пуш-уведомлений

## Добавьте импорт

```
import UIKit
import mindbox_ios
 
@UIApplicationMain

@objc class AppDelegate: MindboxFlutterAppDelegate {
    override func application(
...
```

## Наследуйтесь от нового делегата

Mindbox SDK предоставляет готовый MindboxFlutterAppDelegate.

```
import UIKit
import mindbox_ios
 
@UIApplicationMain

...
```

## Реализуйте метод didFinishLaunchingWithOptions

Опишите метод. Не забудьте вызвать super.application

```
...

@objc class AppDelegate: MindboxFlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
    ...
}
```

## Запрос на разрешение на уведомление

Если вы хотите отключить запрос на уведомления при старте приложения и реализовать свой, то необходимо отключить его.

```
...
@objc class AppDelegate: MindboxFlutterAppDelegate {
    ...
    override func shouldRegisterForRemoteNotifications() -> Bool {
        return false
    }
}
```

## Пример готового кода

```
import UIKit
import mindbox_ios
 
@UIApplicationMain

@objc class AppDelegate: MindboxFlutterAppDelegate {
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
  
    override func shouldRegisterForRemoteNotifications() -> Bool {
        return false
    }
}
```
