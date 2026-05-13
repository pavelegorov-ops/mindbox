---
title: Получение ключей и настройка подключения к APNS
slug: "apns-keys-setup"
source_url: "https://developers.mindbox.ru/docs/apns-keys-setup"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:cb4017a255ce5ae1526baa20e3569fd09f29e59ad5d7ccd1111f9fbe1d200f9c"
---

# Получение ключей и настройка подключения к APNS

### Убедитесь, что эти шаги выполнены успешно:

[Настройка точек интеграции для iOS приложения](add-ios-integration.md)

### Результат шага «Получение ключей для iOS-приложения и настройка подключения к APNs»:

- Получены креды для мобильного приложения;
- Внесены данные в форму «Настройки подключения к сервису Apple Push Notification (APNs)» для нужной точки интеграции.

---

При подключении мобильных push-уведомлений для iOS-приложения нужна связка из четырёх ключей:

- Bundle ID
- Team ID
- Key ID
- Token (файл с разрешением `.p8`)

Получить их можно через свой [Apple Developer Account](https://developer.apple.com/) или в настройках текущего провайдера push-уведомлений.

## 1. Создание APNS Key

Чтобы получить ключ надо сделать следующее:

1. Откройте [консоль разработчика Apple](https://developer.apple.com/account/).
2. Перейдите в **Certificates, Identifiers & Profiles → Keys**
3. Нажмите на знак плюса (+).
4. Укажите название ключа и поставьте галочку напротив «Apple Push Notifications Service (APNS)». Если нужно, можно поставить и другие галочки, для push-уведомлений они не нужны.
5. Заполните настройки интеграции.

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/f0807e7-Screenshot_2022-02-15_at_16.48.41.png)

Раздел «Certificates, Identifiers & Profiles»

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/3b752bf-Screenshot_2022-02-15_at_16.50.50.png)

Подраздел «Keys» и кнопка добавления нового ключа

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a7db954-Screenshot_2022-02-15_at_16.58.22.png)

Настройка нового сертификата

В результате вы получите:

- 10-символьную строку с идентификатором ключа: *Key Id*,
- аутентификационный токен (*Token*) в виде текстового файла (с расширением .p8).

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/f0a2b43-Screenshot_2022-02-15_at_17.00.08.png)

Кнопка скачивания свежего сертификата

### Сохраните токен в надежном месте

Сайт Apple предоставляет токен для скачивания **только один раз**. Если вы не сохранили его при первоначальной генерации и не можете скопировать из другого push-провайдера, **потребуется сгенерировать новый токен**.

### Что делать, если при создании токена нельзя поставить галочку напротив APNS?

## 2. Bundle ID и Team ID

Далее нужно получить **Bundle ID** и **Team ID**.

1. Вернитесь на [страницу разработчика Apple](https://developer.apple.com/account/).
2. Перейдите в раздел «**Certificates, Identifiers & Profiles**».
3. Перейдите в подраздел «**Identifiers**».
4. Найдите строку с названием своего приложения и откройте его.
5. Скопируйте значения «**App ID Prefix**» и «**Bundle ID**» из правой колонки и заполните настройки интеграции.

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1b0fa67-Screenshot_2022-02-15_at_17.06.43.png)

Подраздел идентификаторов

![webpush-page-3.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d6f3d98-Screenshot_2022-02-15_at_17.07.52.png)

Bundle Id и Team Id

![]()

## 3. Настройки интеграции

Вставьте связку ключей в соответствующие поля для точки интеграции, которая была добавлена и настроена на шаге [«Настройка точек интеграции для iOS приложения»](add-ios-integration.md).

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9c1eaa3-__2022-06-29__20.20.47.png)
