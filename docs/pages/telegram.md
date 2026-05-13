---
title: Как отправить рассылку в Telegram через Fasttrack
slug: telegram
source_url: "https://help.mindbox.ru/docs/telegram"
vcs_path: telegram.md
toc_path:
  - Рассылки
  - Уведомления и мессенджеры
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:154ae0c6eddc51fc52dc6c92d24bd6c1751ae0ebafbe6114c409c084c5401795"
---

# Как отправить рассылку в Telegram через Fasttrack

## Подключение Telegram

1. Создайте личный кабинет в [Fasttrack](https://fstrk.io/) — сервисе для отправки сообщений в мессенджеры.
2. Создайте в Mindbox дополнительное поле для хранения идентификаторов из Telegram.

![mailing-telegram-custom-field](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-custom-field.png)

3. Перейдите в раздел **Настройки → Рассылки → Соединения** и добавьте соединение для Telegram:

![telegram-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/telegram-connection.png)

Заполните все поля в настройках соединения:

![telegram-connection-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/telegram-connection-2.png)

- **Бренд** — выберите нужный бренд. Актуально для [мультибрендовых](multibrand.md) проектов.
- **Провайдер** — Fasttrack.
- **Контакт получателя** — выберите дополнительное поле, созданное [во втором пункте инструкции](https://help.mindbox.ru/docs/telegram#podklyuchenie-telegram:~:text=%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%B9%D1%82%D0%B5%20%D0%B2%C2%A0Mindbox%20%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BF%D0%BE%D0%BB%D0%B5%20%D0%B4%D0%BB%D1%8F%20%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2%20%D0%B8%D0%B7%C2%A0Telegram.).

Для завершения настройки выберите бота в Fasttrack и сохраните соединение.

4. [Включите модуль](billing-modules.md#vklyuchit-i-vyklyuchit-modul) «Уведомления и мессенджеры».

## Настройки в Fasttrack

### Отслеживание переходов

Чтобы клики попадали в Mindbox, включите в Fasttrack укорачивание ссылок (раздел **Настройки** → **Системные настройки**):

![mailing-telegram-clicks2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-clicks2.png)

### Создание шаблонов

В Fasttrack создайте шаблоны под разные типы сообщений, которые планируете отправлять: просто текст, текст с картинкой, текст с кнопкой и т.д.

Рассмотрим пример создания шаблона с текстом, картинкой и кнопкой.

1. На вкладке **Конструктор** → **Группа узлов** перейдите в «Шаблоны для рассылок»:

![mailing-telegram-ft-nodes.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-nodes.png)

2. Добавьте шаблон:

![mailing-telegram-ft-create-node.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-create-node.png)

3. Заполните название шаблона. Оно понадобится позже при создании рассылок в Mindbox. Нажмите «Создать сообщение»:

![mailing-telegram-ft-name-node.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-name-node.png)

4. Заполните тело шаблона.

Разметьте все изменяемые части сообщения (текст, ссылка картинки, ссылка перехода у кнопки) переменными — значения для них будут подставляться в рассылку из Mindbox.

Для ввода переменных используйте конструкцию `{{ get_params.* }}`

- Текст и картинка:

![mailing-telegram-ft-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-text.png)*Используется [разметка Markdown](telegram.md#sintaksis-yazyka-razmetki-markdown).*

- Кнопка:

![mailing-telegram-ft-button1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-button1.png)  
![mailing-telegram-ft-button2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-ft-button2.png)

Не забудьте сохраните элементы в конструкторе.

## Создание рассылки в Mindbox

Далее по созданному шаблону можно создавать и отправлять рассылки из Mindbox.

Для этого:

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» и выберите тип рассылки (массовая или автоматическая):

![trigger-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create1.png)

3. Выберите канал «Telegram», [папку](folders.md) и нажмите «Создать»:

![mailing-telegram-mb-create2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mb-create2.png)

### Сообщение

![mailing-telegram-mb-message.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mb-message.png)

- **Отправитель** — создается при добавлении провайдера.
- **Имя шаблона** — скопируйте название шаблона из Fasttrack.
- **Параметры шаблона** — заполните, если в шаблоне Fasttrack используются переменные:
  - **Ключ** — название переменной (часть после `get_params.`)
  - **Значение** — что подставлять вместо этой переменной в сообщении. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) и [разметку Markdown](telegram.md#sintaksis-yazyka-razmetki-markdown).

![mailing-telegram-mb-message-ready.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mb-message-ready.png)

Пример сообщения по такой рассылке:

![mailing-telegram-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-result.png)

## Отправка рассылки

Принцип отправки рассылки такой же как в остальных каналах:

- в массовых кампаниях выбираются получатели и рассылка запускается сразу или на запланированную дату:

![mailing-telegram-mass-ready1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mass-ready1.png)

![mailing-telegram-mass-ready2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mass-ready2.png)

- автоматические отправляются из сценариев после перевода в статус «Готова к использованию»:

![mailing-telegram-auto-ready1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-auto-ready1.png)

![mailing-telegram-auto-ready2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-auto-ready2.png)

![mailing-telegram-auto-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-auto-workflow.png)

### Кому можно отправлять сообщения в Telegram?

Клиенту можно отправить сообщение, если заполнен его идентификатор в мессенджере — добавляйте проверку на его наличие.

При блокировке бота все будущие сообщения будут падать с недоставкой с причиной «Номер не поддерживается провайдером».  
По этому событию можно выделять клиентов и исключать их из рассылок. В таком случае нужно также учитывать, что клиент может разблокировать бота и должен повторно попасть в список получателей.

Пример сегмента получателей:

![mailing-telegram-users.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-users.png)

### После отправки

Взаимодействие с рассылкой фиксируются с помощью [статусов](customer-message-statuses.md). В канале Telegram выдаются отправки, неотправки и недоставки:

![mailing-telegram-client.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-client.png)

## Синтаксис языка разметки Markdown

При создании сообщений для Telegram используется базовый язык разметки Markdown. Его можно использовать как при настройке шаблона в Fasttrack, так и при заполнении переменных в рассылке Mindbox.

Базовая разметка для форматирования:

- Изображение — `![](ссылка на картинку)`
- Изображение с текстом в одном сообщении — `![текст](ссылка на картинку)`
- Ссылка в тексте — `[текст ссылки](адрес перехода)`
- Жирный шрифт — `*текст*`
- Курсив — `_текст_`
- Моноширинный — `` `текст` ``

**Пример:**

![markdown-img-with-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/markdown-img-with-text.png)

![markdown-link-bold.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/markdown-link-bold.png)

**Результат:**

![markdown-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/markdown-result.png)
