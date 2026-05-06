---
title: "Как добавить In-App «Обновите приложение»"
slug: "in-app-app-update"
source_url: "https://help.mindbox.ru/docs/in-app-app-update"
vcs_path: "in-app-app-update.md"
toc_path:
  - Персонализация
  - Персонализация мобильных приложений
  - "Интересные механики In-App"
  - "Примеры информационных In-App"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:a0024f31958afaebc6c2688c268dc7535c8d8c08cd1e4fc037bdff877df6d95b"
deprecation_hint:
  - старая версия
---

# Как добавить In-App «Обновите приложение»

**Цель механики** — рассказать пользователю об обновлении и замотивировать его установить новую версию, чтобы увеличить использование новых функций.

## Как это работает

1. Пользователь заходит в приложение.
2. Показывается In-App-уведомление с просьбой обновить приложение.
3. Пользователь нажимает на In-App и переходит в магазин приложений для обновления.

## Шаги настройки

Некоторые настройки на этой странице требуют обновления SDK приложения до версии 2.14.0. Для обновления SDK версии обратитесь к вашим разработчикам.

### 1. Создайте сегмент клиентов

Создайте [пересчитываемый сегмент клиентов](segment-client-filter-realtime.md) для тех, у кого старая версия приложения:

![in-app-update-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-segment.png)

При условии «Версия приложения — заполнен и **не**» достаточно указать только самую новую версию вместо добавления всех старых версий.

После выхода новой версии достаточно заменить версию в сегменте на актуальную.

### 2. Создайте In-App

Создайте In-App по [инструкции](in-apps.md) с просьбой обновить приложение.

#### Внешний вид формы

- Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

С техническими рекомендациями к размеру и формату картинки для In-app можно ознакомиться [здесь](in-apps.md#shablon-modalnoe-okno).

- Укажите ссылку перехода по In-App на ваше приложение в магазине.

![in-app-update-form.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-form.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Укажите частоту всплывания **«Не чаще одного раза в указанный период»**, например, один раз в 1-3 дня.
- Включите настройку **«Приоритетный In-App»**, чтобы пользователю показался именно эта форма об обновлении, а не любой другой In-App с таким же таргетингом. Это необходимо, чтобы повысить шанс обновления приложения клиентом, если, например, в старой версии есть ошибка.

![in-app-update-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-general.png)

#### Условия всплывания

- Так как по умолчанию In-App отображается сразу после входа в приложение, выберите **«Спустя время после попадания в таргетинг»**, например, через 5 секунд, чтобы дать пользователю немного адаптироваться после входа в приложение.

![in-app-update-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-frequency.png)

#### Таргетинг

- Выберите нужный сегмент пользователей со старыми версиями, созданный на первом шаге.

![in-app-update-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-targeting.png)

### 3. Протестируйте In-App

Чтобы понять, правильно ли отображается In-App, добавьте сегмент с тестовым клиентом в таргетинг In-App. Подробнее в [статье](in-apps.md#kak-protestirovat-in-app).

### 4. Запустите In-App

Когда форма готова и протестирована, запустите ее:

![in-app-update-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-start.png)

## Отслеживайте данные по механике

Отслеживайте метрики по запущенному In-App с помощью [отчета по In-App](report-in-apps.md).

![reports-in-app.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/reports-in-app.png)

По фильтрам Mindbox можно также посмотреть долю пользователей, которые кликнули по сообщению и обновили мобильное приложение. Для этого нужно построить фильтр по клиентам, которые:

- раньше находились в сегменте тех, у кого старая версия приложения;
- кликнули на In-App;
- в этот момент не находятся в этом сегменте.

![in-app-update-check.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-update-check.png)

## Дополнительные материалы

[Rolf запустил In-App, чтобы мотивировать клиентов обновлять приложение. За два месяца 18 тысяч пользователей Android из сегмента тех, у кого старая версия приложения, кликнули на In-App, обновили приложение и были автоматически исключены из сегмента](https://mindbox.ru/journal/education/in-app-primery/?utm_source=help)
