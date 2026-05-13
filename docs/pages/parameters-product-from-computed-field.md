---
title: Параметры для вывода предпочитаемого продукта
slug: "parameters-product-from-computed-field"
source_url: "https://help.mindbox.ru/docs/parameters-product-from-computed-field"
vcs_path: "parameters-product-from-computed-field.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Параметры для механик. Примеры.
  - Механики и списки продуктов
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:132c51e8616757142ff6becc32258a15c54c36df1eec603901e5092c0a39d921"
---

# Параметры для вывода предпочитаемого продукта

Одно из возможных применений [вычисляемого поля](computed-fields.md) — определение продукта, который пользователь чаще всего просматривает или покупает.

Рассмотрим способ вывода такого продукта с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

## Задача

Отправить клиентам товары, которые они чаще всего смотрят, и подборку похожих продуктов, чтобы помочь определиться с выбором.

![MostViewedProduct-user](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/MostViewedProduct-user.png)  
*Пример клиента с вычисленным продуктом.*

## Как собрать параметр

Чтобы обратиться к карточке клиента, используем базовый параметр `Recipient`→ открываем список дополнительных и вычисляемых полей параметром `CustomField` → выбираем нужное вычисляемое поле → получаем параметр вида `Recipient.CustomField.<Вычисляемое поле>`

Для вывода доступны все поля по товару:

![Recipient.CustomField.MostViewedProduct](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Recipient.CustomField.MostViewedProduct.png)

Чтобы отобрать рекомендации, параметром `Recommendations` переходим в список доступных [алгоритмов](personalisation.md#chto-takoe-rekomendacii) к продукту → выбираем нужный → получаем параметр вида `Recipient.CustomField.<Вычисляемое поле>.Recommendations.<Алгоритм>.Take(<Количество элементов коллекции>)`

Для вывода доступны все поля по рекомендованным товарам:

![Recipient.CustomField.MostViewedProduct.Recommendations](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Recipient.CustomField.MostViewedProduct.Recommendations.png)

Так как собранный параметр является коллекцией, для обращения к продуктам в нем нужно использовать цикл [for...end for](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-for-end-for-%D0%B8-set.md).

## Пример верстки

Выведем в рассылке название, описание, цену и картинку продукта.

Упрощенная верстка:

```
Присматриваетесь к покупке?

${Recipient.CustomField.MostViewedProduct.Name}
${Recipient.CustomField.MostViewedProduct.Description}
${Recipient.CustomField.MostViewedProduct.Price}
${Recipient.CustomField.MostViewedProduct.Url}
<a href="${Recipient.CustomField.MostViewedProduct.Url}"><img src="${Recipient.CustomField.MostViewedProduct.PictureUrl}"></a>

Вам также могут понравиться:

@{for item in Recipient.CustomField.MostViewedProduct.Recommendations.Pohozhie.Take(4)}
    ${item.Name}
    ${item.Price}
    ${item.Url}
    <a href="${item.Url}"><img src="${item.PictureUrl}"></a>
@{end for}
```

При использовании [табличной верстки](how-to-display-data-as-a-table.md) для рекомендаций:

```
Вам также могут понравиться:

<table>
@{for row in tableRows(Recipient.CustomField.MostViewedProduct.Recommendations.Pohozhie.Take(4), 2)} 
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

![MostViewedProduct-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/MostViewedProduct-example.png)

В новом конструкторе можно настроить вывод продукта из вычисляемого поля без использования параметров и кода — [инструкция](email-editor-computed-field.md).
