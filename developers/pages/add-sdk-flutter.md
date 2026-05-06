---
title: Добавление SDK в приложение
slug: "add-sdk-flutter"
source_url: "https://developers.mindbox.ru/docs/add-sdk-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:3ae330fe0a3b3ba037210786e6ec2ea401c9ae3d526cdaeb6b2fa072470210d2"
---

# Добавление SDK в приложение

### Результат шага «Добавление SDK в приложение»:

- в навигаторе появился скрытый файл `.flutter-plugins`
- В нем есть строчки:
  - mindbox=…
  - mindbox_android=…
  - mindbox_ios=…

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/5a28dc5bf326220a571d9345a1b6e7cd365ba882cda71f865dc91bf3c6572d9c-__2025-11-17__20.38.46.png)

---

## Инструкция

В файл **`pubspec.yaml`** добавить зависимость на плагин.

Укажите последнюю версию SDK. Актуальную версию вы можете посмотреть на [странице библиотеки в pub.dev](https://pub.dev/packages/mindbox).

```
dependencies:
  flutter:
    sdk: flutter
mindbox: ^{последняя актуальная версия}
// mindbox: ^2.14.0
```

Чтобы установить фиксированную версию Mindbox SDK, требуется указать одинаковые версии всех зависимостей SDK без символа карет (^).

```
mindbox: 2.14.0
mindbox_android: 2.14.0
mindbox_ios: 2.14.0
mindbox_platform_interface: 2.14.0
```
