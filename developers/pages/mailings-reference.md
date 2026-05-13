---
title: Справочник рассылок
slug: "mailings-reference"
source_url: "https://developers.mindbox.ru/docs/mailings-reference"
breadcrumb:
  - Данные для аналитики
  - Описание схемы данных
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:36056a6a21742f6830f72d76f6ce955becd23cf5082f4fe7eb19ad69805a8273"
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
