---
title: Справочник балльных промоакций
slug: "bonus-promotions-reference"
source_url: "https://developers.mindbox.ru/docs/bonus-promotions-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:55648bbe9f761cb22c29ac751a4126f4b1a3259e4043f2a06582e60de57d5487"
---

# Справочник балльных промоакций

Датасет описаний механик изменений балансов: промоакций, сценариев, действий
корректировки баланса в админке и тп

---

### exports.ProcessingOrders.BonusPointsMechanics

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int | Внутренний идентификатор механики | 3 |
| internalId | string | Внутренний идентификатор балльного счета | 502f8872-1f5d-459d-a6e3-fac63a4d5ce4 |
| discriminator | string (nullable) | Описание типа механики | WithOwner |
| name | string (nullable) | Название механики | Начисление баллов за заказ 2% |
| ownerId | string (nullable) | Внутренний идентификатор сущности, которая применила механику | 54cb96d9-3e62-430b-8d71-01e7677f2ed5 |
| ownerType | string (nullable) | Тип сущности, которая применила механику: шаблон действия, промакция, сценарий | ScenarioBlock - если акция была применена в рамках блока в сценарии или Operation - если начисление было произведено в рамках действия корректироки / заказа |
| _isDeleted | bool (nullable) | Признак, что механика была удалена в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
