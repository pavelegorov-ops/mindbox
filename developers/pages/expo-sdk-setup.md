---
title: Базовая установка Expo SDK
slug: "expo-sdk-setup"
source_url: "https://developers.mindbox.ru/docs/expo-sdk-setup"
breadcrumb:
  - Мобильные приложения
  - Expo SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:bae00ed147759671168973f08a9986785c0de59feb560ad485a7495daa7017ff"
---

# Базовая установка Expo SDK

### Результат шага:

- Из Mindbox отправляются мобильные push-уведомление на обе платформы и они отображается на устройстве.
- На обеих платформах отображаются In-App
- Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).
- Проверить, что In-App отображаются, можно с помощью [этой инструкции](https://help.mindbox.ru/docs/in-apps).

## Требования

- Expo SDK 54+
- React Native 0.81.+
- Mindbox sdk не ниже версии 2.14.6
- [Точка интеграции настроена](add-integration-rn.md)

## Установка плагина

Добавьте зависимости в `package.json`:

```
"mindbox-sdk": "^2.14.6",
 "mindbox-expo-plugin": "^1.0.4"
```

Затем выполните установку: `npm install`

Плагин `mindbox-expo-plugin` должен быть первым в списке плагинов.

## Инициализация SDK

[Пример инициализации SDK](https://github.com/mindbox-cloud/expo-plugin/blob/master/examples/MindboxExpoExample/src/screens/HomeScreen.tsx#L69)

### 1. Выбор варианта конфигурации SDK

Выберите вариант конфигурации SDK на основе требований от маркетинга.

Необходимо получить «<эндпоинт проекта>» (системное имя точки интеграции) от вашего менеджера проекта Mindbox, либо посмотреть его в [настройках точки интеграции](add-ios-integration.md). Обратите внимание, что «<ендпоинт проекта>» чувствителен к регистру, то есть имеет значение, используются ли заглавные или строчные буквы.

### Domain API Mindbox

Это домен, по которому будет происходить обращение в API Mindbox.

Чтобы получить нужный домен для вашего проекта, сделайте следующее:

  

1. Перейдите на сайт проекта  
2. Перейдите в список операций через "Кампании" → "Список кампаний" → "Операции"   
3. Откройте любую операцию  
4. Нажмите «Посмотреть описание»  
5. Скопируйте домен из URL в спецификации

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/85d049ea13949fccd34fc1175669e8ec538a31f20e730b7fd98015040d117195-image.png)

---

**1. Хочу передавать в Mindbox анонимных пользователей и отправлять им push-уведомления**

```
const configuration = {
        domain: '',
        endpointId:
          Platform.OS === 'ios'
            ? ''
            : '',
        subscribeCustomerIfCreated: true,
        shouldCreateCustomer: true,
      };
```

**2. Хочу передавать в mindbox анонимных пользователей без возможности отправлять им push-уведомления**

```
const configuration = {
        domain: '',
        endpointId:
          Platform.OS === 'ios'
            ? ''
            : '',
        subscribeCustomerIfCreated: false,
        shouldCreateCustomer: true,
      };
```

**3. Не хочу передавать в mindbox анонимных пользователей**

```
const configuration = {
        domain: '',
        endpointId:
          Platform.OS === 'ios'
            ? ''
            : '',
        subscribeCustomerIfCreated: false,
        shouldCreateCustomer: false,
      };
```

---

### 2. Настройка React Native-части проекта

Инициализировать SDK нужно синхронно в основном файле приложения **`App.tsx / App.js`**, используйте вариант конфигурации, выбранный в пункте выше

```
import MindboxSdk from 'mindbox-sdk';
import React, {useCallback, useEffect, useState} from 'react';

const App = () => {
   const appInitializationCallback = useCallback(async () => {
     try {
       ВСТАВЬТЕ СЮДА ВЫБРАННУЮ НА ЭТАПЕ 1 КОНФИГУРАЦИЮ SDK
       await MindboxSdk.initialize(configuration);
     } catch (error) {
       console.log(error);
     }
   }, []);
   ....
   return ()
 }
```

Чтобы проверить корректность инициализации, добавьте вывод deviceUUID в консоль в любом удобном месте.

### Как можно проверить?

## Конфигурация плагина

### Все доступные параметры

### Android

1. Получите ключи провайдеров для отправки push-уведомлений.

[Firebase](firebase-key-setup.md)

Получение ключей Firebase.

[Huawei](huawei-get-keys.md)

Получение ключей Huawei.

[RuStore](rustore-get-keys.md)

Получение ключей RuStore.

1. Подключите и настройте плагин `mindbox-expo` в `app.json`.

**Пример конфигурации:**

```
"plugins": [
      [
        "mindbox-expo-plugin",
        {
          "androidPushProviders": [
            "firebase",
            "huawei",
            "rustore"
          ],
          "googleServicesFilePath": "./credentials/google-services.json",
          "huaweiServicesFilePath": "./credentials/agconnect-services.json",
          "rustoreProjectId": "hWZJga09nar5gsh0lbKlkZDuCgDJswgN",
          "androidChannelId": "expo_channel_id",
          "androidChannelName": "expo_name",
          "androidChannelDescription": "expo_description",
          "smallIcon": "./assets/icon_mb.png",
          "smallIconAccentColor": "#80F00A0A",
        }
      ]
    ]
```

### iOS

1. [Настройте Sandbox-окружение](sandbox-integration-setup.md).
2. Получите ключи и настройте подключение к APNs по [инструкции](apns-keys-setup.md).
3. Убедитесь, что в `app.json` в разделе `ios` указаны параметры
   `bundleIdentifier` и `appleTeamId`.
4. Если appleTeamId не указан и нет возможности его указать, то в `mindbox-expo-plugin` необходимо добавить `iosDevTeam` и в значении передать идентификатор команды
5. В `mindbox-expo-plugin` укажите `iosMode`.

Возможны 2 значения:

- `"development"` (по умолчанию)
- `"production"`

Если вы используете Expo Notification для отправки и отображения push-уведомлений, [выполните дополнительные настройки](expo-notification.md).

### Запросите разрешения на уведомления и передайте сведения о статусе в Mindbox

Это можно сделать как на стороне Android/iOS, так и в ReactNative

Пример запроса разрешения на уведомления c использованием `Expo Notification`

```
import * as Notifications from 'expo-notifications';

.....

const { status: existingStatus } = await Notifications.getPermissionsAsync();
const finalStatus = existingStatus === 'granted' 
  ? existingStatus 
  : (await Notifications.requestPermissionsAsync()).status;

finalStatus === 'granted' && MindboxSdk.refreshNotificationPermissionStatus();
```
