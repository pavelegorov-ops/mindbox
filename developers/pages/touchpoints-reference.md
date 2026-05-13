---
title: Справочник точек контакта
slug: "touchpoints-reference"
source_url: "https://developers.mindbox.ru/docs/touchpoints-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:35970f7989d8f9a93cbbb025a6f39246654a47b4cb279d25b384005eba3b55be"
---

# Справочник точек контакта

Датасет точек контакта. Содержит список ТК, в которых происходят взаимодействия с клиентами parentId - ссылка на id канала-родителя

---

### exports.ProcessingOrders.PointsOfContact

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int64 | Идентификатор точки контакта как в административной панели | 1044 |
| internalId | string | Внутренний идентификатор точки контакта | a4fb2db8-7681-493c-89f2-e7c450598041 |
| externalId | string (nullable) | Внешний идентификатор точки контакта | 4FFC6C9D1CE460 |
| name | string | Название ТК | Магазин 003 |
| systemName | string | Системное название ТК | Store003 |
| parentId | int64 (nullable) | Ссылка на родительский канал | 391 |
| _isDeleted | bool (nullable) | Признак, что ТК была удалена в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
