---
title: 2. Инициализация SDK
slug: "android-sdk-initialization"
source_url: "https://developers.mindbox.ru/docs/android-sdk-initialization"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0d23f1d1085de86b0fd0adaa7967834e898b25d6b94d4fc7f56a4d3c52d3fe7b"
deprecation_hint:
  - устаревш
---

# 2. Инициализация SDK

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Добавление SDK в приложение](add-android-sdk.md)

### Результат шага «Инициализация SDK»:

- Приложение запустилось без ошибок;
- В консоли разработчика в Android Studio выведен **deviceUUID** SDK mindbox;
- Дополнительно, только если вы делаете интеграцию с созданием и подпиской анонимного пользователя в системе Mindbox — [создастся клиент Mindbox](sdk-subscribe-customer.md).

[Пример инициализации SDK](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/ExampleApplication.kt#L39)

## 1. Выбор варианта конфигурации SDK

Выберите вариант конфигурации SDK на основе требований от маркетинга.

Необходимо получить "Endpoint External ID" от вашего менеджера проекта Mindbox, либо посмотреть его в [настройках точки интеграции](add-android-integration.md). Обратите внимание, что «Endpoint External ID» чувствителен к регистру, то есть имеет значение, используются ли заглавные или строчные буквы.

### Domain API Mindbox

Это домен, по которому будет происходить обращение в API Mindbox.

Чтобы получить нужный домен для вашего проекта, сделайте следующее:

  

1. Перейдите на сайт проекта  
2. Перейдите в список операций через "Кампании" → "Список кампаний" → "Операции"   
3. Откройте любую операцию  
4. Нажмите «Посмотреть описание»  
5. Скопируйте домен из URL в спецификации

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/85d049ea13949fccd34fc1175669e8ec538a31f20e730b7fd98015040d117195-image.png)

Не передавайте в этом поле адрес административного раздела

### Хочу передавать в Mindbox анонимных пользователей и отправлять им push-уведомления

```
val configuration = MindboxConfiguration.Builder(
	applicationContext,
	"",
	"" )
	.shouldCreateCustomer(true)
	.subscribeCustomerIfCreated(true)
	.build()
```

### Хочу передавать в Mindbox анонимных пользователей без возможности отправлять им push-уведомления

```
val configuration = MindboxConfiguration.Builder(
	applicationContext,
	"",
	"<ендпоинт проекта>" )
	.shouldCreateCustomer(true)
	.subscribeCustomerIfCreated(false)
	.build()
```

### Не хочу передавать в Mindbox анонимных пользователей

```
val configuration = MindboxConfiguration.Builder(
	applicationContext,
	"",
	"<ендпоинт проекта>" )
	.shouldCreateCustomer(false)
	.build()
```

## 2. Инициализация SDK

Для корректной работы SDK не должна быть глобально отключена автоматическая инициализация компонентов. Обратите внимание, нет ли у вас в манифесте следующей записи:  
[Disable automatic initialization for all components](https://developer.android.com/topic/libraries/app-startup#disable-all)
Если у вас она отключена для всех компонентов, включите ее и отключите автоматическую инициализацию только для [отдельных компонентов](https://developer.android.com/topic/libraries/app-startup#disable-individua)

Асинхронная инициализация SDK может привести к некорректной работе.

Инициализировать SDK нужно синхронно в методе Application.onCreate, **используйте вариант конфигурации, выбранный на этапе «Выбор варианта конфигурации SDK»**.

Для инициализации передайте в метод `Mindbox.init` `application` вашего приложения.

```
import android.app.Application
import cloud.mindbox.mobile_sdk.*

class MyApp: Application() {
    override fun onCreate() {
        super.onCreate()
        // ВСТАВЬТЕ СЮДА ВЫБРАННУЮ НА ЭТАПЕ 1 КОНФИГУРАЦИЮ SDK                    
        Mindbox.init(application, configuration, listOf())

    }
}
```

### Если у вас single activity application и вы не можете инициализировать SDK в Application

Тогда можно инициализировать Mindbox SDK в вашей Activity, передав в `Mindbox.init` вашу Activity.

```
class MainActivity() : Activity() {
        override fun onCreate() {
            super.onCreate()
            // ВСТАВЬТЕ СЮДА ВЫБРАННУЮ НА ЭТАПЕ 1 КОНФИГУРАЦИЮ SDK  
            Mindbox.init(this@MainActivity, configuration, listOf())
        }
    }
```

### Если вы ранее уже инициализировали SDK

Вам нужно заменить устаревшую реализацию метода инициализации Mindbox.init(context, configuration, list), требующую передачу контекста, на одну из новых: требующую application, при инициализации внутри класса Application и требующую activity, при инициализации внутри класса Activity.

Чтобы проверить корректность инициализации, добавьте вывод deviceUUID в консоль в любом удобном месте.

Далее запустите приложение через Android Studio на реальном устройстве или эмулятор

```
package cloud.mindbox.checkguidandroid

import android.app.Application
import android.util.Log
import cloud.mindbox.mobile_sdk.*

class MyApp: Application() {
    override fun onCreate() {
        super.onCreate()

				...
        Mindbox.init(
           application = this,
           configuration = configuration,
           pushServices = listOf(MindboxFirebase, MindboxHuawei, MindboxRuStore)
        )
        Mindbox.subscribeDeviceUuid { uuid -> Log.i("MindboxDeviceUUID", uuid) }
    }
}
```

### Если вам нужно изменить endpoint

Если ваше приложение используется в нескольких странах, а точное местоположение клиента становится известно только после запуска приложения, может потребоваться смена endpoint для корректной передачи информации о стране. Для этого нужно повторно вызвать `Mindbox.init` и указать в конфигурации новый `endpoint`.

### Использование SDK при собственной инициализации WorkManager

[Документация](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration)  
Внутри Mindbox SDK для отправки ивентов используется WorkManager. Если в вашем проекте отключена автоматическая инициализация WorkManager и инициализируете его вручную, то добавьте:

```
Configuration.Builder().setWorkerFactory(
  DelegatingWorkerFactory().apply {
    // ваши фабрики
     addFactory(Mindbox.mindboxWorkerFactory)
  }
)
```
