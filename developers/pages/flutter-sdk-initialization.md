---
title: Инициализация SDK
slug: "flutter-sdk-initialization"
source_url: "https://developers.mindbox.ru/docs/flutter-sdk-initialization"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:d3f1d2e9fe96ea4e4e5d457123f72556759539f75eb470daa995a6000d01bc93"
---

# Инициализация SDK

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](flutter-new-integration-setup.md#/)
- [Добавление SDK в приложение](add-sdk-flutter.md#/)

### Результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок на обеих платформах (iOS и Android);
- В консоли разработчика в Xcode выведен **deviceUUID** SDK Mindbox;
- *Дополнительно*, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

[Пример инициализации SDK](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/main.dart#L17)

---

## 1. Выбор варианта конфигурации SDK

Выберите вариант конфигурации SDK на основе требований от маркетинга.

Необходимо получить «<эндпоинт проекта>» от вашего менеджера проекта Mindbox, либо посмотреть его в [настройках точки интеграции](add-ios-integration.md). Обратите внимание, что ендпоинт проекта чувствителен к регистру, то есть имеет значение, используются ли заглавные или строчные буквы.

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

**1. Хочу передавать в Mindbox анонимных пользователей и отправлять им push-уведомления**

```
final config = Configuration(
        domain: '',
        endpointIos: '',
        endpointAndroid: '',
        shouldCreateCustomer: true,
        subscribeCustomerIfCreated: true
);
```

**2. Хочу передавать в mindbox анонимных пользователей без возможности отправлять им push-уведомления**

```
final config = Configuration(
        domain: '',
        endpointIos: '',
        endpointAndroid: '',
        shouldCreateCustomer: true,
        subscribeCustomerIfCreated: false
);
```

**3. Не хочу передавать в mindbox анонимных пользователей**

```
final config = Configuration(
        domain: '',
        endpointIos: '',
        endpointAndroid: '',

        shouldCreateCustomer: false
);
```

---

## 2. Инициализация SDK

### 2.1. Настройка Flutter-части проекта

Инициализировать SDK нужно синхронно в файле **`lib/main.dart`** в функции **`main`**.

Используйте вариант конфигурации, **выбранный на этапе 1**.

```
import 'package:flutter/material.dart';
import 'package:mindbox/mindbox.dart';

void main() {
  // ВСТАВЬТЕ СЮДА ВЫБРАННУЮ НА ЭТАПЕ 1 КОНФИГУРАЦИЮ SDK

  Mindbox.instance.init(configuration: config);
  runApp(const MyApp());
}
```

Чтобы проверить корректность инициализации, добавьте вывод deviceUUID в консоль в любом удобном месте.

### Как можно проверить?

На этом этапе вы уже можете **запустить приложение на Android**

---

### 2.2. Настройка iOS-части проекта

Для интеграции Mindbox SDK во Flutter-проект необходимо подключить нативный Mindbox iOS SDK и выполнить соответствующие настройки проекта.

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

---

**Запустите приложение на iOS и проверьте результаты выполнения этапа.**

### Проверьте результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок на обеих платформах (iOS и Android);
- В консоли разработчика в Xсode выведен **deviceUUID** SDK Mindbox;
- Дополнительно, только если вы делаете интеграцию **с созданием и подпиской анонимного пользователя** в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

---

## Изменение endpoint

Если приложение используется в нескольких странах и фактическое местоположение пользователя определяется только после запуска, может потребоваться динамическая смена endpoint для корректной передачи данных о стране.
Для обновления настроек повторно вызовите **`Mindbox.instance.init`** и передайте в конфигурации актуальные значения **`endpointAndroid`** и **`endpointIos`**.
