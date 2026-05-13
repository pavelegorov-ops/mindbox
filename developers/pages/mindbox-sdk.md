---
title: Mindbox SDK
slug: "mindbox-sdk"
source_url: "https://developers.mindbox.ru/docs/mindbox-sdk"
breadcrumb:
  - Мобильные приложения
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:36f5dd9cae390e409523f2bde33c09d3aee9f5139cb625f49d6ea6db0e7ec8bf"
---

# Mindbox SDK

# Mindbox SDK

Это бесплатная библиотека для всех клиентов Mindbox. Код SDK размещен в открытых репозиториях.

## Возможности Mindbox SDK

| Поддерживается в SDK | Не поддерживается в SDK |
| --- | --- |
| - Интеграция мобильных push-уведомлений: мониторинг токенов и разрешения, отрисовка push-уведомлений. - Передача событий в API Mindbox. - Получение данных от API Mindbox. - [In-app в приложениях.](in-app.md) | - Интеграция программы лояльности. - Отображение виджетов товарных рекомендаций. |

Мы оказываем техническую поддержку для двух последних минорных версий SDK — на данный момент: 2.14.x и 2.15.x.

## Поддерживаемые платформы

[Android](android-sdk.md)

**Языки:** Java / Kotlin   
**Android API:** 21+   
**Устройства:** смартфоны Android любых версий

📚 [Документация](android-sdk.md)   
📦 [Пример](https://github.com/mindbox-cloud/android-sdk/tree/develop/example)   
💻 [GitHub](https://github.com/mindbox-cloud/android-sdk)   
📦 [Maven Central](https://central.sonatype.com/artifact/cloud.mindbox/mobile-sdk)

[iOS](ios-sdk.md)

**Языки:** Swift   
**iOS:** 12+   
**Устройства:** смартфоны iPhone любых версий

📚 [Документация](ios-sdk.md)   
📦 [Пример](https://github.com/mindbox-cloud/ios-sdk/tree/develop/Example)   
💻 [GitHub](https://github.com/mindbox-cloud/ios-sdk)   
📦 [SPM](https://swiftpackageindex.com/mindbox-cloud/ios-sdk)   
📦 [CocoaPods](https://cocoapods.org/pods/Mindbox)

[Flutter](flutter-sdk.md)

**Flutter:** 2+   
**Языки:** Dart

📚 [Документация](flutter-sdk.md)   
📦 [Пример](https://github.com/mindbox-cloud/flutter-sdk/tree/develop/example/flutter_example)   
💻 [GitHub](https://github.com/mindbox-cloud/flutter-sdk)   
📦 [pub.dev](https://pub.dev/packages/mindbox)

[React Native](flutter-sdk.md)

**React Native:** 0.60+   
**Языки:** JavaScript / TypeScript

📚 [Документация](react-native-sdk.md)   
📦 [Пример](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp)   
💻 [GitHub](https://github.com/mindbox-cloud/react-native-sdk)   
📦 [npm](https://www.npmjs.com/package/mindbox-sdk)

[Expo](expo-sdk.md)

**React Native:** 0.81+   
**Языки:** JavaScript / TypeScript

📚 [Документация](expo-sdk.md)   
📦 [Пример](https://github.com/mindbox-cloud/react-native-sdk/tree/develop/example/exampleApp)   
💻 [GitHub](https://github.com/mindbox-cloud/expo-plugin/tree/develop/examples/MindboxExpoExample)   
📦 [npm](https://www.npmjs.com/package/mindbox-expo-plugin)

---

## Не поддерживается

Не поддерживаем приложения, созданные:

- на кроссплатформенных технологиях (Xamarin, Native Script).
- на Cordova.
- на Unity.
- как WebView (PWA) приложения без нативной обертки (на Kotlin или Swift), которые нельзя загрузить в маркетплейс приложений (Google Play, App Store, App Gallery, RuStore и другие)*.

Если ваше приложение создано на одной из этих технологий, то обратитесь к консультанту по внедрению или менеджеру проекта.

### 🤔 *Если вы не уверены, поддерживаем ли мы ваше WebView-приложение

попробуйте добавить SDK по инструкции:

- [для Android](android-sdk.md)
- [для iOS](ios-sdk.md)
- [для Flutter](flutter-sdk.md)
- [для React Native](react-native-sdk.md)

Если получится, то поддерживаем. Интегрируйте SDK по стандартной инструкции и не забудьте выполнить шаги по синхронизации deviceUUID между mobile SDK и JS SDK в приложении с WebView:

- [для Android](sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview.md)
- [для iOS](ios-webview-sync-with-sdk.md)
- [для Flutter](sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-flutter.md)
- [для React Native](sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-react-native.md)
