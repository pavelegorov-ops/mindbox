---
title: Вывести последние просмотренные продукты
slug: "parameters-recipient-productviews"
source_url: "https://help.mindbox.ru/docs/parameters-recipient-productviews"
vcs_path: "parameters-recipient-productviews.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:774822eda987715f00e27c6440d3599d9b815dd6b909cefe712aeb702da4026f"
---

# Вывести последние просмотренные продукты

## Задача

Клиентам отправляют недавно просмотренные товары без привязки к конкретной сессии.  
Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам подходящие продукты.

О выводе просмотренных товаров **в брошенной сессии** — в [инструкции](parameters-session-productviews.md).

## Как собрать параметр

Используйте базовый параметр по клиенту `Recipient`:

![Снимок экрана 2023-12-08 в 00.08.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-08%20%D0%B2%2000.08.31.png)

Для просмотров добавьте параметр `ProductViews`:

![Снимок экрана 2023-12-08 в 00.09.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-08%20%D0%B2%2000.09.03.png)

Дальше выберите параметр или функцию в зависимости от того, какие продукты нужно отобрать:

- `FilterBySegment(...)` — из определенного сегмента.  
  Можно дополнительно отобрать случайные, уникальные для каждой группы и доступные в регионе получателя продукты.
- `AvailableForRecipient` — доступные в регионе получателя.  
  Можно дополнительно отобрать случайные и уникальные для каждой группы продукты.
- `SinglePerGroup` — уникальные для каждой группы.  
  Можно дополнительно отобрать случайные продукты.
- `Random` — в случайном порядке.
- `Take(N)` — без фильтрации и сортировки.
- `Products` — продукты без фильтрации и сортировки и без данных по просмотру (доступность и стоимость на момент просмотра). Уникальные продукты из просмотров.

Чтобы отбирать уникальные продукты из просмотров, коллекция должна содержать параметр `Products`.  
Например, `Recipient.ProductViews.AvailableForRecipient.Take(N)` включает все подходящие просмотры, даже с одинаковыми товарами.  
А `Recipient.ProductViews.AvailableForRecipient.Products.Take(N)` — только уникальные продукты из просмотров.

Пример коллекции — просмотры продуктов из сегмента «В наличии»:

![Снимок экрана 2023-12-08 в 00.12.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-08%20%D0%B2%2000.12.21.png)

Для обращения к каждому элементу (просмотру) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

Параметры для вывода данных по каждому отобранному просмотру:

- `IsAvailable` — доступен ли был продукт на момент просмотра.
- `Price` — цена продукта на момент просмотра.

> **Цена и наличие продукта на момент просмотра** — неизменные свойства просмотра, отдельные от цены и наличия продукта на проекте.  
> В них фиксируется состояние товара, каким его увидел конкретный пользователь.

- `Product` — массив данных по текущему состоянию продукта на проекте:

![Снимок экрана 2023-12-08 в 00.13.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-08%20%D0%B2%2000.13.10.png)

В том числе наличие и цена продукта на данный момент.

## Пример верстки

Выведем в рассылке URL, картинку, название, описание и цену уникальных продуктов из просмотров:

```
@{for prod in Recipient.ProductViews.FilterBySegment("VNalichii").Products.Take(4)}
    <a href="${prod.Url}"><img src="${prod.PictureUrl}"></a>
    ${prod.Name}
    ${truncate(prod.Description, 50)}
    ${FormatDecimal(prod.Price, "N0")} ₽
    <a href="${prod.Url}">Купить</a>
@{end for}
```

То же в виде [товарной сетки](how-to-display-data-as-a-table.md):

```
@{for row in tableRows(Recipient.ProductViews.FilterBySegment("VNalichii").Products.Take(4), 2)}
    @{for cell in row.Cells}
        @{if cell.value != null}
            <a href="${cell.value.Url}"><img src="${cell.value.PictureUrl}"></a>
            ${cell.value.Name}
            ${truncate(cell.value.Description, 50)}
            ${FormatDecimal(cell.value.Price, "N0")} ₽
            <a href="${cell.value.Url}">Купить</a>
        @{end if}                                  
    @{end for}
@{end for}
```

Пользователь получит в письме:

![Снимок экрана 2023-12-06 в 02.01.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-06%20%D0%B2%2002.01.07.png)
