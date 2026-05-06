---
title: Справочник сегментов
slug: "segments-reference"
source_url: "https://developers.mindbox.ru/docs/segments-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:4b7ee74d2bdf7b93d132a073469c4ceff232d5df665595d3067c5eabf73fae24"
---

# Справочник сегментов

Датасет сегментов. Содержит список сегментов.

---

### exports.CDP.Segments

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int | Идентификатор сегмента | 25 |
| externalId | string | Внешний идентификатор сегмента | a4fb2db8-7681-493c-89f2-e7c450598041 |
| name | string | Название сегмента | Телемаркетинг |
| systemName | string | Системное имя сегмента | TM |
| segmentationId | int | Идентификатор родительской сегментации | 15 |
| _isDeleted | bool (nullable) | Признак, что сегмент был удалён в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
