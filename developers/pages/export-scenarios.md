---
title: Экспорт сценариев
slug: "export-scenarios"
source_url: "https://developers.mindbox.ru/docs/export-scenarios"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0ddbaa9bdcf8e091f7f8f1a565237d08e946b495e9050f7d7b7ea6c8e45ed2bd"
---

# Экспорт сценариев

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md).

## Контракт экспорта сценариев

**Пример запроса**

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "sinceDateTimeUtc": "<Начальная дата и время изменения сценария (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Конечная дата и время изменения сценария невключительно (UTC, YYYY-MM-DD hh:mm)>"
}
```

Во входных параметрах можно указать:

- Дату "от" в формате UTC. Тогда в выгрузку попадут только сценарии, которые изменились или были созданы в системе после этой даты.
- Дату "до" в формате UTC. Тогда в выгрузку попадут только сценарии, которые изменились или были созданы в системе до этой даты.

## Формат выгружаемого файла

**Описание базовых полей экспорта**

```
{
  "workflows": [
    {
      "name": "<Имя сценария>",
      "id": "",
      "versions": [
        {
          "version": "<Номер версии сценария>",
          "operationStepBlocks": [
            {
              "name": "<Название блока>",
              "id": ""
            }
          ]
        }
      ]
    }
  ]
}
```
