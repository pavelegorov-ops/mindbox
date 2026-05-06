---
title: Справочник балльных счетов
slug: "bonus-accounts-reference"
source_url: "https://developers.mindbox.ru/docs/bonus-accounts-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:9031acbd78c4582223e2a558b0c9e4b13ae6b0552953bf06f5b359e575f84a0d"
---

# Справочник балльных счетов

Датасет описаний балльных счетов

---

### exports.ProcessingOrders.Balances

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int (nullable) | Идентификатор балльного счета как в административной панели | 3 |
| internalId | string | Внутренний идентификатор балльного счета | 502f8872-1f5d-459d-a6e3-fac63a4d5ce4 |
| systemName | string (nullable) | Системное имя балльного счета | MainAccount |
| name | string (nullable) | Название балльного счета | Основной счет |
| description | string (nullable) | Описание балльного счета | Балльный счет программы лояльности |
| _isDeleted | bool (nullable) | Признак, что счет был удален в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
