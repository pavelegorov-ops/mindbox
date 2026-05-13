---
title: "custom-push-notification-rendering"
slug: "custom-push-notification-rendering"
source_url: "https://developers.mindbox.ru/docs/custom-push-notification-rendering"
breadcrumb: []
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:d9ffd89469d3f2b40138a55c542b62998dc10fbff986784cc96c2aae1683e8ac"
---

# custom-push-notification-rendering

## Самостоятельная отрисовка push-уведомлений

Если вы не хотите использовать для отрисовки push-уведомлений встроенный функционал, вы можете использовать собственную отрисовку push-уведомлений, как описано здесь. В этом случае вам также необходимо будет вызвать метод Mindbox.onPushReceived внутри метода onMessageReceived.

```
import cloud.mindbox.mobile_sdk.Mindbox
import com.google.firebase.messaging.*

class MindboxFirebaseMessagingService: FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        // Передача токена в Mindbox SDK
        Mindbox.updatePushToken(applicationContext, token, MindboxFirebase)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        Mindbox.onPushReceived(context, notificationId)
    		//*
        ..Ваша отрисовка..
      	*//
      	
    }
}
```
