---
title: Экспорт сценариев
slug: "export-scenarios"
source_url: "https://developers.mindbox.ru/docs/export-scenarios"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:b4ff5160d0aa1ce7b4a76240e6930c0df67bf309b18efa01df625a997710a5ad"
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
