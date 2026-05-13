---
title: "При клике на push-уведомление информация об этом не отображается в Mindbox"
slug: "sdk-checklist-push-click-not-tracked-in-mindbox"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-push-click-not-tracked-in-mindbox"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:b6a69a86ac797c17406e26d36d1140e36c6b6aff4b7501c2c9b3a0e746dbff59"
---

# При клике на push-уведомление информация об этом не отображается в Mindbox

## Не вызывается метод клика по push-уведомлению при собственной реализации методов

### Как проверить

Проверьте, что есть вызов метода `Mindbox.shared.pushClicked`.

### Как поправить

Реализуйте метод `Mindbox.shared.pushClicked` с помощью [этой инструкции](ios-push-click-forwarding.md).

## Не отображается клик по push-уведомлению при использовании нашего делегата

### Как проверить

Вероятно где-то в коде переопределен делегат UNUserNotificationCenter.

### Как поправить

Реализуйте метод `Mindbox.shared.pushClicked` с помощью [этой инструкции](ios-push-click-forwarding.md).
