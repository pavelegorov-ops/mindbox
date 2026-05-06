---
title: "Навигация по клику на push-уведомление"
slug: "flutter-push-navigation-react-native"
source_url: "https://developers.mindbox.ru/docs/flutter-push-navigation-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:840668639a597c528ab3194b3cb83aa8ed95ee4c754e733e3471e07819db8bff"
---

# Навигация по клику на push-уведомление

### Результат шага

При клике на push-уведомление в консоли разработчика выводится ссылка из этого уведомления.

[Пример реализации](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp)

Для получения ссылки в React Native подпишитесь на событие, которое будет генерироваться в нативной части при клике.

Подписка будет вызвана 2 аргументами:

- `link` — ссылка, указанная в уведомлении;
- `payload` — сериализованный payload push-уведомления. Если передается JSON, то его десериализовать надо самостоятельно.

```
MindboxSdk.onPushClickReceived((pushUrl: String | null, pushPayload: String | null) => {
  console.log(`${pushUrl} ${pushPayload}`);
});
```

Чтобы подписка вызывалась, в нативной части надо реализовать передачу ссылки.

---

## Передача ссылки из iOS-части

В файле `ios/AppDelegate` нужно указать следующий вызов:

```
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    // ...

    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse,
        withCompletionHandler completionHandler: @escaping () -> Void
    ) {
        Mindbox.shared.pushClicked(response: response)
        // Проброс события в JS
        MindboxJsDelivery.emitEvent(response)
        completionHandler()
    }
}
```

---

## Передача ссылки из Android-части

В файле `android/MainActivity.java` нужно передать:

```
import android.content.Context
import android.content.Intent
import android.os.Bundle
import cloud.mindbox.mobile_sdk.Mindbox
import com.mindboxsdk.MindboxJsDelivery

class MainActivity : ReactActivity() {

    private var mJsDelivery: MindboxJsDelivery? = null

    private fun sendIntent(context: Context, intent: Intent) {
        Mindbox.onNewIntent(intent)
        Mindbox.onPushClicked(context, intent)
        mJsDelivery?.sendPushClicked(intent)
    }

    // Инициализация + отправка интента
    private fun initializeAndSentIntent(context: ReactContext) {
        mJsDelivery = MindboxJsDelivery.Shared.getInstance(context)

        if (context.hasCurrentActivity()) {
            sendIntent(context, context.currentActivity!!.intent)
        } else {
            sendIntent(context, this.intent)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Вместо прямого вызова sendIntent(this, intent)
        val reactInstanceManager = reactNativeHost.reactInstanceManager
        val reactContext = reactInstanceManager.currentReactContext

        if (reactContext != null) {
            initializeAndSentIntent(reactContext)
        } else {
            // Ожидаем инициализацию React-контекста
            reactInstanceManager.addReactInstanceEventListener(object :
                ReactInstanceManager.ReactInstanceEventListener {

                override fun onReactContextInitialized(context: ReactContext) {
                    initializeAndSentIntent(context)
                    reactInstanceManager.removeReactInstanceEventListener(this)
                }
            })
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        sendIntent(this, intent)
    }
}
```

Если у вас используется новая архитектура, то перепишите метод onCreate следующим образом

```
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val reactHost = getReactHost()
        val context = reactHost.currentReactContext as? ReactContext
        if (context != null) {
            initializeAndSentIntent(context)
        } else {
            reactHost.addReactInstanceEventListener(object :
                ReactInstanceManager.ReactInstanceEventListener {
                override fun onReactContextInitialized(context: ReactContext) {
                    initializeAndSentIntent(context)
                    reactHost.removeReactInstanceEventListener(this)
                }
            })
        }
    }
```

### Проверьте результат шага

При клике на push-уведомление в консоли разработчика выводится ссылка из этого уведомления.
