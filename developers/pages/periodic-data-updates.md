---
title: Как периодически обновлять данные
slug: "periodic-data-updates"
source_url: "https://developers.mindbox.ru/docs/periodic-data-updates"
breadcrumb:
  - Данные для аналитики
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:d4ce3df08e7b3ac20f55508d0b391f5df6fc70b97688c9e1cdc3ac9518ca2aef"
---

# Как периодически обновлять данные

## Как последовательно обновлять данные

Алгоритм чтения данных выглядит следующим образом:

1. создать таблицы в dwh;
2. загрузить исторические данные с нулевой версии (startingVersion=0);
3. периодически читать данные с N+1 версии, где N — последняя версия данных в dwh;
4. получить ссылки на нужные файлы и прочитать содержимое файлов;
5. данные из файлов складывать в dwh, фиксируя версию, чтобы в следующую итерацию чтения начать с ещё не записанной в dwh версии, а не сначала.

## Пример таблиц и view для Clickhouse

### Таблицы для сырых данных

**Изменения баланса**

```
CREATE TABLE "BonusPointChanges_raw" (
"id" Int,
"kindSystemName" Nullable(String),
"mechanicsInternalId" Nullable(String),
"balanceInternalId" Nullable(String),
"changeAmount" Decimal64 (5),
"availableFromDateTimeUtc" Nullable(String),
"expirationDateTimeUtc" Nullable(String),
"dateTimeUtc" Nullable(String),
"unmergedCustomerId" Nullable(String),
"orderId" Nullable(String),
"comments" Nullable(String),
"pointOfContactInternalId" Nullable(String),
"brandInternalId" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int
)
ENGINE MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192 SETTINGS flatten_nested=0
```

**Механики, в рамках которых происходит списание и начисление**

```
CREATE TABLE "BonusPointsMechanics_raw" (
"id" Int,
"internalId" String,
"discriminator" Nullable(String),
"name" Nullable(String),
"ownerId" Nullable(String),
"ownerType" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int
)
ENGINE MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192 SETTINGS flatten_nested=0
```

**Балльные счета**

```
CREATE TABLE "Balances_raw" (
"internalId" String,
"id" Nullable(Int),
"name" Nullable(String),
"systemName" Nullable(String),
"description" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int
)
ENGINE MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192 SETTINGS flatten_nested=0
```

**Cвязь списаний и начислений**

```
CREATE TABLE "NegativeCustomerBalanceChangeDetails_raw" (
"id" Int,
"negativeCustomerBalanceChangeId" Nullable(Int),
"positiveCustomerBalanceChangeId" Nullable(Int),
"spentAmount" Decimal64 (5),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int
)
ENGINE MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192 SETTINGS flatten_nested=0
```

**Заказы**

```
CREATE TABLE "Orders_raw" (
"id" String,
"unmergedCustomerId" Nullable(Int64),
"firstDateTimeUtc" Nullable(DateTime),
"firstPointOfContactInternalId" Nullable(String),
"firstBrandInternalId" Nullable(String),
"price" Nullable(Decimal64 (5)),
"priceWithDiscounts" Nullable(Decimal64 (5)),
"deliveryPrice" Nullable(Decimal64 (5)),
"deliveryPriceWithDiscounts" Nullable(Decimal64 (5)),
"paidAmount" Nullable(Decimal64 (5)),
"pointOfContactInternalId" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int
)
ENGINE MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192 SETTINGS flatten_nested=0
```

**Точки контакта**

```
CREATE TABLE "PointsOfContact_raw" (
"id" Int64,
"internalId" String,
"externalId" Nullable(String),
"name" String,
"systemName" String,
"parentId" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Статусы позиций заказов**

```
CREATE TABLE "PurchaseStatuses_raw" (
"internalId" String,
"name" Nullable(String),
"externalId" Nullable(String),
"categorySystemName" Nullable(String),
"_isDeleted" Nullable(String),
"_rowversion_ts" DateTime,
"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Позиции заказов**

Для позиции заказа нет признака **_isDeleted**, так как позиция заказа может быть удалена только вместе с заказом.

```
CREATE TABLE "Purchases_raw" (
"orderId" String,
"pricePerItem" Decimal64 (5),
"priceOfLine" Decimal64 (5),
"quantity" Float,
"quantityType" String,
"lineId" Nullable(String),
"lineNumber" Int,
"statusInternalId" String,
"productInternalId" String,
"_rowversion_ts" DateTime,
"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Рассылки**

```
CREATE TABLE "Mailings_raw" (
    "id" String,
    "name" String,
    "systemName" String,
    "type" String,
    "channel" String,
    "creationDateTimeUtc" DateTime,
    "lastUpdateDateTimeUtc" DateTime,
    "folderInternalId" Nullable(String),
    "subscriptionTopicInternalId" Nullable(String),
    "brandInternalId" String,
    "utmSource" Nullable(String),
    "utmMedium" Nullable(String),
    "utmCampaign" Nullable(String),
    "utmContent" Nullable(String),
    "utmTerm" Nullable(String),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Тематики рассылок**

```
CREATE TABLE "SubscriptionTopics_raw"
(
    "internalId" String,
    "systemName" String,
    "name" String,
    "brandInternalId" String,
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Статусы рассылок**

```
CREATE TABLE "CustomerMessagesStatuses_raw"
(
    "messageId" Int64,
    "messageStatusId" String,
    "mailingStatusSystemName" String,
    "dateTimeUtc" DateTime,
    "unmergedCustomerId" Int64,
    "mailingInternalId" String,
    "mailingVariantNum" Nullable(String),
    "mailingLink" Nullable(String),
    "mailingSourceEntityType" Nullable(String),
    "mailingSourceEntityId" Nullable(String),
    "notSentSystemName" Nullable(String),
    "notDeliveredReasonSystemName" Nullable(String),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Теги в рассылках**

```
CREATE TABLE "MailingsTags_raw"
(
    "id" String,
    "mailingInternalId" Nullable(String),
    "tagInternalId" Nullable(String),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Объединения клиентов**

```
CREATE TABLE "MergedCustomers_raw"
(
    "unmergedCustomerId" Int64,
    "mergedCustomerId" Int64,
    "dateTimeUtc" DateTime,
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**История изменений внешних идентификаторов клиентов**

```
CREATE TABLE "ExternalCustomerIdsHistory"
(
    "id" Int64,
    "customFieldKindInternalId" String,
    "value" String,
    "unmergedCustomerId" Int64,
    "historicalCustomerId" Int64,
    "historicalCustomerCreationDateTimeUtc" DateTime,
    "_isDeleted" String,
    "_database_version" Int64,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Сегментации**

```
CREATE TABLE "Segmentations_raw"
(
    "id" Int,
    "externalId" Nullable(String),
    "name" Nullable(String),
    "systemName" Nullable(String),
    "entityType" Nullable(String),
    "creationDateTimeUtc" Nullable(DateTime),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Сегменты**

```
CREATE TABLE "Segments_raw"
(
    "id" Int,
    "externalId" Nullable(String),
    "name" Nullable(String),
    "systemName" Nullable(String),
    "segmentationId" Nullable(Int),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Теги**

```
CREATE TABLE "Tags_raw"
(
    "internalId" String,
    "name" Nullable(String),
    "systemName" Nullable(String),
    "creationDateTimeUtc" Nullable(DateTime),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**История сегментов клиентов**

```
CREATE TABLE "CustomerSegmentHistory_raw"
(
    "id" Int64,
    "unmergedCustomerId" Nullable(Int64),
    "segmentationId" Nullable(Int),
    "segmentId" Nullable(Int),
    "calculatedDateTimeUtc" Nullable(DateTime),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Папки**

```
CREATE TABLE "Folders_raw"
(
    "internalId" String,
    "systemName" String,
    "name" String,
    "parentInternalId" Nullable(String),
    "_isDeleted" Nullable(String),
    "_rowversion_ts" DateTime,
    "_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**АБ-тесты**

```
CREATE TABLE "AbTests_raw"
(
    "internalId" String,
    "name" String,
    "startDateTimeUtc" DateTime,
    "stopDateTimeUtc" DateTime,
    "domain" string,
  	"_isDeleted" Nullable(String),
		"_rowversion_ts" DateTime,
		"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Варианты АБ-тестов**

```
CREATE TABLE "AbTestVariants_raw"
(
    "internalId" String,
    "name" String,
    "abTestId" String,
    "modulusLowerInclusive" Int32,
    "modulusUpperExclusive" Int32,
  	"_isDeleted" Nullable(String),
		"_rowversion_ts" DateTime,
		"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

**Участники АБ-тестов сценариев**

```
CREATE TABLE "ScenariosAbTestParticipants_raw"
(
    "unmergedCustomerId" Int64,
    "abTestId" String,
  	"variantId" String,
  	"deviceUUID" String,
    "timestamp" DateTime,
    "timestamp_year" Int32,
    "timestamp_month" Int32,
    "timestamp_day" Int32,
  	"_isDeleted" Nullable(String),
		"_rowversion_ts" DateTime,
		"_data_version" Int32
)
ENGINE = MergeTree()
ORDER BY tuple()
SETTINGS index_granularity = 8192
```

### Витрины с актуальным состоянием данных

В этих view уже будут только актуальные данные без удаленных вручную данных и без дублей — только последние состояния фактов и сущностей.

**Изменения баланса**

```
CREATE VIEW BonusPointChanges_dm AS
SELECT * FROM ( 
   SELECT * 
   FROM 
   BonusPointChanges_raw
   ORDER BY 
   BonusPointChanges_raw._rowversion_ts DESC
   LIMIT 1 BY BonusPointChanges_raw.id
) AS dm
WHERE 
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Механики, в рамках которых происходит списание и начисление**

```
CREATE VIEW BonusPointsMechanics_dm AS
SELECT * FROM ( 
   SELECT * 
   FROM 
   BonusPointsMechanics_raw
   ORDER BY 
   BonusPointsMechanics_raw._rowversion_ts DESC
   LIMIT 1 BY BonusPointsMechanics_raw.id
) AS dm
WHERE 
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Балльные счета**

```
CREATE VIEW Balances_dm AS
SELECT * FROM ( 
   SELECT * 
   FROM 
   Balances_raw
   ORDER BY 
   Balances_raw._rowversion_ts DESC
   LIMIT 1 BY Balances_raw.id
) AS dm
WHERE 
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Cвязь списаний и начислений**

```
CREATE VIEW NegativeCustomerBalanceChangeDetails_dm AS
SELECT * FROM ( 
   SELECT * 
   FROM 
   NegativeCustomerBalanceChangeDetails_raw
   ORDER BY 
   NegativeCustomerBalanceChangeDetails_raw._rowversion_ts DESC
   LIMIT 1 BY NegativeCustomerBalanceChangeDetails_raw.id
) AS dm
WHERE 
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Заказы**

```
CREATE VIEW Orders_dm AS
SELECT * FROM ( 
   SELECT * 
   FROM 
   Orders_raw
   ORDER BY 
   Orders_raw._rowversion_ts DESC
   LIMIT 1 BY Orders_raw.id
) AS dm
WHERE 
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Точки контакта**

```
CREATE VIEW PointsOfContact_dm AS
SELECT * FROM (
	SELECT *
	FROM
	PointsOfContact_raw
	ORDER BY
	PointsOfContact_raw._rowversion_ts DESC
	LIMIT 1 BY PointsOfContact_raw.id
) AS dm
WHERE
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Статусы позиций заказов**

```
CREATE VIEW PurchaseStatuses_dm AS 
SELECT * FROM
(
    SELECT *
    FROM PurchaseStatuses_raw
    ORDER BY PurchaseStatuses_raw._rowversion_ts DESC
    LIMIT 1 BY PurchaseStatuses_raw.internalId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Позиции заказов**

```
CREATE VIEW Purchases_dm AS
SELECT *
FROM Purchases_raw
ORDER BY Purchases_raw._rowversion_ts DESC
LIMIT 1 BY Purchases_raw.orderId, Purchases_raw.lineId
```

**Рассылки**

```
CREATE VIEW Mailings_dm AS
SELECT *
FROM
(
    SELECT *
    FROM Mailings.Mailings_raw
    ORDER BY Mailings_raw._rowversion_ts DESC
    LIMIT 1 BY Mailings_raw.id
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Тематики рассылок**

```
CREATE VIEW SubscriptionTopics_dm AS
SELECT *
FROM
(
    SELECT *
    FROM SubscriptionTopics_raw
    ORDER BY SubscriptionTopics_raw._rowversion_ts DESC
    LIMIT 1 BY SubscriptionTopics_raw.internalId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Статусы рассылок**

```
CREATE VIEW CustomerMessagesStatuses_dm AS
SELECT *
FROM
(
    SELECT *
    FROM CustomerMessagesStatuses_raw
    ORDER BY CustomerMessagesStatuses_raw._rowversion_ts DESC
    LIMIT 1 BY CustomerMessagesStatuses_raw.messageStatusId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Объединения клиентов**

```
CREATE VIEW MergedCustomers_dm AS
SELECT *
FROM
(
    SELECT *
    FROM MergedCustomers_raw
    ORDER BY MergedCustomers_raw._rowversion_ts DESC
    LIMIT 1 BY
        MergedCustomers_raw.unmergedCustomerId,
        MergedCustomers_raw.mergedCustomerId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**История изменений внешних идентификаторов клиентов**

```
CREATE VIEW ExternalCustomerIdsHistory_dm AS
SELECT *
FROM
(
    SELECT *
    FROM ExternalCustomerIdsHistory_raw
    ORDER BY ExternalCustomerIdsHistory_raw._database_version DESC
    LIMIT 1 BY ExternalCustomerIdsHistory_raw.id,
) AS dm
WHERE dm._isDeleted = 'false'
```

**Сегментации**

```
CREATE VIEW Segmentations_dm AS
SELECT * FROM (
	SELECT *
	FROM
	Segmentations_raw
	ORDER BY
	Segmentations_raw._rowversion_ts DESC
	LIMIT 1 BY Segmentations_raw.id
) AS dm
WHERE
empty(dm._isDeleted) OR dm._isDeleted = 'false'
```

**Сегменты**

```
CREATE VIEW Segments_dm AS
SELECT * FROM (
	SELECT *
	FROM
	Segments_raw
	ORDER BY
	Segments_raw._rowversion_ts DESC
	LIMIT 1 BY Segments_raw.id
) AS dm
WHERE
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Теги**

```
CREATE VIEW Tags_dm AS
SELECT * FROM (
	SELECT *
	FROM
	Tags_raw
	ORDER BY
	Tags_raw._rowversion_ts DESC
	LIMIT 1 BY Tags_raw.internalId
) AS dm
WHERE
empty (dm._isDeleted) OR dm._isDeleted = 'false'
```

**Папки**

```
CREATE VIEW Folders_dm AS
SELECT *
FROM
(
    SELECT *
    FROM Folders_raw
    ORDER BY Folders_raw._rowversion_ts DESC
    LIMIT 1 BY Folders_raw.internalId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**АБ-тесты**

```
CREATE VIEW AbTests__dm AS
SELECT *
FROM
(
    SELECT *
    FROM AbTests_raw
    ORDER BY AbTests_raw._rowversion_ts DESC
    LIMIT 1 BY AbTests_raw.internalId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Варианты АБ-тестов**

```
CREATE VIEW AbTestVariants_dm AS
SELECT *
FROM
(
    SELECT *
    FROM AbTestVariants_raw
    ORDER BY AbTestVariants_raw._rowversion_ts DESC
    LIMIT 1 BY AbTestVariants_raw.internalId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

**Участники АБ-тестов**

```
CREATE VIEW ScenariosAbTestParticipants_dm AS
SELECT *
FROM
(
    SELECT *
    FROM ScenariosAbTestParticipants_raw
    ORDER BY ScenariosAbTestParticipants_raw._rowversion_ts DESC
    LIMIT 1 BY ScenariosAbTestParticipants_raw.unmergedCustomerId, ScenariosAbTestParticipants_raw.abTestId
) AS dm
WHERE empty(dm._isDeleted) OR (dm._isDeleted = 'false')
```

## Пример чтения данных на python

С помощью скрипта читаем данные и записываем в Clickhouse. Это скрипт в дальнейшем можно вызывать ежедневно для записи обновлений в Clickhouse.

Для работы с Clickhouse в примере используется pandahouse. При необходимости нужно будет установить эту библиотеку с помощью `pip3 install pandahouse`

Перед началом работы установите библиотеку delta_sharing с помощью `pip3 install delta_sharing`

```
import delta_sharing
import pandahouse as ph
from delta_sharing.rest_client import DataSharingRestClient
from delta_sharing.protocol import DeltaSharingProfile
from delta_sharing.rest_client import DataSharingRestClient, HTTPError
from delta_sharing.protocol import CdfOptions
import pathlib
import pyarrow.parquet as pq
import requests
import io
from datetime import datetime
import urllib3
import pandas

### Коннект до CH ###
connection = dict(database='БД в вашем DWH',
                  host='URL вашего DWH',
                  user='Логин сервисного пользователя вашего DWH',
                  password='Пароль сервисного пользователя вашего DWH')

class Tables():          
    def __init__(self, database, schema, source, target):  
        self.database = database # БД, откуда читаем из Mindbox
        self.schema = schema # схема, откуда читаем из Mindbox
        self.source = source # таблица, откуда читаем из Mindbox
        self.target = target # таблица, куда пишем в Clickhouse
        

tables = []
tables.append ( Tables('exports', 'ProcessingOrders', 'BonusPointChanges', 'BonusPointChanges_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'BalanceChangeKinds', 'BalanceChangeKinds_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'PointsOfContact', 'PointsOfContact_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'BonusPointsMechanics', 'BonusPointsMechanics_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Balances', 'Balances_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'NegativeCustomerBalanceChangeDetails', 'NegativeCustomerBalanceChangeDetails_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Orders', 'Orders_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Purchases', 'Purchases_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'PurchaseStatuses', 'PurchaseStatuses_raw') )
tables.append ( Tables('exports', 'Mailings', 'Mailings', 'Mailings_raw') )
tables.append ( Tables('exports', 'Mailings', 'SubscriptionTopics', 'SubscriptionTopics_raw') )
tables.append ( Tables('exports', 'Mailings', 'MailingsTags', 'MailingsTags_raw') )
tables.append ( Tables('exports', 'Mailings', 'CustomerMessagesStatuses', 'CustomerMessagesStatuses_raw') )
tables.append ( Tables('exports', 'CDP', 'MergedCustomers', 'MergedCustomers_raw') )
tables.append ( Tables('exports', 'CDP', 'Folders', 'Folders_raw') )
tables.append ( Tables('exports', 'CDP', 'Tags', 'Tags_raw') )
tables.append ( Tables('exports', 'CDP', 'Segmentations', 'Segmentations_raw') )
tables.append ( Tables('exports', 'CDP', 'Segments', 'Segments_raw') )
tables.append ( Tables('exports', 'CDP', 'CustomerSegmentHistory', 'CustomerSegmentHistory_raw') )
tables.append ( Tables('exports', 'AbTests', 'AbTests', 'AbTests_raw') )
tables.append ( Tables('exports', 'AbTests', 'AbTestVariants', 'AbTestVariants_raw') )
tables.append ( Tables('exports', 'AbTests', 'ScenariosAbTestParticipants', 'ScenariosAbTestParticipants_raw') )

### Аутентифицируемся ### 
share_file_path = str(pathlib.Path().resolve()) + "/Profile.json" # аутентифицируемся

# Размер батча для чтения - его можено подредактировать, чтобы пролезало в оперативку
batch_size = 1_000_000 

# Сколько файлов с данными читаем за раз
cdf_batch_size = 10

# для статистики
total_len = 0 
start_datetime = datetime.now()

# для всех таблиц проверяем наличие выгруженных данных и заливаем новые данные в БД
for t in tables:
    
    '''Вставьте ниже ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH'''
    
    # Получаем последнюю версию данных - будем читать все из DS, что старше по версии
    df = ph.read_clickhouse('SELECT _data_version FROM ' + t.target + ' ORDER BY _data_version DESC LIMIT 1', connection=connection)
    
    '''Вставьте выше ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH'''
    
    # Проверяем, есть ли в таблице данные, если нет, то читаем с 0-ой версии
    if df.empty:
        latest_version = 0
    else:
        latest_version = df.iat[0,0] + 1
    
    # Читаем из таблицы 
    # Создаем клиент
    profile = DeltaSharingProfile.read_from_file(share_file_path)
    rest_client = DataSharingRestClient(profile)

    table = delta_sharing.Table(share=t.database, schema=t.schema, name=t.source)

    # Получаем свежие версии данных в таблице - версии, котоыре больше latest_version 
    ver = latest_version

    # читаем по частям - по cdf_batch_size версий за раз, тк есть ограничение на количество запрашиваемых версий
    while True: # читаем пока ошибку не получим
        i = 0
        while True and i < 5: # 5 попыток чтения на случай если сервис недоступен
            i += 1
            try: 
                print (f"Получаем данные для таблицы {t.source} для версий от {ver} до {ver+cdf_batch_size-1}.")
                res = rest_client.list_table_changes(
                    table,
                    cdfOptions=CdfOptions(starting_version=ver, ending_version=ver+cdf_batch_size-1)
                )
            except (delta_sharing.rest_client.HTTPError) as err: # ошибка может упасть, если не загружены новые данные или запрошено более 10 версий за раз
                print (f"Не получили обновленные данные для версий от {ver} до {ver+cdf_batch_size-1} c {i} раза. Причина: {err.response.text}")
                continue    
            break
        
        # если не получилось прочитать данные с 5 попыток, то пробуем читать из следующей таблицы
        if i == 5: 
                break
        
        # Если версии есть, то пишем их в CH
        print (f"Пишем данные версий от {ver} до {ver+cdf_batch_size-1} в таблицу {t.target}")
    
        # Чтение данных частями по batch_size строк
        for cdcFile in res.actions:
            signed_url = cdcFile.url
                
            def read_parquet_from_signed_url_in_batches(signed_url, batch_size):
                # Получаем файл с данными
                response = requests.get(signed_url, stream=True)
                response.raise_for_status()
                buffer = io.BytesIO()

                # Читаем по частям ответ
                for chunk in response.iter_content(chunk_size=1024):
                    buffer.write(chunk)

                buffer.seek(0)

                # Открываем файл
                parquet_file = pq.ParquetFile(buffer)

                # Читаем файл батчами
                for batch in parquet_file.iter_batches(batch_size=batch_size):
                    yield batch

            # Обрабатываем паркет файл батчами
            for batch in read_parquet_from_signed_url_in_batches(signed_url, batch_size):

                # Конвертим батч в датафрейм pandas
                batch_df = batch.to_pandas()
                    
                # Фиксируем версию данных
                batch_df['_data_version'] = cdcFile.version

                if '_tenant' in batch_df.columns: 
                    batch_df = batch_df.drop('_tenant', axis=1) # удаляем колонку с названием проекта - она нам не нужна для аналитики

                # Пишем в целевую таблицу в ClickHouse
                i = 0
                while True and i < 5: # делаем 5 ретраев записи - Clickhouse может не отвечать периодически, поэтому делаем ретрай
                    i += 1
                    try:
                        '''Ниже вставляем код для записи датафрейма в ваше DWH'''
                        
                        ph.to_clickhouse(batch_df, t.target, index=False, chunksize=batch_size, connection=connection)
                        
                        '''Выше вставляем код для записи датафрейма в ваше DWH'''
                        
                        # немного логов выводим
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        message = f"Записали {len(batch_df)} строк с {i} попытки ({current_datetime})"
                        print(message)
                        total_len += len(batch_df)
                    except (urllib3.exceptions.ConnectionError or urllib3.exceptions.HTTPError) as err:
                        print (err.response.text)
                        continue
                    break

        ver += cdf_batch_size #следующая итерация чтения 10 версий

# выводим информацию про то, сколько было прочитано строк, сколько времени работал скрипт и средняя скорость перекладывания данных
current_datetime = datetime.now()
print(f"Записано строк: {total_len} - за: {(current_datetime - start_datetime).total_seconds()} секунд. Средняя скорость чтения и записи: {total_len / (current_datetime - start_datetime).total_seconds()} строк в секунду ")#
```

### Как прочитать зашифрованные данные

Для работы с зашифрованными данными установите библиотеку cryptography c помощью `pip3 install cryptography`  
Пример чтения с зашифрованными данными можно увидеть ниже

В начале скрипта нужно указать:

- `master_key_b64` Ключ шифрования со страницы интеграции
- `decrypt_column_name` Название колонки, которую нужно расшифровать

Для расшифровки используется функция из блока про [зашифрованные данные](how-to-read-data.md#/зашифрованные-данные).

```
# Пример чтения с зашифрованными данными

import delta_sharing
import pandahouse as ph
from delta_sharing.rest_client import DataSharingRestClient
from delta_sharing.protocol import DeltaSharingProfile
from delta_sharing.rest_client import DataSharingRestClient, HTTPError
from delta_sharing.protocol import CdfOptions
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import pathlib
import pyarrow.parquet as pq
import requests
import io
from datetime import datetime
import urllib3
import pandas

### Коннект до CH ###
connection = dict(
    database="БД в вашем DWH",
    host="URL вашего DWH",
    user="Логин сервисного пользователя вашего DWH",
    password="Пароль сервисного пользователя вашего DWH",
)

class Tables:
    def __init__(self, database, schema, source, target):
        self.database = database  # БД, откуда читаем из Mindbox
        self.schema = schema  # схема, откуда читаем из Mindbox
        self.source = source  # таблица, откуда читаем из Mindbox
        self.target = target  # таблица, куда пишем в Clickhouse

tables = []
tables.append(Tables("exports", "cdp", "ExternalCustomerIdsHistory", "ExternalCustomerIdsHistory__raw"))

### Аутентифицируемся ###
share_file_path = str(pathlib.Path().resolve()) + "/Profile.json"  # аутентифицируемся

### Указываем master key (Ключ шифрования из админки) ###
master_key_b64 = ""

### Указываем название колонки, которую нужно расшифровать ###
decrypt_column_name = ""

# Размер батча для чтения - его можено подредактировать, чтобы пролезало в оперативку
batch_size = 1_000_000

# Сколько файлов с данными читаем за раз
cdf_batch_size = 10

# для статистики
total_len = 0
start_datetime = datetime.now()

# для всех таблиц проверяем наличие выгруженных данных и заливаем новые данные в БД
for t in tables:

    """Вставьте ниже ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH"""

    # Получаем последнюю версию данных - будем читать все из DS, что старше по версии
    df = ph.read_clickhouse(
        "SELECT _data_version FROM " + t.target + " ORDER BY _data_version DESC LIMIT 1", connection=connection
    )

    """Вставьте выше ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH"""

    # Проверяем, есть ли в таблице данные, если нет, то читаем с 0-ой версии
    if df.empty:
        latest_version = 0
    else:
        latest_version = df.iat[0, 0] + 1

    # Читаем из таблицы
    # Создаем клиент
    profile = DeltaSharingProfile.read_from_file(share_file_path)
    rest_client = DataSharingRestClient(profile)

    table = delta_sharing.Table(share=t.database, schema=t.schema, name=t.source)

    # Получаем свежие версии данных в таблице - версии, котоыре больше latest_version
    ver = latest_version

    # читаем по частям - по cdf_batch_size версий за раз, тк есть ограничение на количество запрашиваемых версий
    while True:  # читаем пока ошибку не получим
        i = 0
        while True and i < 5:  # 5 попыток чтения на случай если сервис недоступен
            i += 1
            try:
                print(f"Получаем данные для таблицы {t.source} для версий от {ver} до {ver+cdf_batch_size-1}.")
                res = rest_client.list_table_changes(
                    table, cdfOptions=CdfOptions(starting_version=ver, ending_version=ver + cdf_batch_size - 1)
                )
            except (
                delta_sharing.rest_client.HTTPError
            ) as err:  # ошибка может упасть, если не загружены новые данные или запрошено более 10 версий за раз
                print(
                    f"Не получили обновленные данные для версий от {ver} до {ver+cdf_batch_size-1} c {i} раза. Причина: {err.response.text}"
                )
                continue
            break

        # если не получилось прочитать данные с 5 попыток, то пробуем читать из следующей таблицы
        if i == 5:
            break

        # Если версии есть, то пишем их в CH
        print(f"Пишем данные версий от {ver} до {ver+cdf_batch_size-1} в таблицу {t.target}")

        # Чтение данных частями по batch_size строк
        for cdcFile in res.actions:
            signed_url = cdcFile.url

            def read_parquet_from_signed_url_in_batches(signed_url, batch_size):
                # Получаем файл с данными
                response = requests.get(signed_url, stream=True)
                response.raise_for_status()
                buffer = io.BytesIO()

                # Читаем по частям ответ
                for chunk in response.iter_content(chunk_size=1024):
                    buffer.write(chunk)

                buffer.seek(0)

                # Открываем файл
                parquet_file = pq.ParquetFile(buffer)

                # Читаем файл батчами
                for batch in parquet_file.iter_batches(batch_size=batch_size):
                    yield batch

            # Функция для расшифровки значения
            def decrypt(encrypted_data_b64: str, master_key_b64: str) -> str:
                # Декодируем входные параметры из Base64
                encrypted_data = base64.b64decode(encrypted_data_b64)
                master_key = base64.b64decode(master_key_b64)

                NONCE_SIZE = 12  # Размер nonce для AES-GCM

                key_nonce = encrypted_data[0:NONCE_SIZE]  # nonce для расшифровки data_key
                value_nonce = encrypted_data[NONCE_SIZE : NONCE_SIZE * 2]  # nonce для расшифровки значения
                encrypted_data_key = encrypted_data[24:72]  # зашифрованный data_key
                encrypted_value = encrypted_data[72:]  # зашифрованное значение

                # Расшифровка data_key, используя master_key (Ключ шифрования со страницы интеграции)
                aesgcm_master = AESGCM(master_key)
                data_key = aesgcm_master.decrypt(key_nonce, encrypted_data_key, associated_data=None)

                # Расшифровка значения, используя data_key
                aesgcm_data_key = AESGCM(data_key)
                decrypted_value = aesgcm_data_key.decrypt(value_nonce, encrypted_value, associated_data=None)

                return decrypted_value.decode("utf-8")

            # Обрабатываем паркет файл батчами
            for batch in read_parquet_from_signed_url_in_batches(signed_url, batch_size):

                # Конвертим батч в датафрейм pandas
                batch_df = batch.to_pandas()

                # Фиксируем версию данных
                batch_df["_data_version"] = cdcFile.version

                if "_tenant" in batch_df.columns:
                    batch_df = batch_df.drop(
                        "_tenant", axis=1
                    )  # удаляем колонку с названием проекта - она нам не нужна для аналитики

                batch_df[decrypt_column_name] = batch_df.apply(
                    lambda row: decrypt(row[decrypt_column_name], master_key_b64), axis=1
                )

                # Пишем в целевую таблицу в ClickHouse
                i = 0
                while (
                    True and i < 5
                ):  # делаем 5 ретраев записи - Clickhouse может не отвечать периодически, поэтому делаем ретрай
                    i += 1
                    try:
                        """Ниже вставляем код для записи датафрейма в ваше DWH"""

                        ph.to_clickhouse(batch_df, t.target, index=False, chunksize=batch_size, connection=connection)

                        """Выше вставляем код для записи датафрейма в ваше DWH"""

                        # немного логов выводим
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        message = f"Записали {len(batch_df)} строк с {i} попытки ({current_datetime})"
                        print(message)
                        total_len += len(batch_df)
                    except urllib3.exceptions.ConnectionError or urllib3.exceptions.HTTPError as err:
                        print(err.response.text)
                        continue
                    break

        ver += cdf_batch_size  # следующая итерация чтения 10 версий

# выводим информацию про то, сколько было прочитано строк, сколько времени работал скрипт и средняя скорость перекладывания данных
current_datetime = datetime.now()
print(
    f"Записано строк: {total_len} - за: {(current_datetime - start_datetime).total_seconds()} секунд. Средняя скорость чтения и записи: {total_len / (current_datetime - start_datetime).total_seconds()} строк в секунду "
)
```

## Как прочитать изменения, произошедшие в определенную дату

Прочитать данные можно не только с итеративно с помощью версий. Также можно запросить данные, которые были изменены за определенный период времени. Для этого можно воспользоваться функцией `get_table_vesion` из библиотеки `delta_sharing`

Функция `get_table_version` принимает 2 аргумента:

- *url таблицы с данными - это строка вида `{share_file_path}#{database}.{schema}.{table}`
- дата в формате `YYYY-MM-DDThh:mm:ssZ`, начиная с которой, будет вестись поиск подходящей версии данных

Например, *10.10.2024 23:45:00* была загружена *138* версия данных и *11.10.2024 23:45:00* была загружена *139* версия данных для таблицы Orders. Тогда функция `get_table_version`с аргументами *11.10.2024 00:00:00* и `{share_file_path}#exports.ProcessingOrders.Orders` вернет версию *139* - ближайшую версию *после* переданной даты.

Если не передать второй аргумент, то функция вернет максимальную версию данных в таблице

Ниже приведен пример кода, который читает все изменения данных в заданный период с учетом ограничения на количество получаемых за раз версий данных и записывает полученные данные в Clickhouse.

```
import delta_sharing
import pandahouse as ph
from delta_sharing.rest_client import DataSharingRestClient
from delta_sharing.protocol import DeltaSharingProfile
from delta_sharing.rest_client import DataSharingRestClient, HTTPError
from delta_sharing.protocol import CdfOptions
import pathlib
import pyarrow.parquet as pq
import pyarrow as pa
import requests
import io
from datetime import datetime
import urllib3
import pandas
import numpy as np

### Коннект до CH ###
connection = dict(database='БД в вашем DWH',
                  host='URL вашего DWH',
                  user='Логин сервисного пользователя вашего DWH',
                  password='Пароль сервисного пользователя вашего DWH')

# Даты, за которые нам нужны данные. Ниже с помощью функции get_table_version будем получать версии, соотвествующие этим датам
date_start = '2024-10-29T00:00:00Z'
date_end = '2024-10-30T00:00:00Z'

class Tables():          
    def __init__(self, database, schema, source, target):  
        self.database = database # БД, откуда читаем из Mindbox
        self.schema = schema # схема, откуда читаем из Mindbox
        self.source = source # таблица, откуда читаем из Mindbox
        self.target = target # таблица, куда пишем в Clickhouse

tables = []
tables.append ( Tables('exports', 'ProcessingOrders', 'Orders', 'Orders_raw') )

### Аутентифицируемся ### 
share_file_path = str(pathlib.Path().resolve()) + "/Profile.json" # аутентифицируемся

# Размер батча - его можено подредактировать, чтобы пролезало в оперативку
batch_size = 1_000_000 
res_df = pandas.DataFrame()

# читаем по одной версии файлов из delta sharing
cdf_batch_size = 1

total_len = 0
start_datetime = datetime.now()

# для всех таблиц проверяем наличие выгруженных данных и заливаем новые данные в БД
for t in tables:
    print (f"Обрабатываем таблицу {t.source}")
    # Читаем из таблицы DS
    # Создаем клиент
    table_url = f"{share_file_path}#{t.database}.{t.schema}.{t.source}"
    profile = DeltaSharingProfile.read_from_file(share_file_path)
    rest_client = DataSharingRestClient(profile)
    table = delta_sharing.Table(share=t.database, schema=t.schema, name=t.source)

    #Определяем версии, с которой и по которую будем читать
    version_start = delta_sharing.get_table_version (table_url, date_start)
    print (f"Версия, соотвествующая дате {date_start} таблицы {t.source} равна {version_start}")
    
    #Если дата отсутсвует в файлах, то берем просто последнюю версию
    try:
        version_end = delta_sharing.get_table_version (table_url, date_end) 
    except (delta_sharing.rest_client.HTTPError) as err: # потенциально может упасть, если timestamp после последней даты
        print (f"Дата {date_end} после последней метки в таблице - берем последнюю версию")
        version_end = delta_sharing.get_table_version (table_url) 

    print (f"Версия, соотвествующая дате {date_end} таблицы {t.source} равна {version_end}")
    
    # Получаем свежие версии данных в таблице - версии, котоыре больше latest_version 
    ver = version_start
    # читаем по частям - по 1 версии за раз
    while ver <= version_end: # читаем пока ошибку не получим
        try: 
            print (f"Получаем данные для таблицы {t.source} для версий от {ver} до {ver+cdf_batch_size-1}.")
            res = rest_client.list_table_changes(
                table,
                cdfOptions=CdfOptions(starting_version=ver, ending_version=ver+cdf_batch_size-1)
            )
            print(res)
        except (delta_sharing.rest_client.HTTPError) as err: # потенциально может упасть, если не залиты новые данные в этом случае выводим ошибку и не идем дальше
            print (f"Не получили обновленные данные для версий от {ver} до {ver+cdf_batch_size-1}. Причина: {err.response.text}")
            break

        
        # Если версии есть, то пишем их в CH
        print (f"Пишем данные версий от {ver} до {ver+cdf_batch_size-1} в таблицу {t.target}")
       
    
        ### Батчами читаем данные и заливаем в CH (чтобы в оператвку пролезло)
        for cdcFile in res.actions:
            signed_url = cdcFile.url
                
            def read_parquet_from_signed_url_in_batches(signed_url, batch_size):
                # Получаем файл с данными
                response = requests.get(signed_url, stream=True)
                response.raise_for_status()
                buffer = io.BytesIO()

                # Читаем по частям ответ
                for chunk in response.iter_content(chunk_size=1024):
                    buffer.write(chunk)

                buffer.seek(0)

                # Открываем файл
                parquet_file = pq.ParquetFile(buffer)

                # Читаем файл батчами
                for batch in parquet_file.iter_batches(batch_size=batch_size):
                    yield batch

            # Обрабатываем паркет файл батчами
            for batch in read_parquet_from_signed_url_in_batches(signed_url, batch_size):

                # Конвертим батч в датафрейм pandas
                
                batch_df = batch.to_pandas()
                    
                # Фиксируем версию данных
                batch_df['_data_version'] = cdcFile.version

                # Пишем в целевую таблицу в ClickHouse
                i = 0
                while True or i < 5: # делаем 5 ретраев записи - Clickhouse может не отвечать периодически, поэтому делаем ретрай
                    i += 1
                    try:
                        '''Ниже вставляем код для записи датафрейма в ваше DWH'''
                       
                        ph.to_clickhouse(batch_df, t.target, index=False, chunksize=batch_size, connection=connection)
                       
                        '''Выше вставляем код для записи датафрейма в ваше DWH'''
                       
                        # немного логов выводим
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        message = f"Записали {len(batch_df)} строк версии {ver} с {i} попытки ({current_datetime})"
                        print(message)
                        total_len += len(batch_df)
                    except (urllib3.exceptions.ConnectionError or urllib3.exceptions.HTTPError) as err:
                        print (err.args)
                        continue
                    break

        ver += cdf_batch_size #следующая итерация чтения 10 версий

# выводим информацию про то, сколько было прочитано строк, сколько времени работал скрипт и средняя скорость перекладывания данных
current_datetime = datetime.now()
print(f"Записано строк: {total_len} - за: {(current_datetime - start_datetime).total_seconds()} секунд. Средняя скорость чтения и записи: {total_len / (current_datetime - start_datetime).total_seconds()} строк в секунду ")
```

## Как прочитать данные с помощью spark

Перед началом работы установите библиотеку delta_sharing с помощью `pip3 install delta_sharing`

### Версия коннектора

В примере используется последняя на момент написания версия коннектора для Apache Spark 3.2.0. Если у вас возникли проблемы с версией, можно уточнить актуальную [здесь](https://github.com/delta-io/delta-sharing/blob/main/README.md)

```
import delta_sharing
from pyspark.sql import SparkSession
import pathlib
import delta_sharing
from delta_sharing.rest_client import DataSharingRestClient
from delta_sharing.protocol import DeltaSharingProfile
from delta_sharing.rest_client import DataSharingRestClient, HTTPError
from delta_sharing.protocol import CdfOptions
import pyarrow.parquet as pq
import requests
import io
from datetime import datetime
import urllib3

class Tables():          
    def __init__(self, database, schema, source, target):  
        self.database = database # БД, откуда читаем из Mindbox
        self.schema = schema # схема, откуда читаем из Mindbox
        self.source = source # таблица, откуда читаем из Mindbox
        self.target = target # таблица, куда пишем в вашем DWH
        
tables = []
tables.append ( Tables('exports', 'ProcessingOrders', 'BonusPointChanges', 'BonusPointChanges_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'BalanceChangeKinds', 'BalanceChangeKinds_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'BonusPointsMechanics', 'BonusPointsMechanics_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Balances', 'Balances_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'NegativeCustomerBalanceChangeDetails', 'NegativeCustomerBalanceChangeDetails_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Orders', 'Orders_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'Purchases', 'Purchases_raw') )
tables.append ( Tables('exports', 'ProcessingOrders', 'PurchaseStatuses', 'PurchaseStatuses_raw') )
tables.append ( Tables('exports', 'Mailings', 'Mailings', 'Mailings_raw') )
tables.append ( Tables('exports', 'Mailings', 'SubscriptionTopics', 'SubscriptionTopics_raw') )
tables.append ( Tables('exports', 'Mailings', 'MailingsTags', 'MailingsTags_raw') )
tables.append ( Tables('exports', 'Mailings', 'CustomerMessagesStatuses', 'CustomerMessagesStatuses_raw') )
tables.append ( Tables('exports', 'CDP', 'MergedCustomers', 'MergedCustomers_raw') )
tables.append ( Tables('exports', 'CDP', 'Folders', 'Folders_raw') )
tables.append ( Tables('exports', 'CDP', 'Tags', 'Tags_raw') )
tables.append ( Tables('exports', 'CDP', 'Segmentations', 'Segmentations_raw') )
tables.append ( Tables('exports', 'CDP', 'Segments', 'Segments_raw') )
tables.append ( Tables('exports', 'CDP', 'CustomerSegmentHistory', 'CustomerSegmentHistory_raw') )
tables.append ( Tables('exports', 'AbTests', 'AbTests', 'AbTests_raw') )
tables.append ( Tables('exports', 'AbTests', 'AbTestVariants', 'AbTestVariants_raw') )
tables.append ( Tables('exports', 'AbTests', 'ScenariosAbTestParticipants', 'ScenariosAbTestParticipants_raw') )

# Создание SparkSession
spark = (
    SparkSession.builder.config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-azure:3.3.1,io.delta:delta-core_2.12:2.2.0,io.delta:delta-sharing-spark_2.12:3.2.0",
    )
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

share_file_path = str(pathlib.Path().resolve()) + "/Profile.json" # аутентифицируемся

# Сколько файлов с данными читаем за раз
cdf_batch_size = 10

for t in tables:

    '''Вставьте ниже ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH'''
    
    latest_version = #здесь получаем последнюю версию данных из вашего dwh
    
    '''Вставьте выше ваш код для проверки последней прочитанной версии данных, которую скопировали в ваше DWH'''
    
    table_url = share_file_path + f"#{t.database}.{t.schema}.{t.source}"
    # Получаем свежие версии данных в таблице - версии, которые больше latest_version 
    ver = latest_version

    final_version = delta_sharing.get_table_version (table_url) # получаем максимальную версию данных в таблице

    # читаем по частям - по cdf_batch_size версий за раз, тк есть ограничение на количество запрашиваемых версий
    while ver <= final_version: # читаем до последней версии
        i = 0
        while True and i < 5: # 5 попыток чтения на случай если сервис недоступен
            i += 1
            try: 
                print (f"Получаем данные для таблицы {t.source} для версий от {ver} до {ver+cdf_batch_size-1}.")
                res = (
                    spark.read.format("deltaSharing")
                    .option("readChangeFeed", "true")
                    .option("startingVersion", ver)
                    .option("endingVersion", ver+cdf_batch_size-1)
                    .load(table_url)
                )
            except (delta_sharing.rest_client.HTTPError) as err: # ошибка может упасть, если не загружены новые данные или запрошено более 10 версий за раз
                print (f"Не получили обновленные данные для версий от {ver} до {ver+cdf_batch_size-1} c {i} раза. Причина: {err.response.text}")
                continue    
            break
        
        # если не получилось прочитать данные с 5 попыток, то пробуем читать из следующей таблицы
        if i == 5: 
                break      
        
        '''Ниже вставляем код для записи датафрейма res в ваше DWH'''

        print (f"Пишем данные версий от {ver} до {ver+cdf_batch_size-1} в таблицу {t.target}")               
        # Здесь записываем spark датафрейм res в ваше DWH
                       
        '''Выше вставляем код для записи датафрейма res в ваше DWH'''

        ver += cdf_batch_size #следующая итерация чтения 10 версий
```

## Поля _rowversion_ts, _isDeleted, _data_version

`_rowversion_ts` — временная метка, когда произошло изменение данных. Например, в выгрузку может попасть два изменения статуса заказа: сначала его оформили, а затем оплатили. Чтобы выбрать текущее состояние заказа, нужно выбрать запись с максимальным значением `_rowversion_ts`

`_isDeleted` — признак, что запись была вручную удалена из Mindbox, если его значение равно `true`. Автоудаленные записи будут экспортироваться как и обычные данные без признака `_isDeleted = true`

`_data_version` — версия выгруженных данных. Каждую новую выгрузку значение этого поля будет увеличено на 1. Используем для проверки, есть ли новые данные на сервере Mindbox.
