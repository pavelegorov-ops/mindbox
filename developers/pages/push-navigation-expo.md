---
title: "Навигация по клику на push-уведомление в Expo"
slug: "push-navigation-expo"
source_url: "https://developers.mindbox.ru/docs/push-navigation-expo"
breadcrumb:
  - Мобильные приложения
  - Expo SDK
  - Дополнительные настройки
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:38ae834b413000d1f7f43cf0ecdf22e3902451b7c88fd78ff0f0ad7f2f72a78b"
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
