---
title: Firebase
slug: "firebase-send-push-notifications-react-native"
source_url: "https://developers.mindbox.ru/docs/firebase-send-push-notifications-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
  - "Android | Настройка пуш-уведомлений"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:2dc4cbba4d80d7d85987fd03da0e78e48ee656bb2ef13d832acf26d6bb18a2d4"
---

# Firebase

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-android-integration.md)
- [Получение Firebase ключей](firebase-key-setup.md)
- [Добавление SDK в приложение](add-sdk-react-native.md)
- [Инициализация SDK](sdk-initialization-react-native.md)

### Результат шага «Отправка push-notifications на Android через Firebase»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).

[Пример реализации отображения уведомлений Firebase](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp/android/app/src/main/java/com/exampleapp)

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
		...
    implementation 'cloud.mindbox:mindbox-firebase' 
		...
}
```

## 3. Реализовать отображение уведомлений

Подходит, если не требуется кастомная логика.

[Базовая интеграция](firebase-integration-service-implementation.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## 4. Зарегистрируйте сервис обработки push-уведомлений в AndroidManifest.xml

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

## 5. Доработайте метод инициализации, чтобы push-уведомления отображались всегда

В методе `Application.onCreate` нужно вызвать `Mindbox.initPushServices` с `MindboxFirebase`.

Если в вашем проекте нет этого класса, его надо создать:

1. New → Kotlin class.
2. Добавьте код из примера ниже.
3. Зарегистрируйте класс в `AndroidManifest.xml`.

```
import cloud.mindbox.mindbox_firebase.MindboxFirebase
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.pushes.MindboxPushService
  
class MainApplication : Application(), ReactApplication {

	override fun onCreate() {
    super.onCreate()
    Mindbox.initPushServices(this, listOf(MindboxFirebase))
    // Mindbox.initPushServices(this, listOf(MindboxHuawei, MindboxFirebase)) для работы с двумя сервисами
  }
}
```

### Проверьте результат шага «Отправка push-notifications на Android через Firebase»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).
