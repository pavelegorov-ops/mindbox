---
title: Экспорт клиентов из блоков сценариев
slug: "export-customers-from-scenario-blocks"
source_url: "https://developers.mindbox.ru/docs/export-customers-from-scenario-blocks"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:33fe1b545a40aaa5a7223d6200db779967c0ced48aa2af944eb15a655528f30e"
---

# Экспорт клиентов из блоков сценариев

## Требования

Настроенная [операция](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) с шагом «Экспорт — выгрузить клиентов из отчета прохождения сценария».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/486263740a9d074cade4697b28fd1f4e6b8682a010c7df7dff8d4b7de8282dd7-image.png)

## Общий контракт постановки задачи экспорта

Общий контракт постановки задачи экспорта описан [здесь](exports-overview.md#/).

## Контракт экспорта клиентов из отчета прохождения сценария

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Content-Type: application/json; charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}

{
  "sinceDate": "<Начало периода>",
  "tillDate": "<Конец периода>",
  "scenarioId": "<Идентификатор сценария>",
  "scenarioVersion": "<Номер версии сценария>",
  "blockId": "<Идентификатор блока>",
  "outputIndex": "<Номер выхода блока>",
  "onlyStartedInPeriod": "<Только попавшие в сценарий за этот период>"
}
```

Во входных параметрах можно указать:

- Дату «от». В выгрузку попадут только клиенты, прошедшие блок начиная с указанной даты.
- Дату «до». В выгрузку попадут только клиенты, прошедшие блок до указанной даты.
- Номер выхода блока. 1 — соответствует ветке «Да»; 2 — соответствует ветке «Нет».
- Задать настройку, которая выгрузит только тех клиентов, которые попали в сценарий за указанный период. Возможные значения: true, false.

**Как узнать идентификатор сценария и идентификатор блока?**

Способ 1: выполнить [экспорт сценариев](export-scenarios.md#/).

Способ 2: посмотреть в URL сценария. Для этого перейдите в сценарий и нажмите на нужный блок.

https://[название_проекта].mindbox.ru/scenarios/[идентификатор_сценария]/view?blockId=[идентификатор_блока]

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d896907d42b631f2c9b5b3c2d5d6b6de5d3482ed5eddf772bf4237122c509e50-image.png)

**Пример тела ответа**

```
{
  "status": "<Результат выполнения запроса: Success в случае успеха, ValidationError в случае ошибки пользователя, ProtocolError в случае ошибки интеграции, InternalServerError в случае недоступности сервера.>",
  "exportId": "<Идентификатор экспорта, который нужно передать в следующем запросе>",
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

По полученному в ответе операции `exportId`, файл с выгрузкой клиентов можно скачать в разделе «Задачи» или выгрузить по API.

Для выгрузки по API повторно вызовите операцию, указав в теле запроса полученный при предыдущем запросе exportId.

```
https://api.mindbox.ru/v3/operations/sync?endpointId={endpointId}&operation={operation}

Content-Type: application/json; charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}

{
  "exportId": "<Идентификатор экспорта>"
}
```

## Формат выгружаемого файла

В файле будут перечислены MindboxId клиентов, прошедших блок сценария.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a8f571be2560ffb56038775d760aa23fbf5f7e85ff2ed6ac8ab26f7165e073f7-image.png)
