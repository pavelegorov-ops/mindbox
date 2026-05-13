---
title: "[Flutter] [iOS] Быстрая настройка пуш-уведомлений"
slug: "ios-mindboxflutterappdelegate"
source_url: "https://developers.mindbox.ru/docs/ios-mindboxflutterappdelegate"
breadcrumb: []
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:b3b4a75a53305b749cc1b828e9ddb4dcbdcbc046d6df971200f84b180e5815f8"
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
