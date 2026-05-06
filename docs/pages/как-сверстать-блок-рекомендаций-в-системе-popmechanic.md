---
title: Как сверстать внешний вид виджета
slug: "как-сверстать-блок-рекомендаций-в-системе-popmechanic"
source_url: "https://help.mindbox.ru/docs/как-сверстать-блок-рекомендаций-в-системе-popmechanic"
vcs_path: "как-сверстать-блок-рекомендаций-в-системе-popmechanic.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Виджеты рекомендаций
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:21ac9773ec73756b3ed20ac070d7152152fa32b118ca3558bf819340a7d39ada"
---

# Как сверстать внешний вид виджета

**Переходим в редактирование виджета**

В разделе «Виджет рекомендаций» нажмите «Изменить», затем — «Редактировать»:

![Снимок экрана 2023-01-23 в 03.25.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-01-23%20%D0%B2%2003.25.48.png)

Верстка виджета формируется из двух шаблонов: карточки продукта и непосредственно шаблона самого виджета

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28237%29.png)

**Шаблон карточки продукта**

Шаблон карточки задает верстку карточки одного продукта. При отображении на сайте будет выведено столько карточек, сколько вернул алгоритм рекомендаций, привязанный к виджету.

**Шаблон виджета**

Задает верстку контейнера, в котором будут отображены карточки продуктов. В шаблоне задаются параметры виджета, не относящиеся к карточке: заголовок, кнопки перелистывания, буллиты (кружочки внизу виджета, отображающие номер страницы) и т.п

#### **HTML**

**Использование атрибутов продукта**  
В шаблоне карточки продукта можно использовать атрибуты этого продукта: системные или дополнительные поля. Список системных полей, к которым можно обращаться в шаблоне виджета:

- ***{{ product.url }}***— ссылка на продукт
- ***{{ product.discount }}*** — скидка в %
- ***{{ product.pictureUrl }}*** — ссылка на изображение продукта
- ***{{ product.displayName }}*** — название продукта
- ***{{ product.description }}*** — описание продукта
- ***{{ product.price }}*** — цена
- ***{{ product.formattedPrice }}*** — отформатированная цена с разделителями разрядов
- ***{{ product.oldPrice }}*** — старая цена
- ***{{ product.formattedOldPrice }}*** — отформатированная старая цена с разделителями разрядов
- ***{{ product.manufacturer.name }}*** — название производителя
- ***{{ product.vendorCode }}*** — артикул
- ***{{ product.category }}*** — категория продукта (при нескольких берется первая попавшаяся)
- ***{{ product.productGroup.ids.[externalSystemIdName] }}*** — идентификатор группы продуктов во внешней системе (*[externalSystemIdName]* — системное имя внешней системы. Например: *{{ product.productGroup.ids.website }}*)
- ***{{ product.customFields.[name] }}*** — дополнительное поле продукта (*[name]* — системное имя дополнительного поля. Например: *{{ product.customFields.size }}*)
- ***{{ product.ids.mindboxId }}*** — Id продукта в Mindbox
- ***{{ product.ids.[externalSystemIdName] }}*** — идентификатор продукта во внешней системе (*[externalSystemIdName]* — системное имя внешней системы. Например: *{{ product.ids.website}}*)

Системные имена внешних систем и дополнительных полей нужно всегда передавать со строчной буквы, даже если на платформе они пишутся с заглавной. Например:

- WebOurDomain → *{{ product.ids.webOurDomain }}*
- Site → *{{ product.ids.site }}*
- site → *{{ product.ids.site }}*

**Использование условного оператора**

- если нет скидки, то добавляем класс "popmechanic-hidden":

```
<div class="popmechanic-item-discount 
{{ product.discount ? '' : 'popmechanic-hidden' }}">
{{ product.discount }}
</div>
```

  

- примерная структура html слайда выглядит так:

```
<div class="popmechanic-item-card">
    <a href="{{ product.url }}" class="popmechanic-item-wrapper">
    <div class="popmechanic-item-discount {{       product.discount ? '' : 'popmechanic-hidden' }}">-{{ product.discount }}
    </div>
    <div class="popmechanic-item-picture">
<img src="{{ product.pictureUrl }}" alt="{{ product.displayName }}" />
    </div>
    <div class="popmechanic-item-name">{{ product.displayName }}
    </div>
    <div class="popmechanic-item-price {{ product.discount ? 'popmechanic-item-price--highlight' : '' }} ">
{{ product.price }}
<span class="popmechanic-currency">руб.</span>
    </div></a>
</div>
```

[Функции для обработки и форматирования данных](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.md) не доступны в виджетах.

#### **CSS**

Обращения ко всем элементам желательно делать через **#popmechanic-form:#popmechanic-form.popmechanic-item-card** и т.д.

- **основные** :

*-задаем контейнеру слайдов display:flex, чтобы элементы выстроились в линию:*

```
#popmechanic-form .popmechanic-main .popmechanic-items {
    display: flex;
}
```

-*можно задать, карточке display: inline-block, результат будет такой же:*

```
#popmechanic-form .popmechanic-main .popmechanic-item-card {
    display: inline-block;
}
```

-*также задаем transition, для плавности перелистывания слайдера:*

```
#popmechanic-form .popmechanic-main .popmechanic-items {
    transition: 0.3s;
}
```

- **отступы между слайдами:**

-о*тступы между слайдами обязательно нужно задавать в padding:*

```
#popmechanic-form .popmechanic-main .popmechanic-item-card{
    padding: 0 8px;
}
```

Задаст padding между слайдами в 16px (слева 8px и справа 8px).

Отступы также можно задавать в параметрах адаптивности (читать ниже)

- **стрелки**

- *стрелки создаются автоматически, их можно найти в коде шаблона в*

```
<div class="tns-controls">
```

- *включить их можно в правом меню настроек:*

![image.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image%28218%29.png)

- *чтобы убрать слова "prev" и "next" пишем:*

```
#popmechanic-form .popmechanic-main .tns-controls button {
    font-size: 0; 
    color: transparent; 
    background-color: transparent;
}
```

**Картинку в стрелку можно положить только в base64, в виде фонового изображения.**

-*например, это треугольник влево:*

```
background-image: urlurl("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 752 752'%3E%3Cpath fill='%23000' d='m279.23 368.11 177.75-177.75a11.18 11.18 0 0 1 15.8 15.8L302.94 376.01 472.8 545.87a11.18 11.18 0 0 1-7.9 19.08 11.1 11.1 0 0 1-7.9-3.28L279.24 383.9a11.12 11.12 0 0 1 0-15.79z'/%3E%3C/svg%3E");
```

-*это треугольник вправо:*

```
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 752 752'%3E%3Cpath fill='%23000' d='M472.76 368.11 295.01 190.36a11.18 11.18 0 0 0-15.8 15.8l169.86 169.85L279.2 545.87a11.18 11.18 0 0 0 7.9 19.08c2.85 0 5.72-1.09 7.89-3.28L472.77 383.9a11.12 11.12 0 0 0 0-15.79z'/%3E%3C/svg%3E");
```

  

**Параметры адаптивности**

- Можно настроить количество слайдов, которые показываются на разных разрешениях, и отступ между слайдами.

Например:

![Снимок экрана 2021-02-20 в 14.35.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-02-20%20%D0%B2%2014.35.33.png)

Начиная с разрешения 1500px+ показывается 5 слайдов,  
начиная с разрешения 760px+ показывается 4 слайда,  
начиная с разрешения 428px+ показывается 2 слайда.

- Минимальное количество слайдов для показа. Настраиваем в **"Выключить если рекомендаций меньше (0 — показывать всегда)"**

Например,

![Снимок экрана 2021-02-20 в 14.38.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-02-20%20%D0%B2%2014.38.22.png)

Виджет не будет отображаться, если для показа доступно меньше двух продуктов.

- Настроить скрытие или показ кнопок слайдера в зависимости от разрешения экрана можно с помощью параметра **"Пользовательские параметры TNS"**

На примере ниже приведена конфигурация слайдера, когда при ширине экрана менее 768px кнопки слайдера будут скрыты, а при ширине начиная с 768px+ - кнопки слайдера будут отображены.

Когда кнопки слайдера скрыты, карусель можно перематывать с помощью мышки или свайпа влево-вправо на мобильных устройствах

```
{
	preventScrollOnTouch: "auto",
	responsive: {
		0: {
			controls: false,
		},
		768: {
			controls: true,
		},
	}
}
```

- preventScrollOnTouch - для для мобильных устройст предотвращает скролл виджета по тапу - скролл только по свайпу

  

**Настройка автоскрола**

Чтобы продукты перелистывались в виджете автоматически, в блок **"Пользовательские параметры TNS/слайдера"** нужно добавить

```
{
	autoplay: true,
	autoplayTimeout: 3000,
}
```

Чтобы убрать кнопку stop в интерфейсе, добавьте в CSS виджета следующий блок

```
#popmechanic-form [data-action="stop"] {
	display: none;
}
```

[Блок «Похожие товары» в интернет-магазинах](https://mindbox.ru/academy/education/pohozhie-tovary/): как работает алгоритм автоматического подбора
