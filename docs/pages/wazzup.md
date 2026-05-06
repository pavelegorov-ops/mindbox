---
title: Как отправить рассылку в WhatsApp через Wazzup24
slug: wazzup
source_url: "https://help.mindbox.ru/docs/wazzup"
vcs_path: wazzup.md
toc_path:
  - Рассылки
  - Уведомления и мессенджеры
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:56c1150e743df0b671332c2fb5bed6efe02354ce92073ad47c2e4f97ca213a94"
---

# Как отправить рассылку в WhatsApp через Wazzup24

## Подключение WhatsApp

1. Создайте личный кабинет в [Wazzup24](https://wazzup24.ru/) — провайдере для отправки сообщений в WhatsApp*.
2. Перейдите в раздел **Настройки → Рассылки → Соединения** и добавьте соединение для WhatsApp*:

![whatsapp-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/whatsapp-connection.png)

На странице добавления соединения:

![wazzup24-create-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup24-create-connection.png)

2.1 Укажите настройки соединения:

- **Бренд** — выберите нужный бренд. Актуально для [мультибрендовых](multibrand.md) проектов.
- **Провайдер** — Wazzup24.
- **Токен** — введите ключ API. Узнать его можно в разделе «Интеграция с CRM» в личном кабинете Wazzup24. [Подробнее](https://wazzup24.ru/help/api-ru/avtorizaciya/).

2.2 Настройте сервер для получения [статусов рассылок](customer-message-statuses.md):

Выполнение запроса перенаправит все входящие сообщения бизнес-аккаунта WhatsApp* и статусы исходящих сообщений в Mindbox. Убедитесь, что вы не собираете эти данные в других системах.

- Выполните прописанный на странице PATCH-запрос с использованием того же ключа API, который указывался при подключении соединения в поле Token.

3. [Включите модуль](billing-modules.md#vklyuchit-i-vyklyuchit-modul) «Уведомления и мессенджеры».

## Настройки в Wazzup24

### Создание шаблона

Диалог с клиентом в WhatsApp* необходимо начинать с сообщения с согласованным шаблоном. Для того, чтобы создать и отправить шаблон на согласование, в Wazzup24 перейдите в **Шаблоны сообщений → Добавить шаблон**.

![wazzup-template.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-template.png)

В рассылках могут использоваться шаблоны в статусе «Активен»:

![wazzup-template-active.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-template-active.png)

## Данные из Wazzup24, которые понадобятся при создании рассылки в Mindbox

### Идентификатор канала WhatsApp*

Перейдите в **Каналы** и выберите нужный канал. Его идентификатор прописан в адресной строке браузера.

![wazzup24-channelID.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup24-channelID.png)

### Идентификатор шаблона

Для отправки сообщений с согласованным шаблоном. Указан в коде шаблона.

- Параметры шаблона — переменные, вместо которых в сообщении необходимо подставить определенный текст. Задаются при необходимости.

![wazzup-templateID.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-templateID.png)

## Создание рассылки в Mindbox

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» и выберите тип рассылки (массовая или автоматическая):

![trigger-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create1.png)

3. Выберите канал WhatsApp, папку и нажмите «Создать»:

![create-mailing-whatsapp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/create-mailing-whatsapp.png)

### Сообщение

![wazzup24-message.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup24-message.png)

- **Отправитель** — создается при добавлении соединения.
- **Идентификатор канала** — скопируйте [идентификатор канала](wazzup.md#identifikator-kanala-whatsapp) из Wazzup24.
- **Кнопки** — при необходимости вы можете добавить кнопку.
  - **Текст** — введите текст, который должен в ней отображаться.
  - **Payload** — необязательное поле. Заполняется, если на стороне Wazzup24 указана полезная нагрузка кнопки. Не влияет на выдачу кликов в Mindbox.

Дальнейшие настройки будут отличаться в зависимости от выбранного типа сообщения в выпадающем списке.

#### Шаблон

Для отправки сообщений с согласованным шаблоном.

![wazzup-message-template.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-message-template.png)

- **Идентификатор шаблона** — скопируйте [идентификатор шаблона](wazzup.md#identifikator-shablona) из Wazzup24.
- **Значения параметров шаблона** — заполните, если в шаблоне Wazzup24 используются переменные. В поле для ввода значения пропишите, что нужно подставлять вместо переменной в сообщении. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

Если в шаблоне Wazzup24 используется несколько параметров, можно указать значения для каждого из них по клику на кнопку «Добавить». Добавляйте параметры в том порядке, в котором они указаны в шаблоне Wazzup24, чтобы значения подставились корректно.

#### Текст

Для отправки сообщений при открытом 24-часовом окне в диалоге с клиентом.

![wazzup-message-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-message-text.png)

- **Сообщение** — введите текст, который нужно отправить клиенту. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

#### Файл

Для отправки картинок и файлов. Из интерфейса Mindbox можно отправить картинку формата .jpeg, .jpg, .png не более 5 МБ. [Подробнее про ограничения для вложений](https://wazzup24.ru/help/how-to-use/requirements-for-attachments/).

![wazzup-message-file.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/wazzup-message-file.png)

- **Ссылка на контент** — прикрепите ссылку на контент или выберите вложение из галереи картинок.

### Отслеживание переходов

Mindbox не может отслеживать клики по ссылкам, которые прописаны в шаблоне на стороне Wazzup24. Для отслеживания переходов по ссылкам используйте [сокращатель Mindbox](shorten-url-sms.md).

## Отправка рассылки

Принцип отправки рассылки такой же, как и в остальных каналах:

- в массовых кампаниях выбираются получатели и рассылка запускается сразу или на запланированную дату:  
  ![mailing-wa-mass-ready1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-mass-ready1.png)  
  ![mailing-telegram-mass-ready2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-telegram-mass-ready2.png)
- автоматические отправляются из сценариев после перевода в статус «Готова к использованию»:  
  ![mailing-wa-auto-ready1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-auto-ready1.png)  
  ![mailing-wa-auto-ready2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-auto-ready2.png)  
  ![mailing-wa-auto-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-auto-workflow.png)

### Кому можно отправлять сообщения в WhatsApp?

Клиенту можно отправить сообщение, если заполнен его мобильный телефон — добавляйте проверку на его наличие:

![mailing-wa-users.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-users.png)

Можно хранить подписку клиента в дополнительном поле и использовать его в фильтрах кампаний. В таком случае нужно настроить правила записи и передачи этого свойства на этапе интеграции с провайдером.  
Также можно исключать из получателей клиентов с недоставками в канале.

### После отправки

Взаимодействие с рассылкой фиксируются с помощью [статусов](customer-message-statuses.md). В канале WhatsApp* выдаются отправки, открытия и клики, а также неотправки и недоставки:

![mailing-wa-client.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-client.png)

* WhatsApp относится к Meta, деятельность которой признана экстремистской и запрещена на территории России.
