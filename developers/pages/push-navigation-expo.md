---
title: "Навигация по клику на push-уведомление в Expo"
slug: "push-navigation-expo"
source_url: "https://developers.mindbox.ru/docs/push-navigation-expo"
breadcrumb:
  - Мобильные приложения
  - Expo SDK
  - Дополнительные настройки
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e23f8892a071cc4ea402d15d4dc90bbde953dc4cd3b0ae739a9c031e319c7000"
---

# Навигация по клику на push-уведомление в Expo

Для получения ссылки в React Native подпишитесь на событие, которое будет генерироваться в нативной части при клике.

Подписка будет вызвана 2 аргументами:

- `link` — ссылка, указанная в уведомлении;
- `payload` — сериализованный payload push-уведомления. Если передается JSON, то его десериализовать надо самостоятельно.

```
MindboxSdk.onPushClickReceived((pushUrl: String | null, pushPayload: String | null) => {
  console.log(`${pushUrl} ${pushPayload}`);
});
```
