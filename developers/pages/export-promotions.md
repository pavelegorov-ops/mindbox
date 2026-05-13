---
title: Экспорт промоакций
slug: "export-promotions"
source_url: "https://developers.mindbox.ru/docs/export-promotions"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6f17954a7717f8328617768ccc7eb3d89e0287a56b4b6f4b7e5ffec30ad8d52f"
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
