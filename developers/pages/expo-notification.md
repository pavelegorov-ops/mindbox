---
title: Expo Notifications
slug: "expo-notification"
source_url: "https://developers.mindbox.ru/docs/expo-notification"
breadcrumb:
  - Мобильные приложения
  - Expo SDK
  - Дополнительные настройки
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:48496f519e99b6e1b49aeaa93a507bd231ef32adb1d04a3647f1bc7fcfc72527"
---

# Expo Notifications

Expo Notifications позволяет получать и отображать уведомления. Рассмотрим, как установить и настроить библиотеку Expo Notifications для отправки push-уведомлений и для получения разрешений на уведомления.

[Пример использования плагина вместе с Expo Notifications](https://github.com/mindbox-cloud/expo-plugin/tree/example_expo_notification/examples/MindboxExpoExample)

## Установка expo-notification

1. Добавьте `expo-notification` в `package.json`

   ```
   npx expo install expo-notifications
   ```
2. В настройки плагина `mindbox-expo-plugin` добавьте `"usedExpoNotification":true`
3. Добавьте проверку, что push-уведомление пришло от Mindbox, в функциях:

   - Notifications.addNotificationReceivedListener
   - Notifications.addNotificationResponseReceivedListener

   ```
   import { isMindboxPush } from 'mindbox-expo-plugin'; 
   ......
    const notificationListener = Notifications.addNotificationReceivedListener(value => {
         console.log('addNotificationReceivedListener');
           if (isMindboxPush(value)) {
             console.log("Received Mindbox push notification");
             return
           }
         setNotification(value);
       });
   ```
