---
title: Инициализация SDK
slug: "ios-sdk-initialization"
source_url: "https://developers.mindbox.ru/docs/ios-sdk-initialization"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:3aea6b957baefea225b307c752e181181ba9aea1aec6b8ddcfce8d39b7e3260a"
---

# Инициализация SDK

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для iOS приложения](add-ios-integration.md)
- [Добавление SDK в приложение](add-sdk-to-app.md#/)

### Результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок;
- В консоли разработчика в Xcode выведен **deviceUUID** SDK Mindbox;
- Дополнительно, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

## 1. Настройка AppGroup

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/eb50ebb-Untitled.png)

1. Откройте настройки проекта.
2. Выберите основной таргет.
3. Перейдите на вкладку `Signing & Capabilities`.
4. Нажмите на кнопку «добавить» и выберите `AppGroups`.
5. Добавьте новую группу с названием по шаблону `group.cloud.Mindbox.{bundle id приложения}`  
   Например, bundle id приложения - `Mindbox-Sample-App`, тогда значение App Group должно быть `group.cloud.Mindbox.Mindbox-Sample-App`.

### AppGroup должна быть собрана по шаблону:

group.cloud.Mindbox.{bundle id приложения}

Если допустить ошибку в шаблоне AppGroup в Main Target — приложение не соберется.

Фактическое значение лучше проверять через файл с расширением `.entitlements`.

SDK валидирует, что группа названа по шаблону. Если нарушить шаблон, SDK выбросит исключение.

## 2. Выбор варианта конфигурации SDK

Выберите вариант конфигурации СДК на основе требований от маркетинга.

### Важно:

Необходимо получить "<эндпоинт проекта>" от вашего менеджера проекта Mindbox, либо посмотреть его в [настройках точки интеграции](add-ios-integration.md). Обратите внимание, что «<эндпоинт проекта>» чувствителен к регистру, то есть имеет значение, используются ли заглавные или строчные буквы.

### Domain API Mindbox

Это домен, по которому будет происходить обращение в API Mindbox.

Чтобы получить нужный домен для вашего проекта, сделайте следующее:

  

1. Перейдите на сайт проекта  
2. Перейдите в список операций через "Кампании" → "Список кампаний" → "Операции"   
3. Откройте любую операцию  
4. Нажмите «Посмотреть описание»  
5. Скопируйте домен из URL в спецификации

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/85d049ea13949fccd34fc1175669e8ec538a31f20e730b7fd98015040d117195-image.png)

  

---

**1. Хочу передавать в mindbox анонимных пользователей и отправлять им пуши**

```
let mindboxSdkConfig = try MBConfiguration(
	endpoint: "<ендпоинт проекта>",
  domain: "",
  subscribeCustomerIfCreated: true,
  shouldCreateCustomer: true)
```

**2. Хочу передавать в mindbox анонимных пользователей без возможности отправлять им пуши**

```
let mindboxSdkConfig = try MBConfiguration(
  endpoint: "<ендпоинт проекта>",
  domain: "",
  subscribeCustomerIfCreated: false,
  shouldCreateCustomer: true)
```

**3. Не хочу передавать в mindbox анонимных пользователей**

```
let mindboxSdkConfig = try MBConfiguration(
  endpoint: "<ендпоинт проекта>",
  domain: "",
  shouldCreateCustomer: false)
```

## 3. Инициализация SDK

### 3.1 Инициализация SDK без использования запроса на IDFA

Инициализацию следует проводить синхронно, **в главном потоке** .

Первую инициализацию **желательно** проводить **ПОСЛЕ** запроса разрешения на отслеживание действий пользователя по IDFA при помощи *App Tracking Transparency APIs* от Apple (iOS 14+).

Если этого не сделать, то при каждой установке приложения будет использоваться IDFV или генерироваться новый deviceUUID.

**Если вы используете только SwiftUI и у вас нет файла AppDelegate, то его можно создать.**

Данный способ инициализации не учитывает запрос на разрешение использования IDFA, поэтому как идентификатор пользователя будет использоваться IDFV или сгенерированный случайно UUID.

В методе `didFinishLaunchingWithOptions` инициализируйте библиотеку и используйте вариант конфигурации, выбранный на этапе 2.

```
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
    super.application(application, didFinishLaunchingWithOptions: launchOptions)

    // Добавьте сюда выбранную конфигурацию с предыдущего шага.
    Mindbox.shared.initialization(configuration: mindboxSdkConfig)

    // Другая логика

    return true
}
```

Чтобы проверить корректность инициализации, добавьте вывод deviceUUID в консоль в любом удобном месте.

### Как можно проверить?

### 3.2 Инициализация SDK c использованием IDFA запроса

Если хотите использовать IDFA как идентификатор пользователя в Mindbox, то первую инициализацию нужно провести после запроса разрешения на отслеживание действий пользователя по IDFA при помощи *App Tracking Transparency APIs*.

В методе `initializeMindbox` используйте вариант конфигурации, выбранный на этапе 2.  
Если используете жизненный цикл `UISceneDelegate` вместо `UIApplicationDelegate`, показанному в примере ниже, то используйте соответствующий выбранному жизненному циклу метод.

```
import UIKit
import Mindbox
import AppTrackingTransparency

// This is only one use case. It is necessary to adapt the approach to your specific use case.

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    // ...
        
    if ATTrackingManager.trackingAuthorizationStatus != .notDetermined {
      initializeMindbox()
    }
    
    // ...
    return true
    }
    
  // If you're using scenes (iOS 13.0+), UIKit will not call this method. Use `sceneDidBecomeActive(_:)` instead.
  func applicationDidBecomeActive(_ application: UIApplication) {
    if ATTrackingManager.trackingAuthorizationStatus == .notDetermined {
      DispatchQueue.main.async {
        ATTrackingManager.requestTrackingAuthorization { status in
          self.initializeMindbox()
        }
      }
    }
  }
    
  func initializeMindbox() {
    do {
      // ВСТАВЬТЕ СЮДА ВЫБРАННУЮ НА ЭТАПЕ 2 КОНФИГУРАЦИЮ SDK 
      Mindbox.shared.initialization(configuration: mindboxSdkConfig)
    } catch {
      print(error.localizedDescription)
    }
  }
  // ...
}
```

### Проверьте результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок;
- В консоли разработчика в XCode выведен **deviceUUID** SDK mindbox;
- Дополнительно, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

## Если вам нужно изменить endpoint

Если ваше приложение используется в нескольких странах, а точное местоположение клиента становится известно только после запуска приложения, может потребоваться смена endpoint для корректной передачи информации о стране. Для этого нужно повторно вызвать `Mindbox.shared.initialization` и указать в конфигурации новый `endpoint`
