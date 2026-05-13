---
title: "3.1. Отправка push-notifications через Firebase"
slug: "firebase-send-push-notifications"
source_url: "https://developers.mindbox.ru/docs/firebase-send-push-notifications"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:fb8a9e5deb645a66e217321b7d81b74d0cdbedbfc6bb991a1e3b5562efe826d9"
---

# 3.1. Отправка push-notifications через Firebase

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Получение Firebase ключей для Android-приложения](firebase-key-setup.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)

### Результат шага «Отправка push-notifications на Android через Firebase»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).

[Пример реализации отображения уведомлений Firebase](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MindboxFirebaseMessagingService.kt#L9-L52)

## 1. Сделайте интеграцию вашего приложения с Firebase

Из [официальной инструкции по добавлению Firebase](https://firebase.google.com/docs/cloud-messaging/android/client#kotlin+ktx_2) нужны следующие пункты:

- зарегистрировать свое приложение в Firebase;
- скачать и положить по инструкции файл `google-services.json`;
- подключить Сервисы Google в свое приложение;
- добавьте **`firebase-messaging`** в **`build.gradle`**;
- передать менеджеру проекта [Firebase Server Key](firebase-key-setup.md#/).

```
dependencies {
    implementation platform('com.google.firebase:firebase-bom:33.7.0')
    implementation 'com.google.firebase:firebase-analytics-ktx'
    implementation 'com.google.firebase:firebase-messaging-ktx'
   ...
}
```

**Если в вашем приложении указан targetSdk 33**, то для получения уведомлений вам также нужно добавить разрешение (подробнее [тут](https://developer.android.com/develop/ui/views/notifications/notification-permission), пример реализации [тут](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view_model/view_model.dart#L65-L72))

В файле AndroidManifest.xml:

```
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
```

В файле MainActivity.kt:

```
private val requestPermissionLauncher =
    registerForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted ->
        if (isGranted) {
            Mindbox.updateNotificationPermissionStatus(this)
        }
    }
 if (ContextCompat.checkSelfPermission(
                applicationContext,
                Manifest.permission.POST_NOTIFICATIONS
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
        }
```

## 2. Реализовать отображение уведомлений

[Базовая интеграция](_implementation-of-service-for-connection.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## 3 Зарегистрируйте сервис обработки push-уведомлений в AndroidManifest.xml

Добавьте в файл `AndroidManifest.xml` следующие пункты:

```
<application ...>
  ...

  <service android:name=".MindboxFirebaseMessagingService" android:exported="false">
    <intent-filter>
      <action android:name="com.google.firebase.MESSAGING_EVENT"/>
    intent-filter>
  service>

  ...
application>
```

## 4. Доработайте метод инициализации, чтобы push-уведомления отображались всегда

[Пример инициализации](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/ExampleApplication.kt#L34)

## 4.1 Добавьте библиотеку для обработки push-уведомлений

В файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть [на странице библиотеки в Maven Central](https://central.sonatype.com/artifact/cloud.mindbox/mindbox-firebase/2.5.1-rc/versions).

```
dependencies {
   ...
    implementation 'cloud.mindbox:mobile-sdk:{версия}' 
    implementation 'cloud.mindbox:mindbox-firebase'
   ...
}
```

## 4.2 Укажите библиотеку в методе инициализации

В методе `Mindbox.init`, который должен быть размещен в коллбэке onCreate вашего приложения, нужно указать, что в этой сборке используется MindboxFirebase.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.MindboxConfiguration
import cloud.mindbox.mindbox_firebase.MindboxFirebase

class MyApplication : Application() {
   override fun onCreate() {
     super.onCreate()
     // ....

     // Было
     // Mindbox.init(applicationContext, configuration, listOf())

     // Нужно
     Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase))

     // ...
   }
 }
```

Добавьте в коллбэк onCreate вашего приложения вызов метода `Mindbox.initPushServices`.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_firebase.MindboxFirebase
class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // ....
        Mindbox.initPushServices(applicationContext, listOf(MindboxFirebase))
        Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase))
        // ...
    }
}
```

### Проверьте результат шага «Отправка push-notifications через Firebase»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).
