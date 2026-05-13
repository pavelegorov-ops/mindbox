---
title: javascript
slug: catactionjson
source_url: "https://developers.mindbox.ru/docs/catactionjson"
breadcrumb:
  - Номенклатура
  - Действия с категориями
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:da435acd58010335a9a96a142fb90512881ef58ed27419db4a5d239ad1f9936b"
---

# javascript

## Описание метода

Осуществляется в трекере с помощью вызова метода `async` с передачей идентификатора категории продукта. Название операции и набор принимаемых полей настраиваются в системе Майндбокс.

```
mindbox('async', {
  operation: '<Название операции>',
  data: {
    productCategory: {
      ids: {
        <Идентификатор>: '<Значение идентификатора категории>'
      }
    }
  }
});
```

## Примеры операций

```
mindbox('async', {
  operation: 'ViewCategory',
  data: {
    productCategory: {
      ids: {
        bitrixId: '364'
      }
    }
  }
});
```
