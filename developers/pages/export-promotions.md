---
title: Экспорт промоакций
slug: "export-promotions"
source_url: "https://developers.mindbox.ru/docs/export-promotions"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:1e14f35c8ddbb7d6be2bc1d10ae5896e4badfc661ba25c924714ad9d5251b357"
---

# Экспорт промоакций

## Общий контракт постановки задачи экспорта

Способ постановки задачи экспорта описан [здесь](exports-overview.md).

## Контракт экспорта промоакций

Во входных параметрах можно указать:

- Дату в формате UTC. Тогда в выгрузку попадут только промоакции, которые изменялись после этой даты
- externalID сегмента промоакций, если таковой не был выбран в настройке операции

В выгрузку не попадут промоакции в статусе "В разработке".

## Формат выгружаемого файла

**Описание базовых полей экспорта**

```
{
  "promotions": [
    {
      "ids": {
        "externalId": "<Внешний идентификатор промоакции>"
      },
      "name": "<Название промоакции>",
      "description": "<Описание промоакции>",
      "startDateTimeUtc": "<Дата старта промоакции>",
      "endDateTimeUtc": "<Дата окончания промоакции>",
      "state": "Paused/Archived/Execution",
      "customFields": {
        "customField1" "<Значение поля>"
      },
      "products": {
        "includedSegments": [{
          "segmentation": {
            "ids": {
              "externalId": "<Внешний идентификатор сегментации>"
            }
          },
          "segment": {
            "ids": {
              "externalId": "<Внешний идентификатор сегмента>"
            }
          }
        }],
        "excludedSegments": [{
          "segmentation": {
            "ids": {
              "externalId": "<Внешний идентификатор сегментации>"
            }
          },
          "segment": {
            "ids": {
              "externalId": "<Внешний идентификатор сегмента>"
            }
          }
        }]
      },
      "areas": [
        {
          "ids": {
            "externalId": "<Внешний идентификатор зоны>"
          }
        },
        {
          "ids": {
            "externalId": "<Внешний идентификатор зоны>"
          }
        }
      ],
      "pointsOfContact": [
        {
          "ids": {
            "externalId": "<Внешний идентификатор точки контакта>"
          }
        },
        {
          "ids": {
            "externalId": "<Внешний идентификатор точки контакта>"
          }
        }
      ]
    }
  ]
}
```
