---
title: Справочник статусов позиций заказов
slug: "order-line-statuses-reference"
source_url: "https://developers.mindbox.ru/docs/order-line-statuses-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:be5c1fd4085a814fad14dc7bda6059619b04fa99406c7fd185823c87dbb0e5ea"
---

# Справочник статусов позиций заказов

Датасет статусов позиций заказов

---

### exports.ProcessingOrders.PurchaseStatuses

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| internalId | string | Внутренний id статуса заказа | 8e9695e5-7890-11ec-aba9-005056010ebd |
| name | string | Название статуса позиции заказа (Доставлена / В корзине / Ожидает обработки и тп) | В корзине |
| externalId | string | Внешний id статуса заказа | InCart |
| categorySystemName | string | Название категории статуса заказа (В корзине / Оплачен и тп) | InCart |
| _isDeleted | bool (nullable) | Признак, что статус удален в Mindbox | True |
| _rowversion_ts | datetime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-10-15 10:00:00.000 |
