---
title: Справочник дополнительных полей
slug: "customfields-reference"
source_url: "https://developers.mindbox.ru/docs/customfields-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:c7134be59bd973cb16e2251eba101ddd3c1094501ca5926a426cd74f1f33d870"
---

# Справочник дополнительных полей

Датасет дополнительных полей. Содержит список типов дополнительных полей.

---

### exports.CDP.CustomFieldsKinds

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| internalId | string | Внешний идентификатор дополнительного поля | cf21fdb5-b7d8-4fe9-b3c8-2d995fc3a90f |
| name | string | Название дополнительного поля | Дополнительное поле 1 |
| systemName | string | Системное имя дополнительного поля | customfieldsystemname1 |
| typeSystemName | string | Тип дополнительного поля | TechnicalIdentity |
| entityType | string | Тип сущности дополнительного поля | User |
| _isDeleted | bool | Признак, что дополнительное поле было удалено в Mindbox | True |
| _database_version | int64 | Служебное поле для отслеживания версии записи при изменениях | 5 |
