---
title: Экспорт рассылок
slug: "export-mailings"
source_url: "https://developers.mindbox.ru/docs/export-mailings"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:99867e70ca41cdd4f4e1cbe8c0eb57cd34aab6e8bf3569e8bcc0e5a9a33da59a"
---

# Экспорт рассылок

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md)

## Контракт экспорта рассылок

**Пример запроса**

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "sinceDateTimeUtc": "<Начальная дата и время изменения рассылки (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Конечная дата и время изменения рассылки невключительно (UTC, YYYY-MM-DD hh:mm)>"
}
```

Во входных параметрах можно указать:

- Дату "от" в формате UTC. Тогда в выгрузку попадут только рассылки, которые изменились или были созданы в системе после этой даты
- Дату "до" в формате UTC. Тогда в выгрузку попадут только рассылки, которые изменились или были созданы в системе до этой даты

## Формат выгружаемого файла

**Описание базовых полей экспорта**

```
{
  "mailings": [
    {
      "name": "<Название рассылки>",
      "mailingUtmName": "<Название рассылки для использования в UTM метке>",
      "type": "<Тип рассылки>",
      "channel": "<Канал отправки рассылки>",
      "creationDateTimeUtc": "<Дата создания рассылки в системе в UTC>",
      "lastChangedDateTimeUtc": "<Дата последнего изменения рассылки в UTC>",
      "ids": {
        "systemName": "<Системное имя рассылки>",
        "id": "<Идентификатор Mindbox>"
      },
      "subscriptionTopic": {
        "name": "<Название тематики>",
        "ids": {
          "externalId": "<Системное имя тематики>"
        }
      },
      "folder": {
        "name": "<Название папки>",
        "ids": {
          "systemName": "<Системное имя папки>"
        }
      },
      "brand": {
        "name": "<Название бренда>",
        "ids": {
          "systemName": "<Системное имя бренда>"
        }
      },
      "utm": {
        "utmSource": "<Значение UTM-метки utm_source>",
        "utmMedium": "<Значение UTM-метки utm_medium>",
        "utmCampaign": "<Значение UTM-метки utm_campaign>",
        "utmContent": "<Значение UTM-метки utm_content>"
      },
      "tags": [
        {
          "name": "<Название тега>",
          "ids": {
            "systemName": "<Системное имя тега>"
          }
        },
        {
          "name": "<Название тега>",
          "ids": {
            "systemName": "<Системное имя тега>"
          }
        }
      ]
    }
  ]
}
```

Тип рассылки (`type`) может иметь три значения:

- `mass` - массовая рассылка
- `trigger` - триггерная рассылка
- `transaction` - транзакционная рассылка
