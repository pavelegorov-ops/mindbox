---
title: Примеры настройки подарочных карт
slug: "gift-cards-examples"
source_url: "https://help.mindbox.ru/docs/gift-cards-examples"
vcs_path: "gift-cards-examples.md"
toc_path:
  - Лояльность и акции
  - Подарочные карты
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:1486fbaa1008355663c28b5b75d5e7efb5dcfc95c8ce3775b5c4b03f7eac4833"
---

# Примеры настройки подарочных карт

Эта статья описывает три типовых сценария работы с подарочными картами:

1. Карты с фиксированным номиналом
2. Карты с произвольной суммой
3. Миграция проданных карт из других систем.

Для загрузки карт в каждом сценарии необходимо:

1. Импортировать пул подарочных карт. [Общая инструкция по импорту](https://help.mindbox.ru/docs/gift-card-pools-import).
2. Загрузить список подарочных карт в созданный ранее пул. [Общая инструкция по загрузке](https://help.mindbox.ru/docs/gift-cards-import).

## Кейс 1: Карта с фиксированным номиналом и CVV

### Описание сценария

Компания продает физические или электронные подарочные карты с параметрами:

- Номинал: **1000 ₽**
- CVV: **обязателен**
- Срок действия карты: **3 года** с момента продажи

### Пул подарочных карт

Импортируйте пул со следующими параметрами:

- Фиксированный номинал (`Amount`): 1000
- Требовать CVV (`IsCvvRequired`): true
- Срок действия 3 года:
  - `ExpirationType`: Year
  - `Expiration`: 3

**Пример импорта пула:**

| PoolName | PoolSystemName | ProductExternalId | ExternalSystem | Amount | IsCvvRequired | ExpirationType | Expiration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Подарочная карта на 1000 | Gift1000Cvv3y | Gift1000Cvv3y | Site | 1000 | true | Year | 3 |

**Пример в формате строки с разделителем**

```
PoolName;PoolSystemName;ProductExternalId;ExternalSystem;Amount;IsCvvRequired;ExpirationType;Expiration;
Подарочная карта на 1000;Gift1000Cvv3y;Gift1000Cvv3y;Site;1000;true;Year;3;
```

### Импорт карт

Поле `Amount` обязательно для каждой карты, даже если в пуле установлен фиксированный номинал.

**Пример файла импорта карт:**

| Number | PoolSystemName | Cvv | Amount | Status |
| --- | --- | --- | --- | --- |
| 1234 | Gift1000Cvv3y | 123 | 1000 | Inactive |
| 5678 | Gift1000Cvv3y | 456 | 1000 | Inactive |

**Пример в формате строки с разделителем**

```
Number;PoolSystemName;Cvv;Amount;Status;
1234;Gift1000Cvv3y;123;1000;Inactive;
5678;Gift1000Cvv3y;456;1000;Inactive;
```

Результат

- Карты загружены в статусе **«Не активирована»**;
- Карты доступны для продажи;
- При продаже карта активируется и начинается отсчет срока действия (3 года)

---

## Кейс 2: Карта с произвольной суммой (сумма задается при продаже)

### **Описание сценарий:**

Компания продает подарочные карты с **произвольной суммой**, которую клиент выбирает при покупке (например, от 500 до 10 000 ₽).

- Номинал: задается при продаже
- CVV: не используется
- Срок действия: 3 года с момента продажи

### Пул подарочных карт

Создайте пул со следующими параметрами:

- Без фиксированного номинала (`IsCustomAmount`): **true**
- Требовать CVV (`IsCvvRequired`): **false**
- Срок действия 3 года:
  - `ExpirationType`: Year
  - `Expiration`: 3

**Файл импорта пула:**

| PoolName | PoolSystemName | ProductExternalId | ExternalSystem | IsCvvRequired | ExpirationType | Expiration | IsCustomAmount |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Подарочная карта без фиксированного номинала | GiftOpenAmount3y | GiftOpenAmount3y | Site | false | Year | 3 | true |

**Пример в формате строки с разделителем**

```
PoolName;PoolSystemName;ProductExternalId;ExternalSystem;IsCvvRequired;ExpirationType;Expiration;IsCustomAmount;
Подарочная карта без фиксированного номинала;GiftOpenAmount3y;GiftOpenAmount3y;Site;false;Year;3;true;
```

### Импорт карт

Для карт с произвольной суммой не нужно указывать номинал карты (`Amount`).

**Пример файла импорта карт:**

| Number | PoolSystemName | Status |
| --- | --- | --- |
| 1234 | GiftOpenAmount3y | Inactive |
| 5678 | GiftOpenAmount3y | Inactive |

**Пример в формате строки с разделителем**

```
Number;PoolSystemName;Status;
1234;Gift1000Cvv3y;Inactive;
5678;Gift1000Cvv3y;Inactive;
```

Результат

- Карта загружается в систему в статусе **«Не активирована»**;
- При продаже:

  - карта активируется
  - карте присваивается номинал, указанный покупателем
  - запускает отсчет срока действия (3 года)

---

## Кейс 3: Импорт проданных карт (миграция)

### Описание сценария

Компания переносит подарочные карты из старой системы:

- Карты уже **были проданы** ранее;
- Известна дата продажи;
- Карты должны быть **активными**;
- Срок действия считается от даты покупки в прошлом.

### Пул подарочных карт

Для этого сценария пул должен иметь заданный **срок действия** (`ExpirationType` и `Expiration`).

Создайте пул со следующими параметрами:

- Фиксированный номинал (`Amount`): **3000 ₽**
- Срок действия 3 года:
- `ExpirationType`: Year
- `Expiration`: 3 года

**Файл импорта пула:**

| PoolName | PoolSystemName | ProductExternalId | ExternalSystem | IsCvvRequired | ExpirationType | Expiration | Amount |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Подарочная карта на 3000 | Gift3000Migration3y | Gift3000Migration3y | Site | false | Year | 3 | 3000 |

**Пример в формате строки с разделителем**

```
PoolName;PoolSystemName;ProductExternalId;ExternalSystem;IsCvvRequired;ExpirationType;Expiration;Amount;
Подарочная карта на 3000;Gift3000Migration3y;Gift3000Migration3y;Site;false;Year;3;3000;
```

### Импорт карт

Передайте дополнительные поля:

- `PurchasePointOfContact` - идентификатор точки контакта, где карта была выдана.

  Как определить значение `PurchasePointOfContact`

  1. Перейдите в раздел **Настройки → Клиенты и действия → Точки контакта**.
  2. Найдите нужную точку контакта по его названию. Для импорта нужно значение из колонки «Внешний идентификатор»:  
     ![point-of-contact](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/point-of-contact.png)
- `PurchaseDateTimeUtc` - дата и время покупки в UTC.

Карты должны быть в статусе `CanBeUsed`.

**Пример файла импорта карт:**

| Number | PoolSystemName | Amount | Status | PurchasePointOfContact | PurchaseDateTimeUtc |
| --- | --- | --- | --- | --- | --- |
| 1234 | Gift3000Migration3y | 3000 | CanBeUsed | offline_store_12 | 2025-05-10 |
| 5678 | Gift3000Migration3y | 3000 | CanBeUsed | offline_store_12 | 2025-05-10 |

**Пример в формате строки с разделителем**

```
Number;PoolSystemName;Amount;Status;PurchasePointOfContact;PurchaseDateTimeUtc;
1234;Gift3000Migration3y;3000;CanBeUsed;offline_store_12;2025-05-10;
5678;Gift3000Migration3y;3000;CanBeUsed;offline_store_12;2025-05-10;
```

Результат

- Карты импортированы в статусе «Активна»
- Карту нельзя продать повторно благодаря `PurchaseDateTimeUtc`;
- Срок действия считается как **PurchaseDateTimeUtc + срок действия пула**.
