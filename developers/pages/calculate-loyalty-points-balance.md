---
title: Как рассчитать балльный баланс
slug: "calculate-loyalty-points-balance"
source_url: "https://developers.mindbox.ru/docs/calculate-loyalty-points-balance"
breadcrumb:
  - Данные для аналитики
  - Как периодически обновлять данные
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:cc46927972675e56a494b13f0f48a18d76d40114f15cea06cfb05231d2f16e3b"
---

# Как рассчитать балльный баланс

# Как рассчитать балльный баланс

Эта статья содержит готовые SQL-скрипты для анализа балльного баланса клиентов: начислений, списаний, сгораний и остатков баллов на определенные даты. Используйте их для построения отчетов в вашей системе.

## Предварительные требования

Перед использованием запросов убедитесь, что вы:

- Выгрузили данные из Mindbox по инструкции [«Как прочитать данные»](how-to-read-data.md);
- Создали необходимые таблицы: `BonusPointChanges_dm`, `BonusPointsMechanics_dm`, `NegativeCustomerBalanceChangeDetails_dm` по инструкции [«Как периодически обновлять данные»](periodic-data-updates.md).

---

### Обратите внимание

Все скрипты используют преобразование времени `date_add(hour, 3, ...)` для приведения времени в формате UTC к московскому времени (UTC+3). Если ваша система работает в другом часовом поясе, измените значение на нужное смещение.

## Начисления за период

```
--2024-07-01 - дата начала периода
--2024-07-07 - дата конца периода

SELECT 
    name, 
    SUM (am)
FROM ( 
    SELECT  
        toFloat32 ( bpc.changeAmount ) AS am,
        bpm.name AS name
    FROM 
        BonusPointChanges_dm bpc
    JOIN BonusPointsMechanics_dm bpm ON bpc.mechanicsInternalId = bpm.id
    WHERE 
        date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) )  >= '2024-07-01' 
        AND date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) ) < '2024-07-07'
)
WHERE 
    am > 0
GROUP BY 
    name
```

## Сгорания за период

```
--2024-07-01 - дата начала периода
--2024-07-07 - дата конца периода

SELECT 
    name, 
    SUM (am)
FROM ( 
    SELECT  
        toFloat32 ( bpc.changeAmount ) AS am,
        bpm.name AS name
    FROM 
        BonusPointChanges_dm bpc
    JOIN BonusPointsMechanics_dm bpm ON bpc.mechanicsInternalId = bpm.id
    WHERE 
        date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) )  >= '2024-07-01' 
        AND date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) ) < '2024-07-07'
        AND changeTypeSystemName IN ( 'Expired' )
)
WHERE 
    am < 0
GROUP BY 
    name
```

## Списания за период

```
--2024-07-01 - дата начала периода
--2024-07-07 - дата конца периода

SELECT 
    name, 
    SUM (am)
FROM (
    SELECT 
        bpm.name AS name,
        toFloat32 (n.spentAmount) AS am
    FROM 
        NegativeCustomerBalanceChangeDetails_dm n
    JOIN BonusPointChanges_dm bpc_positive ON n.positiveCustomerBalanceChangeId = bpc_positive.id
    JOIN BonusPointChanges_dm bpc_negative ON n.negativeCustomerBalanceChangeId = bpc_negative.id
    JOIN BonusPointsMechanics_dm bpm ON bpc_negative.mechanicsInternalId = bpm.id
    WHERE 
        date_add ( hour, 3, toDateTime64 (bpc_negative.dateTimeUtc, 0) )  >= '2024-07-01' 
        AND date_add ( hour, 3, toDateTime64 (bpc_negative.dateTimeUtc, 0) ) < '2024-07-07' 
        AND bpc_negative.changeTypeSystemName in ( 'RetailOrderPayment', 'Custom' )
) 
GROUP BY 
    name
```

## Сумма баллов на начало периода / конец периода

```
--2024-07-01 - дата начала / конца периода

SELECT --Все начисления до начала периода
    name, 
    SUM (amount) 
FROM (
    SELECT 
        name, 
        SUM (am) AS amount
    FROM ( 
        SELECT  
            bpm.name AS name,
            toFloat32OrZero ( bpc.changeAmount ) AS am
        FROM 
            BonusPointChanges_dm bpc
        JOIN BonusPointsMechanics_dm bpm ON bpc.mechanicsInternalId = bpm.id
        WHERE 
            date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) )  < '2024-07-01' 
    )
    WHERE 
        am > 0
    GROUP BY 
        name

    UNION ALL  

    SELECT --Все списания / сгорания до начала периода
    name, 
        (-1) * SUM (am) AS amount
    FROM (
        SELECT 
            bpm.name AS name,
        toFloat32 (n.spentAmount) AS am
        FROM 
            NegativeCustomerBalanceChangeDetails_dm n
        JOIN BonusPointChanges_dm bpc_positive ON n.positiveCustomerBalanceChangeId = bpc_positive.id
        JOIN BonusPointChanges_dm bpc_negative ON n.negativeCustomerBalanceChangeId = bpc_negative.id
        JOIN BonusPointsMechanics_dm bpm ON bpc_positive.mechanicsInternalId = bpm.id
        WHERE 
            date_add ( hour, 3, toDateTime64 (bpc_negative.dateTimeUtc, 0) )  < '2024-07-01' 
    ) 
    GROUP BY 
        name
)
GROUP BY 
    name
```

## Сумма активных баллов на начало периода / конец периода

```
--2024-07-01 - дата начала / конца периода

SELECT --Все активированные баллы до начала периода
    name, 
    SUM (amount) 
FROM (
    SELECT 
        name, 
        SUM (am) AS amount
    FROM ( 
        SELECT  
            toFloat32OrZero ( bpc.changeAmount ) AS am,
            bpm.name AS name
        FROM 
            BonusPointChanges_dm bpc
        JOIN BonusPointsMechanics_dm bpm ON bpc.mechanicsInternalId = bpm.id
        WHERE 
            date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) )  < '2024-07-01' 
            AND ( bpc.availableFromDateTimeUtc < '2024-07-01' OR empty(bpc.availableFromDateTimeUtc) )
    )
    WHERE 
        am > 0
    GROUP BY 
        name

    UNION ALL   

    SELECT --Все списания / сгорания до начала периода
        name, 
        (-1) * SUM (am) AS amount
    FROM (
        SELECT 
            bpm.name AS name,
            toFloat32 (n.spentAmount) AS am
        FROM 
            NegativeCustomerBalanceChangeDetails_dm n
        JOIN BonusPointChanges_dm bpc_positive ON n.positiveCustomerBalanceChangeId = bpc_positive.id
        JOIN BonusPointChanges_dm bpc_negative ON n.negativeCustomerBalanceChangeId = bpc_negative.id
        JOIN BonusPointsMechanics_dm bpm ON bpc_positive.mechanicsInternalId = bpm.id
        WHERE 
            date_add ( hour, 3, toDateTime64 (bpc_negative.dateTimeUtc, 0) )  < '2024-07-01' 
    ) 
    GROUP BY 
        name
)
GROUP BY 
    name
```

## Сумма заблокированных баллов на начало периода / конец периода

```
--2024-07-01 - дата начала / конца периода

SELECT 
    name, 
    SUM (am) AS amount
FROM ( 
	SELECT  
	    toFloat32OrZero ( bpc.changeAmount ) AS am,
	    bpm.name AS name
	FROM 
	    BonusPointChanges_dm bpc
	JOIN BonusPointsMechanics_dm bpm ON bpc.mechanicsInternalId = bpm.id
	WHERE 
	    date_add ( hour, 3, toDateTime64 (dateTimeUtc, 0) )  < '2024-07-01' 
	    AND bpc.availableFromDateTimeUtc >= '2024-07-01' AND notEmpty (bpc.availableFromDateTimeUtc)
)
WHERE 
    am > 0
GROUP BY 
    name
```
