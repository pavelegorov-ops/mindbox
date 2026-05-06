---
title: Настройка отправки пушей на сайт через Firebase
slug: "get-firebase-keys-for-web-push"
source_url: "https://developers.mindbox.ru/docs/get-firebase-keys-for-web-push"
breadcrumb:
  - Рассылки
  - Вебпуши
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:5c44f14d106d49a1163049ec0d81bd80f464fb59dd1223b6e05bcd987045e1dd"
---

# Настройка отправки пушей на сайт через Firebase

### Результат выполнения данного шага:

- Получены учетные данные из проекта Firebase (**Private key** проекта и **config** приложения).
- Данные внесены в настройки нужной интеграции Mindbox.

## 1. Создайте проект в Firebase

> Если проект уже создан, переходите ко второму шагу.

Проект в Firebase нужен для отправки пушей на сайт.

Для его создания перейдите по [ссылке](https://console.firebase.google.com), кликните на **Create a project** и следуйте подсказкам сервиса:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ef066e7-__2024-02-02__09.56.39.png)

## 2. Создайте JSON-файл с приватным ключом

В настройках **Project settings** перейдите на вкладку **Service accounts.**

Нажмите **Generate new private key**:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c4a4186-2e08289-fcm3.1.jpg)

Подтвердите действие — нажмите **Generate key**:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/feb0057-5ed0fe3-fcm4.1.jpg)

Сохраните JSON-файл. Он потребуется на дальнейших шагах для загрузки в Mindbox.

## 3. Создайте приложение в Firebase

### Учетные данные Firebase должны быть из одного и того же проекта

Приложение нужно создавать в том же проекте, где генерировался Private key

> Если приложение уже создано, переходите к следующему шагу.

В настройках **Project settings** перейдите на вкладку **General**.

Создайте приложение на платформе **Web**:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9a918e7-__2024-05-22__16.03.26.png)

Далее действуйте по инструкции Firebase.

## 4. Скопируйте конфигурацию созданного приложения

В настройках **Project settings** перейдите на вкладку **General**. Созданное приложение появится в разделе **Your apps** (Web apps).

Скопируйте его SDK конфигурацию (**SDK setup and configuration** → **Config**):

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/acfe6d3-__2024-05-22__16.08.52.png)

## 5. Загрузите параметры проекта и приложения Firebase в Mindbox

В Mindbox [создайте интеграцию](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8) типа Веб-сайт или выберете существующую, если она уже есть:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/22d67fc-__2024-04-04__22.29.45.png)

В разделе **Настройка отправки пушей на сайт**:

- **Интеграция приложения** — вставьте конфигурацию приложения, которую скопировали на шаге 5.
- **Интеграция проекта** — загрузите JSON-файл с приватным ключом, который был сгенерирован на шаге 3.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/0fb158d-__2024-05-24__12.33.19.png)

**Нажмите на "Сохранить" в блоке и в правом углу страницы**. Понадобится некоторое время, чтобы настройки интеграции обновились.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a4308c5-__2024-05-30__11.25.28.png)
