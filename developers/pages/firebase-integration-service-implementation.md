---
title: Реализация сервиса для подключения Firebase
slug: "firebase-integration-service-implementation"
source_url: "https://developers.mindbox.ru/docs/firebase-integration-service-implementation"
breadcrumb: []
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:ad33c605f4897e9ea3772f52d0583c4b496ae0e90ef2eb496f652ace90b40107"
---

# Реализация сервиса для подключения Firebase

## Передать в SDK Firebase-токен

Создайте новый kotlin класс с названием MindboxFirebaseMessagingService.  
Сделайте этот класс наследником от FirebaseMessagingService(), если в приложении уже есть наследник FirebaseMessagingService, то новый создавать не нужно, а все последующие изменения нужно добавить в существующий класс наследник FirebaseMessagingService.  
Реализуйте метод onNewToken.

```
import cloud.mindbox.mobile_sdk.Mindbox
import com.google.firebase.messaging.*

class MindboxFirebaseMessagingService: FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        // Передача токена в Mindbox SDK
        Mindbox.updatePushToken(applicationContext, token, MindboxFirebase)
    }
...
```

## Укажите, какие адреса могут приходить в push-уведомлении и как они соотносятся с активити приложения

В каждом push-уведомлении приходит ссылка, которую настроили в административном разделе. Также в push-уведомлениях может быть до 3 кнопок, у каждой своя ссылка.

Чтобы корректно обработать открытие приложения и открыть ту активити, которую задумывалось, сформируйте Map. Укажите в нем ссылки и активити, которые они должны открывать.

Для реализации базового отображения push-уведомлений мы предоставляем готовый метод Mindbox.handleRemoteMessage. Этот метод обработает получение push-уведомления, скачает картинку и отобразит push-уведомление.

При формировании Map activities для описания ссылок вы можете использовать маску с символом `_`. Например,`https://mindbox.ru/push/_` будет соответствовать:

- `https://mindbox.ru/push/`,
- `https://mindbox.ru/push/1`,
- `https://mindbox.ru/push/foo`,
- `https://mindbox.ru/push/foo?product=123`.

Push-уведомления и кнопки с таким URL будут открываться в одной активити, которую вы указали.

```
...
        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >"      // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >"         // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = R.mipmap.ic_launcher

        // Перечисление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity,
        )
...
```

## Укажите, какая активити должна вызываться по умолчанию

Эта активити будет отображена, если в push-уведомлении пришла ссылка, которой нет в списке.

```
...
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активити поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >"      // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >"         // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = R.mipmap.ic_launcher
        
...
```

## Придумайте id, название и описание канала для push-уведомлений

При первом push-уведомлении мы создадим собственный канал для уведомлений. Для него нужно придумать вместе с маркетологом название и описание. Подробнее про каналы уведомлений на Android можно прочитать тут.

Идентификатор может быть любой уникальной для вашего приложения строкой.

```
...
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активити поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >"      // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >"         // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = R.mipmap.ic_launcher
...
```

## Отрисовка уведомления

Для отрисовки push-уведомлений можно использовать встроенный функционал. Для этого необходимо вызвать метод Mindbox.handleRemoteMessage() и передать ему соответствующие параметры.

Метод возвращает TRUE, если push-уведомление успешно обработано и отображено, и FALSE, если push-уведомлений не обработано. На этот статус вы можете завязать логику обработки push-уведомления другими методами.

```
...
        // Метод возвращает boolen, чтобы можно было сделать фолбек для обработки push-уведомлений
        val messageWasHandled = Mindbox.handleRemoteMessage(
            context = applicationContext,
            message = remoteMessage,
            activities = activities,
            channelId = channelId, // Идентификатор канала для уведомлений, отправленных из Mindbox
            channelName = channelName,
            pushSmallIcon = pushSmallIcon, // Маленькая иконка для уведомлений
            defaultActivity = defaultActivity,
            channelDescription = channelDescription
        )
...
```

## Пример готового файла

```
import cloud.mindbox.mobile_sdk.Mindbox
import com.google.firebase.messaging.*

class MindboxFirebaseMessagingService: FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        // Передача токена в Mindbox SDK
        Mindbox.updatePushToken(applicationContext, token, MindboxFirebase)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активити поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >"      // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >"         // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = R.mipmap.ic_launcher

        
        // Перечисление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity,
        )

        // Метод возвращает boolen, чтобы можно было сделать фолбек для обработки push-уведомлений
        val messageWasHandled = Mindbox.handleRemoteMessage(
            context = applicationContext,
            message = remoteMessage,
            activities = activities,
            channelId = channelId, // Идентификатор канала для уведомлений, отправленных из Mindbox
            channelName = channelName,
            pushSmallIcon = pushSmallIcon, // Маленькая иконка для уведомлений
            defaultActivity = defaultActivity,
            channelDescription = channelDescription
        )

        if (!messageWasHandled) {
            // Если push-уведомление было не от Mindbox или в нем некорректные данные, то можно написать фолбек для его обработки
        }
    }
}
```
