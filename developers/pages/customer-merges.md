---
title: Объединения клиентов
slug: "customer-merges"
source_url: "https://developers.mindbox.ru/docs/customer-merges"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:d355b13331d194aa104ba4f06e15d3333663df0ed1a3c6afe6fa8d60427503ac"
---

# Объединения клиентов

События объединений клиентов

---

### exports.CDP.MergedCustomers

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| unmergedCustomerId | Int64 | Идентификатор клиента до объединения | 123812 |
| mergedCustomerId | Int64 | Идентификатор клиента после объединения | 134511 |
| dateTimeUtc | DateTime | Время объединения клиентов в формате UTC | 2024-08-21 10:10:10.000 |
| _isDeleted | Bool | Признак, что событие было удалено (не автоудалением!) в Mindbox | True |
| _rowversion_ts | DateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
