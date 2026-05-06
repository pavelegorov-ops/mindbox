---
title: Методы iOS SDK
slug: "ios-sdk-methods"
source_url: "https://developers.mindbox.ru/docs/ios-sdk-methods"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e357313b38a49905d76e94811c69cc88ab1e86d98ca1903c396262a9e5d750a6"
---

# Методы iOS SDK

## Методы для инициализации

## initialization

Метод инициализации SDK.

> Нужно вызывать **после получения ответа пользователя на отслеживание IDFA/IDFV**

---

> Нужно вызывать **только в Main потоке**

```
Mindbox.shared.initialization(configuration: MBConfiguration)
```

## notificationsRequestAuthorization

Метод передачи в SDK статуса разрешения на уведомления

#### Описание

```
Mindbox.shared.notificationsRequestAuthorization(granted: Bool)
```

#### Пример вызова

## apnsTokenUpdate

Метод передачи в SDK полученного APNS токена

Вызывается в методе `didRegisterForRemoteNotificationsWithDeviceToken` в `AppDelegate`

```
Mindbox.shared.apnsTokenUpdate(deviceToken: deviceToken)
```

## registerBGTasks

Метод регистрации фоновых задач для iOS 13 и выше

Вызывается в методе `didFinishLaunchingWithOptions` в `AppDelegate`

```
if #available(iOS 13.0, *) {
  Mindbox.shared.registerBGTasks()
}
UIApplication.shared.setMinimumBackgroundFetchInterval(UIApplication.backgroundFetchIntervalMinimum)
```

# Получение данных от SDK

## getDeviceUUID

Метод вызывает переданный колбек со значением DeviceUUID, который используется для работы SDK

Возвращает идентификатор, который можно использовать для отписки от колбека

#### Описание

```
public func getDeviceUUID(_ completion: @escaping (String) -> Void)
```

#### Пример вызова

## sdkVersion

Свойство, в котором хранится текущая версия SDK.

```
Mindbox.shared.sdkVersion
```

## isMindboxPush (since 2.8.3)

Метод принимает в качестве параметра UNNotification

Возвращает значение true/false, в зависимости от того пришло пуш-уведомление от Mindbox или нет.

#### Описание

```
public func isMindboxPush(notification: UNNotification) -> Bool
```

#### Пример вызова

## getMindboxPushData (since 2.8.3)

Метод принимает в качестве параметра UNNotification

Возвращает опциональную модель MBPushNotification если пуш-уведомление пришло от Mindbox. В ином случае вернется nil

#### Описание

```
public func getMindboxPushData(notification: UNNotification) -> MBPushNotification?
```

#### Пример вызова

## getAPNSToken

Метод вызывает переданный колбек со значением APNS токена, который сохранен в SDK  
Возвращает идентификатор, который можно использовать для отписки от колбека.

#### Описание

```
public func getAPNSToken(_ completion: @escaping (String) -> Void)
```

#### Пример вызова

## Передача статистики по пушу

## pushClicked

Метод передачи факта клика по пуш уведомления.  
Принимает либо целиком объект нотификации, либо строки уникальных ключей.  
В случае клика на тело пуша надо передать только строку uniqueKey. Если был клик по кнопке, то uniqueKey и buttonUniqueKey (той кнопки, на которую кликнул пользователь)

Принимает 3 варианта аргументов:

- response: <#T##UNNotificationResponse#>
- uniqueKey: <#T##String#>
- uniqueKey: <#T##String#>, buttonUniqueKey: <#T##String?#>

#### Описание

```
Mindbox.shared.pushClicked( )
```

#### Пример вызова

## Передача событий

Передача событий в Mindbox происходит через выполнение операций, заведенных в административном разделе. Операции можно выполнять в 2 режимах:

- асинхронно - API Mindbox отвечает 200 сразу, как получил данные. Обработка данных происходит в фоновом режиме
- синхронно - API Mindbox начинает обрабатывать запрос в момент получения и отвечает актуальным статусом обработки

[Подробное описание передачи событий через iOS SDK](ios-sdk-events.md)

## executeAsyncOperation

Метод выполнения операции в асинхронном режиме.

```
Mindbox.shared.executeAsyncOperation(
  operationSystemName: "<системное имя операции>",
  operationBody:  <тело запроса>
)
```

## executeSyncOperation

Метод для выполнения операции в синхронном режиме. Данные возвращаются в переданные колбеки

#### С использование стандартного класса ответа

```
public func executeSyncOperation<T>(
  operationSystemName: "<системное имя операции>",
  operationBody: <тело запроса>,
  completion: @escaping (Result<OperationResponse, MindboxError>) -> Void
) where T: OperationBodyRequestType {}
```

#### С использованием собственного класса ответа

## Управление логированием

Для управления уровнем логирования во время разработки вы можете установить нужное значение в параметр `logger`

Принимаемые значения:

- debug - 🪲
- info - ℹ️
- default - 💡
- error - ‼️
- fault - ⚠️
- none

```
Mindbox.logger.logLevel = .error
```

## Mindbox.logger.log()

Специальная функция для отображения данных через наш логгер. Используйте ее, если вам нужно залогировать что-то относящееся к работе Mindbox

#### Swift

```
Mindbox.logger.log(level: LogLevel, message: String)
```

#### Swift
