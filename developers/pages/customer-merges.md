---
title: Объединения клиентов
slug: "customer-merges"
source_url: "https://developers.mindbox.ru/docs/customer-merges"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:cb92fd0de71ffeb6d041c42b66c5649f4daa0ff91755e411ff2b445c4e2ddac6"
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
