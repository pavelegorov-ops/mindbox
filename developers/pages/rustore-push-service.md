---
title: RuStore Push Service
slug: "rustore-push-service"
source_url: "https://developers.mindbox.ru/docs/rustore-push-service"
breadcrumb: []
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7fd616834d3fde493b0b3fb86cde5b43f241c310111fee7dc69e2dab8b5c6521"
---

# RuStore Push Service

## Передать в SDK push-токен

1. Создайте новый kotlin класс с названием `MindboxRuStoreMessagingService`.
2. Сделайте этот класс наследником от `RuStoreMessagingService()`, если в приложении уже есть наследник `RuStoreMessagingService`, то новый создавать не нужно, а все последующие изменения нужно добавить в существующий класс наследник `RuStoreMessagingService`.
3. Реализуйте метод `onNewToken`.

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_rustore.MindboxRuStore
import ru.rustore.sdk.pushclient.messaging.*

class MindboxRuStoreMessagingService : RuStoreMessagingService() {

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxRuStore)
    }
...
```

## Укажите, какие адреса могут приходить в push-уведомлении и как они соотносятся с активити приложения

В каждом push-уведомлении приходит ссылка, которую настроили в административном разделе. Также в push-уведомлении может быть до 3 кнопок, у каждой своя ссылка.

Чтобы корректно обработать открытие приложения и открыть ту активити, которую задумывалось, сформируйте Map. Укажите в нем ссылки и активити, которые они должны открывать. Этот метод обработает получение push-уведомлений, скачает картинку и отобразит push-уведомление.

При формировании Map activities для описания ссылок вы можете использовать маску с символом `*`. Например,`https://mindbox.ru/push/*` будет соответствовать:

- `https://mindbox.ru/push/`,
- `https://mindbox.ru/push/1`,
- `https://mindbox.ru/push/foo`,
- `https://mindbox.ru/push/foo?product=123`.

Push-уведомления и кнопки с таким URL будут открываться в одном активити, который вы указали.

```
...
class MindboxRuStoreMessagingService : RuStoreMessagingService() {

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxRuStore)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активти поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        // Перечесление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity
        )
...
```

## Укажите, какая активити должна вызываться по умолчанию

Эта активити будет отображена, если в push-уведомлении пришла ссылка, которой нет в списке.

```
...
class MindboxRuStoreMessagingService : RuStoreMessagingService() {

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxRuStore)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активти поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        // Перечесление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity
        )
...
```

## Придумайте название и описание канала для push-уведомлений

При первом push-уведомлении мы создадим собственный канал для уведомлений. Для него нужно придумать вместе с маркетологом название и описание.  
Идентификатор может быть любым, уникальным для вашего приложения.

```
...
class MindboxRuStoreMessagingService : RuStoreMessagingService() {
  ...
  override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активти поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        // Перечесление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity
        )

        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >" // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >" // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = "< ИКОНКА ДЛЯ УВЕДОМЛЕНИЙ >" // R.mipmap.ic_launcher
...
```

## Вызовите метод для отрисовки push-уведомлений

Для реализации отображения push-уведомлений вызовите метод `Mindbox.handleRemoteMessage` и передайте в него подготовленные данные.

Метод возвращает `TRUE`, если push-уведомление успешно обработано и отображено, и `FALSE`, если push-уведомление не обработано. На этот статус вы можете завязать логику обработки push-уведомления другими методами.

```
...
class MindboxRuStoreMessagingService : RuStoreMessagingService() {
  ...
  override fun onMessageReceived(remoteMessage: RemoteMessage) {
    ...
      // Метод возвращает boolen, чтобы можно было сделать фолбек для обработки push-уведомлений
      val messageWasHandled = Mindbox.handleRemoteMessage(
          context = applicationContext,
          message = remoteMessage,
          activities = activities,
          channelId = channelId,
          channelName = channelName,
          pushSmallIcon = pushSmallIcon,
          defaultActivity = defaultActivity,
          channelDescription = channelDescription
        )
```

## Пример готового кода

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_rustore.MindboxRuStore
import ru.rustore.sdk.pushclient.messaging.*

class MindboxRuStoreMessagingService : RuStoreMessagingService() {

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxRuStore)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Активти поумолчанию. Откроется, если пришла ссылка, которой нет в перечислении
        val defaultActivity = MainActivity::class.java

        // Перечесление ссылок и активити, которые должны открываться по разным ссылкам
        val activities = mapOf(
            "https://mindbox.ru/" to defaultActivity
        )

        val channelId = "< ИДЕНТИФИКАТОР КАНАЛА >" // "my_android_app_channel"
        val channelName = "< НАЗВАНИЕ КАНАЛА >" // "Рекламные рассылки"
        val channelDescription = "< ОПИСАНИЕ КАНАЛА >"  // "Рассылки, которые содержат рекламу"
        val pushSmallIcon = "< ИКОНКА ДЛЯ УВЕДОМЛЕНИЙ >" // R.mipmap.ic_launcher

        // Метод возвращает boolen, чтобы можно было сделать фолбек для обработки push-уведомлений
        val messageWasHandled = Mindbox.handleRemoteMessage(
          context = applicationContext,
          message = remoteMessage,
          activities = activities,
          channelId = channelId,
          channelName = channelName,
          pushSmallIcon = pushSmallIcon,
          defaultActivity = defaultActivity,
          channelDescription = channelDescription
        )

        if (!messageWasHandled) {
          // Если push-уведомление было не от Mindbox или в нем некорректные данные, то можно написать фолбек для его обработки
        } 
    }
    
    override fun onDeletedMessages() {
    }

    override fun onError(errors: List<RuStorePushClientException>) {
    }
}
```
