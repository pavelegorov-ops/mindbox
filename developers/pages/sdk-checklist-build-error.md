---
title: Приложение не собирается — ошибка сборки
slug: "sdk-checklist-build-error"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-build-error"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:33bba892f02afbb6f11a4232dbd5958a40310c3004d27eee025e308c87ec46cf"
---

# Приложение не собирается — ошибка сборки

## Не прописана App Group

### Как проверить

1. Убедитесь, что выполнили [этот пункт инструкции](ios-sdk-initialization.md#1-настройка-appgroup).
2. Проверьте расширение `.entitlements` — в нем видно, какое значение App Group ввели.

### Как поправить

Пропишите App Group строго по шаблону [в инструкции](ios-sdk-initialization.md#1-настройка-appgroup).

## Не обернули передачу статуса разрешения в async

### Как проверить

Убедитесь, что вызов метода `Mindbox.shared.notificationsRequestAuthorization` обернут в `DispatchQueue.main.async`.

### Как поправить

Обновите вызов метода в соответствии [с этой инструкцией](ios-quick-setup-push-notifications.md#настройка-пуш-уведомлений).

## Есть вызовы от SDK до отрабатывания `didFinishLaunchingWithOptions`

### Как проверить

Уточните, вызываются ли какие-либо методы Mindbox SDK до того, как отработает `didFinishLaunchingWithOptions`.

### Как поправить

Если какие-то методы вызываются, то уберите эти вызовы и сделайте так, чтобы они вызывались строго после `didFinishLaunchingWithOptions`.
