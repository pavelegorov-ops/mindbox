---
title: Справочник рассылок
slug: "mailings-reference"
source_url: "https://developers.mindbox.ru/docs/mailings-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:1e3b9054779dca415137858e3bce7997d40240d524849535bd35035ff8b2a575"
---

# Справочник рассылок

### exports.Mailings.Mailings

| Поле | Тип | Описание | Пример |
| --- | --- | --- | --- |
| id | String | Идентификатор рассылки | a4fb2db8-7681-493c-89f2-e7c450598041 |
| name | String | Название рассылки | С Днем рождения |
| systemName | String | Системное имя рассылки | SDnemRozhdenya |
| type | String | Тип рассылки - массовая, автоматическая или транзакционная. | Одно из значений: mass, transaction, trigger |
| channel | String | Канал рассылки | SMS |
| creationDateTimeUTC | DateTime | Дата создания рассылки в формате UTC | 2024-08-21 10:10:10.000 |
| lastUpdateDateTimeUtc | DateTime | Дата изменения рассылки в формате UTC | 2024-08-21 10:10:10.000 |
| folderInternalId | String | Id папки | a4fb2db8-7681-493c-89f2-e7c450598041 |
| subscriptionTopicInternalId | String | Id тематики | a4fb2db8-7681-493c-89f2-e7c450598043 |
| brandInternalId | String | Системное имя бренда | Nike |
| utmSource | String | utmSource | email |
| utmMedium | String | utmMedium | cpc |
| utmCampaign | String | utmCampaign | marketing |
| utmContent | String | utmContent | banner_1 |
| utmTerm | String | utmTerm | term |
| _isDeleted | Bool | Признак, что событие было удалено (не автоудалением!) в Mindbox | True |
| _rowversion_ts | DateTime | Временная метка в формате UTC, когда данные стали доступны для экспорта | 2024-08-21 10:10:10.000 |
