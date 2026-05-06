---
title: javascript
slug: catactionjson
source_url: "https://developers.mindbox.ru/docs/catactionjson"
breadcrumb:
  - Номенклатура
  - Действия с категориями
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0f6e30686f5b4ff63137d857ba67ff43b5e2704a55d44eebd9a0c9b05d038d38"
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
