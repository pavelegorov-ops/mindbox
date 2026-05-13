---
title: Параметры для рассылки «Цена на самый просматриваемый или покупаемый продукт снизилась»
slug: "parameters-customfield-computed-field-price"
source_url: "https://help.mindbox.ru/docs/parameters-customfield-computed-field-price"
vcs_path: "parameters-customfield-computed-field-price.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:1b909667ca702df5d00f2060d796e5365b3862f211f860797fb32c239bade34e"
---

# Параметры для рассылки «Цена на самый просматриваемый или покупаемый продукт снизилась»

## Задача

С помощью [сценария](workflow-computed-field-lower-price.md) клиентам отправляется уведомление о снижении цены на продукт из их [вычисляемого поля](computed-fields.md).

Нужно составить верстку рассылки, чтобы с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) выводить клиентам данный продукт.

## Как собрать параметр

Чтобы обратиться к продукту, используйте базовый параметр `Product`:

![parameters.Product](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/aa/parameters.Product.png)

Можно вывести любые поля по продукту, в том числе рекомендации к нему:

![parameters.Product.Recommendation](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/aa/parameters.Product.Recommendations.png)

## Пример верстки

Выведем в рассылке название, описание и текущую стоимость продукта:

```
На интересовавший вас товар снизилась цена:
${Product.Name}
${Truncate(Product.Description, 35)}
${Product.Price} р.

Вам также могут понравиться:
@{for reco in Product.Recommendations.Pohozhie.Take(3)}
<a href="${reco.Url}"><img src="${reco.PictureUrl}"></a>
    ${reco.Name}
    ${reco.Description}
    ${reco.Price}
@{end for}
```

Пользователь получит в письме:

> На один из ваших любимых товаров снизилась цена:  
> **Набор для бровей**  
> Серо-коричневые оттенки, кисточк...  
> 2390 р.
>
> Вам также могут понравиться:
>   
> ...
