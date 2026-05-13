---
title: "iOS | Передача кликов по push-уведомлениям"
slug: "ios-get-click-react-native"
source_url: "https://developers.mindbox.ru/docs/ios-get-click-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:4c54e671dd3dbc0c69ed8cd106ebdb7c6d93c68ac621466d7863bbcd11cf7f1f"
---

# iOS | Передача кликов по push-уведомлениям

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции](add-ios-integration.md)
- [Получение ключей для iOS-приложения и настройка подключения к APNs](apns-keys-setup.md#/)
- [Добавление SDK в приложение](add-sdk-react-native.md)
- [Инициализация SDK](sdk-initialization-react-native.md)
- [Настройка push-notifications](ios-send-push-notifications-react-native.md)

### Результат шага «Получение кликов на мобильные push-уведомления на iOS»:

Push должен отправиться и отобразиться на вашем телефоне, и по клику на него статус в системе поменялся на «есть клик».

Проверить, что клики приходят, можно с помощью [этой инструкции](mobile-push-check.md#проверить-что-клики-приходят-в-систему).

[Пример вызова метода](https://github.com/mindbox-cloud/react-native-sdk/blob/develop/example/exampleApp/ios/AppDelegate.swift#L76)

В файле `AppDelegate` реализуйте метод `userNotificationCenter.didReceive` и вызвать `Mindbox.shared.pushClicked(response: response)`.

```
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {

    // ...

    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse,
        withCompletionHandler completionHandler: @escaping () -> Void
    ) {
        // Передача клика в Mindbox
        Mindbox.shared.pushClicked(response: response)
        completionHandler()
    }
}
```

**Проверьте результаты выполнения шага**
