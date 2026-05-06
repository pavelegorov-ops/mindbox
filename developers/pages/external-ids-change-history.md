---
title: История изменений внешних идентификаторов клиентов
slug: "external-ids-change-history"
source_url: "https://developers.mindbox.ru/docs/external-ids-change-history"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:f013a59bb6cc472a8fce44ca2f1c74385865e5c52e458ae6dd5f75d6b19d8273"
---

# История изменений внешних идентификаторов клиентов

Датасет истории изменений внешних идентификаторов клиентов. Каждое изменение внешнего идентификатора будет представлено отдельной записью в датасете.

---

### exports.CDP.ExternalCustomerIdsHistory

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | int64 | Идентификатор записи в истории идентификаторов клиента | 25 |
| unmergedCustomerId | int64 | Внутренний идентификатор клиента на момент события | 12381 |
| customfieldKindInternalId | string | Внешний идентификатор дополнительного поля | cf21fdb5-b7d8-4fe9-b3c8-2d995fc3a90f |
| value | string | Зашифрованное значение внешнего идентификатора клиента |  |
| historicalCustomerId | int64 | Идентификатор исторического слепка клиента | 15 |
| historicalCustomerCreationDateTimeUtc | datetime | Дата создания исторического слепка клиента в формате UTC | 2024-08-21 10:10:10.000 |
| _isDeleted | bool | Признак, что внешний идентификатор был удалён в Mindbox | True |
| _database_version | int64 | Служебное поле для отслеживания версии записи при изменениях | 5 |
