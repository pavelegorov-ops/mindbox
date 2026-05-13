---
title: Экспорт статусов рассылок
slug: "export-mailing-statuses"
source_url: "https://developers.mindbox.ru/docs/export-mailing-statuses"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:aac7eec6ea3969082beb74b598f9aea3366f3490f69127702ddb3b6df3cbfba8"
---

# Экспорт статусов рассылок

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md)

## Контракт экспорта статусов рассылок

**Пример запроса**

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}
Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "sinceDateTimeUtc": "<Дата и время самого раннего статуса (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Дата и время самого позднего статуса невключительно (UTC, YYYY-MM-DD hh:mm)>"
}
```

Во входных параметрах можно указать:

- Дату "от" (sinceDateTimeUtc) в формате UTC. Тогда в выгрузку попадут только статусы созданные в системе после этой даты
- Дату "до" (tillDateTimeUtc) в формате UTC. Тогда в выгрузку попадут только статусы созданные в системе до этой даты

## Формат ответа

```
{
  "status": "<Результат выполнения запроса: Success в случае успеха, ValidationError в случае ошибки пользователя, ProtocolError в случае ошибки интеграции, InternalServerError в случае недоступности сервера.>",
  "exportId": "<Идентификатор экспорта>",
  "isDuplicate": "<Вызван повторный запрос экспорта. Экспорт с аналогичными настройками уже формируется>",
  "exportResult": {
    "processingStatus": "<Статус готовности файла>",
    "cancellationReason": "<Причина отмены экспорта>",
    "urls": [
      "<Ссылка на файл с результатом>",
      "<Ссылка на файл с результатом>"
    ]
  }
}
```

## Формат выгружаемого файла

#### Описание базовых полей экспорта

```
{
  "customerMessageStatuses": [
    {
      "dateTimeUtc": "<Дата и время статуса рассылки>",
      "ids": {
        "id": "<Идентификатор статуса>"
      },
      "customerMessage": {
        "dateTimeUtc": "<Дата и время участия в рассылке в UTC>",
        "ids": {
          "id": "<Идентификатор участия в рассылке>"
        }
      },
      "mailing": {
        "name": "<Название рассылки>",
        "variantNum": "<Номер варианта рассылки>",
        "link": "<Ссылка>",
        "ids": {
          "id": "<Идентификатор рассылки>"
        },
        "notSentReason": {
          "name": "<Описание статуса, почему рассылка не отправилась>",
          "ids": {
            "systemName": "<Системное имя статуса, почему рассылка не отправилась>"
          }
        },
        "notDeliveredReason": {
          "name": "<Описание статуса, почему рассылка не доставилась>",
          "ids": {
            "systemName": "<Системное имя статуса, почему рассылка не доставилась>"
          }
        },
        "brand": {
          "ids": {
            "systemName": "<Системное имя бренда>"
          }
        },
        "channel": {
          "ids": {
            "systemName": "<Системное имя канала рассылки>"
          }
        }
      },
      "mailingSource": {
        "entityType": "<Тип сущности>",
        "entityId": "",
        "entityName": "<Имя сущности>"
      },
      "mailingStatus": {
        "ids": {
          "systemName": "<Системное имя статуса рассылки>"
        }
      }
    },
    {
      "dateTimeUtc": "<Дата и время статуса рассылки>",
      "ids": {
        "id": "<Идентификатор статуса>"
      },
      "customerMessage": {
        "dateTimeUtc": "<Дата и время участия в рассылке в UTC>",
        "ids": {
          "id": "<Идентификатор участия в рассылке>"
        }
      },
      "mailing": {
        "name": "<Название рассылки>",
        "variantNum": "<Номер варианта рассылки>",
        "link": "<Ссылка>",
        "ids": {
          "id": "<Идентификатор рассылки>"
        },
        "notSentReason": {
          "name": "<Описание статуса, почему рассылка не отправилась>",
          "ids": {
            "systemName": "<Системное имя статуса, почему рассылка не отправилась>"
          }
        },
        "notDeliveredReason": {
          "name": "<Описание статуса, почему рассылка не доставилась>",
          "ids": {
            "systemName": "<Системное имя статуса, почему рассылка не доставилась>"
          }
        },
        "brand": {
          "ids": {
            "systemName": "<Системное имя бренда>"
          }
        },
        "channel": {
          "ids": {
            "systemName": "<Системное имя канала рассылки>"
          }
        }
      },
      "mailingSource": {
        "entityType": "<Тип сущности>",
        "entityId": "",
        "entityName": "<Имя сущности>"
      },
      "mailingStatus": {
        "ids": {
          "systemName": "<Системное имя статуса рассылки>"
        }
      }
    }
  ]
}
```
