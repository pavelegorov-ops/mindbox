---
title: "Участники АБ-тестов"
slug: "ab-test-participants"
source_url: "https://developers.mindbox.ru/docs/ab-test-participants"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:d67f5c15125623437f676979c5dcc2315128f78cd817a9e39cb5f5182a883d56"
---

# Участники АБ-тестов

### exports.AbTests.ScenariosAbTestParticipants

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| unmergedCustomerId | Int | Идентификатор клиента | 109243 |
| abTestId | String | Идентификатор АБ-теста | a4fb2db8-7681-493c-89f2-e7c450598041 |
| variantId | String | Идентификатор варианта АБ-теста | a4fb2db8-7681-493c-89f2-e7c450598041 |
| deviceUUID | String | Идентификатор устройства клиента | a4fb2db8-7681-493c-89f2-e7c450598041 |
| timestamp | DateTime | Временная метка в формате UTC, когда клиент стал участником АБ-теста | 2024-08-21 10:10:10.000 |
| _isDeleted | Bool | Признак, что участие клиента в АБ-тесте было удалено в Mindbox | True |
| _rowversion_ts | DateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
