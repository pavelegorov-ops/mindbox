---
title: Экспорт журнала событий
slug: "export-event-log"
source_url: "https://developers.mindbox.ru/docs/export-event-log"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:90eacbbf3cb9516a777528bc40906d61b8b676983091280380932a64561983c2"
---

# Экспорт журнала событий

## Требования

- Подключенный модуль «Усиленная безопасность»;
- Настроенная [операция](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) с шагом «Экспорт — выгрузить журнал действий».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ae013e5-image_1.png "image (1).png")

Для создания данного шага необходимы права «Экспорт журнала событий», по умолчанию имеющиеся у роли «Владельцы».

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md)

## Контракт экспорта журнала событий

**Пример запроса**

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Accept: application/json
Content-Type: application/json
Authorization: SecretKey {Секретный ключ}

{
  "sinceDateTimeUtc": "<Дата и время самого раннего действия (UTC, YYYY-MM-DD hh:mm)>",
  "tillDateTimeUtc": "<Дата и время самого позднего действия невключително (UTC, YYYY-MM-DD hh:mm)>"
}
```

Во входных параметрах можно указать:

- Дату «от» в формате UTC. В выгрузку попадут только события, которые появились в журнале после этой даты;
- Дату «до» в формате UTC. Тогда в выгрузку попадут только события, которые появились в журнале до этой даты.

**Описание базовых полей журнала событий**

```
{
  "eventLogEntries": [
    {
      "loggedDateTimeUtc": "<Время события в формате UTC>",
      "staffId": "",
      "staffLogin": "<Логин персонала, совершившего действие>",
      "staffEmail": "",
      "staffIpAddress": "",
      "entityType": "<Название сущности>",
      "entityTypeDescription": "<Опциональное, описание сущности>", 
      "entityId": "",
      "entityLink": "<Ссылка на сущность>",
      "eventType": "<Название действия>", 
      "eventTypeDescription": "<Описание действия>",
      "comments": "<Комментарий>"
    }
  ]
}
```

## Обратная совместимость

Обратная совместимость значений полей экспорта не поддерживается.  
При возникновении проблем необходимо корректировать правила корреляции в SIEM.
