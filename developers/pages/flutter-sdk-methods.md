---
title: Методы Flutter SDK
slug: "flutter-sdk-methods"
source_url: "https://developers.mindbox.ru/docs/flutter-sdk-methods"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:855d9f621774d4e8d6e6d41035669033fd9abff42f453784090ba5a75d4a72d1"
---

# Методы Flutter SDK

# Инициализация

## `Mindbox.instance.init`

Создайте конфигурацию и инициализируйте SDK:

```
final config = Configuration(
  domain: "домен API Mindbox",
  endpointIos: "endpoint для iOS",
  endpointAndroid: "endpoint для Android",
  subscribeCustomerIfCreated: true,
);

Mindbox.instance.init(configuration: config);
```

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

## Получение данных от SDK

### getDeviceUUID

Метод получения UUID устройства после присвоения. Может вызываться в любое время, но вернет строку в колбек только после инициализации.

```
Mindbox.instance.getDeviceUUID((uuid) {
  print(uuid);
});
```

### getToken

Метод получения token(APNS/FMS) после присвоения. Может вызываться в любое время, но вернет строку в коллбек только после инициализации.

```
Mindbox.instance.getToken((token) {
  print(token);
});
```

### sdkVersion

Свойство, в котором хранится текущая версия SDK.

```
Mindbox.instance.nativeSdkVersion
```

---

## Обработка кликов по уведомлениям

### onPushClickReceived

Метод для подписки на событие кликов по уведомлениям. Переданный коллбек вызывается в момент, когда пользователь нажимает на уведомление и запускается приложение.

В качестве аргументов передаются ссылка и payload, которые были в нажатом пуше. Если нажатие было по кнопке, то возвращается ссылка из кнопки, если по телу — то ссылка с тела.

```
Mindbox.instance.onPushClickReceived((link, payload) {
  switch (link) {
    case 'mindbox.cloud':
      Navigator.push(context,
        MaterialPageRoute(builder: (_) => ContentPage()));
      break;

    case 'mindbox.cloud/user':
      Navigator.push(context,
        MaterialPageRoute(builder: (_) => ProfilePage()));
      break;

    default:
      Navigator.push(context,
        MaterialPageRoute(builder: (_) => HomePage()));
  }
});
```

---

## Передача данных (выполнение операций)

Передача событий в Mindbox происходит через выполнение операций, заведенных в административном разделе. Операции можно выполнять в 2 режимах:

- асинхронно — API Mindbox отвечает 200 сразу, как получил данные. Обработка данных происходит в фоновом режиме.
- синхронно — API Mindbox начинает обрабатывать запрос в момент получения и отвечает актуальным статусом обработки.

[Подробное описание передачи событий через iOS SDK](ios-sdk-events.md)

### executeAsyncOperation

Метод выполнения операции в асинхронном режиме.

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: '<системное имя операции>',
  operationBody: {
    <Map<String, dynamic> с данными>
  },
);
```

### executeSyncOperation

Метод для выполнения операции в синхронном режиме. Данные возвращаются в переданные коллбеки.

```
Mindbox.instance.executeSyncOperation(
  operationSystemName: '<системное имя операции>',
  operationBody: {
    <Map<String, dynamic> с данными>
  },
  onSuccess: (data) {
    // обработка успешного ответа
  },
  onError: (error) {
    // обработка ошибки
  },
);
```

## Управление логированием

Для управления тем, что будет писать в консоль Mindbox SDK, есть специальный метод установки уровня логирования: setLoglevel.

Логи пишутся только в debug сборке. В продакшн режиме Mindbox SDK ничего не пишет в консоль.

```
Mindbox.instance.setLogLevel(logLevel: LogLevel.debug);
```

Варианты значения:

- LogLevel.verbose
- LogLevel.debug
- LogLevel.info
- LogLevel.warn
- LogLevel.error
- LogLevel.none

## registerInAppCallbacks

Метод используется для реализации своей обработки клика и закрытия In-App  
Подробнее можно прочитать в разделе [In-App](in-app.md#flutter)

```
Mindbox.instance.registerInAppCallbacks(inAppCallbacks: [
  CustomInAppCallback(
    clickHandler: (id, redirectUrl, payload) {
      print(id);
      print(redirectUrl);
      print(payload);
    },
    dismissedHandler: (id) {
      print(id);
    },
  ),
]);
```

## refreshNotificationPermissionStatus (since 2.14.3)

Метод используется для обновления статуса разрешения на получение уведомлений

#### Dart

```
Mindbox.instance.refreshNotificationPermissionStatus()
```

#### Пример
