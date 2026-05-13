---
title: javascript
slug: "javascript-1"
source_url: "https://developers.mindbox.ru/docs/javascript-1"
breadcrumb:
  - Клиент
  - Получение данных клиента
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0fab6d3764ccf82858e32a2ac6a0e4baff7c75577518c40281bc344464fdc62b"
---

# javascript

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется в трекере с помощью вызова метода `sync`. Название операции и набор принимаемых полей настраиваются в системе Майндбокс.

```
mindbox('sync', {
  operation: '<Название операции>',
  data: {
    customer: {
      ids: {
        mindboxId: <Идентификатор в mindbox>,
      	<Идентификатор>: '<Значение идентификатора>',
      },
      mobilePhone: '<Мобильный телефон клиента>',
      email: '<Емэйл клиента>'
    }
  },
  onSuccess: <Функция, вызываемая в случае успеха>,
  onError: <Функция, вызываемая в случае ошибки>
});
```

## Примеры операций

#### Получение данных по сессии

```
mindbox('sync', {
  operation: 'GetCustomerDataBySession',
  onSuccess: function(response) {
    console.log(response.customer.ids.mindboxId);
    console.log(response.customer.ids.webSiteId);
  }
});
```

#### Получение данных по Id сайта
