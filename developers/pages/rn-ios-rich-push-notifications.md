---
title: "iOS | Настройка Rich-push уведомлений"
slug: "rn-ios-rich-push-notifications"
source_url: "https://developers.mindbox.ru/docs/rn-ios-rich-push-notifications"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:50bc265b6a9d5e8ceb2d4be6681fc5673d38ba437fc7d222abbd6907d0b4d1ac"
---

# iOS | Настройка Rich-push уведомлений

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md#/)
- [Добавление SDK в приложение](add-sdk-react-native.md)
- [Инициализация SDK](sdk-initialization-react-native.md)
- [Отправка push-notifications](ios-send-push-notifications-react-native.md)

### Результат шага «Rich Push»:

- Мобильное push-уведомление должно отобразится с маленькой квадратной картинкой справа.
- Мобильное push-уведомление по длинному нажатию должно раскрыться и под ним нарисоваться картинка во всю ширину экрана и настроенные кнопки.

[Пример реализации](https://github.com/mindbox-cloud/flutter-sdk/tree/develop/example/flutter_example/ios)

**Rich-push** — это push-уведомления, в которых помимо заголовка и текста (как в обычных push-уведомлениях) можно разместить картинку со ссылкой и до 3 кнопок со ссылками.

### На страницах расписаны 2 основных шага по настройке rich push-уведомлений:

**Первый шаг** - "[Отображение превью картинки](ios-rich-push-image-preview-react-native.md#/)"

  

В процессе выполнения этого шага в проект будет добавлен Notification**Service**Extension. В результате можно будет увидеть маленькую картинку (превью) в push-уведомлении.

  

**Второй шаг** - "[Отображение картинки и кнопок при раскрытии push-уведомления](ios-rich-push-image-and-button-react-native.md#/)"

  

На этом шаге в проект будет добавлен Notification**Content**Extension. После выполнения этого шага можно будет увидеть картинку во всю ширину экрана и кнопки при раскрытии push-уведомления путем длинного нажатия.
