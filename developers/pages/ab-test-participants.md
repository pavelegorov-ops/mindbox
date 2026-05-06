---
title: "Участники АБ-тестов"
slug: "ab-test-participants"
source_url: "https://developers.mindbox.ru/docs/ab-test-participants"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:f98c3ff0b4c37aa7d604a414e86e56238f59cded540a55c6c71274701a493cea"
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
