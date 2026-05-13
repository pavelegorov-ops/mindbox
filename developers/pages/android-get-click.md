---
title: "4. Получение кликов на мобильные push-уведомления"
slug: "android-get-click"
source_url: "https://developers.mindbox.ru/docs/android-get-click"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:ad2730cdb4135590958c018575ba2da3120921d53da885a7d62a59a0efac4532"
---

# 4. Получение кликов на мобильные push-уведомления

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Получение Firebase ключей для Android-приложения](firebase-key-setup.md)  
  или
  [Получение Huawei ключей для Android-приложения](huawei-get-keys.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)
- [Отправка push-notifications через Firebase](firebase-send-push-notifications.md)  
  или
  [Отправка push-notifications через Huawei](huawei-send-push-notifications.md)

### Результат шага «Получение кликов на мобильные push-уведомления»:

Мобильное push-уведомление отправляется и отображается на вашем телефоне, по клику на него статус в системе поменялся на «есть клик».

Проверить, что клики приходят, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-клики-приходят-в-систему).

[Пример реализации метода отправки события клика и получения данных из пуша](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/Utils.kt#L27) и [Пример вызова метода](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MainActivity.kt#L33)

## 1. Передача кликов по push-уведомлениям

#### Отрисовка уведомлений через Mindbox

В тех активити, которые вы указали в методе `onMessageReceived` на предыдущем шаге, надо разместить вызов метода `Mindbox.onPushClicked`.

Вызывать этот метод надо в 2 коллбеках: `onNewIntent` и `onCreate`.

```
import cloud.mindbox.mobile_sdk.*

class MainActivity : AppCompatActivity() {

    private fun processMindboxIntent(intent: Intent?) {
        // Добавляем событие клика по push-уведомлению
        intent?.let { Mindbox.onPushClicked(this, it) }
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        processMindboxIntent(intent)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        processMindboxIntent(intent)
        
        // ...
    }

    // ...
}
```

Метод `Mindbox.onPushClicked` дополнительно возвращает `true`, если интент распознан SDK и обработан корректно, и `false` в противном случае.

Вы можете это использовать для реализации дополнительной логики, если нужно.

#### Самостоятельная отрисовка уведомлений

## 2. Навигация в приложении

По клику открывается та активити, которую указали при отрисовке push-уведомлений. Если вам нужно дополнительно обработать какие-то данные из push-уведомления, то вы можете получить их, вызвав методы `getUrlFromPushIntent` и `getPayloadFromPushIntent`.

```
val pushUrl = Mindbox.getUrlFromPushIntent(intent)
val payload = Mindbox.getPayloadFromPushIntent(intent)
```

### Результат шага «Получение кликов на мобильные push-уведомления»:

Мобильное push-уведомление отправляется и отображается на вашем телефоне, по клику на него статус в системе поменялся на «есть клик».

Проверить, что клики приходят, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-клики-приходят-в-систему).
