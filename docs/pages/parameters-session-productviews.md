---
title: Параметры для механики «Брошенный просмотр продукта»
slug: "parameters-session-productviews"
source_url: "https://help.mindbox.ru/docs/parameters-session-productviews"
vcs_path: "parameters-session-productviews.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:18303d44c00a22dc1a01d3107570e9eb20f379ea790d1b3d81f22f91a6621496"
---

# Параметры для механики «Брошенный просмотр продукта»

## Задача

В сценарии по [брошенной сессии](workflow-session.md) клиентам отправляются просмотренные продукты. Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам подходящие продукты.

О выводе просмотренных товаров **без привязки к сессии** — в [инструкции](parameters-recipient-productviews.md).

## Как собрать параметр

Чтобы обратиться в письме к данным из сессии используйте соответствующий базовый параметр:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28349%29.png)

Для просмотров в сессии добавьте параметр `ProductViews`:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28350%29.png)

Дальше выберите параметр или функцию в зависимости от того, какие просмотренные продукты нужно отобрать:

- `FilterBySegment(...)` — из определенного сегмента.  
  Можно дополнительно отобрать случайные, уникальные для каждой группы и доступные в регионе получателя продукты.
- `AvailableForRecipient` — доступные в регионе получателя.  
  Можно дополнительно отобрать случайные и уникальные для каждой группы продукты.
- `SinglePerGroup` — уникальные для каждой группы.  
  Можно дополнительно отобрать случайные продукты.
- `Random` — в случайном порядке.
- `Take(N)` — без фильтрации и сортировки.
- `Products` — без фильтрации и сортировки и без данных по просмотру (доступность и стоимость на момент просмотра). Уникальные продукты из просмотров.

Чтобы отбирать уникальные продукты из просмотров, коллекция должна содержать параметр `Products`.  
Например, `Session.ProductViews.AvailableForRecipient.Take(N)` включает все подходящие просмотры, даже с одинаковыми товарами.  
А `Session.ProductViews.AvailableForRecipient.Products.Take(N)` — только уникальные продукты из просмотров.

Пример коллекции — просмотры продуктов из сегмента «Известные в наличии»:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28351%29.png)

Для обращения к каждому элементу (просмотру) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

Параметры для вывода данных по каждому отобранному просмотру:

- `IsAvailable` — доступен ли был продукт на момент просмотра.
- `Price` — цена продукта на момент просмотра.

> **Цена и наличие продукта на момент просмотра** — неизменные свойства просмотра, отдельные от цены и наличия продукта на проекте.  
> В них фиксируется состояние товара, каким его увидел конкретный пользователь.

- `Product` — массив данных по текущему состоянию продукта на проекте:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28352%29.png)

В том числе наличие и цена продукта на данный момент.

## Пример верстки

Выведем в рассылке URL, картинку, название, описание и цену уникальных продуктов из просмотров:

```
@{for prod in Session.ProductViews.FilterBySegment("IzvestnyeVNalichii").Products.Take(4)}
    <a href="${prod.Url}"><img src="${prod.PictureUrl}"></a>
    ${prod.Name}
    ${truncate(prod.Description, 50)}
    ${FormatDecimal(prod.Price, "N0")} ₽
    <a href="${prod.Url}">Купить</a>
@{end for}
```

То же в виде [товарной сетки](how-to-display-data-as-a-table.md):

```
@{for row in tableRows(Session.ProductViews.FilterBySegment("IzvestnyeVNalichii").Products.Take(4), 2)}
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

В новом конструкторе можно настроить вывод просмотренных продуктов без использования параметров и кода — [инструкция](new-email-builder-viewed-products-in-session.md).
