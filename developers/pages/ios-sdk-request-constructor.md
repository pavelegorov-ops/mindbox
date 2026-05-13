---
title: Структура конструктора запроса iOS SDK
slug: "ios-sdk-request-constructor"
source_url: "https://developers.mindbox.ru/docs/ios-sdk-request-constructor"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c319f714d756160b8b3e6c97dd124c448263bf22859b065fdb27566570f0743c"
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
