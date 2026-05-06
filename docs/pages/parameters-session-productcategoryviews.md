---
title: Параметры для механики «Брошенная категория»
slug: "parameters-session-productcategoryviews"
source_url: "https://help.mindbox.ru/docs/parameters-session-productcategoryviews"
vcs_path: "parameters-session-productcategoryviews.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:2c92f6b1e824ac7ca36167c47290364c0afbe07bad556be1ac098258dcd5fd7e"
---

# Параметры для механики «Брошенная категория»

После просмотра категорий клиенту можно отправить:

- продукты из просмотренных категорий;
- список просмотренных категорий;
- продуктовые рекомендации к ним.

Рассмотрим примеры задач и решения для каждой из них.

## Вывести продукты из просмотренных категорий

### Задача

В сценарии по [брошенной сессии](workflow-session.md) клиентам отправляются продукты из просмотренных категорий. Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам подходящие продукты.

### Как собрать параметр

Чтобы обратиться в письме к данным из сессии используйте соответствующий базовый параметр:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28349%29.png)

Для просмотров категорий в сессии добавьте параметр `ProductCategoryViews` и отберите уникальные категории функцией `GetUnique()`:

![Снимок экрана 2023-12-07 в 00.41.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2000.41.15.png)

Параметр `Products` отберет продукты из просмотренных категорий:

![Снимок экрана 2023-12-07 в 22.17.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2022.17.26.png)

Дальше выберите параметр или функцию в зависимости от того, какие продукты из просмотренных категорий нужно отобрать:

- `FilterBySegment(...)` — из определенного сегмента.  
  Можно дополнительно отобрать случайные, уникальные для каждой группы и доступные в регионе получателя продукты.
- `AvailableForRecipient` — доступные в регионе получателя.  
  Можно дополнительно отобрать случайные и уникальные для каждой группы продукты.
- `SinglePerGroup` — уникальные для каждой группы.  
  Можно дополнительно отобрать случайные продукты.
- `Random` — в случайном порядке.
- `Take(N)` — без фильтрации и сортировки.

Коллекция для вывода продуктов из просмотренных в сессии категорий, входящих в сегмент «Известные в наличии»:

![Снимок экрана 2023-12-07 в 00.55.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2000.55.07.png)

Для обращения к каждому элементу (категории) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

В новом конструкторе можно настроить вывод продуктов из просмотренной категории без использования параметров и кода — [инструкция](email-editor-products-from-viewed-categories-in-session.md).

### Пример верстки

Выведем в рассылке URL, картинку, название, описание и цену продукта:

```
@{for prod in Session.ProductCategoryViews.GetUnique(4).Products.FilterBySegment("IzvestnyeVNalichii").Take(4)}
    <a href="${prod.Url}"><img src="${prod.PictureUrl}"></a>
    ${prod.Name}
    ${truncate(prod.Description, 50)}
    ${FormatDecimal(prod.Price, "N0")} ₽
    <a href="${prod.Url}">Купить</a>
@{end for}
```

То же в виде [товарной сетки](how-to-display-data-as-a-table.md):

```
@{for row in tableRows(Session.ProductCategoryViews.GetUnique(4).Products.FilterBySegment("IzvestnyeVNalichii").Take(4), 2)}
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

Пользователь получит в письме:

![Снимок экрана 2023-12-06 в 03.44.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-06%20%D0%B2%2003.44.21.png)

## Вывести просмотренные категории

### Задача

В сценарии по [брошенной сессии](workflow-session.md) клиентам отправляется список просмотренных категорий. Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам подходящие категории.

### Как собрать параметр

Чтобы обратиться в письме к данным из сессии используйте соответствующий базовый параметр:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28349%29.png)

Для просмотров категорий в сессии добавьте параметр `ProductCategoryViews` и отберите уникальные категории функцией `GetUnique()`:

![Снимок экрана 2023-12-07 в 00.41.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2000.41.15.png)

Параметр `Categories` отберет коллекцию с просмотренными категориями:

![Снимок экрана 2023-12-07 в 19.25.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2019.25.38.png)

Для обращения к каждому элементу (категории) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

Параметры для вывода данных по каждой категории:

- `IDs` — идентификатор категории во [внешней системе](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D1%8E%D1%8E-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83.md).
- `Name` — название категории.
- `Recommendations` — рекомендации к категории. [Подробнее](parameters-session-productcategoryviews.md#vyvesti-rekomendacii-k-prosmotrennym-kategoriyam).

Использовать дополнительно функцию `Take` не нужно, так как количество категорий уже задано в функции `GetUnique()`.

### Пример верстки

Выведем в рассылке названия просмотренных категорий:

```
Вас заинтересовали категории:
@{for cat in Session.ProductCategoryViews.GetUnique(10).Categories}
    ${cat.Name}
@{end for}
```

Результат:

> Вас заинтересовали категории: Аксессуары Верхняя одежда

Чтобы вывести их через запятую:

```
Вас заинтересовали категории:
@{set all = ""}
@{for cat in Session.ProductCategoryViews.GetUnique(10).Categories}
    @{if all != ""}
        @{set all = all & ", "}
    @{end if}
@{set all = all & cat.Name}
@{end for}
${all}
```

Результат:

> Вас заинтересовали категории: Аксессуары, Верхняя одежда

## Вывести рекомендации к просмотренным категориям

## Задача

В сценарии по [брошенной сессии](workflow-session.md) клиентам отправляются рекомендации с популярными товарами из просмотренных категорий. Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам подходящие продукты.

## Как собрать параметр

Чтобы обратиться в письме к данным из сессии используйте соответствующий базовый параметр:

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28349%29.png)

Для просмотров категорий в сессии добавьте параметр `ProductCategoryViews` и отберите уникальные категории функцией `GetUnique()`:

![Снимок экрана 2023-12-07 в 00.41.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2000.41.15.png)

Параметр `Categories` отберет коллекцию с просмотренными в сессии категориями:

![Снимок экрана 2023-12-07 в 19.25.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2019.25.38.png)

Для обращения к каждому элементу (категории) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

Использовать дополнительно функцию `Take` не нужно, так как количество категорий уже задано в функции `GetUnique()`.

Для получения коллекции с продуктовыми рекомендациями к категориям добавьте параметр `Recommendations` и выберите подходящие [рекомендации](recommendations-bestsellers.md) (доступен алгоритм типа «Популярные продукты по категориям»). Можно ограничить количество продуктов функцией `Take`:

![Снимок экрана 2023-12-07 в 22.38.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2022.38.59.png)

Для обращения к каждому элементу (рекомендованному продукту) собранной коллекции используйте цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

То есть для вывода рекомендаций нужно использовать два цикла `for...end for`.

#### Пример верстки

Выведем в рассылке URL, картинку, название и цену рекомендаций:

```
Популярные товары в категории @{for item in Session.ProductCategoryViews.GetUnique(1).Categories}${item.Name}

@{for reco in item.Recommendations.RecoCategory.Take(4)}

<a href="${reco.Url}"><img src="${reco.PictureUrl}"></a>
    ${reco.Name}
    ${FormatDecimal(reco.Price, "N0")} ₽
    <a href="${reco.Url}">Купить</a>
@{end for}
@{end for}
```

То же в виде [товарной сетки](how-to-display-data-as-a-table.md):

```
Популярные товары в категории 
@{for item in Session.ProductCategoryViews.GetUnique(1).Categories}${item.Name}
    @{for row in tableRows(item.Recommendations.RecoCategory.Take(4), 2)}
        @{for reco in row.Cells}
            @{if reco.value != null}
                <a href="${reco.Value.Url}"><img src="${reco.Value.PictureUrl}"></a>
                ${reco.Value.Name}
                ${FormatDecimal(reco.Value.Price, "N0")} ₽
                <a href="${reco.Value.Url}">Купить</a>
            @{end if}
        @{end for}
    @{end for}
@{end for}
```

Пользователь получит в письме:

![Снимок экрана 2023-12-07 в 23.25.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-07%20%D0%B2%2023.25.04.png)
