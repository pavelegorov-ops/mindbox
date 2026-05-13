---
title: Теги в рассылках
slug: "tags-in-mailings"
source_url: "https://developers.mindbox.ru/docs/tags-in-mailings"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f87c9e1aba4042ba4e917faba74c04ed43469dcbf9d712c4a83d30226798b8bd"
---

# Теги в рассылках

Датасет использования тегов в рассылках

---

### exports.Mailings.MailingsTags

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | string | Уникальный идентификатор | a4fb2db8-7681-493c-89f2-e7c450598042_7c37a133-a627-4649-b677-acf21c8a45d3 |
| mailingInternalId | string | Идентификатор рассылки | 7c37a133-a627-4649-b677-acf21c8a45d3 |
| tagInternalId | string | Идентификатор тега | a4fb2db8-7681-493c-89f2-e7c450598042 |
| _isDeleted | bool (nullable) | Признак, что тег в рассылке был удалён в Mindbox | False |
| _rowversion_ts | dateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
