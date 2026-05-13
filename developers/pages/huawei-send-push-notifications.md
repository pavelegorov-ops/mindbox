---
title: "3.2. Отправка push-notifications через Huawei"
slug: "huawei-send-push-notifications"
source_url: "https://developers.mindbox.ru/docs/huawei-send-push-notifications"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f141986c75ccabac16ca0cdfa00de382cb3698954f984228221fd5ff3aab9aa4"
---

# 3.2. Отправка push-notifications через Huawei

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Получение Huawei ключей для Android-приложения](huawei-get-keys.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)

### Результат шага «Отправка push-notifications через Huawei»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).

## 1. Сделайте интеграцию вашего приложения с Huawei

Из [официальной инструкции по добавлению Huawei](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-app-quickstart-0000001071490422) нужны следующие пункты:

- зарегистрировать свое приложение в AppGallery;
- интегрируйте HMS Core SDK.

Для удобства можете воспользоваться [набором инструментов HMS Toolkit](https://developer.huawei.com/consumer/en/huawei-toolkit/).

После того, как эти шаги сделаны, можно переходить к реализации сервиса, который будет отвечать за получение токенов и push-уведомлений.

```
dependencies {
     implementation 'com.huawei.hms:push:6.13.0.300'
     ...
}
```

**Если в вашем приложении указан targetSdk 33**, то для получения уведомлений вам также нужно добавить разрешение (подробнее [тут](https://developer.android.com/develop/ui/views/notifications/notification-permission), пример реализации [тут](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MainActivity.kt#L71))

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

[Пример реализации отображения уведомлений Huawei](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MindboxHuaweiMessagingService.kt)

[Базовая интеграция](huawei-push-service.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](custom-push-notification-rendering.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

Для выбора поведения при ошибке загрузки картинок или для написания собственной логики используйте метод [setMessageHandling](android-sdk-methods.md#setmessagehandling-since-261)

## 3. Зарегистрируйте сервис обработку push-уведомлений в AndroidManifest.xml

Добавьте в файл `AndroidManifest.xml` следующие пункты:

```
<application ...>
  ...
 
  <service android:name=".MindboxHuaweiMessagingService" android:exported="false">
    <intent-filter>
      <action android:name="com.huawei.push.action.MESSAGING_EVENT"/>
    intent-filter>
  service>

  ...
application>

<queries>
  <intent>
    <action android:name="com.huawei.hms.core.aidlservice" />
  intent>
queries>
```

## 4. Доработайте метод инициализации, чтобы push-уведомления отображались при выгруженном приложении

[Пример инициализации](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/ExampleApplication.kt#L41)

## 4.1 Добавьте библиотеку для обработки push-уведомлений

В файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть [на странице библиотеки в Maven Central](https://search.maven.org/artifact/cloud.mindbox/mindbox-firebase).

### Начиная с версии 2.10.0 не нужно указывать фиксированную версию huawei, вместо этого следует:

implementation 'cloud.mindbox'

```
dependencies {
   ...
    implementation 'cloud.mindbox:mobile-sdk:{версия}' 
    implementation 'cloud.mindbox:mindbox-huawei' # since 2.10.0
   ...
}
```

## 4.2 Укажите библиотеку в методе инициализации

В методе `Mindbox.init`, который должен быть размещен в коллбеке onCreate вашего приложения, нужно указать, что в этой сборке используется MindboxHuawei.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.MindboxConfiguration
import cloud.mindbox.mindbox_firebase.MindboxHuawei

class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // .... 

        // Было 
				// Mindbox.init(applicationContext, configuration, listOf())  
        
        // Нужно 
        Mindbox.init(applicationContext, configuration, listOf(MindboxHuawei))  

        // ...

    }
}
```

Добавьте в коллбэк onCreate вашего приложения вызов метода `Mindbox.initPushServices`

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_huawei.MindboxHuawei
class MyApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // ....
        Mindbox.initPushServices(applicationContext, listOf(MindboxHuawei))
        Mindbox.init(applicationContext, configuration, listOf(MindboxHuawei))
        // ...
    }
}
```

## 5. Настройка получения статусов сообщений

Huawei предоставляет сервис для получения статусов по отправленным сообщениям. Мы с ним интегрированы, и за счет этого можем быстрее и точнее получать информацию о том, что происходит с отправкой push-уведомлений.

Для его использования вам нужно:

1. Открыть [консоль AppGallery](https://developer.huawei.com/consumer/ru/service/josp/agc/index.html#/);
2. Перейти в раздел Push Kit;
3. Открыть вкладку «Настройки»;
4. Выбрать ваше приложение.
5. В разделе «Подтверждение приложения» выключить режим передачи статусов;

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a1e844c-4f063c0-Screenshot_2022-04-04_at_12.19.41.png)

6. Добавить наш домен;

Для того, чтобы узнать адрес домена, вам нужно открыть настройки точки интеграции на вашем проекте.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9812dee-__2024-07-26__16.32.22.png)

Нажать "Изменить" в блоке "Настройка отправки мобильных пушей Android".

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ad41968-__2024-07-23__15.10.08.png)

Скопировать адрес домена, который вы увидите в информационной панели.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/f888c81-__2024-07-23__15.11.58.png)

7. Нажать «Отправить». Статусы в нашей системе начнут обрабатываться автоматически.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/39574fd-__2024-07-23__18.12.13.png)

### Проверьте результат шага «Отправка push-notifications через Huawei»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).
