---
title: "Справочник АБ-тестов"
slug: "ab-tests-reference"
source_url: "https://developers.mindbox.ru/docs/ab-tests-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:df3d884c2cfd3e12e527334a36e098607dec7d6f05b9370529508a0b804e995b"
---

# Справочник АБ-тестов

### exports.AbTests.AbTests

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| internalId | String | Идентификатор АБ-теста | a4fb2db8-7681-493c-89f2-e7c450598041 |
| name | String | Название АБ-теста | Реактивация с разными офферами |
| startDateTimeUTC | DateTime | Дата запуска АБ-теста в формате UTC | 2024-08-21 10:10:10.000 |
| stopDateTimeUTC | DateTime | Дата остановки АБ-теста в формате UTC | 2024-09-21 10:10:10.000 |
| domain | String | Тип сущности АБ-теста | Scenario |
| _isDeleted | Bool | Признак, что АБ-тест был удален в Mindbox | True |
| _rowversion_ts | DateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
