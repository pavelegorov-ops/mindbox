---
title: Инициализация SDK
slug: "sdk-initialization-react-native"
source_url: "https://developers.mindbox.ru/docs/sdk-initialization-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:a30d50dd0516017fc587ca1caac60d10affb66a0c29861d7dcfbb2c0d8d7b7cc"
---

# Инициализация SDK

### Убедитесь, что эти шаги выполнены успешно:

Настройка точек интеграции:

- [iOS](add-ios-integration.md)
- [Android](add-android-integration.md)
- [Добавление SDK в приложение](add-sdk-react-native.md)

### Результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок на обеих платформах (iOS и Android);
- В консоли разработчика в Xcode выведен **deviceUUID** SDK mindbox;
- Дополнительно, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

[Пример инициализации SDK](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/src/screens/HomeScreen.tsx#L44)

## 1. Выбор варианта конфигурации SDK

Выберите вариант конфигурации SDK на основе требований от маркетинга.

Необходимо получить «<эндпоинт проекта>» от вашего менеджера проекта Mindbox, либо посмотреть его в [настройках точки интеграции](add-ios-integration.md). Обратите внимание, что «<ендпоинт проекта>» чувствителен к регистру, то есть имеет значение, используются ли заглавные или строчные буквы.

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

## 2. Инициализация SDK

### 2.1. Настройка React Native-части проекта

Инициализировать SDK нужно синхронно в основном файле приложения **`App.tsx / App.js`**, используйте вариант конфигурации, выбранный на этапе 1.

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

На этом этапе вы уже можете **запустить приложение на Android**

---

## 2.2. Настройка iOS-части проекта

Для работы Mindbox SDK в React-Native проекте нужно добавить Mindbox iOS SDK в нативную часть проекта и выполнить необходимые настройки.

### 2.2.1. Добавление AppGroups

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/eb50ebb-Untitled.png)

1. Откройте настройки проекта.
2. Выберите основной таргет.
3. Перейдите на вкладку `Signing & Capabilities`.
4. Нажмите на кнопку «добавить» и выберите `AppGroups`.
5. Добавьте новую группу с названием по шаблону `group.cloud.Mindbox.{bundle id приложения}`  
   Например, bundle id приложения - `Mindbox-Sample-App`, тогда значение App Group должно быть `group.cloud.Mindbox.Mindbox-Sample-App`.

### AppGroup должна быть собрана по шаблону:

group.cloud.Mindbox.{bundle id приложения}

Если допустить ошибку в шаблоне AppGroup в Main Target — приложение не соберется.

Фактическое значение лучше проверять через файл с расширением `.entitlements`.

SDK валидирует, что группа названа по шаблону. Если нарушить шаблон, SDK выбросит исключение.

---

### Проверьте результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок на обеих платформах (iOS и Android);
- В консоли разработчика в Xcode выведен **deviceUUID** SDK mindbox;
- Дополнительно, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

## Если вам нужно изменить endpoint

Если ваше приложение используется в нескольких странах, а точное местоположение клиента становится известно только после запуска приложения, может потребоваться смена **`endpoint`** для корректной передачи информации о стране. Для этого нужно повторно вызвать **`MindboxSdk.initialize`** и указать в конфигурации новые **`endpoint`**
