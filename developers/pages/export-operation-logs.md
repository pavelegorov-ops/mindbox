---
title: Экспорт логов операций
slug: "export-operation-logs"
source_url: "https://developers.mindbox.ru/docs/export-operation-logs"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:93b44aaf86f7d61013a9c8a275eb9b5efe56a55ba3a267a8de62e032c023dbb4"
---

# Экспорт логов операций

## Требования

Настроенная [операция](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) с шагом «Экспорт — Выгрузить логи операций».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/36c42f7-__2023-06-09__14.32.21.png)

Для доступа к файлу экспорта нужна пермиссия «Экспорт логов интеграций», по умолчанию имеющаяся у роли «Владельцы».

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md)

## Контракт экспорта логов операций

**Пример запроса**

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "exportId": "<Идентификатор экспорта>",
  "sinceDateTimeUtc": "<Начальная дата и время вызова операции (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Конечная дата и время вызова операции невключительно (UTC, YYYY-MM-DD hh:mm)>",
  "resultState": "<Результат выполнения операции>",
  "hasErrors": "<Были ошибки?>",
  "endpoint": {
    "ids": {
      "externalId": "<Внешний идентификатор точки интеграции>"
    }
  },
  "operations": [
    {
      "ids": {
        "systemName": "<Системное имя операции>"
      }
    },
    {
      "ids": {
        "systemName": "<Системное имя операции>"
      }
    }
  ]
}
```

Во входных параметрах можно указать:

- Дату «от» в формате UTC. В выгрузку попадут только вызовы, которые появились в логах после этой даты.
- Дату «до» в формате UTC. В выгрузку попадут только вызовы, которые появились в логах до этой даты.
- Результат выполнения операции (completed|failed|processing).
- Были ли ошибки при вызове (true|false).
- Системные имена интересующих операций и точек интеграций.

**Описание базовых полей логов операций**

- OperationLogTransactionId: Уникальный идентификатор вызова
- OperationLogStartDateTimeUtc: Время вызова в UTC
- OperationLogEndDateTimeUtc: Время выполнения в UTC
- OperationLogOperationSystemName: Системное имя операции
- OperationLogOperationName: Название операции
- OperationLogEndpointExternalId: Системное имя точки интеграци
- OperationLogIntegrationName: Название точки интеграци
- OperationLogHasErrors: Наличие ошибок при вызове или выполнении операции (true|false). Для неуспешных вызовов всегда значение true, для успешных может быть true, если при выполнении операции возникли валидационные ошибки, которые не блокируют выполнение сценария.
- OperationLogErrorMessages: Текст ошибки
- OperationLogDevice: [DeviceUUID](https://help.mindbox.ru/docs/deviceuuid) из вызова операции. Может отсутствовать
- OperationLogStatus: Статус выполнения операции (completed|failed|processing)
- OperationLogHttpMethod: HTTP-метод вызова
- OperationLogUrl: URL-адрес вызова
- OperationLogRequestHeaders: Заголовки вызова
- OperationLogRequestBody: Тело вызова
- OperationLogHTTPStatusCode: Код ответа
- OperationLogResponseHeaders: Заголовки ответа
- OperationLogResponseBody: Тело ответа
