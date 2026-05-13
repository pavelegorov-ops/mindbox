---
title: Параметры для вывода продуктов из предпочитаемой категории
slug: "parameters-category-from-computed-field"
source_url: "https://help.mindbox.ru/docs/parameters-category-from-computed-field"
vcs_path: "parameters-category-from-computed-field.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:ddfd1c56f1b4bc9b8d0e2488c4646d0bfc2564018cce2778a1786ddb59d2fc1d"
---

# Параметры для вывода продуктов из предпочитаемой категории

Одно из возможных применений [вычисляемого поля](computed-fields.md) — определение категории, которую пользователь чаще всего просматривает или покупает.

Рассмотрим способ вывода продуктов из такой категории с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

## Задача

Отправить клиентам, которые давно не совершали покупок, подборку с популярными новинками из их любимой категории.

![MostBoughtCategory-user](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/MostBoughtCategory-user.png)  
*Пример клиента с вычисленной категорией.*

## Как собрать параметр

Чтобы обратиться к карточке клиента, используем базовый параметр `Recipient`→ открываем список дополнительных и вычисляемых полей параметром `CustomField` → выбираем нужное вычисляемое поле → получаем параметр вида `Recipient.CustomField.<Вычисляемое поле>`

Для вывода доступны поля по категории:

![Recipient.CustomField.MostBoughtCategory](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Recipient.CustomField.MostBoughtCategory.png)

Чтобы отобрать рекомендации, параметром `Recommendations` переходим в список доступных [алгоритмов](personalisation.md#chto-takoe-rekomendacii) по категории → выбираем нужный → получаем параметр вида `Recipient.CustomField.<Вычисляемое поле>.Recommendations.<Алгоритм>.Take(<Количество элементов коллекции>)`

Для вывода доступны все поля по рекомендованным товарам:

![Recipient.CustomField.MostBoughtCategory.Recommendations](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Recipient.CustomField.MostBoughtCategory.Recommendations.png)

Так как собранный параметр является коллекцией, для обращения к продуктам в нем нужно использовать цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

## Пример верстки

Выведем в рассылке название категории, а также название, цену и картинку рекомендованных из него товаров.

Упрощенная верстка:

```
Подборка новинок из вашей любимой категории ${Recipient.CustomField.MostBoughtCategory.Name} 

@{for item in Recipient.CustomField.MostBoughtCategory.Recommendations.RecoCategory.Take(4)}
    ${item.Name}
    ${item.Price}
    ${item.Url}
    <a href="${item.Url}"><img src="${item.PictureUrl}"></a>
@{end for}
```

При использовании [табличной верстки](how-to-display-data-as-a-table.md) для рекомендаций:

```
Подборка новинок из вашей любимой категории ${Recipient.CustomField.MostBoughtCategory.Name}

<table>
@{for row in tableRows(Recipient.CustomField.MostBoughtCategory.Recommendations.RecoCategory.Take(4), 2)} 
    <tr>
    @{for cell in row.cells} 
        <td>
        @{if cell.value != null} 
            ${cell.Value.Name}
            ${cell.Value.Price}
            ${cell.Value.Url}
            <a href="${cell.Value.Url}"><img src="${cell.Value.PictureUrl}"></a>    
        @{end if} 
        </td>
    @{end for}
    </tr> 
@{end for}
</table>
```

Пользователь получит в письме:

![MostBoughtCategory-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/MostBoughtCategory-example.png)
