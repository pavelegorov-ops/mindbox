---
title: "В push-уведомлении не отображаются кнопки по нажатию"
slug: "sdk-checklist-push-no-large-image-on-click"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-push-no-large-image-on-click"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - IOS
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:5e147b2793dcfb8367057e4ffa86a1477997e60c4aeb6f079b3da23c0ebaf9fd"
---

# В push-уведомлении не отображаются кнопки по нажатию

## Не реализован Content Extension

### Как проверить

Убедитесь, что реализована [эта инструкция](rich-push-notifications-buttons.md).

### Как поправить

Выполните [эту инструкцию](rich-push-notifications-buttons.md).

## В Content Extension не реализованы App Groups

### Как проверить

1. Убедитесь, что выполнили [этот пункт инструкции](rich-push-notifications-buttons.md#22-app-groups).
2. Проверьте расширение `.entitlements` — в нем видно, какое значение App Group ввели.

### Как поправить

Пропишите App Group строго по шаблону [в инструкции](rich-push-notifications-buttons.md#22-app-groups).

## В Content Extension нет кода, который скачает картинку

### Как проверить

Убедитесь, что код в расширении совпадает с кодом [в этой инструкции](rich-push-notifications-buttons.md#4-реализация-кода-расширения-в-приложении). Если нет, значит, у вас собственная реализация расширения, которую не может дебажить разработка Mindbox.

### Как поправить

Используйте [готовую реализацию](rich-push-notifications-buttons.md#4-реализация-кода-расширения-в-приложении), в ином случае поддерживать расширение нужно будет на вашей стороне.

## Неверное значение категории в `info.plist` при использовании нашей функции

### Как проверить

Убедитесь, что выполнены пункты [из этой инструкции](rich-push-notifications-buttons.md#настройка-infoplist).

- в строке с ключом `UNNotificationExtensionCategory` прописано `MindBoxCategoryIdentifier`;
- в строке `NSExtensionPrincipalClass` прописано то же, что в инструкции.

### Как поправить

Пропишите правильные значения [по инструкции](rich-push-notifications-buttons.md#настройка-infoplist).

## В пуше с картинкой изображение весит больше 10 Мб

### Как проверить

Проверьте, что картинка для пуша весит меньше 10 Мб.

### Как поправить

Уменьшите вес нужной картинки (рекомендуемый вес — меньше 5 Мб) и попробуйте отправить пуш заново.
