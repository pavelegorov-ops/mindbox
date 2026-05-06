---
title: Добавление SDK в приложение
slug: "add-sdk-to-app"
source_url: "https://developers.mindbox.ru/docs/add-sdk-to-app"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:17d0e7c8c81138ea2412a93f1caf7f9fe4681939bf8c76fe083bc0a3d9910974"
---

# Добавление SDK в приложение

Поддерживаются 2 варианта добавления SDK в приложение:

#### Swift Package Manager

### Результат:

В Package Dependencies появляется пакет **Mindbox** .

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c55fed9-Untitled_9.png)

---

**Инструкция:**

1. Откройте ваш проект в Xcode
2. Перейдите в `File → Add Package`
3. Вставьте URL репозитория Mindbox SDK:
   <https://github.com/mindbox-cloud/ios-sdk>
4. Выберите версию SDK
5. Выберите ваш `Main Target` и нажмите `Add Package`

#### Cocoapods
