---
title: Справочник балльных счетов
slug: "bonus-accounts-reference"
source_url: "https://developers.mindbox.ru/docs/bonus-accounts-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:753abef21619de4db528c9373d44be7c5d17b47ffe4bc43ec3db38f4d02b6f70"
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
