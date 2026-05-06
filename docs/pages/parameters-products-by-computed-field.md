---
title: Параметры для подборки по вычисляемому полю клиента
slug: "parameters-products-by-computed-field"
source_url: "https://help.mindbox.ru/docs/parameters-products-by-computed-field"
vcs_path: "parameters-products-by-computed-field.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:7bec2870e43ace69eda1a9446a262336589773c542437325b3010cfb61996356"
---

# Параметры для подборки по вычисляемому полю клиента

Инструкция подходит для любых задач, где нужно ограничить вывод продуктов значением [вычисляемого поля](computed-fields.md) клиента по дополнительному полю продукта, то есть отбирать товары с предпочитаемым признаком.

Можно выводить подборки по любимому цвету, стране отдыха, жанру книг и т.д.

Рассмотрим на примере размера одежды.

## Задача

С помощью вычисляемого поля определили, какие размеры чаще всего покупают клиенты.  
Хотим отправить им подборку новинок и выводить только товары в подходящем размере.

Для этого нужно составить верстку рассылки с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

## Как это работает

- На проекте есть [вычисляемое поле](computed-fields.md), которое определяет, какой размер ([дополнительное поле](additional-data.md) по продукту) клиент чаще всего покупает, и записывает значение в карточку:

![parameters-products-by-computed-field-formula](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/parameters-products-by-computed-field-formula.png)

![parameters-products-by-computed-field-client](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/parameters-products-by-computed-field-client.png)  
*Клиент чаще всего покупает вещи в размере M*

- С помощью функции шаблонизатора можно из любого сегмента отбирать только продукты с нужным значением для конкретного клиента:

![parameters-products-by-computed-field-product](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/parameters-products-by-computed-field-product.png)  
*Размер соответствует вычисленному значению для клиента — продукт можно выводить в рассылке.*

## Как собрать параметр

Чтобы обратиться к списку всех уникальных продуктов, используйте базовый параметр `Products`:

![Products](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Products.png)

Выберите сегмент продуктов с помощью функции `GetBySegment()`:

![Products.GetBySegment](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Products.GetBySegment.png)

Отфильтруйте подборку по вычисляемому полю клиента функцией `FilterByRecipientCustomField()`:

![Products.GetBySegment.FilterByRecipientCustomField](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Products.GetBySegment.FilterByRecipientCustomField.png)

Задайте дополнительную фильтрацию и сортировку продуктов:

- `AvailableForRecipient` — доступные в регионе получателя.  
  Можно дополнительно отобрать случайные и уникальные для каждой группы продукты.
- `Random` — в случайном порядке.
- `SinglePerGroup` — уникальные для каждой группы.  
  Можно дополнительно отобрать случайные продукты.
- `Take()` — без фильтрации и сортировки.

Можно вывести любые поля по продуктам из собранной коллекции:

![Products.GetBySegment.FilterByRecipientCustomField.Take](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Products.GetBySegment.FilterByRecipientCustomField.Take.png)

## Пример верстки

Выведем в рассылке название, картинку, цену и размер продукта:

```
Новинки, которые вам идеально подойдут

@{for item in Products.GetBySegment("Novinki").FilterByRecipientCustomField("BoughtSize").Take(4)}
    <a href="${item.URL}"}><img src="${item.PictureUrl}"></a>
    ${item.Name}
    Размер: ${item.CustomField.Size.Name}
    ${item.Price} руб.
@{end for}
```

Пользователь получит в письме:

![parameters-products-by-computed-field-result](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/parameters-products-by-computed-field-result.png)
