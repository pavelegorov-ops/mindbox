---
title: Huawei
slug: "huawei-send-push-notifications-flutter"
source_url: "https://developers.mindbox.ru/docs/huawei-send-push-notifications-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
  - "Android | Настройка пуш-уведомлений"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:b41bb9e21bb5d6302b11f62edf7965a7e0d0b424c5fc8dd0122ebc9458ccf87a"
---

# Huawei

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-android-integration.md)
- [Получение Huawei ключей](huawei-get-keys.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)

### Результат шага «Отправка push-notifications на Android через Huawei»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).

[Пример реализации отображения уведомлений Huawei](https://github.com/mindbox-cloud/flutter-sdk/tree/develop/example/flutter_example/android/app/src/main/kotlin/cloud/mindbox/flutter_example)

## 1. Сделайте интеграцию вашего приложения с Huawei

Из [официальной инструкции по добавлению Huawei](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-app-quickstart-0000001071490422) нужны следующие пункты:

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

Для получения уведомлений вам также нужно добавить разрешение (подробнее [тут](https://developer.android.com/develop/ui/views/notifications/notification-permission), пример реализации [тут](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view_model/view_model.dart#L65-L72))

В файле AndroidManifest.xml:

```
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
```

## 2. Реализовать отображение уведомлений

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

## 4.1. Добавьте библиотеку для обработки push-уведомлений

В файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть на странице библиотеки в [Maven Central](https://search.maven.org/artifact/cloud.mindbox/mindbox-firebase).

```
dependencies {
   ...
    implementation 'cloud.mindbox:mindbox-huawei'
   ...
}
```

## 4.2. Укажите библиотеку в методе инициализации

В методе `Application.onCreate` нужно вызвать `Mindbox.initPushServices` с `MindboxHuawei`.

Если в вашем проекте нет этого класса, его надо создать:

1. New → Kotlin class.
2. Впишите код из примера ниже.
3. Зарегистрируйте класс в `AndroidManifest.xml`.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.MindboxConfiguration
import cloud.mindbox.mindbox_huawei.MindboxHuawei

class MainApplication : Application() {
  override fun onCreate() {
        super.onCreate()
        // .... 
        
        // Нужно 
        Mindbox.initPushServices(applicationContext, listOf(MindboxHuawei))  

        // ...

    }
}
```

## 5. Настройка получения статусов сообщений

Huawei предоставляет сервис для получения статусов по отправленным сообщениям.Мы с ним интегрированы и за счет этого можем быстрее и точнее получать информацию о том, что происходит с отправкой push-уведомлений.

Для его использования вам нужно:

1. Открыть [консоль AppGallery](https://developer.huawei.com/consumer/ru/service/josp/agc/index.html#/).
2. Перейти в раздел Push Kit.
3. Открыть вкладку «Настройки».
4. Выбрать ваше приложение.
5. В разделе «Подтверждение приложения» выключить режим передачи статусов.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/b2c4690-a1e844c-4f063c0-Screenshot_2022-04-04_at_12.19.41.png)

6. Добавить наш домен.

Для того, чтобы узнать адрес домена, вам нужно открыть настройки точки интеграции на вашем проекте.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d9b82a0-__2024-07-26__16.32.22.png)

Нажать "Изменить" в блоке "Настройка отправки мобильных пушей Android".

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/3c9acc5-ad41968-__2024-07-23__15.10.08.png)

Скопировать адрес домена, который вы увидите в информационной панели.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/39163b7-f888c81-__2024-07-23__15.11.58.png)

7. Нажать «Отправить». Статусы в нашей системе начнут обрабатываться автоматически.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/df059cd-39574fd-__2024-07-23__18.12.13.png)

### Проверьте результат шага «Отправка push-notifications на Android через Huawei»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).
