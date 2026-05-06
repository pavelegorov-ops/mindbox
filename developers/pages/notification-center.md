---
title: Центр уведомлений
slug: "notification-center"
source_url: "https://developers.mindbox.ru/docs/notification-center"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:510afb03896db115c58ad3857ad3f48b445807065574accdef0556df6c16ff7f"
deprecation_hint:
  - не используется
---

# Центр уведомлений

**Центр уведомлений (ЦУ)** позволяет пользователям мобильного приложения просматривать отправленные им ранее мобильные пуши.

Для реализации ЦУ приложение должно быть интегрировано с SDK Mindbox

### В результате этой интеграции вы сможете:

- настроить сохранение и отображение пушей Mindbox в ЦУ;
- передавать данные об открытии ЦУ и пушей в нем в Mindbox для дальнейшей аналитики.

### Вывод промокодов

Если основная задача — вывод промокодов, ее можно решить запросом на [доступные для клиента промоакции](get-promotions-for-customer.md). Это позволит выводить актуальные на данный момент промокоды **без привязки к ранее полученным коммуникациям**. В таком случае сохранение пушей в ЦУ не понадобится.

## 1. Получить тело пуша из SDK

Этот шаг нужен для того, чтобы извлечь и обработать данные пушей, которые будут отображаться в ЦУ.

## Получить тело пуша в iOS

Чтобы пуши сохранялись в центр уведомлений и в активном, и в фоновом состоянии приложения, добавьте соответствующие методы из разделов ниже (в зависимости от версии SDK) в расширения `NotificationServiceExtension` и `NotificationContentExtension`.

### Пример JSON структуры пуш-уведомления с кнопкой и картинкой

```
{
  "clickUrl": "https://mindbox.ru/",
  "payload": "{\n  \"payload\": \"data\"\n}",
  "uniqueKey": "{ Значение Guid }",
  "imageUrl": "https://mobpush-images.mindbox.ru/Mpush-test/63/5933f4cd-47e3-4317-9237-bc5aad291aa9.png",
  "buttons": [
    {
      "url": "https://developers.mindbox.ru/docs/mindbox-sdk",
      "text": "Documentation",
      "uniqueKey": "{ Guid кнопки }"
    }
  ],
  "aps": {
    "mutable-content": 1,
    "alert": {
      "title": "Test title",
      "body": "Test description"
    },
    "content-available": 0,
    "sound": "default"
  }
}
```

### Версия SDK 2.11.0 и выше

В версии SDK 2.11.0 сделали доступными методы `isMindboxPush` и `getMindboxPushData` в таргетах `Mindbox` и `MindboxNotifications`. Методы можно использовать в `Notification Service Extension` или `Notification Content Extension`:

- `isMindboxPush` — возвращает `true`, если сообщение получено от Mindbox, и `false`, если нет.
- `getMindboxPushData` — возвращает модель `MBPushNotification`, в которой содержатся данные полученного пуша:

```
public struct MBPushNotification: Codable {
    public let aps: MBAps?
    public let clickUrl: String?
    public let imageUrl: String?
    public let payload: String?
    public let buttons: [MBPushNotificationButton]?
    public let uniqueKey: String?

    enum CodingKeys: String, CodingKey {
        case aps, clickUrl, imageUrl, payload, buttons, uniqueKey
    }
}
public struct MBAps: Codable {
    public let alert: MBApsAlert?
    public let sound: String?
    public let mutableContent: Int?
    public let contentAvailable: Int?

    enum CodingKeys: String, CodingKey {
        case alert, sound
        case mutableContent = "mutable-content"
        case contentAvailable = "content-available"
    }
}
public struct MBApsAlert: Codable {
    public let title: String?
    public let body: String?
}
public struct MBPushNotificationButton: Codable {
    public let text: String?
    public let url: String?
    public let uniqueKey: String?
}
```

Описание параметров:

- **uniqueKey** - уникальный идентификатор пуш-уведомления. Помогает определить, что уведомление пришло именно от Mindbox
- **clickUrl** - ссылка, на которую нужно перейти, если пользователь нажмет на пуш-уведомление
- **imageUrl** - ссылка на изображение, которое будет показано в пуш-уведомлении
- **payload** - дополнительная информация, переданная вместе с пуш-уведомлением
- **buttons** - кнопки, которые могут быть отображены в уведомлении. Каждая кнопка содержит:
  - **uniqueKey** - уникальный ключ кнопки пуша от Mindbox. Не используется
  - **text** - текст на кнопке
  - **url** - ссылку, на которую нужно перейти при нажатии на кнопку
- **aps**- блок данных, который содержит основную информацию, необходимую для отображения пуш-уведомления на устройстве пользователя
  - **alert** отвечает за текстовое содержимое пуш-уведомления. Включает в себя:
    - **title** - заголовок пуша
    - **body** - тело пуша

#### Пример использования методов в расширениях в `NotificationServiceExtension` или `NotificationContentExtension`

Вы можете использовать данные методы после импорта `MindboxNotifications` в расширениях `NotificationServiceExtension` или `NotificationContentExtension`.

#### NotificationServiceExtension

```
import UserNotifications
import MindboxNotifications

class NotificationService: UNNotificationServiceExtension {
    
    lazy var mindboxService: MindboxNotificationServiceProtocol = MindboxNotificationService()
    
    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
        let userInfo = request.content.userInfo
        
        if mindboxService.isMindboxPush(userInfo: userInfo), let mindboxPushNotification = mindboxService.getMindboxPushData(userInfo: userInfo) {
            // Do some code
        }
        
        mindboxService.didReceive(request, withContentHandler: contentHandler)
    }
    // ...
}
```

#### NotificationContentExtension

### Версии SDK ниже 2.11.0

Если вы используете версию SDK ниже 2.11.0, то для обработки push-уведомлений в расширениях `NotificationServiceExtension` или `NotificationContentExtension` используйте параметр `userInfo` из `UNNotificationRequest.UNNotificationContent`. Этот параметр содержит данные push-уведомления в виде словаря (dictionary), из которого можно извлекать нужные объекты по конкретным ключам.

Чтобы упростить чтение и обработку структуры данных пуш-уведомления, вы можете сериализовать `userInfo` в JSON-формат или работать с данными напрямую как со словарем типа `[String: Any]`. Полный список полей, которые могут содержаться в модели пуш-уведомления, можно найти [здесь](центр-уведомлений.md#пример-json-структуры-пуш-уведомления-с-кнопкой-и-картинкой).

Вы также можете самостоятельно реализовать в таргете `Notification Service Extension` структуру `MBPushNotification`, которая была описана ранее.

#### Словарь userInfo

```
import UserNotifications
import MindboxNotifications

class NotificationService: UNNotificationServiceExtension {
  
  lazy var mindboxService = MindboxNotificationService()
  
  override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
      
      let userInfo = request.content.userInfo
      
  			if let jsonData = try? JSONSerialization.data(withJSONObject: userInfo, options: .prettyPrinted), let jsonString = String(data: jsonData, encoding: .utf8) {
          print("Pretty printed JSON: \(jsonString)")
      }
      
      // Преобразование `userInfo` в словарь
      if let jsonDict = userInfo as? [String: Any] {
          
          // Извлекаем значения полей по ключам
          if let clickUrl = jsonDict["clickUrl"] as? String {
              print("Click URL: \(clickUrl)")
          }
          
          if let payload = jsonDict["payload"] as? String {
              print("Payload: \(payload)")
          }
          
          if let uniqueKey = jsonDict["uniqueKey"] as? String {
              print("Unique Key: \(uniqueKey)")
          }
          
          if let imageUrl = jsonDict["imageUrl"] as? String {
              print("Image URL: \(imageUrl)")
          }
          
          // Работа с массивом кнопок
          if let buttons = jsonDict["buttons"] as? [[String: Any]] {
              for button in buttons {
                  if let text = button["text"] as? String,
                     let url = button["url"] as? String,
                     let buttonUniqueKey = button["uniqueKey"] as? String {
                      print("Button text: \(text), URL: \(url), Unique Key: \(buttonUniqueKey)")
                  }
              }
          }
          
          // Работа с вложенным объектом aps
          if let aps = jsonDict["aps"] as? [String: Any] {
              if let alert = aps["alert"] as? [String: Any] {
                  if let title = alert["title"] as? String,
                     let body = alert["body"] as? String {
                      print("Alert title: \(title), body: \(body)")
                  }
              }
              
              if let sound = aps["sound"] as? String {
                  print("Sound: \(sound)")
              }
              
              if let mutableContent = aps["mutable-content"] as? Int {
                  print("Mutable Content: \(mutableContent)")
              }
              
              if let contentAvailable = aps["content-available"] as? Int {
                  print("Content Available: \(contentAvailable)")
              }
          }
      }
      
      mindboxService.didReceive(request, withContentHandler: contentHandler)
  }
// Other code...
}
```

#### Своя структура PushNotification

## Получить тело пуша в Android

В приложении используются сервисы уведомлений, наследуемые от `FirebaseMessagingService` и `HmsMessageService`. Метод `onMessageReceived` в этих сервисах обрабатывает все входящие пуш-уведомления, включая уведомления от Mindbox, и позволяет отслеживать получение пушей как в активном режиме (когда приложение открыто), так и в фоновом режиме (когда приложение свернуто или закрыто).

### Версия SDK 2.8.4 и выше

В версии SDK 2.8.4 были добавлены два новых метода у объектов `MindboxFirebase` и `MindboxHuawei`:

- `isMindboxPush` - возвращает `true`, если сообщение получено от Mindbox, и `false`, если нет
- `convertToMindboxRemoteMessage` - возвращает объект `MindboxRemoteMessage`, в котором содержатся данные полученного пуша:

```
data class MindboxRemoteMessage(
    val uniqueKey: String,
    val title: String,
    val description: String,
    val pushActions: List<PushAction>,
    val pushLink: String?,
    val imageUrl: String?,
    val payload: String?,
)
data class PushAction(
    @SerializedName("uniqueKey") val uniqueKey: String?,
    @SerializedName("text") val text: String?,
    @SerializedName("url") val url: String?,
)
```

Описание параметров:

- **uniqueKey** - уникальный идентификатор пуш-уведомления. Помогает определить, что уведомление пришло именно от Mindbox
- **title** - заголовок пуша
- **description** - тело пуша
- **pushLink** - ссылка, на которую нужно перейти, если пользователь нажмет на пуш-уведомление
- **imageUrl** - ссылка на изображение, которое будет показано в пуш-уведомлении
- **payload** - дополнительная информация, переданная вместе с пуш-уведомлением
- **pushActions** - кнопки, которые могут быть отображены в уведомлении. Каждая кнопка содержит:
  - **uniqueKey** - уникальный ключ кнопки пуша от Mindbox. Не используется
  - **text** - текст на кнопке
  - **url** - ссылку, на которую нужно перейти при нажатии на кнопку

**Пример структуры пуш-уведомления с кнопкой и картинкой при использовании функции`convertToMindboxRemoteMessage`**

```
{
  "description": "Test description",
  "imageUrl": "https://mobpush-images.mindbox.ru/Mpush-test/63/5933f4cd-47e3-4317-9237-bc5aad291aa9.png",
  "payload": "{\n  \"payload\": \"data\"\n}",
  "pushActions": [
    {
      "text": "Documentation",
      "uniqueKey": "{ Значение Guid }",
      "url": "https://developers.mindbox.ru/docs/mindbox-sdk"
    }
  ],
  "pushLink": "https://mindbox.ru/",
  "title": "Test title",
  "uniqueKey": "{ Значение Guid }"
}
```

**Пример вызова методов**

```
class FcmMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)
         /*
            Ранее используемый код
         */
        val isMindboxPush = MindboxFirebase.isMindboxPush(remoteMessage)
        Log.d("Mindbox","Current push notification with id ${remoteMessage.messageId} belongs to mindbox = $isMindboxPush")
        if (isMindboxPush) {
            val message = MindboxFirebase.convertToMindboxRemoteMessage(remoteMessage)
            Log.d("Mindbox","Successfully converted message to $message")
        }
    }
}
```

```
class HmsMessagingService : HmsMessageService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)
         /*
            Ранее используемый код
         */
        val isMindboxPush = MindboxHuawei.isMindboxPush(remoteMessage)
        Log.d("Mindbox","Current push notification with id ${remoteMessage.messageId} belongs to mindbox = $isMindboxPush")
        if (isMindboxPush) {
            val message = MindboxHuawei.convertToMindboxRemoteMessage(remoteMessage)
            Log.d("Mindbox","Successfully converted message to $message")
        }
    }
}
```

### Версии SDK ниже 2.8.4

Для обработки пуш-уведомлений от Mindbox в версиях SDK ниже 2.8.4, данные уведомлений извлекаются из параметра `remoteMessage: RemoteMessage` и преобразуются в модели следующим образом:

- для Firebase — из массива [remoteMessage.data](https://github.com/mindbox-cloud/android-sdk/blob/c9959cafad5435274758de6d3cf7322a40a156e8/mindbox-firebase/src/main/java/cloud/mindbox/mindbox_firebase/FirebaseRemoteMessageTransformer.kt#L27)
- для Huawei — из JSON [remoteMessage.data](https://github.com/mindbox-cloud/android-sdk/blob/c9959cafad5435274758de6d3cf7322a40a156e8/mindbox-huawei/src/main/java/cloud/mindbox/mindbox_huawei/HuaweiRemoteMessageTransformer.kt#L13)

```
data class RemoteMessage(
    @SerializedName("uniqueKey") val uniqueKey: String,
    @SerializedName("title") val title: String,
    @SerializedName("message") val description: String,
    @SerializedName("buttons") val pushActions: List<PushAction>,
    @SerializedName("clickUrl") val pushLink: String?,
    @SerializedName("imageUrl") val imageUrl: String?,
    @SerializedName("payload")  val payload: String?
)

data class PushAction(
    @SerializedName("uniqueKey") val uniqueKey: String?,
    @SerializedName("text") val text: String?,
    @SerializedName("url") val url: String?
)
```

Описание параметров:

- **uniqueKey** - уникальный идентификатор пуш-уведомления. Помогает определить, что уведомление пришло именно от Mindbox
- **title** - заголовок пуша
- **message** - тело пуша
- **clickUrl** - ссылка, на которую нужно перейти, если пользователь нажмет на пуш-уведомление
- **imageUrl** - ссылка на изображение, которое будет показано в пуш-уведомлении
- **payload** - дополнительная информация, переданная вместе с пуш-уведомлением
- **buttons** - кнопки, которые могут быть отображены в уведомлении. Каждая кнопка содержит:
  - **uniqueKey** - уникальный ключ кнопки пуша от Mindbox. Не используется
  - **text** - текст на кнопке
  - **url** - ссылку, на которую нужно перейти при нажатии на кнопку

**Пример структуры пуш-уведомления с кнопками и картинкой при получении данных из`remoteMessage`**

```
{
  "data" : {
      "title" : "Привет, это push! 😄😄",
      "message" : "Тестовый текст пуша, смотри, я помещаюсь нормально?\nТут проверка в бэкграунд режиме"
			"clickUrl":"https:\/\/glvrd.ru\/",
      "imageUrl":"https:\/\/mobpush-images.mindbox.ru\/Mpush-test\/223\/59c92f76-c417-4cf5-a468-af49d8296c49.gif",
      "payload":"",
      "buttons":[
            {
                "url" : "https:\/\/pushok.mindbox.ru\/?b=1&k=2",
					      "text" : "Кнопка 1😡",
					      "uniqueKey" : "{ Guid кнопки }"
            },
            {
                "url" : "https:\/\/pushok.mindbox.ru\/?b=1&k=3",
					      "text" : "Кнопка 2😡",
					      "uniqueKey" : "{ Guid кнопки }"
            }
        ],
        "uniqueKey":"{ Guid сообщения }"
    }
}
```

## 2. Сохранить пуш

Полученное пуш-уведомление необходимо сохранить либо на бэкенде, либо непосредственно на устройстве пользователя.

### Сохранение пушей в кроссплатформенном приложении

В кроссплатформенном приложении на Flutter или React Native, при сохранении пуш-уведомлений на устройстве используйте нативные механизмы хранения для iOS и Android отдельно.

- [Android](https://github.com/mindbox-cloud/android-sdk/blob/3c83f9bdacb9af01ce98048738706752eef6a315/example/app/src/main/java/com/mindbox/example/MindboxFirebaseMessagingService.kt#L46)
- [iOS](https://github.com/mindbox-cloud/ios-sdk/blob/develop/Example/MindboxNotificationServiceExtension/NotificationService.swift)
- React Native - [Android](https://github.com/mindbox-cloud/react-native-sdk/blob/1ba10bd765f88d1093f9be4d600ddb43c37dc1cf/example/exampleApp/android/app/src/main/java/com/exampleapp/MindboxFirebaseMessagingService.kt#L35-L39), [iOS](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/ios/MindboxNotificationServiceExtension/NotificationService.swift)
- Flutter - [Android](https://github.com/mindbox-cloud/flutter-sdk/blob/7d9ca60313ccd5d333d3c6a90ad0897112724728/example/flutter_example/android/app/src/main/kotlin/cloud/mindbox/flutter_example/MindboxFirebaseMessagingService.kt#L37-L41), [iOS](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/ios/MindboxNotificationServiceExtension/NotificationService.swift)

## 3. Отрисовать пуш в мобильном приложении

Выведите пуши в центре уведомления. В payload можно передавать любые признаки, которые будут влиять на отрисовку пуша. Например, признак даты актуальности пуша.

Рекомендуем отрисовать пуши только для авторизованных клиентов, так как есть вероятность вывести чужие пуши, если на устройстве логинилось несколько пользователей.

## 4. Передать события в Mindbox

Этот шаг не обязателен. Позволяет фиксировать в Mindbox факт открытия ЦУ и клики по пушам в нем в виде действий.

1. Настроить операции для выдачи действий.

- [Создать шаблоны действия](https://help.mindbox.ru/docs/template-create)

  - Для открытия ЦУ. Системное имя - `NotificationCentrOpen`:

  ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7c0091a-__2024-08-19__16.39.36.png)

  - Для открытия пуша из ЦУ. Системное имя - `NotificationCentrPushOpen`

  ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/3b040852fcc2095e387a60bdc671ac30c81f71c9420630468d767a8ef2be3345-__2024-09-16__17.54.39.png)
- [Создать дополнительные поля](https://help.mindbox.ru/docs/additional-data) или использовать уже имеющиеся, чтобы передавать в них данные по открытому пушу. Например:

  - Транслитерированное название пуша - по этому полю будем искать рассылку:
    - для сущности - действие клиента
    - системное имя - `MobPushTranslateName`
    - тип поля - строковый

  ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/471fb19-__2024-07-31__13.19.34.png)

  - Дата пуша:

    - для сущности - действие клиента
    - системное имя - `MobPushSendDateTime`
    - тип поля - Дата и время

    ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/8b2f660-__2024-07-31__14.14.42.png)
- [Создать операции](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F#%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v3)

  - Для открытия ЦУ. Системное имя - `mobileapp.NCOpen`

    ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/b8d48f8-__2024-07-31__13.40.35.png)
  - Для открытия пуша из ЦУ. Системное имя - `mobileapp.NCPushOpen`

    ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1cae6ad-__2024-07-31__13.45.18.png)

2. Реализовать обработку клика по пушу из ЦУ.
3. Разметить payload пуша, чтобы в дальнейшем передать в Mindbox информацию при его открытии из ЦУ. Например, для передачи названия и даты отправки пуша:

```
{
"pushName":"test name push open",
"pushDate":"test date push open"
}
```

4. Передать в Mindbox действие открытия ЦУ.

### Пример вызова метода для передачи открытия ЦУ

- [для нативного android](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/NotificationHistoryActivity.kt#L38-L42)
- [для нативного iOS](https://github.com/mindbox-cloud/ios-sdk/blob/9298ff42747ce437caf108205129090b9a8ce26b/Example/Example/ViewModels/NotificationCenterViewModel.swift#L62-L64)
- [для React Native](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/src/utils/MindboxOperations.tsx#L66-L75)
- [для Flutter](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view/main_page/main_page.dart#L67-L71)

При открытии ЦУ приложение отправляет запрос для выполнения операции, настроенной в пункте 1.3.

```
mindbox("async", {
    operation: "mobileapp.NCOpen",
    data: {
        // Сюда можно добавить другие необходимые данные, если они требуются
    }
});
```

Если вызов прошел успешно, то в карточке клиента появится действие “Открытие центра уведомлений”:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7981e95-__2024-07-31__14.05.47.png)

5. Передать в Mindbox действие открытия пуша из ЦУ.

### Пример вызова метода для передачи открытия пуша из ЦУ

- [для нативного android](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/NotificationHistoryActivity.kt#L48-L62)
- [для нативного iOS](https://github.com/mindbox-cloud/ios-sdk/blob/9298ff42747ce437caf108205129090b9a8ce26b/Example/Example/ViewModels/NotificationCenterViewModel.swift#L41-L56)
- [для React Native](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/src/utils/MindboxOperations.tsx#L78-L98)
- [для Flutter](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view/notification_center_page/notification_center_page.dart#L63-L70)

При открытии пуша в ЦУ приложение отправляет запрос для выполнения операции, настроенной в пункте 1.3.

В вызове передаем сохраненные значения из `push_name` и `push_date`.

```
mindbox("async", {
  operation: "mobileapp.NCPushOpen",
  data: {
  customerAction: {
    customFields: {
      mobPushSendDateTime: "<Дата отправки пуша>",
      mobPushTranslateName: "<Транслитированное название пуша>"
    }
  }
}
});
```

Если вызов прошел успешно, то в карточке клиента появится действие “Открытие пуша в центре уведомлений” с доп. полями:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1308aaf-__2024-07-31__14.02.10.png)

Как использовать данные об открытии ЦУ и пушей в нем для дальнейшей аналитики описали в [инструкции](https://help.mindbox.ru/docs/notification-center)
