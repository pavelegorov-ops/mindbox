---
title: Как отправить рассылку в WhatsApp через Edna Pulse
slug: "edna-pulse"
source_url: "https://help.mindbox.ru/docs/edna-pulse"
vcs_path: "edna-pulse.md"
toc_path:
  - Рассылки
  - Уведомления и мессенджеры
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:79edf4b378e64e0822dc7fa4771a2f97adb03d4e6228e1b1fff4336a0c807680"
---

# Как отправить рассылку в WhatsApp через Edna Pulse

## Подключение WhatsApp

1. Создайте личный кабинет в [Edna Pulse](https://edna.ru/pulse/) — провайдере для отправки сообщений в WhatsApp*.
2. [Создайте канал](https://docs-pulse.edna.ru/docs/channel/whatsapp/channel-whatsapp-signup) WhatsApp* в Edna Pulse:

![edna-channel.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-channel.png)

Автоматически при создании канала будет создан [каскад](https://docs-pulse.edna.ru/docs/cascades). Его идентификатор понадобится для настроек подключения.

3. Перейдите в раздел Mindbox **Настройки** → **Рассылки** → **Соединения** и добавьте соединение для WhatsApp*:

![whatsapp-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/whatsapp-connection.png)

4. На странице добавления соединения укажите настройки соединения:

![edna-create-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-create-connection.png)

- **Бренд** — выберите нужный бренд. Актуально для [мультибрендовых](https://help.mindbox.ru/docs/multibrand) проектов.
- **Провайдер** — Edna Pulse.
- **Идентификатор каскада**.

Как найти идентификатор каскада

Перейдите в раздел **«Каскады»** в Edna Pulse и найдите каскад созданного ранее канала. Его название будет соответствовать отправителю канала.

Отправитель канала:  
![edna-channel-name.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-channel-name.png)

ID и название каскада:  
![edna-cascade-name.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-cascade-name.png)

- **API-ключ** — введите ключ API. Узнать его можно в разделе **Интеграция** → **Настройки** в личном кабинете Edna Pulse. [Подробнее](https://docs-pulse.edna.ru/docs/integrations/api-settings).

5. Настройте сервер для получения [статусов рассылок](customer-message-statuses.md):

Выполнение запроса перенаправит все входящие сообщения бизнес-аккаунта WhatsApp* и статусы исходящих сообщений в Mindbox. Убедитесь, что вы не собираете эти данные в других системах.

Выполните прописанные на странице HTTP-запросы с использованием того же **API-ключа**, который указывался при подключении соединения.

6. [Включите модуль](billing-modules.md#vklyuchit-i-vyklyuchit-modul) «Уведомления и мессенджеры».

## Создание шаблона в Edna Pulse

Диалог с клиентом в WhatsApp* необходимо начинать с сообщения с согласованным шаблоном. Для того, чтобы создать и отправить шаблон на согласование, в Edna Pulse перейдите в **Настройки** → **Шаблоны**. Создайте операторский шаблон и согласуйте его по [инструкции](https://docs-pulse.edna.ru/docs/template/whatsapp/operator-template).

В рассылках могут использоваться шаблоны только в статусе **«Активный»**.

## Создание рассылки в Mindbox

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» и выберите тип рассылки (массовая или автоматическая):

![trigger-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create1.png)

3. Выберите канал WhatsApp, папку и нажмите «Создать»:

![create-mailing-whatsapp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/create-mailing-whatsapp.png)

4. Перейдите к настройке сообщения. Выберите отправителя, созданного при настройке соединения с Edna Pulse.

![edna-message.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message.png)

Дальнейшие настройки будут отличаться в зависимости от выбранного типа сообщения.

На стороне Edna Pulse шаблон сообщения определяется по тексту сообщения (кроме сообщений с одноразовым паролем и Flow).

### Текст

![edna-message-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-text.png)

Доступные элементы:

- **Текст сообщения**
- **Тип заголовка** (текст, изображение, документ или видео). Подробнее о технических требованиях к заголовкам [в документации Edna Pulse](https://docs-pulse.edna.ru/docs/template/whatsapp/template-header).
- **Подпись**
- **Кнопки**. Максимальная длина текста кнопки — 20 символов.

Кнопки могут быть трех типов:

- **Ссылка для перехода**. Динамическая часть ссылки может использоваться с параметрами [шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).
- **Номер телефона**, который набирается для звонка при нажатии кнопки.
- **Быстрый ответ**. Необходимо указать **код кнопки** — дополнительное значение, которое возвращается в ответе, если получатель нажал на кнопку. Используется для сбора аналитики на стороне Edna Pulse.

### Одноразовый пароль

Сообщение с одноразовым паролем и кнопкой копирования.

![edna-message-password.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-password.png)

- **Текст сообщения**
- **Идентификатор шаблона**. Найдите нужный шаблон в разделе **«Шаблоны»** в Edna Pulse и скопируйте его идентификатор:

![edna-template-id.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-template-id.png)

### Сообщение с вложением

Отправляйте клиентам **медиафайлы**:

- Изображение
- Документ
- Видео-сообщение
- Аудио-сообщение

![edna-message-media.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-media.png)

Для таких сообщений необходимы:

- **Подпись** — необходимо для описания вложения.
- **Ссылка на вложение** — укажите ссылку или выберите вложение из галереи картинок.

Ознакомиться с техническими требованиями к вложениям можно [в документации Edna Pulse](https://docs-pulse.edna.ru/docs/api/messages/sending#%D1%82%D0%B8%D0%BF%D1%8B-%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9).

### Местоположение

Отправьте данные о местоположении: например, адрес мероприятия или вашего офиса.

![edna-message-location.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-location.png)

- **Долгота**. Диапазон значений — от -180 до 180.
- **Широта**. Диапазон значений — от -90 до 90.
- Адрес и название места

### Список элементов

Список элементов представляет собой интерактивное меню WhatsApp*, в котором клиент может выбрать варианты ответа.

![edna-message-listpicker.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-listpicker.png)

- **Текст сообщения**
- **Текст кнопки**. Максимальная длина — 20 символов.
- **Заголовок секции**, который отображается клиенту.
- **Список объектов**
  - Идентификатор элемента
  - Заголовок и подзаголовок элемента (до 24 символов с учетом пробелов)

### Flow

Сообщение, содержащее [WhatsApp Flows](https://developers.facebook.com/docs/whatsapp/flows)*. Подробнее о настройке Flows [в документации Edna Pulse](https://docs-pulse.edna.ru/docs/additional-info/whatsapp/wa-flows).

![edna-message-flow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/edna-message-flow.png)

- **Текст сообщения**
- **Идентификатор Flow** — присваивается в WhatsApp Manager в момент создания Flow.
- **Текст кнопки**, после нажатия на которую запускается Flow.
- **Тип взаимодействия** — с запросом к конечной точке или без. Для запроса к конечной точке необходимо настроить точку [по инструкции Meta](https://developers.facebook.com/docs/whatsapp/flows/guides/implementingyourflowendpoint)*.
- **Идентификатор экрана** (необязательно), который первым будет отображаться во Flow.

## Отслеживание переходов

Mindbox не может отслеживать клики по ссылкам, которые прописаны в шаблоне на стороне Edna Pulse. Для отслеживания переходов по ссылкам используйте [сокращатель Mindbox](shorten-url-sms.md).

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

Взаимодействие с рассылкой фиксируются с помощью [статусов](customer-message-statuses.md). В канале WhatsApp* выдаются отправки, открытия и клики, а также неотправки и недоставки:

![mailing-wa-client.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mailing-wa-client.png)

* WhatsApp относится к Meta, деятельность которой признана экстремистской и запрещена на территории России.
