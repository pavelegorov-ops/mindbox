---
title: Отображение превью картинки
slug: "ios-rich-push-image-preview"
source_url: "https://developers.mindbox.ru/docs/ios-rich-push-image-preview"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
  - "iOS | Настройка Rich-push уведомлений"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6aa090ef7adfb67096c718ebd1c768ce240cf193f4607435417448f0218aba49"
---

# Отображение превью картинки

### Результат этапа «Отображение превью картинки»:

Push-уведомление должно отобразится с маленькой квадратной картинкой справа.

Проверить, что push-уведомления с картинкой отправляются корректно, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-с-картинкой-отправляется-корректно).

## 1. Создание расширения

1. В Xcode выбрать `Select File > New > Target`
2. Выбрать `Notification Service Extension` и нажать `Next`.
3. Ввести `Product name` **MindboxNotificationServiceExtension** и нажать Finish.
4. Нажать `Activate` на диалоговом окне Activate scheme.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7f677c7fec12351b65390f955c424567ec191862ecb63f9eb44f0ebf1c13a7cb-__2025-03-21__12.07.09.png)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/36d6441ac44c8ef38558e053c2e4ccc62ae027cbf04f3963d2098a7cfc0ba5a6-__2025-03-21__11.50.07.png)

---

## 2. Настройка расширения

### 2.1. iOS Deployment Target

Проверьте версии iOS Deployment Target. Версии iOS Deployment Target должны быть одинаковыми в:

- Main target,
- Service extension
- Content extension.

Их можно найти по пути `Your Project Name -> Targets -> Target Name -> General -> Minimum Deployments -> iOS`

### iOS Deployment Target очень важный пункт для правильной работы Service Extension и Content Extension

Важно следить за этим параметром, особенно после обновления на новую версию Xcode. Он может измениться автоматически, что приведет к неправильной работе Service Extension и Content Extension

  

### 2.2. App groups

1. Откройте настройки проекта;
2. Выберите таргет `MindboxNotificationServiceExtension`;
3. Перейдите на вкладку `Signing & Capabilities`;
4. Нажмите на кнопку «**добавить**» и выберите `AppGroups`;
5. Добавьте новую группу с названием по шаблону `group.cloud.Mindbox.{bundle id приложения}`;  
   Например, bundle id приложения — `Mindbox-Sample-App`, тогда значение App Group должно быть `group.cloud.Mindbox.Mindbox-Sample-App`.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/19983627d02e2575218443e5d9666cbca5f32884af0112d3351d084719ac89c2-__2025-03-21__12.07.54.png)

### Настройка App Group обязательная для работы Mindbox SDK

Если упустить этот шаг, то при получении push-уведомления расширение может упасть с ошибкой, которую будет очень тяжело отловить.

### 2.3. Подпись расширения

Нужно подписать расширение тем же сертификатом, что и основное приложение. Если у вас стоит автоматическая подпись — все подпишется само, если ручная — необходимо вручную создать сертификаты для таргетов и проставить в «Signing & Capabilities».

### 2.4. Проверка rich-push уведомлений, используя Xcode debug сборки.

Проверьте в разделе `Target -> Build Phases -> Embed App Extension` -> галочка с `Copy only when installing` должна быть убрана

Убирайте эту галочку ТОЛЬКО если вы собираетесь проверять Rich-Push Notifications используя Debug-сборки, собранные через Xcode напрямую.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/23159363c9021cef626fcadaaa91cb413cb63025ff89a02ed3bab720a0792e29-__2025-03-21__17.44.58.png)

  

---

## 3. Добавление SDK в проект

  

#### Swift Package Manager

1. В Xcode нажмите в верхнем меню “File” -> “Add Packages…”
2. В открывшемся окне добавьте ссылку на Mindbox SDK <https://github.com/mindbox-cloud/ios-sdk> и нажмите на «Add Package».
3. После загрузки пакета, необходимо указать таргеты:

- `MindboxNotificationsService` добавьте в ранее созданный `MindboxNotificationServiceExtension`
- `MindboxNotificationsContent` добавьте в ранее созданный `MindboxNotificationContentExtension`

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/bab3dcd6b70986bac52dcae9225daa65b16afd8fb7ce39f15351beb87150eff9-__2025-03-24__18.41.57.png)

#### CocoaPods

---

## 4. Настройка SDK в приложении

#### Быстрая настройка

Необходимо в основном файле расширения сделать следующие настройки:

- импортировать библиотеку MindboxNotifications;
- вызвать метод MindboxNotificationService();
- поставить в 2 местах вызовы методов didReceive и serviceExtensionTimeWillExpire.

  

```
import UserNotifications
import MindboxNotifications

class NotificationService: UNNotificationServiceExtension {

 lazy var mindboxService: MindboxNotificationServiceProtocol = MindboxNotificationService()

 override func didReceive(_ request: UNNotificationRequest,
                          withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
   mindboxService.didReceive(request, withContentHandler: contentHandler)
 }

 override func serviceExtensionTimeWillExpire() {
   mindboxService.serviceExtensionTimeWillExpire()
 } 
}
```

#### Самостоятельная настройка

---

### Проверка результата «Отображение превью картинки»

- Мобильное push-уведомление должно отобразится с маленькой квадратной картинкой справа.
- [Проверьте](mobile-push-check.md#проверить-что-мобильное-push-уведомление-с-картинкой-отправляется-корректно), что push-уведомление с картинкой отправляется корректно.

Если вы тестируете push-уведомления в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md#/)
