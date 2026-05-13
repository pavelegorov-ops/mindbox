---
title: Переход с V1 на V2 Android SDK
slug: "v1-v2-android-sdk"
source_url: "https://developers.mindbox.ru/docs/v1-v2-android-sdk"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c4ac467584b6527481db2e70881641dadb7eb545dda0cea10004a4f625c372c8"
---

# Переход с V1 на V2 Android SDK

В Mindbox SDK версии 2.0 мы разделили код на 3 пакета и изменили несколько методов API нескольких методов.

# Состав пакетов Mindbox SDK

- mobile-sdk: базовый функционал
- mindbox-firebase: пакет для работы с Firebase
- mindbox-huawei: пакет для работы с Huawei

Обновленные инструкции по интеграции

- [Настройка пуш уведомлений через Firebase](firebase-send-push-notifications.md)
- [Настройка пуш уведомлений через Huawei](huawei-send-push-notifications.md)

# mindbox.init

Было: `Mindbox.init(applicationContext, configuration)`  
Стало: `Mindbox.init(applicationContext, configuration, listOf(<список сервисов для работы с пуш-уведомлениями>))`

Возможные варианты:

- Без мобильных пушей: `Mindbox.init(applicationContext, configuration, listOf())`
- Только Firebase: `Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase))`
- Только Huawei: `Mindbox.init(applicationContext, configuration, listOf(MindboxHuawei))`
- Оба сервиса. Первый в списке считается приоритетным, если на телефоне пользователя доступна оба сервиса: `Mindbox.init(applicationContext, configuration, listOf(MindboxFirebase, MindboxHuawei))`

# updateFmsToken

Метод переименован в `updatePushToken`  
Было: `Mindbox.updateFmsToken(applicationContext, token)`  
Стало: `Mindbox.updatePushToken(applicationContext, token)`

# subscribeFmsToken

Метод переименован в `subscribePushToken`  
Было: `Mindbox.subscribeFmsToken {token -> print(token)}`  
Стало: `Mindbox.subscribePushToken {token -> print(token)}`

# getFmsTokenSaveDate

Метод переименован в `getPushTokenSaveDate`  
Было: `Mindbox.getFmsTokenSaveDate()`  
Стало: `Mindbox.getPushTokenSaveDate()`

# disposeFmsTokenSubscription

Метод переименован в `disposePushTokenSubscription`  
Было: `Mindbox.disposeFmsTokenSubscription(subscriptionId: String)`  
Стало: `Mindbox.disposePushTokenSubscription(subscriptionId: String)`
