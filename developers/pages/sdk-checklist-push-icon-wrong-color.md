---
title: "Иконка push-уведомления отображается другим цветом"
slug: "sdk-checklist-push-icon-wrong-color"
source_url: "https://developers.mindbox.ru/docs/sdk-checklist-push-icon-wrong-color"
breadcrumb:
  - Мобильные приложения
  - "Чек-лист проверки интеграции SDK"
  - Android
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:2d74f4473c35f2228d56c2164d54e4dd9fbe2acccd411fb95b71c8c47fee839e"
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
