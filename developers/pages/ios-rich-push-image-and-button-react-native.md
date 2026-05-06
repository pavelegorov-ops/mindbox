---
title: Отображение картинки и кнопки
slug: "ios-rich-push-image-and-button-react-native"
source_url: "https://developers.mindbox.ru/docs/ios-rich-push-image-and-button-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
  - "iOS | Настройка Rich-push уведомлений"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8c8433eda520dd1e174accd8ab3316d41c00aa9c6fb237c2afedce5a18534810"
---

# Отображение картинки и кнопки

### Результат этапа «Отображение картинки и кнопок при раскрытии push-уведомления»:

Мобильное push-уведомление должно раскрыться путем длинного нажатия и под ним нарисоваться картинка во всю ширину экрана и настроенные кнопки.

Проверить, что картинка и кнопки отрисовались при длинном нажатии на push-уведомление, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-кнопки-отрисовались-при-клике-на-пуш).

## 1. Создание расширения

1. В Xcode выбрать `Select File > New > Target`
2. Выбрать `Notification Content Extension` и нажать `Next`.
3. Ввести `Product name` MindboxNotificationContentExtension и нажать Finish.
4. Нажать `Activate` на диалоговом окне Activate scheme.

![__2025-03-21__12.07.09](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7f677c7fec12351b65390f955c424567ec191862ecb63f9eb44f0ebf1c13a7cb-__2025-03-21__12.07.09.png)
![__2025-03-24__19.06.11](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/8a3b27913c715f278095b6818aa037be9534c7016a9c59370a8c52ae9714762a-__2025-03-24__19.06.11.png)

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
2. Выберите таргет `MindboxNotificationContentExtension`;
3. Перейдите на вкладку `Signing & Capabilities`;
4. Нажмите на кнопку «**добавить**» и выберите `AppGroups`;
5. Добавьте новую группу с названием по шаблону `group.cloud.Mindbox.{bundle id приложения}`;  
   Например, bundle id приложения — `Mindbox-Sample-App`, тогда значение App Group должно быть `group.cloud.Mindbox.Mindbox-Sample-App`.

![__2025-03-24__19.29.35](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/3580de63b6e87d65739a1a2b078176258ebc630b1b578c735e853a3804d4ea06-__2025-03-24__19.29.35.png)

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

#### Cocoapods

---

## 4. Реализация кода расширения в приложении

Для реализации надо сделать 2 шага:

- импортировать библиотеку в файл `NotificationViewController.swift` и вызвать там метод `MindboxNotificationService();`
- поправить настройки в файле `Info.plist`

```
import UserNotificationsUI
import MindboxNotifications

class NotificationViewController: UIViewController, UNNotificationContentExtension {

  lazy var mindboxService: MindboxNotificationContentProtocol = MindboxNotificationService()

  func didReceive(_ notification: UNNotification) {
    mindboxService.didReceive(notification: notification, viewController: self, extensionContext: extensionContext)
  }
}
```

### Настройка Info.plist

В файле `Info.plist` в `MindboxNotificationContent` нужно внести следующие изменения:

1. Удалить пункт `NSExtensionMainStoryboard`.
2. Добавить пункты:

| Пункт | Значение |
| --- | --- |
| `NSExtensionPrincipalClass` | Собирается по шаблону: `{название расширения}.{название контроллера}`  Если все сделано точно по инструкции, тогда должно быть такое значение: `MindboxNotificationContentExtension.NotificationViewController` |
| `UNNotificationExtensionCategory` | если используете простую реализацию Service Extension: `MindBoxCategoryIdentifier` |
| `UNNotificationExtensionInitialContentSizeRatio` | `0,0001` |

**Пример**:

![image.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/feaf0b2d70cb1879b40337a95521f8f933a91547c00228256ed39f4242d669db-image.png)

### Удаление MainInterface.storyboard

При создании расширения в папке создается файл с расширением .storyboard. Его необходимо удалить, потому что наш метод обработает UI самостоятельно.

Если вам не подходит способ реализации, описанный выше, предлагаем использовать продвинутый способ: для использования собственной верстки Rich Push нужно реализовать весь код самостоятельно.

Специальных рекомендаций тут нет, никакие дополнительные методы указывать не нужно.

---

[Проверьте](mobile-push-check.md#проверить-что-кнопки-отрисовались-при-клике-на-пуш), что картинка и кнопки отрисовались при клике на push-уведомление.

Дебаг стандартных ошибок — [здесь](sdk-integration-checklist.md).

### Проверка результата «Отображение превью картинки»

- Мобильное push-уведомление по длинному нажатию должно раскрыться и под ним нарисоваться картинка во всю ширину экрана и настроенные кнопки.

Если вы тестируете push-уведомления в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md#/)
