---
title: Связь между списаниями и начислениями баллов
slug: "link-between-bonus-redemptions-and-accruals"
source_url: "https://developers.mindbox.ru/docs/link-between-bonus-redemptions-and-accruals"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:be8d852f2da581b226fb62be6eabad0e42be5f9a6facf17ddc246e11eddf88ab"
---

# Связь между списаниями и начислениями баллов

Датасет связи списаний и начислений баллов. Условно в рамках акции "С Днем Рождения" было начислено 100 баллов, 50 из которых были потрачены через неделю после начисления, а оставшиеся 50 через месяц. В итоге в датасете будет 2 записи с spentAmount = 50

---

### exports.ProcessingOrders.NegativeCustomerBalanceChangeDetails

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int | Внутренний идентификатор связи | 3890 |
| negativeCustomerBalanceChangeId | int (nullable) | Внутренний идентификатор события списания | 123985 |
| positiveCustomerBalanceChangeId | int (nullable) | Внутренний идентификатор события начисления | 135801 |
| spentAmount | decimal (25,5) (nullable) | Cумма списания | 100,00 |
| _isDeleted | bool (nullable) | Признак, что связь удалена в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
