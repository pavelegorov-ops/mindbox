---
title: Firebase
slug: "firebase-send-push-notifications-flutter"
source_url: "https://developers.mindbox.ru/docs/firebase-send-push-notifications-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
  - "Android | Настройка пуш-уведомлений"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:6396a424f7ca3359abdc8e567557bdf080cd60c8764b81aa37f3c4c1b758b623"
---

# Firebase

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-android-integration.md)
- [Получение Firebase ключей](firebase-key-setup.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)

### Результат шага «Отправка push-notifications на Android через Firebase»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).

[Пример реализации отображения уведомлений Firebase](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/android/app/src/main/kotlin/cloud/mindbox/flutter_example/MindboxFirebaseMessagingService.kt)

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

## 2. Добавьте Mindbox SDK явно в build.gradle

Для работы Mindbox SDK нужно добавить зависимость в файл `build.gradle` (уровень app).

```
dependencies {
  
    //Дополнительно, если необходимо получение push-уведомлений через Firebase:
    implementation 'com.google.firebase:firebase-messaging:24.1.0'

    // Дополнительно, если необходимо получение push-уведомлений через Huawei:
    implementation 'com.huawei.hms:push:6.13.0.300'

}
```

## 3. Реализовать отображение уведомлений

[Базовая интеграция](firebase-integration-service-implementation.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## Зарегистрируйте сервис обработки push-уведомлений в AndroidManifest.xml

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

## 4.1. Добавьте библиотеку для обработки push-уведомлений

В файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть [на странице библиотеки в Maven Central](https://search.maven.org/artifact/cloud.mindbox/mindbox-firebase).

```
dependencies {
   ...
    implementation 'cloud.mindbox:mindbox-firebase
   ...
}
```

## 4.2. Укажите библиотеку в методе `Mindbox.initPushServices`

В методе `Application.onCreate` нужно вызвать `Mindbox.initPushServices` с `MindboxFirebase`.

Если в вашем проекте нет этого класса, его надо создать:

1. New → Kotlin class.
2. Впишите код из примера ниже.
3. Зарегистрируйте класс в `AndroidManifest.xml`.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_firebase.MindboxFirebase

class MainApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // .... 
        
        // Нужно 
        Mindbox.initPushServices(applicationContext, listOf(MindboxFirebase))  

        // ...

    }
}
```

### Проверьте результат шага «Отправка push-notifications на Android через Firebase»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).
