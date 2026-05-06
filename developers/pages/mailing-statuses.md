---
title: Статусы рассылок
slug: "mailing-statuses"
source_url: "https://developers.mindbox.ru/docs/mailing-statuses"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:675f6e20a9b529d1711360ae2fe04bd6456fbb93db8bf4f20f6e718ebe4f435d"
---

# Статусы рассылок

Датасет статусов рассылок: отправок, открытий, кликов и тп.

---

В отличие от экспорта статусов рассылок с помощью [операций](export-mailing-statuses.md) в текущем датасете отсуствуют статусы "InQueue" ("рассылка запланирована к отправке")

### exports.Mailings.CustomerMessagesStatuses

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| messageId | int64 | Идентификатор экземпляра рассылки. Например, клиенту отправили письмо - все его статусы: Отправка, Открытие, Клик и тп будут с одним messageId | 2313 |
| messageStatusId | string | Уникальный идентификатор статуса | a4fb2db8-7681-493c-89f2-e7c450598042 |
| mailingStatusSystemName | string | Системное имя статуса: Sent, Opened, Clicked, Unsubscribe, NotSent, NotDelivered | Sent |
| dateTimeUTC | string | Дата и время события | 2024-08-21 10:10:10.000 |
| unmergedCustomerId | Int64 | Идентификатор клиента - адресата рассылки | 4456124 |
| mailingInternalId | string | Идентификатор рассылки | a4fb2db8-7681-493c-89f2-e7c450598041 |
| mailingVariantNum | int | Идентификатор варианта рассылки (номер ветки для АБ-теста) | 1 |
| mailingLink | string | Ссылка, по которой кликнул клиент - только для mailingStatusSystemName == Clicked | <<http://ya.ru>> |
| mailingSourceEntityType | string | Тип сущности, инициировавшей рассылку | ScenarioBlock |
| mailingSourceEntityId | string | Идентификатор сущности, инициирвоавшей рассылку | a4fb2db8-7681-493c-89f2-e7c450598041 |
| notSentSystemName | string | Причина неотправки | InvalidContact |
| notDeliveredReasonSystemName | string | Причина недоставки | EmailBlackList |
| _isDeleted | bool | Признак, что событие было удалено (не автоудалением!) в Mindbox | True |
| _rowversion_ts | dateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
