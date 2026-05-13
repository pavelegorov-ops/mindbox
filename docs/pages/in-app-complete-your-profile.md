---
title: "Как добавить In-App «Заполните данные профиля и получите подарок»"
slug: "in-app-complete-your-profile"
source_url: "https://help.mindbox.ru/docs/in-app-complete-your-profile"
vcs_path: "in-app-complete-your-profile.md"
toc_path:
  - Персонализация
  - Персонализация мобильных приложений
  - "Интересные механики In-App"
  - Механики для сбора данных клиентов
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:eb580d275b254aeb0381939d2821916f9f421b6765b74c6f598c9da7dd19ab25"
---

# Как добавить In-App «Заполните данные профиля и получите подарок»

**Цель механики** — cобрать больше данных о пользователях, чтобы отправлять им персонализированные коммуникации и в дальнейшем увеличить среднюю выручку с пользователя.

Как настроить In-App для подздравления клиента с днем рождения, расказываем [тут](/doc/in-app-happy-birthday).

## Как это работает

1. Пользователь заходит в приложение и видит In-App с просьбой заполнить какие-либо данные о себе (например, день рождения) в обмен на бонусы или любой другой подарок.
2. Пользователь переходит по диплинку из In-App и заполняет данные.
3. После этого пользователю показывается In-App о том, что ему начислены баллы, которые он может потратить.

## Шаги настройки

Некоторые настройки на этой странице требуют обновления SDK приложения до версии 2.14.0. Для обновления SDK версии обратитесь к вашим разработчикам.

Рассмотрим создание механики на примере сбора данных о дате рождения клиентов и выдачи за это бонусных баллов.

### 1. Создайте сегмент тех, у кого не заполнена дата рождения

Создайте [пересчитываемый сегмент клиентов](segment-client-filter-realtime.md):

- у кого есть нужное приложение,
- кто авторизован (зависит от способа авторизации в приложение),
- у кого не заполнена дата рождения.

Пример сегмента с авторизацией по номеру или почте:

![inn-app-complete-profile-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/inn-app-complete-profile-segment.png)

### 2. Создайте In-App с просьбой заполнить дату рождения

Создайте In-App по [инструкции](in-apps.md).

#### Внешний вид формы

Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

С техническими рекомендациями к размеру и формату картинки для In-app можно ознакомиться [здесь](in-apps.md#shablon-modalnoe-okno).

Добавьте ссылку перехода по клику на In-App, чтобы сократить путь пользователя и сразу направить на страницу редактирования профиля. Рекомендуемый формат диплинка: `https://link`.

![in-app-complete-profile-form.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-form.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Укажите частоту всплывания **«Не чаще одного раза в указанный период»**, например, один раз в 14 или 30 дней.
- Если эта механика должна быть с более высоким приоритетом, чем другие формы, и игнорировать лимиты показов, включите настройку **«Приоритетный In-App»**.

![in-app-complete-profile-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-general.png)

#### Условия всплывания

Так как по умолчанию In-App отображается сразу после входа в приложение, укажите в настройке всплывания **«Спустя время после попадания в таргетинг»**, например, через 5 секунд. Так форма не будет всплывать в ту же секунду после входа в приложения.

![in-app-complete-profile-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-frequency.png)

#### Таргетинг

- Выберите созданный ранее сегмент клиентов, у кого не заполнена дата рождения.
- При первом входе в приложение клиент получает несколько системных окон для настройки приложения и онбординга. Чтобы не перегружать клиента уведомлениями, добавьте условие **«Количество входов в приложение больше или равно 2»**. Так In-App покажется только после второго входа в приложение.

![in-app-complete-profile-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-targeting.png)

Первый In-App готов

Он покажется пользователям с незаполненной датой рождения спустя 5 секунд после входа в приложение не чаще, чем 1 раз в 30 дней.

### 3. Создайте операцию заполнения даты рождения в профиле

Чтобы показать In-App только тем клиента, кто заполнил дату рождения в приложении, необходимо настроить таргетинг In-App по вызову операции заполнения данных в профиле.

Если такой операции ещё нет:

- Cоздайте новый [шаблон действия](template-create.md):

![in-app-complete-profile-action.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-action.png)

- Настройте операцию авторизации пользователя [по инструкции](https://help.mindbox.ru/docs/in-app-location):

![in-app-complete-profile-operation.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-operation.png)

Разработчики должны настроить вызов операции в приложении и выпустить новый релиз приложения.

### 4. Создайте сценарий для начисления баллов

Создайте сценарий по [инструкции](what-is-workflow.md#sozdanie-i-nastrojka-scenariya).

В настройках запуска:

- Укажите запуск по событию [«Выдано действие»](workflow-events.md#dejstviya-klientov). В качестве действия укажите то действие, которое выдается в вашей операции.
- Чтобы клиент получил бонус только один раз, добавьте ограничение по частоте попадания в сценарий.

![in-app-complete-profile-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-workflow.png)

Далее добавьте блок [«Группа шагов»](workflow-steps.md) с начислением баллов:

![in-app-complete-profile-workflow-steps.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-workflow-steps.png)

### 5. Создайте In-App о начислении бонусов

Создайте In-App по [инструкции](in-apps.md) с уведомление, что бонусы начислены.

#### Внешний вид формы

- Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

![in-app-complete-profile-bonus.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-bonus.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Чтобы пользователь увидел In-App только один раз, укажите частоту всплывания **«Всего один раз»**.
- Если эта механика должна быть с более высоким приоритетом, чем другие формы, и игнорировать лимиты показов, включите настройку **«Приоритетный In-App»**.

![in-app-complete-profile-bonus-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-bonus-general.png)

#### Условия всплывания

- Выберите **«Сразу после попадания пользователя в таргетинг»**, чтобы сообщить клиенту о бонусах сразу после получения.

![in-app-complete-profile-bonus-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-bonus-frequency.png)

#### Таргетинг

- Укажите таргетинг по операции заполнения даты рождения.
- Задайте условие **«Количество входов в приложение»** больше или равно 2, чтобы не показывать In-App с промокодом тем, кто только что установил приложение и авторизовался.

![in-app-complete-profile-bonus-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-bonus-targeting.png)

Второй In-App готов

Он покажется только 1 раз только что заполнившим дату рождения, даже если пользователь уже достиг лимитов по In-App, которые выставлены на проекте.

### 6. Протестируйте формы

Чтобы понять, правильно ли отображается In-App, добавьте сегмент с тестовым клиентом в таргетинг In-App. Подробнее в [статье](in-apps.md#kak-protestirovat-in-app).

### 7. Запустите формы

Когда обе формы готовы и протестированы, запустите их:

![in-app-complete-profile-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-start.png)

## Как найти участников механики

Отслеживайте метрики по запущенному In-App с помощью [отчета по In-App](report-in-apps.md).

![reports-in-app.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/reports-in-app.png)

Чтобы понять, сколько пользователей заполнили дату рождения после показа первого In-App, можно использовать 2 способа. Оба варианта помогут вам оценить, сколько заполненных профилей вы получили, благодаря механике в In-App

1. Постройте фильтр по тем, кто получил первый In-App и прошел сценарий:

![in-app-complete-profile-check.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-check.png)

Так как таргетинг формы настроен на показ клиентам без дня рождения, то фильтр найдет тех, у кого ранее дата рождения была неизвестна и получил бонусы за заполнение.

2. Постройте фильтр по тем, кто видел оба In-App:

![in-app-complete-profile-check2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-complete-profile-check2.png)

## Дополнительные материалы

- [In-App помогают «Читай-городу» продвигать крупные акции, проводить опросы и собирать клиентские данные](https://mindbox.ru/journal/cases/chitai-gorod-in-app/?utm_source=help)
- [Как и зачем обувной бренд ASH внедрил In-App. Кейс для магазинов с мобильным приложением](https://mindbox.ru/journal/cases/ash-in-app/?utm_source=help)
