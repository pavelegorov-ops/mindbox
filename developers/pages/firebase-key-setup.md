---
title: Получение Firebase ключей
slug: "firebase-key-setup"
source_url: "https://developers.mindbox.ru/docs/firebase-key-setup"
breadcrumb:
  - Мобильные приложения
  - Android SDK
  - Получение ключей провайдеров пушей
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:503318bd4419a444fd0ca6a289d16d99c17739086f955cd2bb5470056150f77a"
---

# Получение Firebase ключей

### Убедитесь, что эти шаги выполнены успешно:

[Настройка точек интеграции для Android приложения](add-android-integration.md)

### Результаты выполнения данного шага:

- Получены креды для мобильного приложения
- Внесены данные в форму "Настройка отправки мобильных push-уведомлений Android" для нужной точки интеграции

Для отправки push-уведомлений на Android-устройства нужен *Firebase**Server key*** и JSON файл с новым **Private key**.

## **1. Создайте проект в Firebase**

Для создания или перехода к существующему проекту вам нужно воспользоваться этой [ссылкой](https://console.firebase.google.com/).

Проект в Firebase нужен для отправки пушей на Android. Если вы впервые настраиваете проект в Firebase, то кликните на **Add project** и следуйте подсказкам, чтобы настроить проект.

Если вы уже ранее создавали проект, сразу переходите ко второму шагу.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/e6c2905-__2024-01-25__15.29.12.png)

  

## **2. Создайте JSON-файл с приватным ключом**

В настройках проекта перейдите на вкладку **Service accounts.** Можете воспользоваться [этой ссылкой](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk?hl=ru&_gl=1*16vau9g*_ga*MTA1NDQ0MDMwLjE2OTE2NDYwOTc.*_ga_CW55HF8NVT*MTcwNTY1MjMyMi4yNi4xLjE3MDU2NTI4NjEuNDEuMC4w) для быстрого перехода.

Подойдет ключ от сервисного аккаунта с любой ролью, у которой есть [право](https://cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.messages.create) `cloudmessaging.messages.create` — это не обязательно должна быть административная роль.

Нажмите **Generate new private key**  внизу страницы.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c4a4186-2e08289-fcm3.1.jpg)

Затем вы увидите окно предупреждения. Нажмите **Generate key**.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/feb0057-5ed0fe3-fcm4.1.jpg)

Сохраните файл JSON. Вам потребуется доступ к нему для загрузки в Mindbox.

## **3. Загрузите файл JSON в Mindbox**

На странице настроек интеграции с приложением Android в блоке для настроек отправки пушей должна быть включена отправка через Firebase.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/12506ee-__2024-05-30__10.48.21.png)

Выберете файл JSON, который сгенерировали и сохранили на прошлом шаге.

Если загрузка успешная, в таком случае блок вы увидите загруженные параметры интеграции.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c5c7909-__2024-05-30__10.43.41.png)

## Нажмите на "Сохранить" в блоке и в правом углу страницы.

Понадобится некоторое время, чтобы настройки интеграции обновились.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/98c2ece-__2024-01-25__15.12.51.png)

**Если файл загружен и настройки сохранены, тогда интеграция завершена.**

После перезагрузки страницы и открытия блока с настройками вы увидите все заполненные поля.
