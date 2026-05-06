---
title: Интеграция Mindbox с TextBack
slug: "integration-mindbox-textback"
source_url: "https://help.mindbox.ru/docs/integration-mindbox-textback"
vcs_path: "integration-mindbox-textback.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:cdb39b20bc0ff00429bea12b579a94c4385b6d4cb31bb915701e51d6bc851c2e"
---

# Интеграция Mindbox с TextBack

[TextBack](https://textback.ru/) — это платформа для общения с клиентами в WhatsApp*, Telegram или любом другом мессенджере.

**Возможности интеграции Mindbox с TextBack**

Доступна двусторонняя интеграция:

- TextBack → Mindbox — передача событий клиентов и изменение данных профиля.
- Mindbox → TextBack — отправка рассылок через вебхуки.

## Передача данных из TextBack в Mindbox

Из TextBack можно вызывать:

- Выдачу действия клиенту в Mindbox;
- Редактирование поля в карточке клиента в Mindbox.

От задачи зависит набор создаваемых сущностей, но для передачи данных в любом случае нужно создать интеграцию.

### Создание интеграции

Добавьте [интеграцию](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) по пресету «Другое».  
Задайте название интеграции, остальные настройки — по умолчанию:

![Снимок экрана 2024-06-26 в 07.27.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2007.27.38.png)

### Для выдачи действий

С помощью действий можно фиксировать статус отправленного сообщения. Для настройки нужно создать:

1. Шаблон действия;
2. Дополнительные поля для данных по действию (сообщению);
3. Операцию, в которой это действие выдается.

#### Создание шаблона действия

Добавьте [шаблон действия](template-create.md) для выдачи статуса рассылки:

![textback-create-action.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/textback-create-action.png)

#### Создание дополнительных полей

Добавьте [дополнительные поля](additional-data.md) для передачи в действии названия рассылки и ее статуса.

![Снимок экрана 2024-06-26 в 07.45.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2007.45.23.png)

![Снимок экрана 2024-06-26 в 07.46.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2007.46.31.png)

- *Для сущности* — Действие клиента
- *Тип поля* — Перечисление
- *Создавать значение перечисления, если не найдено* — включить

#### Создание операции

Добавьте [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sozdanie-operacii-v3) для выдачи действия (операцию нужно создать в той же папке, в которой был создан выдаваемый шаблон действия):

![Снимок экрана 2024-06-26 в 07.54.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2007.54.19.png)

### Для заполнения данных клиента

Для заполнения поля клиента, нужно:

1. Настроить дополнительное поле для клиента или определить, какое основное поле будет отвечать за данные о событии в TextBack;
2. Настроить операцию для редактирования поля.

#### Создание дополнительных полей

Добавьте нужные [дополнительные поля](additional-data.md), например, для отметки о наличии контакта в WhatsApp

![Снимок экрана 2024-06-26 в 08.03.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.03.47.png)

#### Создание операции

Добавьте [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sozdanie-operacii-v3) для заполнения созданного поля:

![Снимок экрана 2024-06-26 в 08.07.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.07.30.png)

## Передача данных из Mindbox в TextBack (отправка рассылок)

Отправка осуществляется через вебхук. Для настройки нужно:

1. Создать интеграцию для вебхуков;
2. Создать вебхук с рассылкой;
3. Настроить вызов вебхука через сценарий.

### Создание интеграции

Добавьте [интеграцию](webhooks.md#sozdanie-tochki-integracii) по пресету «Интеграция для вебхуков»:

- Общие настройки:
  - URL — `https://api.textback.io`
  - Ограничение скорости отправки запросов в секунду — 8
- Заголовки:
  - `Content-Type` — `application/json` — Публичный
  - `Authorization` — `Bearer {сгенерированный токен из раздела «Интеграции» ЛК TextBack}` — Секретный
  - `User-Agent` — `Mindbox` — Публичный

![Снимок экрана 2024-06-26 в 08.31.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.31.35.png)

### Создание вебхука

Добавьте [вебхук](webhooks.md#sozdanie-vebhuka) в созданной интеграции:

- Метод — POST
- Корневой URL — `https://api.textback.io`
- URL — можно дополнить:
  - `/api/messages` — метод для отправки сообщения в textBack
  - `transactionalId=${WebhookRequest.TransactionalId}` — ключ идемпотентности для повторных попыток подключения при получении ошибки (можно добавить по кнопке из интерфейса создания вебхука)

![Снимок экрана 2024-06-26 в 08.44.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.44.51.png)

- Добавленные заголовки:
  - ClientPhone — `${Recipient.MobilePhone}`
  - ClientId — `${Recipient.Id}`

![Снимок экрана 2024-06-26 в 08.45.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.45.11.png)

- Заполнение тела запроса проходит по [документации](https://buildin.ai/textback/share/44cca4f6-1750-469d-850f-bb9189b84964).
  - Для remoteAddress используется параметр Mindbox — `${Recipient.MobilePhone}`
  - Дополнительно в переменные можно добавить другие параметры из [шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

![Снимок экрана 2024-06-26 в 08.45.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.45.38.png)

Сохраните вебхук и добавьте новую пару ключ-значение: webhookId и идентификатор **созданного** вебхука из адресной строки:

![Снимок экрана 2024-06-26 в 08.49.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-26%20%D0%B2%2008.49.51.png)

Этот заголовок нужен для того, чтобы упростить процесс диагностики со стороны TextBack.

### Создание сценария

Рассылки через вебхуки отправляются с помощью [сценариев](what-is-workflow.md).

Настройте логику механики в сценарии; для отправки рассылки в блоке «Группа шагов» укажите вызов созданного вебхука:

![textback-webhook.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/textback-webhook.png)

Ответ сервиса и ошибки можно проверить в [логах вызова вебхуков](webhook-logs).

Рекомендуем сначала протестировать отправку на тестовом пользователе. Для этого задайте любой его идентификатор через блок [Условие](workflow-conditions.md).

* WhatsApp относится к Meta, деятельность которой признана экстремистской и запрещена на территории России.
