---
title: Интеграция Mindbox c Chat2Desk для отправки сообщений
slug: "chat2desk-integration"
source_url: "https://help.mindbox.ru/docs/chat2desk-integration"
vcs_path: "chat2desk-integration.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:2718c6853da6890f151450381446e08987557c7dd3297ac773e455676ab9aa46"
---

# Интеграция Mindbox c Chat2Desk для отправки сообщений

[Chat2Desk](https://chat2desk.com) — чат-центр для работы и коммуникации с клиентами в мессенджерах, например, WhatsApp* и Telegram.  
Внешние системы могут взаимодействовать с чат-центром по API. API-методы и параметры описаны в [документации](https://documenter.getpostman.com/view/8899980/UVC8BRBo#intro) Chat2Desk.

## Ограничение интеграции

При помощи API можно взаимодействовать с Chat2Desk без использования дополнительных платных функций чат-центра, таких как туннели и скрипты. При необходимости автоматической отправки информации из Chat2Desk понадобится подключение платных функций.

## Создание дополнительных полей

На стороне Mindbox необходимо хранить ID чата с клиентом для каждого мессенджера. Для хранения ID необходимо создать дополнительные поля для сущности **Клиент** согласно [инструкции](additional-data.md).

Пример настройки дополнительного поля для ID чата в WhatsApp:

1. В поле **Для сущности** выберите **Клиент**.
2. В поле **Имя** введите «Chat2Desk. ID в WhatsApp».
3. В поле **Системное имя** введите «ch2dWhatsAppID».
4. В поле **Тип** поля выберите **Строковый**.

![Снимок экрана 2023-08-04 в 11.59.12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2011.59.12.png)

## Создание точки интеграции для вебхуков

Перед настройкой вебхуков необходимо создать точку интеграции согласно [инструкции](webhooks.md#sozdanie-tochki-integracii). Для интеграции с Chat2Desk укажите следующие параметры:

1. В разделе **Общие настройки**, в поле **URL**, введите «https://api.chat2desk.com».
2. В поле **Ограничение скорости отправки запросов в секунду** введите «10».
3. В разделе **Заголовки** выполните следующие действия:

- Для ключа **Content-Type** выберите значение **application/json** и тип **Публичный**.
- Для ключа **User-Agent** выберите значение Mindbox и тип **Публичный**.
- Для ключа **Authorization** выберите значение **API токен аккаунта** и тип **Секретный**.

![Снимок экрана 2023-08-04 в 12.02.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2012.02.08.png)

Чтобы узнать API токен аккаунта, авторизуйтесь на платформе Chat2Desk как администратор и перейдите в раздел **Settings** → **API**.

## Создание вебхука для проверки наличия клиента в Chat2Desk

Чтобы проверить наличие клиента в Chat2Desk по номеру телефона, необходимо создать вебхук согласно [инструкции](webhooks.md#sozdanie-vebhuka) с использованием метода [GET clients](https://documenter.getpostman.com/view/8899980/UVC8BRBo#542073df-3443-43f5-b322-777dd475ee9e).

1. В разделе **Общие настройки**, в поле **Системное имя**, введите «ch2dCheckCustomer».
2. В поле **Метод** выберите **GET**.
3. В поле **URL** введите: `/v1/clients?phone=${Recipient.MobilePhone}&${WebhookRequest.TransactionalId}`
4. В разделе **Заголовки** выберите **Унаследованы из интеграции**.
5. В разделе **Настройки ответа** включите **Принимать ответы в формате JSON** и [добавьте](workflows-webhook-responses.md) одну переменную для получения ID клиента в Chat2Desk:

- В поле **Название** введите «ch2dId».
- В поле **Путь в теле ответа** введите «data[0].id».

![Снимок экрана 2023-08-08 в 11.18.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.18.36.png)

## Создание вебхука для импорта клиента в Chat2Desk

Чтобы импортировать клиента в Chat2Desk, необходимо создать вебхук согласно [инструкции](webhooks.md#sozdanie-vebhuka) с использованием метода [POST clients](https://documenter.getpostman.com/view/8899980/UVC8BRBo#7d243850-a5aa-4d0f-ae29-7759db9a95ff).

1. В разделе **Общие настройки**, в поле **Системное имя**, введите «ch2dImportCustomer».
2. В поле **Метод** выберите **POST**.
3. В поле **URL** введите: `/v1/clients?transactionId=${WebhookRequest.TransactionalId}`
4. В разделе **Заголовки** выберите **Унаследованы из интеграции**.
5. В разделе **Настройки ответа** включите **Принимать ответы в формате JSON** и [добавьте](workflows-webhook-responses.md) одну переменную для получения ID клиента в Chat2Desk:

- В поле **Название** введите «ch2dId».
- В поле **Путь в теле ответа** введите «data.id».

![Снимок экрана 2023-08-08 в 11.28.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.28.04%281%29.png)

## Создание вебхуков для отправки сообщений в Chat2Desk

Чтобы отправлять сообщения в Chat2Desk, необходимо создать вебхук согласно [инструкции](webhooks.md#sozdanie-vebhuka) с использованием метода [POST messages](https://documenter.getpostman.com/view/8899980/UVC8BRBo#5a55b9b4-640a-4095-8d7a-2695605b0700).

В инструкции настраивается отправка HSM-шаблона в WhatsApp:

1. В разделе **Общие настройки**, в поле **Системное имя**, введите «ch2dSendWATemplate».
2. В поле **Метод** выберите **POST**.
3. В поле **URL** введите `/v1/messages`
4. В разделе **Заголовки** выберите **Унаследованы из интеграции**.
5. В разделе **Тело запроса** вставьте следующее:

```
{
    "text": "ID HSM шаблона",
    "client_id": ${Дополнительное поле клиента с Chat2Desk ID для WhatsApp}
}
```

![Снимок экрана 2023-08-08 в 11.20.39.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.20.39.png)

## Создание сценария для отправки сообщений

Создайте [сценарий](what-is-workflow.md) для отправки сообщения клиенту. Сценарий на основании выданного события показан на схеме:

![Снимок экрана 2023-08-08 в 11.40.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.40.33.png)

Описание логики работы сценария:

1. Запуск — выберите событие для попадания в сценарий в зависимости от задачи.
2. Проверяем, заполнен ли [идентификатор в мессенджере](chat2desk-integration.md#sozdanie-dopolnitelnyh-polej).
3. Если заполнен, то [отправляем сообщение](chat2desk-integration.md#sozdanie-vebhukov-dlya-otpravki-soobshenij-v-chat2desk) с помощью вебхука, если нет — отправляем вебхук для [проверки наличия](chat2desk-integration.md#sozdanie-vebhuka-dlya-proverki-nalichiya-klienta-v-chat2desk) клиента на стороне Chat2Desk.
4. Проверяем ответ вебхука: ![Снимок экрана 2023-08-08 в 11.42.49.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.42.49.png)

- Если клиент есть, [записываем](workflows-webhook-responses.md) полученный в ответе идентификатор в карточку клиента: ![Снимок экрана 2023-08-08 в 11.45.00.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.45.00.png) И также отправляем сообщение.
- Если клиент не был найден, отправляем вебхук для [импорта клиента в Chat2Desk](chat2desk-integration.md#sozdanie-vebhuka-dlya-importa-klienta-v-chat2desk) и проверяем успешность вызова: ![Снимок экрана 2023-08-08 в 11.51.37.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-08%20%D0%B2%2011.51.37.png) После [записываем](workflows-webhook-responses.md) полученный в ответе идентификатор в карточку клиента и также отправляем сообщение.

* WhatsApp относится к Meta, деятельность которой признана экстремистской и запрещена на территории России.
