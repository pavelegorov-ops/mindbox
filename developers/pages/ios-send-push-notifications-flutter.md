---
title: "iOS | Настройка пуш-уведомлений"
slug: "ios-send-push-notifications-flutter"
source_url: "https://developers.mindbox.ru/docs/ios-send-push-notifications-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:e24f02d23bd00cfba8213369543f32cb1b519cd5149baa7b4daa1c3e0d2a31ad"
---

# iOS | Настройка пуш-уведомлений

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](flutter-new-integration-setup.md#/)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md)
- [Добавление SDK в приложение](add-sdk-flutter.md#/)
- [Инициализация SDK](flutter-sdk-initialization.md#/)

### Результат шага «Отправка push-notifications»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).

## 1. Добавить работу с push-уведомлениями в настройках приложения

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/51f0ee2-Untitled_5.png)

1. Откройте настройки проекта;
2. Выберите основной target;
3. Перейдите на вкладку `Signing & Capabilities`;
4. Нажмите на кнопку «добавить» и выберите `Push Notifications` и `Background modes`;
5. В разделе Background Modes поставьте 3 галки:
   - Background fetch;
   - Remote notifications;
   - Background processing.

Передайте менеджеру проекта ключи для подключения к [Apple Push Notification service](apns-keys-setup.md#/) или добавьте ключи самостоятельно.

---

## 2. Настройка AppDelegate

Выберите один из вариантов предоставленных ниже, и следуйте инструкциям.

[Базовая интеграция](ios-mindboxflutterappdelegate.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](flutter-ios-advanced-push-setup.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

---

### Проверьте результат шага «Отправка push-notifications на iOS»:

Push-уведомление отправляется из Mindbox и отображается на устройстве. Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md).

Если вы тестируете push-уведомления в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md#/)
