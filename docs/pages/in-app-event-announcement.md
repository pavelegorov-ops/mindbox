---
title: "Как добавить In-App для анонса важного события"
slug: "in-app-event-announcement"
source_url: "https://help.mindbox.ru/docs/in-app-event-announcement"
vcs_path: "in-app-event-announcement.md"
toc_path:
  - Персонализация
  - Персонализация мобильных приложений
  - "Интересные механики In-App"
  - "Примеры информационных In-App"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:59d2a238948bf8d8c225984c00d056b54e63cc6ccf4c8eae30df80820b009bbe"
---

# Как добавить In-App для анонса важного события

**Цель механики** — быстро сообщить пользователям о важных событиях без привлечения разработки и обновления приложения.

Например:

- открытие нового филиала магазина,
- день рождения бренда,
- старт игры,
- временный технический сбой,
- новые возможности приложения,
- и т.д.

## Шаги настройки

Некоторые настройки на этой странице требуют обновления SDK приложения до версии 2.14.0. Для обновления SDK версии обратитесь к вашим разработчикам.

### 1. Создайте In-App

Создайте In-App по [инструкции](in-apps.md) с уведомлением.

#### Внешний вид формы

- Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

С техническими рекомендациями к размеру и формату картинки для In-app можно ознакомиться [здесь](in-apps.md#shablon-modalnoe-okno).

![in-app-event-announcement-form.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-event-announcement-form.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Укажите частоту всплывания **«Всего один раз»**, чтобы сообщить пользователю новость только один раз и не беспокоить повтором формы.
- Включите настройку **«Приоритетный In-App»**, чтобы пользователю показался именно эта форма о важном событии, а не любой другой In-App с таким же таргетингом. Приоритетный In-App будет игнорировать лимиты по количеству In-App в сутки или в сессию, выставленные на проекте.

![in-app-event-announcement-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-event-announcement-general.png)

#### Условия всплывания

- Так как по умолчанию In-App отображается сразу после входа в приложение, выберите **«Спустя время после попадания в таргетинг»**, например, через 5 секунд, чтобы дать пользователю немного адаптироваться после входа в приложение.

![in-app-event-announcement-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-event-announcement-frequency.png)

#### Таргетинг

- Если мероприятие или уведомление направлены на определенную группу клиентов, укажите сегмент.
- При необходимости добавьте условие **«Количество входов в приложение больше или равно 2»**, чтобы уведомление не показывалось клиентам, которые только установили приложение.

![in-app-event-announcement-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-event-announcement-targeting.png)

### 2. Протестируйте In-App

Чтобы понять, правильно ли отображается In-App, добавьте сегмент с тестовым клиентом в таргетинг In-App. Подробнее в [статье](in-apps.md#kak-protestirovat-in-app).

### 3. Запустите In-App

Когда форма готова и протестирована, запустите ее:

![in-app-event-announcement-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-event-announcement-start.png)

## Отслеживайте данные по механике

Отслеживайте метрики по запущенному In-App с помощью [отчета по In-App](report-in-apps.md).

![reports-in-app.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/reports-in-app.png)

## Дополнительные материалы

- [Первый In-App ASH приглашает поучаствовать в игре. Каждый пользователь видит его только один раз. Click rate — 6,8%](https://mindbox.ru/journal/cases/ash-in-app/?utm_source=help)
- [В «Читай-городе» обновили программу лояльности. Об изменениях рассказывали во всех доступных каналах: отправили email-рассылку, добавили баннер на главной странице сайта, опубликовали в соцсетях и запустили попапы и In-App.](https://mindbox.ru/journal/cases/chitai-gorod-in-app/?utm_source=help)
