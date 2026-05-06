---
title: Как работать с массивами пользовательских параметров
slug: "custom-parameters-massive"
source_url: "https://help.mindbox.ru/docs/custom-parameters-massive"
vcs_path: "custom-parameters-massive.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Пользовательские параметры
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:c8fb325ec1a8f33630b70fa918b6ab56d54f73542780cf87351caab6771c063a"
---

# Как работать с массивами пользовательских параметров

Об основах работы с пользовательскими параметрами можно почитать в [статье](custom-parameters-operation.md).  
В данной статье рассмотрим принципы использования массивов.

Например, в вызове мы получаем данные по заказу. Он содержит город и дату доставки, а также вложенный массив с позициями заказа.

#### Как выглядит верстка

```
@{for ord in CustomParameters.Order}
    Город доставки: ${ord.City}
    Дата доставки: ${ord.Date} 
   
   @{for ordItem in ord.Items}
        ${ordItem.Name}
        ${ordItem.Count}шт   
   @{end for}

@{end for}
```

#### Как передаются параметры в операции

Пример в json:

```
{
  "customer": {
    "email": "****"
  },
  "emailMailing": {
    "customParameters": {
      "Order": [
        {
          "City": "Москва",
          "Date": "01.01.2021",
          "Items": [
            {
              "Name": "Пальто",
              "Count": "2"
            },
            {
              "Name": "Брюки",
              "Count": "2"
            }
          ]
        },
        {
          "City": "Псков",
          "Date": "03.03.2021",
          "Items": [
            {
              "Name": "Шарф",
              "Count": "5"
            }           
          ]
        }
      ]
    },
  }
}
```

#### Что получаем в письме

> Город доставки: Москва  
> Дата доставки: 01.01.2021  
> Пальто 2шт  
> Брюки 2шт  
>   
>   
> Город доставки: Псков  
> Дата доставки: 03.03.2021  
> Шарф 5шт

Как [ускорить верстку email-рассылок](https://mindbox.ru/academy/education/kak-uskorit-verstku-email-rassylok-s-pomoshhyu-universalnogo-shablona/) с помощью универсального шаблона
