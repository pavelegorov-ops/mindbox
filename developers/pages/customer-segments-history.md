---
title: История сегментов клиентов
slug: "customer-segments-history"
source_url: "https://developers.mindbox.ru/docs/customer-segments-history"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:eb384ba84853fcb5859e50ae91307f6714878dd7251b037b492d853087253a41"
---

# История сегментов клиентов

Датасет истории сегментов клиентов. Каждый вход клиента в сегмент и каждый выход из сегмента будут представлены отдельными записями в датасете.

---

### exports.CDP.CustomerSegmentHistory

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int64 | Идентификатор события | 2578932 |
| unmergedCustomerId | int64 | Внутренний идентификатор клиента на момент события | 12381 |
| segmentationId | int | Внутренний идентификатор сегментации | 15 |
| segmentId | int (nullable) | Внутренний идентификатор сегмента. NaN — если произошёл выход из сегмента | 23 |
| calculatedDateTimeUtc | datetime | Дата в формате UTC, когда клиент попал/вышел из сегмента | 2024-10-15 10:00:00.000 |
| isDeleted | bool (nullable) | Признак, что запись была удалена в Mindbox | True |
| rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 11:00:00.000 |
