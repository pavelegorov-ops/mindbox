---
title: Универсальные ссылки
slug: "universal-links"
source_url: "https://developers.mindbox.ru/docs/universal-links"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:62cade25faed0691316bcccb915b4aabf704f0aea5de30c86984970cd096ca8f"
---

# Универсальные ссылки

Универсальные ссылки позволяют открывать ссылки, которые отправляются в Email-рассылках через Mindbox, непосредственно в мобильном приложении без перенаправления на сайт. Данная инструкция описывает необходимые действия для работы универсальных ссылок

### Для корректной работы универсальных ссылок и сбора статистики по кликам

- у всех ваших пользователей должно быть установлено приложение с SDK mindbox
- на каждом домене и поддомене вашего сайта установлен JS трекер и файл ассоциации iOS/Android
- в приложении настроена поддержка универсальных ссылок

## Добавление и инициализация SDK

*Если у вас уже есть интеграция с SDK, эти пункты выполнять не нужно*

**Для iOS**

1. [Настройка точек интеграции](add-ios-integration.md)
2. [Добавление SDK мобильных приложений в приложение](add-sdk-to-app.md)
3. [Инициализация SDK мобильных приложений](ios-sdk-initialization.md)

**Для Android и Huawei**

1. [Настройка точек интеграции](add-android-integration.md)
2. [Добавление SDK мобильных приложений в приложение](add-android-sdk.md)
3. [Инициализация SDK мобильных приложений](android-sdk-initialization.md)

## Настройка JS трекера

[Документация](javascript-sdk.md)

Для корректного отслеживания кликов необходимо добавить JS трекер на **каждом** домене и поддомене, ссылки на которые будут обрабатываться, как универсальные

## Настройка поддержки универсальных ссылок

## iOS

### 1. Поддержка связанных доменов

Создайте связь между приложением и веб-сайтом и укажите URL-адреса, которые обрабатывает ваше приложение, как описано в инструкции Apple - [Поддержка связанных доменов](https://developer.apple.com/documentation/Xcode/supporting-associated-domains)

Обратите внимание, что каждый домен и поддомен, используемый для универсальных ссылок, должен иметь файл Apple App Site Association (AASA) в подкаталоге `.well-known`. Файл должен быть доступен через HTTPS без каких-либо перенаправлений — по адресу `https:///.well-known/apple-app-site-association`.

### 2. Поддержка универсальных ссылок в приложении

Обновите App Delegate или Scene Delegate, чтобы он отвечал на действие пользователя, когда тот переходит в приложение по универсальной ссылке, как описано в документации Apple - [Поддержка универсальных ссылок в вашем приложении](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app). Используйте соотвествующие вызовы `Mindbox.shared.track(_:)` в методах жизненного цикла приложения, если не используете `MindboxSceneDelegate` или `MindboxAppDelegate`.

#### SceneDelegate

```
import UIKit
import Mindbox

final class SceneDelegate: UIResponder, UIWindowSceneDelegate {

  var window: UIWindow?

  // If your app uses the AppDelegate lifecycle (no scenes),
  // use `application(_:didFinishLaunchingWithOptions:)` instead.
  func scene(
      _ scene: UIScene,
      willConnectTo session: UISceneSession,
      options connectionOptions: UIScene.ConnectionOptions
  ) {
    
        // Set up `windowScene` and `window` here.

      Mindbox.shared.track(.launchScene(connectionOptions))
    
      // Mindbox.shared.track(.launch(launchOptions)) // For AppDelegate lifecycle

      // Handle Universal Link on a cold start:
      // The app was launched from a URL (not already running).
      // Read the link from `connectionOptions.userActivities` and route to the right screen.
  }

  // If your app uses the AppDelegate lifecycle (no scenes),
  // use `application(_:continue:restorationHandler:)` instead.
  func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
      Mindbox.shared.track(.universalLink(userActivity))
      
      // Handle Universal Link on a warm start:
      // The app is already running (foreground or background) and receives a new URL.
      // Use `scene(_:continue:)` to parse and route the link.
  }
}
```

#### MindboxSceneDelegate

## Android и Huawei

### 1. Добавить intent-filter

[Документация](https://developer.android.com/training/app-links/verify-site-associations#add-intent-filters)

В манифест добавить intent-filter, содержащий атрибут `autoVerify="true"`. Пример фильтра:

```
…
    
        
        
        

        
            android:host="domain1.com" 
            android:pathPrefix=”/foo”/>

    
…
```

Если в приложении каждый экран - отдельная активити - то можно для каждой указать свой intent-filter. Тогда определенная ссылка будет открывать определенную активити.

### 2. Указать связь между сайтом и intent-filter

[Документация](https://developer.android.com/training/app-links/verify-site-associations#web-assoc)

На сайт необходимо положить файл `https://domain.name/.well-known/assetlinks.json`. Пример файла:

```
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.example",
    "sha256_cert_fingerprints": ["<ключ сертификата>"]
  }
}]
```

## Настройка на проекте Mindbox

Указать домен и поддомены, на которых расположены универсальные ссылки:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7672cf3-__2022-10-26__21.58.08.png)

[Инструкция на help.mindbox.ru](https://help.mindbox.ru/docs/unique-links)
