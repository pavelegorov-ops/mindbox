---
title: Методы React Native SDK
slug: "react-native-sdk-methods"
source_url: "https://developers.mindbox.ru/docs/react-native-sdk-methods"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7f6dd13cefcebdeebb4646f81257ee13fadc69606bd5a2ed2ae5e36422a18d5c"
---

# Методы React Native SDK

[Использование всех методов можно найти в примере по реализации интеграции с Mindbox SDK](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/src/screens/HomeScreen.tsx)

## Инициализация

### Mindbox.initialize

Создание конфигурации и инициализация SDK

```
MindboxSdk.initialize({
        domain: 'домен API mindbox',
        endpointId:
          Platform.OS === 'ios'
            ? ''
            : '',
        subscribeCustomerIfCreated: true,
        shouldCreateCustomer: true,
        previousInstallId: '',
        previousUuid: '',
      })
```

### Domain API Mindbox

Домен, по которому будет обращение в API Mindbox.

Возможные значения:  
api.mindbox.ru - выбирается, если адрес проекта project.mindbox.ru  
api.mindbox.cloud - выбирается, если адрес проекта project.mindbox.cloud

❗️ Не передавайте в этом поле адрес административного раздела

## Получение данных от SDK

### getDeviceUUID

Метод получения UUID устройства после присвоения. Может вызываться в любое время, но вернет строку в колбек только после инициализации.

```
MindboxSdk.getDeviceUUID(uuid => {
    console.log(uuid);
  });
```

### getToken

Метод получения token(APNS/FMS) после присвоения. Может вызываться в любое время, но вернет строку в колбек только после инициализации.

```
MindboxSdk.getToken(token => {
    console.log(token);
  });
```

## Обработка кликов по уведомлениям

### onPushClickReceived

Метод для подписки на событие кликов по уведомлениям. Переданный колбек вызывается в момент, когда пользователь нажимает на уведомление и запускается приложение  
В качестве аргумента передается та ссылка, которая была в нажатом пуше.  
Если нажатие было по кнопке - возвращается ссылка из кнопки, если по телу - то ссылка с тела

```
MindboxSdk.onPushClickReceived((pushUrl: String | null, pushPayload: String | null) => { 
  console.log(pushUrl);
  console.log(pushPayload);
});
```

## Передача событий (вызов операций)

Передача событий в Mindbox происходит через выполнение операций, заведенных в административном разделе. Операции можно выполнять в 2 режимах:

- асинхронно - API Mindbox отвечает 200 сразу, как получил данные. Обработка данных происходит в фоновом режиме
- синхронно - API Mindbox начинает обрабатывать запрос в момент получения и отвечает актуальным статусом обработки

[Подробное описание передачи событий через iOS SDK](rn-sdk-events.md)

### executeAsyncOperation

Метод выполнения операции в асинхронном режиме.

```
MindboxSdk.executeAsyncOperation({
  operationSystemName: '<системное имя операции>',
  operationBody: {  },
});
```

### executeSyncOperation

Метод для выполнения операции в синхронном режиме. Данные возвращаются в переданные колбеки

```
MindboxSdk.executeSyncOperation({
  operationSystemName: '<системное имя операции>',
  operationBody: {  },
  onSuccess: (data) => { ... },
  onError: (error) => { ... },
});
```

## getSdkVersion

Метод для получения текущей версии SDK.

```
import MindboxSdk from "mindbox-sdk";

MindboxSdk.getSdkVersion((version) => { ... })
```

## setLogLevel

Для управления тем, что будет писать в консоль Mindbox SDK, есть специальный метод установки уровня логирования: **setLogLevel**.

Логи пишутся только в debug сборке. В продакшн режиме Mindbox SDK ничего не пишет в консоль.i

```
import MindboxSdk, { LogLevel} from "mindbox-sdk";

MindboxSdk.setLogLevel(LogLevel.DEBUG)
```

Варианты значения LogLevel:

- LogLevel.VERBOSE
- LogLevel.DEBUG
- LogLevel.INFO
- LogLevel.WARN
- LogLevel.ERROR
- LogLevel.NONE

## refreshNotificationPermissionStatus (since 2.14.5)

Метод для передачи информации о смене статуса разрешения на уведомления. Нужно вызвать после получения разрешения на уведомления от пользователя, для немедленного обновления статуса в Mindbox SDK.

```
import MindboxSdk from "mindbox-sdk";

MindboxSdk.refreshNotificationPermissionStatus();
```
