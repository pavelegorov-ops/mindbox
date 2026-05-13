---
title: Как отправить рассылку в WhatsApp через Fasttrack
slug: whatsapp
source_url: "https://help.mindbox.ru/docs/whatsapp"
vcs_path: whatsapp.md
toc_path:
  - Рассылки
  - Уведомления и мессенджеры
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:582a6217310d12bb2f82a238f00825664a5bb9006a2407d8c41a2208fd7a0c24"
---

# Как отправить рассылку в WhatsApp через Fasttrack

## Подключение WhatsApp

1. Создайте личный кабинет в [Fasttrack](https://fstrk.io/) — сервисе для настройки ботов в WhatsApp*.
2. Подключите провайдера для отправки сообщений в мессенджеры. Доступный список можно уточнить на стороне Fasttrack.
3. Перейдите в раздел **Настройки → Рассылки → Соединения** и добавьте соединение для WhatsApp*:

![whatsapp-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/whatsapp-connection.png)

Заполните все поля в настройках соединения:  
![whatsapp-connection-fasttrack.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/whatsapp-connection-fasttrack.png)

- **Бренд** — выберите нужный бренд. Актуально для [мультибрендовых](multibrand.md) проектов.
- **Провайдер** — Fasttrack.

Для завершения настройки выберите бота в Fasttrack и сохраните соединение.

4. [Включите модуль](billing-modules.md#vklyuchit-i-vyklyuchit-modul) «Уведомления и мессенджеры».

## Настройки в Fasttrack

### Отслеживание переходов

Чтобы клики по ссылкам передавались в Mindbox, установите в качестве хоста URL-укорачивателя `https://fstrk.cc` (раздел **Настройки** → **Мессенджеры** → **WhatsApp**):

![mailing-wa-clicks1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-clicks1.png)

И в каждом шаблоне включите сокращение ссылок:

![mailing-wa-clicks2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-clicks2.png)

### Создание шаблона

Шаблоны создаются и согласовываются на стороне провайдера, а далее подтягиваются в личный кабинет Fasttrack.

Для этого в Fasttrack перейдите на вкладку **Маркетинг** → **Рассылки** → **WhatsApp шаблоны** и нажмите «Синхронизация с провайдером»:

![mailing-wa-template.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-template.png)

Данные из шаблона, которые понадобятся при создании рассылки в Mindbox:

- идентификатор шаблона:

![mailing-wa-ft-param.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-ft-param.png)

- переменные из сообщения в формате `{{v1}}`:

![mailing-wa-ft-message.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-ft-message.png)

## Создание рассылки в Mindbox

По шаблону можно отправить рассылку из Mindbox.

Для этого:

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» и выберите тип рассылки (массовая или автоматическая):

![trigger-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create1.png)

3. Выберите канал WhatsApp, папку и нажмите «Создать»:

![create-mailing-whatsapp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/create-mailing-whatsapp.png)

### Сообщение

![mailing-wa-mb-message.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-mb-message.png)

- **Отправитель** — создается при добавлении провайдера.
- **Название шаблона** — скопируйте идентификатор шаблона из Fasttrack.
- **Параметры шаблона** — заполните, если в шаблоне Fasttrack используются переменные:
  - **Ключ** — название переменной (часть без `{{}}`)
  - **Значение** — что подставлять вместо этой переменной в сообщении. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

## Отправка рассылки

Принцип отправки рассылки такой же как в остальных каналах:

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

Взаимодействие с рассылкой фиксируются с помощью [статусов](customer-message-statuses.md). В канале WhatsApp выдаются отправки, открытия и клики, а также неотправки и недоставки:

![mailing-wa-client.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-client.png)

* WhatsApp относится к Meta, деятельность которой признана экстремистской и запрещена на территории России.
