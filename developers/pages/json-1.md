---
title: javascript
slug: "json-1"
source_url: "https://developers.mindbox.ru/docs/json-1"
breadcrumb:
  - Рассылки
  - Отправка рассылок по API
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7440663838cbddc41b5e7ebe63584b9455aa1a75ab119c2bc817220b87c87226"
---

# javascript

## Описание метода

Осуществляется в трекере с помощью вызова метода `async` с дополнительными полями. Название операции и набор принимаемых полей настраивается в системе Майндбокс.

```
mindbox('async', {
  operation: '<Название операции>',
  <transactionId>: '',
  data: {
    customer: {
      ids: {
      	<Идентификатор>: '<Значение идентификатора>',
      },
      mobilePhone: '<Мобильный телефон клиента>',
      email: '',
    },
    <emailMailing/smsMailing/viberMailing>: {
      customParameters: {
        <Название параметра>: '<Значение параметра>'
      }
    }
  }
});
```

## Примеры операций

```
mindbox('async', {
  operation: 'sendWelcome',
  transactionId: '123123323',
  data: {
    customer: {
      email: 'pivan@mindbox.ru'
    },
    emailMailing: {
      customParameters: {
        PromoEndDate: '2017-09-25'
      }
    }
  }
});
```
