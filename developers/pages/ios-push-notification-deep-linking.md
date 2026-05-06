---
title: "Переход по ссылке из push-уведомления"
slug: "ios-push-notification-deep-linking"
source_url: "https://developers.mindbox.ru/docs/ios-push-notification-deep-linking"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:fe37fc3b261e78f3b8240e242e0f69e1526001c0a6fb12df69d574c73fcc6d5e"
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
