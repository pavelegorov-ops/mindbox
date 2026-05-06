---
title: Описание схемы данных
slug: "analytics-data-schema"
source_url: "https://developers.mindbox.ru/docs/analytics-data-schema"
breadcrumb:
  - Данные для аналитики
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0b02255baf3ad4f83b673b93063a39870f2224a7496f0684c3c0194daa964984"
---

# Описание схемы данных

# Доступные схемы и таблицы

### ProcessingOrders

В текущей реализации не экспортируются дополнительные поля заказов, дополнительные поля позиций заказов и информация о скидочных акциях в заказах.

Схема содержит информацию о заказах, баллах, промоакциях, позициях заказов

| Таблица | Описание | Ключ |
| --- | --- | --- |
| BonusPointChanges | События изменений балансов баллов клиентов | id |
| BonusPointsMechanics | Справочник балльных промоакций | id |
| NegativeCustomerBalanceChangeDetails | Связь между списаниями и начислениями баллов | id |
| Balances | Справочник балльных счетов | id |
| Orders | Заказы клиентов | id |
| Purchases | Состав заказов клиентов | orderId + lineNumber / lineId |
| PurchaseStatuses | Справочник статусов позиций заказов | internalId |
| PointsOfContact | Справочник точек контакта | id |

### Mailings

Схема содержит информацию о рассылках, действиях с рассылками (открытия/клики/недоставки и тп)

| Таблица | Описание | Ключ |
| --- | --- | --- |
| Mailings | Справочник рассылок | id |
| SubscriptionTopics | Справочник тематик рассылок | internalId |
| CustomerMessagesStatuses | Статусы рассылок (открытия/клики/недоставки и тп) | messageStatusId |
| MailingsTags | Теги в рассылках | id |

### CDP

Схема содержит общую информацию

| Таблица | Описание | Ключ |
| --- | --- | --- |
| MergedCustomers | Объединения клиентов | unmergedCustomerId + mergedCustomerId |
| Folders | Справочник папок | internalId |
| Segmentations | Справочник сегментаций | id |
| Segments | Справочник сегментов | id |
| CustomerSegmentHistory | История сегментов клиентов | id |
| Tags | Справочник тегов действий/рассылок | internalId |
| CustomFieldsKinds | Справочник дополнительных полей | internalId |
| ExternalCustomerIdsHistory | История изменений внешних идентификаторов клиентов | id |

### AbTests

Схема содержит информацию об АБ-тестах, их вариантах и участниках АБ-тестов (сейчас только участники АБ-тестов сценариев)

| Таблица | Описание | Ключ |
| --- | --- | --- |
| AbTests | Справочник АБ-тестов | internalId |
| AbTestVariants | Справочник вариантов АБ-тестов | abTestId |
| ScenariosAbTestParticipants | Участники АБ-тестов | unmergedCustomerId + abTestId / variantId |

### Зачем нужен ключ?

Чтобы получить последнее состояние сущности или состояние сущности на какой-то момент времени, вам потребуется ключ - по нему будут происходить группировка строк в таблице и отбор подходящих значений.

Рассмотрим пример: вы уже скачали данные по заказу id198123, но сегодня вместе с экспортом пришла информация об обновлении заказа. Как получить только одну актуальную запись? Для этого можно воспользоваться, например, вот таким скриптом:

```
SELECT * 
FROM 
Orders --таблица заказов
ORDER BY 
Orders._rowversion_ts DESC --сотрируем таблицу с заказами по дате изменения
LIMIT 1 BY Orders.id --берем одну строку для каждого уникального id
```

# Схема таблиц

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/e052cf0e966f36a618991f437b1d07a565f07b3884455e57287cba04f4ff9243-data-mission_exports_-_Export_tables.jpg)
