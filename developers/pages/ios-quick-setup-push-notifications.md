---
title: "Настройка push-уведомлений"
slug: "ios-quick-setup-push-notifications"
source_url: "https://developers.mindbox.ru/docs/ios-quick-setup-push-notifications"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:909f33b521b1d723a53fac899fd2edde362867941454a3ef0b201b74f5414f18"
---

# Настройка push-уведомлений

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для iOS приложения](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md)
- [Добавление SDK в приложение](add-sdk-to-app.md#/)
- [Инициализация SDK](ios-sdk-initialization.md#/)

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

## Настройка пуш уведомлений

Выберите один из вариантов предоставленных ниже, и следуйте инструкциям.

[Базовая интеграция](ios-push-notifications-setup.md)

Подходит, если не требуется кастомная логика.

[Продвинутая интеграция](ios-push-notifications-setup-advanced.md)

Подходит, если требуется кастомная логика для самостоятельной отрисовки push-уведомлений.

---

### Проверьте результат шага «Отправка push-notifications»:

Из Mindbox отправляется мобильное push-уведомление, и оно отображается на устройстве.

Проверить, что push-уведомления отправляются, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-мобильное-push-уведомление-отправляется).

Если вы тестируете push-уведомления в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md#/)
