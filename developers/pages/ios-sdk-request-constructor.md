---
title: Структура конструктора запроса iOS SDK
slug: "ios-sdk-request-constructor"
source_url: "https://developers.mindbox.ru/docs/ios-sdk-request-constructor"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:ec13392aa2815a2da85d9e426fd299988a9d418ca362a40ce43bfec35e1b2db1"
---

# Структура конструктора запроса iOS SDK

### IDS

`IDS` — структура для передачи набора идентификаторов в формате словаря **[String: String]**.

Дополнительно доступен инициализатор с параметром mindboxId, если требуется передать числовой идентификатор Mindbox.

```
let ids = IDS(value: ["externalUserId": "12345"], mindboxId: 67890)
```

Также есть возможность оперировать IDS как обычной коллекцией:

```
let ids: IDS = ["someId": "someValue"]
let someValue = ids["someId"] // "someValue"
```

---

### CustomFields

`CustomFields` используется для передачи дополнительных настраиваемых параметров в запросах.
Тип данных — **[String: Any]**. Доступа к значениям (чтения) не предусмотрено — объект используется **только для отправки**.

```
let customFields: CustomFields = ["someId": 1, "someId2": "2"]
```

---

### DateOnly

`DateOnly` передаёт дату в формате yyyy-MM-dd.

Создание и использование:

```
let date = Date()
// 1 вариант
let only = DateOnly(date)
// 2 вариант
date.asDateOnly()
```

---

### DateTime

`DateTime` - класс, используется для передачи на сервер даты и времени

Создание и использование:

```
let date = Date()
// 1 вариант
let dateTime = DateTime(date)
// 2 вариант
date.asDateTime()
```

---

## Запросы

### CustomerRequest

Используется для создания или обновления данных клиента.
Создаётся с помощью конструктора, в котором передаются необходимые данные клиента.

### DiscountRequest

Используется при работе со скидками.
Доступны два разных конструктора — выбор зависит от того, используете ли вы:
• promoCode, или
• externalPromoAction

### LineRequest

Создаётся с указанием количества и типа количества (quantityType).
quantityType — это enum, выбирается при инициализации.

### ProductListItemRequest

Имеет несколько конструкторов.
Выбор подходящего зависит от того, какие поля требуются в конкретном сценарии.

### ViewProductRequest

Содержит четыре конструктора.
Выберите подходящий исходя из того, какие данные доступны при формировании события.
