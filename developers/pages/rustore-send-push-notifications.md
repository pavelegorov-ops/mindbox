---
title: "3.3. Отправка push-notifications через RuStore"
slug: "rustore-send-push-notifications"
source_url: "https://developers.mindbox.ru/docs/rustore-send-push-notifications"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:294c12525ff18e2b4534e190bda508ee938100b8a0d13cf7714b1406d4b35d67"
---

# 3.3. Отправка push-notifications через RuStore

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Получение RuStore ключей для Android-приложения](rustore-get-keys.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)

### Результат шага «Отправка push-notifications через RuStore»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).

## 1. Сделайте интеграцию вашего приложения с RuStore

Из [официальной инструкции по добавлению RuStore](https://www.rustore.ru/help/sdk/push-notifications/kotlin-java/6-5-0) нужны следующие пункты:

- Используется актуальная версия SDK.
- Приложение загружено в Консоль RuStore.
- Приложение прошло модерацию (публиковать приложение необязательно).
- На устройстве пользователя установлена актуальная версия RuStore.
- Приложение RuStore поддерживает функциональность push-уведомлений.
- Приложению RuStore разрешен доступ к работе в фоновом режиме. Без этого разрешения push-уведомления будут приходить, но со значительной задержкой.
- Отпечаток подписи приложения, установленного на девайсе, совпадает с отпечатком подписи приложения, которое загружено в Консоль RuStore.

### RuStore поддерживает Android 7.0 и выше

На устройствах Android версии API ниже 24 (Android 7) использовать MindboxRuStore можно, но push уведомления приходить не будут. На такие устройства нельзя установить магазин приложений RuStore, который требуется для работы push уведомлений от RuStore.

После того, как эти шаги сделаны, можно переходить к реализации сервиса, который будет отвечать за получение токенов и push-уведомлений.

```
repositories {
    maven {
        url = uri("https://artifactory-external.vkpartner.ru/artifactory/maven")
    }
}
```

```
dependencies {
    implementation("ru.rustore.sdk:pushclient:6.10.0")
    ...
}
```

**Если в вашем приложении указан targetSdk 33**, то для получения уведомлений вам также нужно добавить разрешение (подробнее [тут](https://developer.android.com/develop/ui/views/notifications/notification-permission), пример реализации [тут](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MainActivity.kt#L71))

В файле AndroidManifest.xml добавить разрешение на push-уведомления и RuStore ProjectId вашего приложения:

```
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
 
 <application ...>
  ...
  <meta-data
    android:name="ru.rustore.sdk.pushclient.project_id"
    android:value="YOUR_RUSTORE_PROJECT_ID" />
application>
```

В файле MainActivity.kt запросить разрешение на отправку push уведомлений:

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

[Пример реализации отображения уведомлений RuStore](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MindboxRuStoreMessagingService.kt)

[Базовая интеграция](rustore-push-service.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## 3 Зарегистрируйте сервис обработку push-уведомлений в AndroidManifest.xml

Добавьте в файл `AndroidManifest.xml` следующие пункты:

```
<application ...>
  ...
 
	<service
         android:name=".MindboxRuStoreMessagingService"
         android:exported="true"
         tools:ignore="ExportedService">
  <intent-filter>
    <action android:name="ru.rustore.sdk.pushclient.MESSAGING_EVENT" />
  intent-filter>
  service>

  ...
application>
```

## 4. Доработайте метод инициализации, чтобы push-уведомления отображались при выгруженном приложении

[Пример инициализации](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/ExampleApplication.kt#L34)

## 4.1 Добавьте библиотеку для обработки push-уведомлений

В файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть [на странице библиотеки в Maven Central](https://central.sonatype.com/artifact/cloud.mindbox/mindbox-rustore).

```
dependencies {
   ...
    implementation 'cloud.mindbox:mobile-sdk:{версия}' # 2.12.0 и выше
    implementation 'cloud.mindbox:mindbox-rustore'
   ...
}
```

## 4.2 Укажите библиотеку в методе инициализации

В методе `Mindbox.init`, который должен быть размещен в коллбеке onCreate вашего приложения, нужно указать, что в этой сборке используется MindboxRuStore.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.MindboxConfiguration
import cloud.mindbox.mindbox_rustore.MindboxRuStore

class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // .... 

        // Было 
				// Mindbox.init(applicationContext, configuration, listOf())  
        
        // Нужно 
        Mindbox.init(applicationContext, configuration, listOf(MindboxRuStore))  

        // ...

    }
}
```

Добавьте в коллбэк onCreate вашего приложения вызов метода `Mindbox.initPushServices`

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_rustore.MindboxRuStore

class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // ....
        Mindbox.initPushServices(applicationContext, listOf(MindboxRuStore))
        Mindbox.init(applicationContext, configuration, listOf(MindboxRuStore))
        // ...
    }
}
```

### Проверьте результат шага «Отправка push-notifications через RuStore»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).
