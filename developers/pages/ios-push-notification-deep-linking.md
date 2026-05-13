---
title: "Переход по ссылке из push-уведомления"
slug: "ios-push-notification-deep-linking"
source_url: "https://developers.mindbox.ru/docs/ios-push-notification-deep-linking"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:5b26101546d52c72e559bd8607d7e90d116785a6094e90dfd0d9d9e5b58f0f2e"
---

# Переход по ссылке из push-уведомления

Если вы используете встроенную отрисовку push-уведомлений Mindbox SDK, то для обработки перехода по нажатию необходимо переопределить метод **userNotificationCenter(_:didReceive:withCompletionHandler:)** в **AppDelegate**.
В обработчике получите данные пуша через **Mindbox.shared.getMindboxPushData(...)**, определите URL (кнопка или основной), и передайте его в свой обработчик навигации.

```
override func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
  	super.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)  
  	if let pushModel = Mindbox.shared.getMindboxPushData(userInfo: response.notification.request.content.userInfo), Mindbox.shared.isMindboxPush(userInfo: response.notification.request.content.userInfo) {
        var url = ""
        if let buttons = pushModel.buttons, let clickedButton = buttons.first(where: { $0.uniqueKey == response.actionIdentifier}), let buttonUrl = clickedButton.url  {
            url = buttonUrl
        } else if let clickUrl = pushModel.clickUrl {
            url = clickUrl
        }

        // Обработайте URL клика
        handleUrl(url)
    }  
}
```

Важно добавить обработку URL на стороне приложения. SDK не предоставляет обработку URL по умолчанию
