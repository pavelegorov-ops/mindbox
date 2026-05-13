---
title: Как вывести в письме начисленные за заказ баллы
slug: "parameters-order-balance-earned"
source_url: "https://help.mindbox.ru/docs/parameters-order-balance-earned"
vcs_path: "parameters-order-balance-earned.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Заказы и сегменты
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:fe3dee97ec6de473b664cb523acd1bb029177bda5bfd67c5be0ff6a8a29fbddf"
---

# Как вывести в письме начисленные за заказ баллы

Чтобы собрать параметр для вывода начисленных баллов, используйте следующие составляющие:

1. Базовый параметр `Order` (для автоматических рассылок по конкретному заказу) или `Recipient.Orders.FilterBySegment("X").Take(N)` (для вывода заказов клиента без привязки к событию);
2. `AppliedPromotions` — обращается ко всем акциям в заказе;
3. Функция `GetEarnedBonusPoints()` — отбирает все начисления баллов за заказ:

![Снимок экрана 2023-05-03 в 15.12.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-05-03%20%D0%B2%2015.12.43.png)

4. Дальше — по задаче:

- `TotalAmount` — выводит все полученные баллы.

Параметр учитывает возвраты и отмены, поэтому выводит актуальное количество.

- `ByPromotion` — используется для разбивки начислений по акциям, по каждой из которых можно вывести:
  - `Amount` — количество баллов;
  - `Coupon.Code` — использованный промокод;
  - `Promotion.Name` — название акции.

Если акция применилась по нескольким позициям, каждое начисление по акции выводится отдельно.

> Например, есть заказ с двумя позициями. По акции получено в целом 200 баллов, по 100 на каждый товар. Хоть акция и одна, для системы это два разных начисления на каждую из позиций, поэтому параметр `ByPromotion` выведет каждое из них отдельно.

Примеры верстки по задачам.

**Вывести все начисленные за заказ баллы:**

```
За заказ получено баллов: ${Order.AppliedPromotions.GetEarnedBonusPoints("OsnovnojSchet").TotalAmount}
```

*"OsnovnojSchet" — название балльного счета; может отличаться от проекта к проекту.*

**Разбивка по акциям:**

```
В том числе:

@{for bonus in Order.AppliedPromotions.Discounts.GetBonusPointsDiscounts("OsnovnojSchet").ByPromotion}
    <br>${bonus.Amount} по акции ${bonus.Promotion.Name}.
@{end for}
```
