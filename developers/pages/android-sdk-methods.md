---
title: Методы Android SDK
slug: "android-sdk-methods"
source_url: "https://developers.mindbox.ru/docs/android-sdk-methods"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e36d61f0872e31c9cba5d615f22ffb875264eb3be4118d4d0da4ddf0d25b1e02"
---

# Методы Android SDK

## Методы для инициализации

Примеры вызова методов можно найти [тут](https://github.com/mindbox-cloud/android-sdk/tree/develop/example/app/src/main/java/com/mindbox/example)

## init

Метод инициализации SDK

Вызывается в методе `onCreate` в классе наследнике от `Application`

```
Mindbox.init(
  context: Context,
  configuration: MindboxConfiguration,
  listOf: List<MindboxPushService>
)
```

Возможные варианты:

- Без мобильных пушей: Mindbox.init(applicationContext, configuration, listOf())
- Только Firebase: Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase))
- Только Huawei: Mindbox.init(applicationContext, configuration, listOf(MindboxHuawei))
- Только RuStore: Mindbox.init(applicationContext, configuration, listOf(MindboxRuStore))
- Все сервисы. Первый в списке считается приоритетным, если на телефоне пользователя доступны все сервисы: Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase, MindboxHuawei, MindboxRuStore))

## initPushServices

Метод для инициализации push-сервисов  
Вы должны вызвать этот метод в onCreate вашего класса Application, если вы вызываете метод init в Activity

```
Mindbox.initPushServices(
  context = applicationContext,
  pushServices = listOf(MindboxFirebase, MindboxHuawei, MindboxRuStore)
)
```

## updatePushToken

Метод для передачи в SDK токена FMS/HMS/RuStore.  
Вызывается в методе `onNewToken` класса наследника `MessagingService`

#### Описание

```
Mindbox.updatePushToken(context: Context, token: String, pushService: MindboxPushService)
```

#### Пример вызова FMS

#### Пример вызова HMS

#### Пример вызова RuStore

## Получение данных от SDK

## subscribeDeviceUuid и disposeDeviceUuidSubscription

### subscribeDeviceUuid

Метод получение deviceUUID. Работает через подписку, чтобы избежать проблем в случае вызова до инициализации Mindbox SDK.  
Значение вернется строкой в переданном колбеке.

Вызов метода возвращает идентификатор, который можно использовать для отписки от колбека

#### Описание

```
Mindbox.subscribeDeviceUuid(
    context: Context,
    subscription: (String) → Unit
  ): String

  Mindbox.disposeDeviceUuidSubscription(
    subscriptionId: String
  )
```

#### Пример вызова

### disposeDeviceUuidSubscription

Метод очистки подписки на получение deviceUUID. Принимает идентификатор, который вернул метод подписки

## subscribePushTokens и disposePushTokenSubscription

### subscribePushTokens

Метод получения токенов Firebase, HMS, RuStore  
Работает через подписку, чтобы избежать проблем в случае вызова до инициализации Mindbox SDK.
Значение вернется в переданный колбек строкой json вида `{"FCM":"token1","HMS":"token2","RuStore":"token3"}`

Вызов метода возвращает идентификатор, который можно использовать для отписки от колбека.

#### Описание

```
Mindbox.subscribePushTokens(
subscription: (String?) → Unit
): String

Mindbox.disposePushTokenSubscription(
subscriptionId: String
)
```

#### Пример вызова

### disposePushTokenSubscription

Метод очистки подписки на получение FMS/HMS/RuStore токенов. Принимает идентификатор, который вернул метод подписки

## getPushTokensSaveDate

Возвращает даты сохранения токенов FMS/HMS/RuStore формате пак ключ-значение (проваейдер-timestamp)

```
Mindbox.getPushTokensSaveDate(): Map<String, Long>
```

## getSdkVersion

Возвращает версию SDK

```
Mindbox.getSdkVersion(): String
```

## Передача статистики по пушу

## onPushReceived

Метод для передачи статуса “Пуш получен”.  
Используется в коде обработки пуша

Не используйте этот метод, если вы пользуетесь handleRemoteMessage

#### Описание

```
Mindbox.onPushReceived(
context: Context,
uniqKey: String
)
```

#### Пример вызова

## onPushClicked

Метод передачи клика по пушу.  
uniq_push_key - обязательный - идентификатор пуша
uniq_push_button_key - опционально - идентификатор кнопки, передается, если кликнули по кнопке

#### Описание

```
Mindbox.onPushClicked(
context: Context,
uniq_push_key: String,
uniq_push_button_key: String
)
```

#### Пример вызова

## setLogLevel

Для управления тем, что будет писать в консоль Mindbox SDK, есть специальный метод установки уровня логирования: `setLoglevel`

Варианты значения:  
Level.NONE
Level.VERBOSE
Level.INFO
Level.DEBUG
Level.WARN
Level.ERROR

Логи пишутся только в debug сборке. В продакшн режиме Mindbox SDK ничего не пишет в консоль.

```
Mindbox.setLogleve(level)
```

## Передача событий

Передача событий в Mindbox происходит через выполнение операций, заведенных в административном разделе. Операции можно выполнять в 2 режимах:

- асинхронно - API Mindbox отвечает 200 сразу, как получил данные. Обработка данных происходит в фоновом режиме
- синхронно - API Mindbox начинает обрабатывать запрос в момент получения и отвечает актуальным статусом обработки

[Подробное описание передачи событий через Android SDK](android-integration-of-actions.md)

## executeAsyncOperation

Метод выполнения операции в асинхронном режиме.

```
Mindbox.executeAsyncOperation(
  context = context,
  operationSystemName = "<системное имя операции>",
  operationBody = <тело запроса>
)
```

## executeSyncOperation

Метод для выполнения операции в синхронном режиме. Данные возвращаются в переданные колбеки

#### С использованием системного класса ответа

```
Mindbox.executeSyncOperation(
context: Context,
operationSystemName: "<системное имя операции>",
operationBody: <тело запроса>,
onSuccess: (OperationResponse) -> Unit,
onError: (MindboxError) -> Unit
)
```

#### С использование собственного класса ответа

## Получение данных кликнутого пуша

При обработке клика на пуш, который отрисован методом `handleRemoteMessage` вы можете получить данные, которые были в этом пуше

## getUrlFromPushIntent

Метод для получения ссылки кликнутого пуша.  
Возвращает ссылку, которую настроили в административном разделе. Если пользователь нажал на тело пуша - вернется ссылка с тела, если на кнопку - ссылка этой кнопки

```
Mindbox.getUrlFromPushIntent(intent)
```

## getPayloadFromPushIntent

Метод для получения payload кликнутого пуша.  
Возвращает данные, которые были указаны в качестве payload пуша в административном разделе.

Данные возвращаются строкой. Если был указан JSON, то его нужно самостоятельно сериализовать

```
Mindbox. getPayloadFromPushIntent(intent)
```

## setMessageHandling (since 2.6.1)

В методе реализованы различные стратегии обработки ошибок при загрузке изображений уведомлений. Также предоставлена возможность реализовать собственную стратегию загрузки изображений.

По умолчанию используется стратегия `applyDefaultStrategy` (при возникновении ошибки будет показан push без изображения) и дефолтный способ загрузки изображения

```
fun setMessageHandling(
        imageFailureHandler: MindboxImageFailureHandler = PushNotificationManager.messageHandler.imageFailureHandler,
        imageLoader: MindboxImageLoader = PushNotificationManager.messageHandler.imageLoader,
    )
```

### Возможные стратегии обработки ошибок при загрузке картинок:

Мы предоставляем 5 решений:

- **cancellationStrategy**: Используйте `MindboxImageFailureHandler.cancellationStrategy()`  
  Если произошла ошибка загрузки картинки, то пуш не будет показан
- **applyDefaultStrategy**: Используйте `MindboxImageFailureHandler.applyDefaultStrategy(defaultImage)`  
  При возникновении ошибки загрузки картинки используется изображение по умолчанию, указанное в конструкторе (если значение `defaultImage` равно null, то пуш будет показан без изображения)
- **retryOrDefaultStrategy**: Используйте `MindboxImageFailureHandler.retryOrDefaultStrategy(maxAttempts, delay, defaultImage)`  
  Если произошла ошибка загрузки картинки, произойдут попытки повторить загрузку изображения максимальное количество раз с интервалом задержки. Если изображение в итоге не получится загрузить, то отобразится push с изображением по умолчанию (или без изображения, если `defaultImage` равно null)
- **applyDefaultAndRetryStrategy**: Используйте `MindboxImageFailureHandler.applyDefaultAndRetryStrategy(maxAttempts, delay, defaultImage)`  
  Если произошла ошибка загрузки картинки, отобразится пуш с `defaultImage` (или без изображения, если `defaultImage` равен null) и произойдет попытка повторить загрузку изображения максимальное количество раз с интервалом задержки. **Требуется minSdkLevel = M (23)**
- **retryOrCancelStrategy**: Используйте `MindboxImageFailureHandler.retryOrCancelStrategy(maxAttempts, delay)`.  
  Если произошла ошибка загрузки картинки, произойдет попытка повторить загрузку изображения максимальное количество раз с интервалом задержки. Если изображение не загрузится, то пуш не будет показан пользователю

Для использования этих стретегий необходимо в `Application.onCreate()` (или в вашей Activity) вызвать метод`Mindbox.setMessageHandling(imageFailureHandler = strategy)`

```
class App: Application {
 
    override fun onCreate() {
        ...
        val defaultImage = ContextCompat.getDrawable(this, R.drawable.ic_placeholder)?.toBitmap()
        Mindbox.setMessageHandling(
                imageFailureHandler = MindboxImageFailureHandler.retryOrDefaultStrategy(
                    maxAttempts = 5,
                    delay = 3_000L,
                    defaultImage = defaultImage,
                ),
        )
        ...
    }
 
}
```

Вы можете реализовать свои собственные стратегии, реализовав `MindboxImageFailureHandler` и переопределив метод `onImageLoadingFailed`

```
fun onImageLoadingFailed(  
    context: Context,  
    message: RemoteMessage,  
    state: MessageHandlingState,  
    error: Throwable,  
): ImageRetryStrategy
```

`message: RemoteMessage` модель отображаемого уведомления,  
`state: MessageHandlingState` содержит количество попыток показа данного push и флаг `isMessageDisplayed`, показывающий, был ли показан пуш.
Возвращаемое значение - `ImageRetryStrategy`, которое является одним из следующих:

- `ImageRetryStrategy.Cancel`: остановить процесс и не показывать пуш
- `ImageRetryStrategy.ApplyDefault(defaultImage)`: остановить процесс загрузки и показать пуш с изображением по умолчанию
- `ImageRetryStrategy.Retry(delay)`: повторить загрузку изображения через интервал задержки
- `ImageRetryStrategy.ApplyDefaultAndRetry(delay, defaultImage)`: показать push с изображением по умолчанию (или без него, если defaultImage равно null)

Примеры можно посмотреть в исходном коде sdk

### Cпособы загрузки изображения

Мы предоставляем одно решение по умолчанию, которое делает прямой запрос на получение изображения. Для его получения используйте `MindboxImageLoader.default()`.  
Для его использования необходимо в Application.onCreate() (или в вашей Активити) вызвать `Mindbox.setMessageHandling(imageLoader = loader)`

```
class App: Application {
 
    override fun onCreate() {
        ...
        Mindbox.setMessageHandling(
            imageLoader = MindboxImageLoader.default(),
        )
        ...
    }
 
}
```

Вы можете реализовать собственную стратегию загрузки изображений, реализовав интерфейс `MindboxImageLoader` и переопределив его метод onLoadImage

```
fun onLoadImage(
    context: Context,
    message: RemoteMessage,
    state: MessageHandlingState,
): Bitmap?
```

`message: RemoteMessage` модель отображаемого уведомления,  
`state: MessageHandlingState` содержит количество попыток показа этого push и флаг `isMessageDisplayed`, показывающий, был ли показан push.
Необходимо загрузить изображение и вернуть его в результате работы данного метода

## updateNotificationPermissionStatus (since 2.8.1)

Метод для передачи информации о смене статуса разрешения на уведомления

```
Mindbox.updateNotificationPermissionStatus(context:Context)
```

## handleRemoteMessage

Метод для отрисовки push-уведомления

Если используете этот метод, не вызывайте onPushReceived()

```
fun handleRemoteMessage(
        context: Context,
        message: Any?,
        channelId: String,
        channelName: String,
        @DrawableRes pushSmallIcon: Int,
        defaultActivity: Class<out Activity>,
        channelDescription: String? = null,
        activities: Map<String, Class<out Activity>>? = null,
    ): Boolean
```

## isMindboxPush

Метод для проверки принадлежит ли push Mindbox

#### Since 2.13.3

```
// For MindboxFirebase, MindboxHuawei, MindboxRuStore

fun isMindboxPush(remoteMessage: RemoteMessage): Boolean

fun isMindboxPush(remoteMessageData: Map<String, String>): Boolean
```

#### Since 2.8.4

## convertToMindboxRemoteMessage

Метод для конвертации модели уведомления провайдера в модель уведомления Mindbox

#### Since 2.13.3

```
// For MindboxFirebase, MindboxHuawei, MindboxRuStore

fun convertToMindboxRemoteMessage(remoteMessage: RemoteMessage?): MindboxRemoteMessage?

fun convertToMindboxRemoteMessage(remoteMessageData: Map<String, String>): MindboxRemoteMessage?
```

#### Since 2.8.4

## Изменение цвета иконки pushSmallIcon (since 2.10.0)

Чтобы поменять цвет монохромной иконки, в уведомлении задайте цвет в ресурсе `mindbox_default_notification_color` в файле `res/values/colors.xml`. Изменение цвета может не работать на некоторых версиях Android в зависимости от изготовителя устройства.

```
<color name="mindbox_default_notification_color">#FF0000color>
```

## Включение отображения In-App на DialogFragment (since 2.13.5)

Чтобы включить возможность отрображения In-App поверх DialogFragment, добавьте булевый ресурс `mindbox_support_inapp_on_fragment` со значением `true` в файле `res/values/bools.xml`

```
<bool name="mindbox_support_inapp_on_fragment">truebool>
```

# Классы Android SDK

## Mindbox

Синглтон, содержащий все публичные методы Mindbox SDK

## MindboxFirebase

Синглтон, отвественный за использование провайдера push-уведомлений Firebase.

Может быть использован при инициализации в application в методе Mindbox.init() или в методе initPushServices, при инициализации в activity

## MindboxHuawei

Синглтон, отвественный за использование провайдера push-уведомлений Huawei.

Может быть использован при инициализации в application в методе Mindbox.init() или в методе initPushServices, при инициализации в activity

## MindboxRuStore

Синглтон, отвественный за использование провайдера push-уведомлений RuStore.

Может быть использован при инициализации в application в методе Mindbox.init() или в методе initPushServices, при инициализации в activity

Можно передать projectId RuStore, для инициализации через метод `MindboxRuStore(RUSTORE_PROJECT_ID)`

## MindboxError

Класс, отвечающий за ошибку, произошедшую в sdk.

Может быть получена при отправке синхронной операции

## InitializeMindboxException

Класс, отвечающий за ошибку при инициализации SDK. Такая ошибка будет выброшена ошибке в инициализациию

## PushAction

Класс, отвечающий за хранение информации о кнопке в push-уведомлении. Может быть использован в качестве модели, если вы используете собственную реализацию отрисовки уведомлений.

## RemoteMessage

Класс, отвечающий за хранение информации о push-уведомлении. Может быть использован в качестве модели, если вы используете собственную реализацию отрисовки уведомлений.
