---
title: Экспорт логов вебхуков
slug: "export-webhook-logs"
source_url: "https://developers.mindbox.ru/docs/export-webhook-logs"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:7ad91e3e1ac1888d5f52950cee67f308a23ffaf3a5ac124bedcacaab8b31926a"
---

# Экспорт логов вебхуков

## Требования

Настроенная [операция](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) с шагом «Экспорт — Выгрузить логи вебхуков».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/23ecc9e-image1.png)

Для доступа к файлу экспорта нужна пермиссия «Экспорт логов интеграций», по умолчанию имеющаяся у роли «Владельцы».

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md)

## Контракт экспорта логов вебхуков

**Пример запроса**

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "exportId": "<Идентификатор экспорта>",
  "sinceDateTimeUtc": "<Начальная дата и время вызова вебхука (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Конечная дата и время вызова вебхука невключительно (UTC, YYYY-MM-DD hh:mm)>",
  "isSuccessful": "<Выполнено успешно?>",
  "webhooks": [
    {
      "ids": {
        "id": "<Идентификатор вебхука>"
      }
    },
    {
      "ids": {
        "id": "<Идентификатор вебхука>"
      }
    }
  ]
}
```

Во входных параметрах можно указать:

- Дату «от» в формате UTC. В выгрузку попадут только вызовы, которые появились в логах после этой даты;
- Дату «до» в формате UTC. Тогда в выгрузку попадут только вызовы, которые появились в логах до этой даты;
- Выгружать ли только успешные или только ошибочные вызовы;
- Идентификаторы вебхуков, которые можно найти в их URL  
  ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/f384fba-image.png)

**Описание базовых полей логов вебхуков**

- WebhookLogTransactionId: Уникальный идентификатор вызова хука. Совпадает для повторных попыток отправки вебхука
- WebhookLogStartDateTimeUtc: Время вызова вебхука в UTC
- WebhookLogWebhookSourceId Уникальный идентификатор блока сценария, из которого вызван вебхук. Включает id сценария, версию и id блока сценария
- WebhookLogWebhookSourceType: Тип механики, из которой вызван вебхук. Сейчас поддерживается только блок сценария
- WebhookLogWebhookSourceName: Название механики, из которой вызван вебхук.
- WebhookLogWebhookSourceUrl: Ссылка на механику, из которой вызван вебхук.
- WebhookLogWebhookId: Уникальный идентификатор вебхука
- WebhookLogWebhookName: Название вебхука
- WebhookLogIntegrationId: Уникальный идентификатор интеграции вебхука
- WebhookLogIntegrationName: Название интеграции вебхука
- WebhookLogStatus: Результат вызова вебхука. Успех или ошибка
- WebhookLogHttpMethod: HTTP метод вебхука
- WebhookLogUrl: URL адрес вебхука
- WebhookLogRequestHeaders: Заголовки вызова вебхука
- WebhookLogRequestBody: Тело вызванного вебхука
- WebhookLogHTTPStatusCode: Код ответа вебхука
- WebhookLogResponseHeaders: Заголовки ответа вебхука
- WebhookLogResponseBody: Тело ответа вебхука
- WebhookLogRetryNumber: Номер попытки вызова вебхука
