---
title: "In-App"
slug: "in-app"
source_url: "https://developers.mindbox.ru/docs/in-app"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e9d1c9254bee62873a5493f84c67dacd05563659e237885e0a8548f6ad3f0a61"
---

# In-App

Для поддержки in-app в вашем приложении, необходимо добавить в приложение и инициализировать SDK.  
*На данный момент функционал in-app доступен для нативных приложений и для приложений на Flutter и React-Native*

# iOS

### Убедитесь, что эти шаги выполнены

- [Добавление SDK в приложение](add-sdk-to-app.md)
- [Инициализация SDK](ios-sdk-initialization.md)

## Настройка навигации

## Версия SDK [2.6.4](https://github.com/mindbox-cloud/ios-sdk/releases/tag/2.6.4) и выше

### DefaultInappMessageDelegate

По умолчанию реализовано следующее поведение, при клике на in-app:

- если в настройках In-App’а указана ссылка перехода, осуществляется переход по ссылке, либо диплинку.
- если в настройках In-App’а в поле payload указан текст (не JSON или XML), то содержимое копируется в буфер обмена
- если в настройках ничего не указано, in-app продолжает отображаться, пока пользователь его не закроет

Инициализируйте SDK и обработка кликов по In-app будет работать.

---

### Другие протоколы для обработки кликов по In-App

Если вы не используете вариант по-умолчанию, реализуйте нужный протокол из списка ниже и добавьте строку сразу после инициализации Mindbox SDK

```
Mindbox.shared.inAppMessagesDelegate = self
```

---

### InAppMessagesDelegate

Настоятельно рекомендуем использовать данный протокол, если вы хотите использовать кастомную реализацию методов.

`func inAppMessageTapAction(id: String, url: URL?, payload: String)` - для обработки нажатия по in-app

`func inAppMessageDismissed(id: String)` - для обработки закрытия in-app

Если методы оставить пустыми, при клике на in-app не будет происходить никаких действий. При клике на крестик, либо по другой области приложения, In-app закроется.

---

### URLInappMessageDelegate

Если в настройках In-App’а указана ссылка перехода, осуществляется переход по ссылке, либо диплинку

---

### CopyInappMessageDelegate

Если в настройках In-App’а в поле payload указан текст (не JSON или XML), то содержимое копируется в буфер обмена

---

### CompositeInappMessageDelegate

Так же, вы можете использовать CompositeInappMessageDelegate, чтобы варьировать предыдущие реализации, если это необходимо.

```
class ClassA: URLInappMessageDelegate { }
class ClassB: CopyInappMessageDelegate { } 

class ViewController: CompositeInappMessageDelegate { 
		var delegates: [InAppMessagesDelegate]
		let classA = ClassA()
		let classB = ClassB()

		init() { 
				delegates = [classA, classB]
				initMindBox()
				Mindbox.shared.inAppMessagesDelegate = self
		}
}
```

## Версия SDK [2.6.3](https://github.com/mindbox-cloud/ios-sdk/releases/tag/2.6.3) и ниже

В данных версиях SDK настройка навигации по умолчанию не реализована. Для того, чтобы клики по in-app'у обрабатывались, необходимо добавить

```
Mindbox.shared.inAppMessagesDelegate = inAppMessagesDelegate
```

сразу после инициализации sdk. Тип объекта `inAppMessagesDelegate` должен реализовывать протокол`InAppMessagesDelegate` . В реализации протокола поддержать 2 метода:

`func inAppMessageTapAction(id: String, url: URL?, payload: String)` - для обработки нажатия по in-app

`func inAppMessageDismissed(id: String)` - для обработки закрытия in-app

# Android

### Убедитесь, что эти шаги выполнены:

- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)

## Настройка навигации

## Версия SDK [2.6.3](https://github.com/mindbox-cloud/android-sdk/releases/tag/2.6.3) и выше

[Пример использования метода](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/MindboxInappMethods.kt)

По умолчанию реализовано следующее поведение, при клике на in-app (**ComposableInAppCallback**):

- если в настройках In-App’а указана ссылка перехода, осуществляется переход по ссылке, либо диплинку.
- если в настройках In-App’а в поле payload указан текст (не JSON или XML), то содержимое копируется в буфер обмена
- если в настройках ничего не указано, in-app продолжает отображаться, пока пользователь его не закроет

Инициализируйте SDK и обработка кликов по In-app будет работать.

### ComposableInAppCallback

*(по умолчанию)*

Реализация **ComposableInAppCallback** включает в себя реализации UrlInAppCallback, DeeplinkInAppCallback, CopyPayloadInAppCallback и LoggingInAppCallback (описаны ниже).

Так же, вы можете использовать ComposableInAppCallback, чтобы использовать разные сочетания предыдущих реализаций, если это необходимо.

```
ComposableInAppCallback(
    UrlInAppCallback(),
    DeepLinkInAppCallback(),
    CopyPayloadInAppCallback(),
    LoggingInAppCallback()
)
```

### Важное замечание

В случае, если вам не подходит реализация по умолчанию, вам нужно вызвать метод `fun registerInAppCallback(inAppCallback: InAppCallback)` после инициализации  SDK и передать туда нужный вам коллбэк.

### UrlInAppCallback

Используя этот коллбэк, у вас будет работать открытие URL в браузере.

---

### DeepLinkInAppCallback

Используя этот коллбэк, по умолчанию у вас будет работать открытие диплинков

---

### CopyPayloadInAppCallback

Используя этот коллбэк, по умолчанию у вас будет копироваться Payload.

---

### LoggingInAppCallback

Используя этот коллбэк, у вас будут логироваться клики по инаппу и его закрытие

---

### EmptyInAppCallback

Если вы не хотите, чтобы клики по In-app как-либо обрабатывались, то вам нужно использвать этот коллбэк

---

### InAppCallback

Если вам не подходит ни один из предыдущих вариантов, то вы можете реализовать свой коллбэк, используя этот интерфейс

```
Mindbox.registerInAppCallback(object : InAppCallback {
    override fun onInAppClick(id: String, redirectUrl: String, payload: String) {
TODO("Not yet implemented")
    }

    override fun onInAppDismissed(id: String) {
TODO("Not yet implemented")
    }
})
```

## Версия SDK [2.6.2](https://github.com/mindbox-cloud/android-sdk/releases/tag/2.6.2) и ниже

В данных версиях SDK настройка навигации по умолчанию не реализована. Для того, чтобы клики по in-app'у обрабатывались, необходимо добавить после инициализации sdk вызвать метод `registerInAppCallback(obj: InAppCallback)`, в параметрах передать ему объект реализующий интерфейс `InAppCallback`, в интерфейсе 2 метода:

`fun onInAppClick(id: String, url: String, payload: String)` - для обработки нажатия по in-app

`fun onInAppDismissed(id: String)` - для обработки закрытия in-app

---

Метод закрытия можно оставить пустым, если там не нужны какие-то дополнительные действия. Если in-app не предполагает никаких переходов при клике - onInAppClick тоже можно оставить пустым. В таком случае in-app никак не будет реагировать на клики по нему, если url и payload для in-app'а не заполнены в административной панели. Или будет закрываться при клике, если одно из них или оба заполнены.  
Если действия или переходы при клике по in-app'у предполагаются (например, переход по диплинку) нужно самостоятельно реализовать их в методе onInAppClick. Sdk только передает поля url и payload, заполняемые для in-app'ов в административной панели.

Пример обработки клика в InApp c открытием URL в браузере по умолчанию:

```
Mindbox.registerInAppCallback(object : InAppCallback {
    override fun onInAppClick(
        id: String,
        redirectUrl: String,
        payload: String
    ) {
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(redirectUrl))
        if (intent.resolveActivity(requireActivity().packageManager) != null) {
            startActivity(intent)
        }
    }

    override fun onInAppDismissed(id: String) {
    }
})
```

# Flutter

1. [Добавление SDK в приложение](add-sdk-flutter.md)
2. [Инициализация SDK](flutter-sdk-initialization.md)

## Настройка навигации

## Версия SDK 2.8.0 и выше

[Пример использование метода](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/main.dart#L24)

По умолчанию реализовано следующее поведение, при клике на in-app:

- если в настройках In-App’а указана ссылка перехода, осуществляется переход по ссылке, либо диплинку
- если в настройках In-App’а в поле payload указан текст (не JSON или XML), то содержимое копируется в буфер обмена
- если в настройках ничего не указано, in-app продолжает отображаться, пока пользователь его не закроет

Инициализируйте SDK и обработка кликов по In-app будет работать.

### Важное замечание

В случае, если вам не подходит реализация по умолчанию, вам нужно вызвать метод Mindbox.instance.registerInAppCallback({required `List` callbacks}) после инициализации SDK и передать туда нужный вам коллбэк.

### UrlInAppCallback

Используя этот коллбэк, у вас будет работать открытие URL

---

### CopyPayloadInAppCallback

Если конформиться от этого протокола, то по умолчанию у вас будет копироваться Payload

---

### EmptyInAppCallback

Если вы не хотите, чтобы клики по In-app как-либо обрабатывались, то вам нужно использвать этот коллбэк

---

### CustomInAppCallback

Если вам не подходит ни один из предыдущих вариантов, то вы можете реализовать свой коллбэк, используя этот интерфейс

```
Mindbox.instance.registerInAppCallback(callbacks: [
          CustomInAppCallback(
            (id, redirectUrl, payload) => {
              /* your custom click handling logic */
            },
            (id) => {
              /* your custom dismiss handling logic */
            },
          )
        ]);
```

## Версия SDK 2.6.3 и ниже

В данных версиях SDK настройка навигации по умолчанию не реализована. Следующие методы нужно определить после инициализации sdk:  
`Mindbox.instance.onInAppClickRecieved((id, redirectUrl, payload) { });` - для обработки нажатия по in-app  
`Mindbox.instance.onInAppDismissed((id) { });` - для обработки закрытия in-app

### Для проверки отображения in-app:

1. Создайте [пересчитываемый](https://help.mindbox.ru/docs/segment-client-filter-recalculate) или [статический](https://help.mindbox.ru/docs/segment-client-static) сегмент с клиентами, которые должны увидеть in-app
2. Создайте in-app по [инструкции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-in-app)
3. Запустите in-app
4. Через 1-2 минуты in-app отобразится в устройстве клиентов из сегмента. Обратите внимание, что если вы запускаете in-app без таргетинга по операции, то он будет показан при старте мобильного приложения. Поэтому приложение перед запуском должно быть выгружено из памяти
5. Действие показа и клика по in-app'у можно увидеть в админке в карточке клиента

# React Native

## Версия SDK [2.8.2](https://github.com/mindbox-cloud/react-native-sdk/releases/tag/v2.8.2) и выше

[Пример использование метода](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/src/utils/InAppCallbacks.tsx)

По умолчанию реализовано следующее поведение, при клике на in-app:

- если в настройках In-App’а указана ссылка перехода, осуществляется переход по ссылке, либо диплинку.
- если в настройках In-App’а в поле payload указан текст (не JSON или XML), то содержимое копируется в буфер обмена
- если в настройках ничего не указано, in-app продолжает отображаться, пока пользователь его не закроет

Инициализируйте SDK и обработка кликов по In-app будет работать.

### Важное замечание

В случае, если вам не подходит реализация по умолчанию, вам нужно вызвать метод MindboxSdk.registerInAppCallbacks(callbacks: `Array`) после инициализации SDK и передать туда нужный вам коллбэк.

### UrlInAppCallback

Используя этот коллбэк, у вас будет работать открытие URL в браузере и открытие диплинков.

---

### CopyPayloadInAppCallback

Используя этот коллбэк у вас будет копироваться Payload.

---

### EmptyInAppCallback

Если вы не хотите, чтобы клики по In-app как-либо обрабатывались, то вам нужно использвать этот коллбэк

---

### InAppCallback

Если вам не подходит ни один из предыдущих вариантов, то вы можете реализовать свой коллбэк, используя этот интерфейс

```
export interface InAppCallback {

  getName(): string

  onInAppClick(id: string, redirectUrl: string, payload: string): void

  onInAppDismissed(id: string): void

}
```
