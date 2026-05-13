---
title: javascript
slug: "json-1"
source_url: "https://developers.mindbox.ru/docs/json-1"
breadcrumb:
  - Рассылки
  - Отправка рассылок по API
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8873aec7d6820ff85ec866cff3962654d95922c6ced4a18109ae0ab13ece9d29"
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
