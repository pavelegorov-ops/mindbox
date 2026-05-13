---
title: RuStore
slug: "rustore-send-push-notifications-react-native"
source_url: "https://developers.mindbox.ru/docs/rustore-send-push-notifications-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
  - "Android | Настройка пуш-уведомлений"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:39b44c77bdce161d243ffad693b0d87147ecd0871784d0cc4d6df73c55a317b8"
---

# RuStore

# RuStore

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-android-integration.md)
- [Получение RuStore ключей](rustore-get-keys.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)

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
  implementation 'cloud.mindbox:mindbox-rustore'
  implementation 'ru.rustore.sdk:pushclient:6.10.0'
  ...
}
```

Для получения уведомлений вам также нужно добавить разрешение (подробнее [тут](https://developer.android.com/develop/ui/views/notifications/notification-permission), пример реализации [тут](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view_model/view_model.dart#L65-L72))

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

## 2. Реализовать отображение уведомлений

[Базовая интеграция](rustore-push-service.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## 3. Зарегистрируйте сервис обработку push-уведомлений в AndroidManifest.xml

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

В методе `Application.onCreate` нужно вызвать `Mindbox.initPushServices` с `MindboxRustore`.

Если в вашем проекте нет этого класса, его надо создать:

1. New → Kotlin class.
2. Впишите код из примера ниже.
3. Зарегистрируйте класс в AndroidManifest.xml.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.MindboxConfiguration
import cloud.mindbox.mindbox_rustore.MindboxRuStore

class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        Mindbox.initPushServices(applicationContext, listOf(MindboxRuStore))
        // Mindbox.initPushServices(this, listOf(MindboxFirebase, MindboxHuawei, MindboxRustore)) для 		         работы с несколькими сервисами сервисами
				// ...
    }
}
```

### Проверьте результат шага «Отправка push-notifications через RuStore»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).
