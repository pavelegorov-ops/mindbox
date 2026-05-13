---
title: Справочник сегментаций
slug: "segmentations-reference"
source_url: "https://developers.mindbox.ru/docs/segmentations-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8b943055f8720a99d1e3b088c82533a48e36ba2f6e6876e3c4c2861b588f51d9"
---

# Справочник сегментаций

Датасет сегментаций. Содержит список сегментаций.

---

### exports.CDP.Segmentations

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int | Идентификатор сегментации как в административной панели | 15 |
| externalId | string | Внешний идентификатор сегментации | a4fb2db8-7681-493c-89f2-e7c450598041 |
| name | string | Название сегментации | Новые клиенты |
| systemName | string | Системное имя сегментации | NewCustomers |
| entityType | string | Тип сущности сегментации | User |
| creationDateTimeUtc | datetime | Дата создания сегментации в формате UTC | 2025-02-27 11:41:31.890 |
| _isDeleted | bool (nullable) | Признак, что сегментация была удалена в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
