---
title: Как получать пуши из нескольких источников отправки
slug: "how-to-receive-push-notifications-from-multiple-sources"
source_url: "https://developers.mindbox.ru/docs/how-to-receive-push-notifications-from-multiple-sources"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:af56fad55cfe783ffa027557c924ee8b0bacf31ac9aade1dd7fcde65a7a29d6b"
---

# Как получать пуши из нескольких источников отправки

**Результат выполнения шага:**

- Обработка мобильных пушей полученных не из Mindbox

Доработки нужно проводить в созданных вами раннее, при интеграции Mindbox сервисах, унаследованных от `FirebaseMessagingService`, `HmsMessageService`, `HmsMessageService`.

Далее инструкция на примере работы с Firebase. Для остальных провайдеров логика идентична

**Необходимо провести следующие изменения:**

1. Добавить метод отправки токена на ваш бекэнд
2. Определить поставщика пуша и выбрать способ отрисовки
3. Удалить методы инициализациии и получения токена Firebase. Они уже добавлены в Mindbox SDK

## Добавление метода отправки токена на ваш бэкенд

В метод `onNewToken` добавьте вызов метода для отправки токена на ваш backend

```
...
    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(
            context = applicationContext,
            token = token,
            pushService = MindboxFirebase
        )
        // Your method to send firebase token to your backend
        sendTokenToYourBackend(token)
    }
...
```

## Определите получен пуш из Mindbox или нет

Для определения источника пуша используется метод `isMindboxPush`

В метод передается сообщение, полученное в `onMessageReceived`:

- Для Firebase вызовите его у объекта `MindboxFirebase`,
- для Huawei у `MindboxHuawei`,
- для RuStore у `MindboxRustore`.

```
class MindboxFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        if (MindboxFirebase.isMindboxPush(remoteMessage = message)) {
            val messageWasHandled = Mindbox.handleRemoteMessage(
                context = applicationContext,
                message = message,
                activities = activities,
                channelId = channelId,
                channelName = channelName,
                pushSmallIcon = pushSmallIcon,
                defaultActivity = defaultActivity,
                channelDescription = channelDescription
            )
...
```

## Реализуйте отображение пуша полученного не из Mindbox

```
class MindboxFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        if (MindboxFirebase.isMindboxPush(remoteMessage = message)) {
            val messageWasHandled = Mindbox.handleRemoteMessage(
                context = applicationContext,
                message = message,
                activities = activities,
                channelId = channelId,
                channelName = channelName,
                pushSmallIcon = pushSmallIcon,
                defaultActivity = defaultActivity,
                channelDescription = channelDescription
            )
        } else {
            // Your code for display notification
            showNotification(title = message.data["title"], body = message.data["body"])
        }
    }
...
```

## Пример готового кода

```
class MindboxFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        if (MindboxFirebase.isMindboxPush(remoteMessage = message)) {
            val messageWasHandled = Mindbox.handleRemoteMessage(
                context = applicationContext,
                message = message,
                activities = activities,
                channelId = channelId,
                channelName = channelName,
                pushSmallIcon = pushSmallIcon,
                defaultActivity = defaultActivity,
                channelDescription = channelDescription
            )
        } else {
            // Your code for display notification
            showNotification(title = message.data["title"], body = message.data["body"])
        }
    }

    override fun onNewToken(token: String) {
        Mindbox.updatePushToken(
            context = applicationContext,
            token = token,
            pushService = MindboxFirebase
        )
        // Your method to send firebase token to your backend
        sendTokenToYourBackend(token)
    }
}
```

Метод `onMessageReceived()` всегда срабатывает только для `data` пушей.  
Для [notification](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type) пушей в свернутом и выгруженном состоянии приложения метод вызван не будет. Уведомление в таком случае будет отрисовано системой.

Исключение составляет RuStore: метод `onMessageReceived()` будет вызван для любого типа пуша
