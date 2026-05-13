---
title: javascript
slug: prodactionjson
source_url: "https://developers.mindbox.ru/docs/prodactionjson"
breadcrumb:
  - Номенклатура
  - Действия с продуктами
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:c7a672388f6bba4098c5fc894ced9e640a701cdf7502bd7602d7e3135bbc5f74"
---

# javascript

## Описание метода

Осуществляется в трекере с помощью вызова метода `async` с передачей идентификатора продукта. Название операции и набор принимаемых полей настраиваются в системе Майндбокс.

```
mindbox('async', {
  operation: '<Название операции>',
  data: {
    customer: {
      ids: {
      	<Идентификатор>: '<Значение идентификатора>',
      },
    },
    product: {
      ids: {
        <Идентификатор>: '<Значение идентификатора продукта>'
      }
    },
    productGroup: {
      ids: {
        <Идентификатор>: '<Значение идентификатора продукта>'
      }
    }
  }
});
```

## Примеры операций

#### Просмотр продукта

```
mindbox('async', {
operation: 'ViewProduct',
data: {
  product: {
    ids: {
      bitrixId: '26765438'
    }
  }
}
});
```

#### Просмотр группы продуктов

#### Просмотр продукта авторизованным клиентом
