---
title: Справочник дополнительных полей
slug: "customfields-reference"
source_url: "https://developers.mindbox.ru/docs/customfields-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f2b47a14dc2225e34fa77d05e042a4037506063a1aefa3746c2916be548dd15c"
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
