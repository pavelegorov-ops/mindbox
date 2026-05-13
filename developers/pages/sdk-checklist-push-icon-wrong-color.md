---
title: "Иконка push-уведомления отображается другим цветом"
slug: "sdk-checklist-push-icon-wrong-color"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-push-icon-wrong-color"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6c619a4c71d5c48a769f6efe5e3a81840200504ddcf33c06979b731fd3648d17"
---

# Иконка push-уведомления отображается другим цветом

## Не задан цвет фона при использовании монохромной иконки

### Как проверить

1. Убедитесь, что вы используете монохромную иконку:
   - Если иконка одного цвета, например, только белая, то она монохромная;
   - Если иконка векторная, то в файле xml должен использоваться только один цвет.
2. Проверьте, не задан ли цвет фона в ресурсе `mindbox_default_notification_color` в файле `res/values/colors.xml`, начиная с [SDK версии](https://github.com/mindbox-cloud/android-sdk/releases) 2.10.0.

### Как поправить

Поменять или установить цвет фона иконки можно, начиная с [SDK версии](https://github.com/mindbox-cloud/android-sdk/releases) 2.10.0. Чтобы поменять цвет иконки в push-уведомлении, задайте цвет ресурса `mindbox_default_notification_color` в файле `res/values/colors.xml` .

Например, строка `#FF0000` поменяет цвет вашей монохромной иконки на красный.
