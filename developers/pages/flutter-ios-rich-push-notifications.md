---
title: "iOS | Настройка Rich-push уведомлений"
slug: "flutter-ios-rich-push-notifications"
source_url: "https://developers.mindbox.ru/docs/flutter-ios-rich-push-notifications"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7bb2a77d64867401d0bfbfe9a888d75c9c562a77cee7bf9a6fc7f0d4161b36f8"
---

# iOS | Настройка Rich-push уведомлений

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для iOS приложения](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)
- [Отправка push-notifications](ios-send-push-notifications-flutter.md)

### Результат шага «Rich Push»:

- Мобильное push-уведомление должно отобразится с маленькой квадратной картинкой справа.
- Мобильное push-уведомление по длинному нажатию должно раскрыться и под ним нарисоваться картинка во всю ширину экрана и настроенные кнопки.

[Пример реализации](https://github.com/mindbox-cloud/flutter-sdk/tree/develop/example/flutter_example/ios)

**Rich-push** — это push-уведомления, в которых помимо заголовка и текста (как в обычных push-уведомлениях) можно разместить картинку со ссылкой и до 3 кнопок со ссылками.

### На страницах расписаны 2 основных шага по настройке rich push-уведомлений:

**Первый шаг** - "[Отображение превью картинки](rich-push-notifications-preview.md#/)"

  

В процессе выполнения этого шага в проект будет добавлен Notification**Service**Extension. В результате можно будет увидеть маленькую картинку (превью) в push-уведомлении.

  

**Второй шаг** - "[Отображение картинки и кнопок при раскрытии push-уведомления](rich-push-notifications-buttons.md#/)"

  

На этом шаге в проект будет добавлен Notification**Content**Extension. После выполнения этого шага можно будет увидеть картинку во всю ширину экрана и кнопки при раскрытии push-уведомления путем длинного нажатия.
