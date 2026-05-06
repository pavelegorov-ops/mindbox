---
title: javascript
slug: prodactionjson
source_url: "https://developers.mindbox.ru/docs/prodactionjson"
breadcrumb:
  - Номенклатура
  - Действия с продуктами
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:a8ecf3f526c4fc804a248b0aa0247a6a774d8a3c51bab88b1ace8edc05ab87f5"
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
