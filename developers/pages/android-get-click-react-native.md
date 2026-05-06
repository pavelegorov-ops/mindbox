---
title: "Android | Передача кликов по push-уведомлениям"
slug: "android-get-click-react-native"
source_url: "https://developers.mindbox.ru/docs/android-get-click-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:544c6b0163625566809a864f9b5b73fcd94a0b213c4ec921af033e99227ec108"
---

# Android | Передача кликов по push-уведомлениям

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-android-integration.md)
- [Добавление SDK в приложение](add-sdk-react-native.md#/)
- [Инициализация SDK](sdk-initialization-react-native.md#/)
- [Получение Firebase ключей](firebase-key-setup.md#/)
- [Отправка push-notifications через Firebase](firebase-send-push-notifications-react-native.md#/)

или

- [Получение Huawei ключей](huawei-get-keys.md#/)
- [Отправка push-notifications через Huawei](huawei-send-push-notifications-react-native.md#/)

### Результат шага «Получение кликов на мобильные push-уведомления на Android»:

Push должен отправиться и отобразиться на вашем телефоне, и по клику на него статус в системе поменялся на «есть клик».

Проверить, что клики приходят, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-клики-приходят-в-систему).

[Пример реализации](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/android/app/src/main/java/com/exampleapp/MainActivity.kt#L40)

## 1. Передача кликов по push-уведомлениям

В файле `android/MainActivity.kt` нужно разместить вызов метода `Mindbox.onPushClicked`.

Вызывать этот метод нужно в 2 коллбеках: `onNewIntent` и `onCreate`.

```
package com.testmbsdk

import android.content.Context
import android.content.Intent
import android.os.Bundle
import com.facebook.react.ReactActivity
import cloud.mindbox.mobile_sdk.Mindbox

class MainActivity : ReactActivity() {
    private fun sendIntent(context: Context, intent: Intent) {
        Mindbox.onNewIntent(intent)
        Mindbox.onPushClicked(context, intent)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // ...
        intent?.let { sendIntent(this, it) }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        // ...
        sendIntent(this, intent)
    }
}
```

Метод `Mindbox.onPushClicked` дополнительно возвращает `true`, если интент распознан SDK и обработан корректно, и `false` в противном случае.

Вы можете это использовать для реализации дополнительной логики, если нужно.
