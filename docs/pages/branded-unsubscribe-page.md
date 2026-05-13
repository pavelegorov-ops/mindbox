---
title: Как настроить брендированную страницу отписки
slug: "branded-unsubscribe-page"
source_url: "https://help.mindbox.ru/docs/branded-unsubscribe-page"
vcs_path: "branded-unsubscribe-page.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Страница отписки
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:2c549f578682b921be2382e9e9fc5a24cccdec479c55846eb61e362a33599fae"
---

# Как настроить брендированную страницу отписки

Настраивайте свою собственную страницу отписки в дизайне вашего бренда вместо стандартной страницы. Это поможет сохранить узнаваемость, повысить доверие и перевести подписчика на сайт или в соцсети.

**Преимущества**:

- Сборка в конструкторе — не нужна команда разработки.
- Страница автоматически появится во всех рассылках (даже в уже отправленных), где используется [базовая ссылка отписки](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BE%D1%82-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%B0-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8.md).
- Единое брендовое оформление снижает ощущение фишинга и повышает доверие.
- Прозрачный интерфейс снижает негатив при отписке.
- Есть возможность добавить ссылки на сайт, соцсети и мессенджеры для перевода в другие каналы.
- Управление подписками: клиент может как отписаться, так и подписаться.

![branded-unsubscribe-page-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-example.png)

## Перед настройкой

- Убедитесь, что рассылки используют стандартные ссылки отписки `${Message.UnsubscribeLink}` или `${Message.TopicUnsubscribeLink}`
- При использовании блока с тематиками поверьте, что на проекте созданы все необходимые [тематики рассылок](как-создать-тематику-рассылки).

## Создание страницы

Перейдите в раздел **Настройки** → **Рассылки** → **Страница отписки**

![branded-unsubscribe-page-path](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-path.png)

Нажмите «Создать» и выберите бренд, в котором будет использоваться страница:

![branded-unsubscribe-page-create](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-create.png)

Для каждого бренда на проекте можно создать одну страницу отписки.

Страница состоит из двух экранов:

- **Экран отписки** — это экран, который подписчик увидит первым при попадании на страницу отписки через клик в футере.
- **Экран «Спасибо»** — показывается после подтверждения отписки или сохранения изменений в подписках на тематики.

## Экран отписки

Перейдите в настройку страницы отписки:

![branded-unsubscribe-screen-create](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-screen-create.png)

Страница строится из блоков с различными настройками. Перетаскивайте нужные элементы в рабочую область и настраивайте их под свой бренд так же, как в [конструкторе для Email-писем](email-editor.md):

![branded-unsubscribe-page-editor-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-editor-2.png)

На странице отписки недоступны параметры шаблонизатора.

### Блоки отписки от тематики

Список тематик формируется автоматически по данным проекта. Перед настройкой страницы отписки убедитесь, что у вас созданы все необходимые тематики. Новые тематики можно [создать по инструкции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md#sozdat-tematiku).

Предлагайте клиенту настроить свои подписки, чтобы вместо полной отписки от канала клиент мог отписаться только от части тематик и подписаться на интересные ему рассылки.

1. Добавьте в рабочую область блок из категории «Блоки отписки» с названием «Блок с тематиками»:

   ![branded-unsubscribe-page-editor-themes-path](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-editor-themes-path.png)
2. Выберите список тематик, подписку на которые клиент сможет отредактировать. Например, можно скрыть технические тематики, которые используются для настройки механик.

   ![branded-unsubscribe-page-editor-themes](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-editor-themes.png)

**Настраивайте внешний вид блока:**

- Переименуйте тематики на понятные получателю названия.
- Настраивайте их порядок.
- Добавляйте описания тематик, чтобы помочь клиенту сделать выбор.

**Поведение чекбоксов:**

- Если клиент уже подписан на тематику или подписка на нее в статусе «Требует подтверждения» (при наличии [DOI](doi-turn-on.md)), она будет отмечена галочкой.
- Чтобы отписаться от тематики, нужно снять галочку.
- Чтобы подписаться — поставить галочку.

## Экран спасибо

Когда основной экран готов, настройте экран «Спасибо» с благодарностями за уделенное время. Добавляйте на экран кнопки для перехода на сайт или в соцсети:

![branded-thankyou-screen](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-thankyou-screen.png)

## Фавикон и название страницы

Задайте фавикон и заголовок вкладки в «Общих настройках» конструктора. Это повысит узнаваемость бренда.

![branded-unsubscribe-page-example-favicon](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-example-favicon.png)

## Предпросмотр

Оценить внешний вид страницы и протестировать работу блоков можно по кнопке «Посмотреть»:

![branded-unsubscribe-page-test](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-test.png)

Полноценное тестирование подписки/отписки доступно только после включения брендированной страницы отписки по ссылке из любого отправленного письма со стандартной ссылкой отписки.

## Запуск

Включите страницу в работу по кнопке «Включить»:

![branded-unsubscribe-screen-start](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-screen-start.png)

**После включения:**

- Брендированная страница отписки автоматически заменит стандартную во всех письмах бренда со ссылками `${Message.UnsubscribeLink}` или `${Message.TopicUnsubscribeLink}`.
- Если в проекте есть тематики и используется ссылка `${Message.TopicUnsubscribeLink}`:
  - Кнопка «Отписаться» отписывает от всего канала Email, а не от тематики рассылки.
  - Для отписки от тематики используйте [блок тематик с чекбоксами](branded-unsubscribe-page.md#bloki-otpiski-ot-tematiki).

Если необходимо скорректировать страницу отписки, изменения можно внести в любой момент. После сохранения они сразу применятся во всех рассылках.

При необходимости страницу можно выключить — во всех письмах снова отобразится стандартная страница.

## Как работает отписка и подписка на странице отписки

1. Клиент полностью отписался по кнопке «Отписаться». Клиенту выдается действие «Отказ от рекламы» с полной отпиской от канала «Email»:

   ![branded-unsubscribe-page-channel-unsub](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-channel-unsub.png)
2. Клиент снимает галочки у отдельных тематик и сохраняет. Выдается действие «Отказ от рекламы» со списком тематик:

   ![branded-unsubscribe-page-theme-unsub](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-theme-unsub.png)
3. Клиент ставит галочки у нужных тематик и сохраняет. Выдается действие «Согласие на рекламу» со списком тематик:

   ![branded-unsubscribe-page-theme-sub](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/branded-unsubscribe-page-theme-sub.png)

### Как меняется подписка при DOI

Если в бренде подключено [DOI](https://help.mindbox.ru/docs/doi-turn-on) и у клиента есть тематика в статусе «Требует подтверждения»:

- Тематика отображается с галочкой.
- Если клиент не убирает галочку и сохраняет подписку — фиксируется действие «Согласие на рекламу», тематика получает статус «Подписан».
- Если клиент снимает галочку — статус «Требует подтверждения» меняется на «Отписан».
