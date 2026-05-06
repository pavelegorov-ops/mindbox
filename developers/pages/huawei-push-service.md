---
title: Huawei Push Service
slug: "huawei-push-service"
source_url: "https://developers.mindbox.ru/docs/huawei-push-service"
breadcrumb: []
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:57c0f75e99baac119f3d29e4efb21359999b2db591684fa50ccdec4ba37dc603"
---

# Huawei Push Service

## Передать в SDK HMS-токен

1. Создайте новый kotlin класс с названием `MindboxHuaweiMessagingService`.
2. Сделайте этот класс наследником от `HmsMessageService()`, если в приложении уже есть наследник `HmsMessageService`, то новый создавать не нужно, а все последующие изменения нужно добавить в существующий класс наследник `HmsMessageService`.
3. Реализуйте метод `onNewToken`

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_huawei.MindboxHuawei
import com.huawei.hms.push.*
import kotlinx.coroutines.*

class MindboxHuaweiMessagingService : HmsMessageService() {

    private val coroutineScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxHuawei)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
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

При первом push-уведомлении мы создадим собственный канал для уведомлений. Для него нужно придумать вместе с маркетологом название и описание. Подробнее про каналы уведомлений на Android можно почитать [тут](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%8B-%D1%83%D0%B2%D0%B5%D0%B4%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8-%D0%BD%D0%B0-android).

Идентификатор может быть любым, уникальным для вашего приложения.

```
...
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
        // Метод возвращает boolen, чтобы можно было сделать фолбек для обработки push-уведомлений
        coroutineScope.launch {
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
...
```

## Пример готового файла

```
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mindbox_huawei.MindboxHuawei
import com.huawei.hms.push.*
import kotlinx.coroutines.*

class MindboxHuaweiMessagingService : HmsMessageService() {

    private val coroutineScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(applicationContext, token, MindboxHuawei)
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
        coroutineScope.launch {
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
                // Если push-уведомление было не от Mindbox или в нем некорректные данные, то можно написать фолбе для его обработки
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        coroutineScope.cancel()
    }
}
```
