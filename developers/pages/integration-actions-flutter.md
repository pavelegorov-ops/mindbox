---
title: Интеграция действий в приложении
slug: "integration-actions-flutter"
source_url: "https://developers.mindbox.ru/docs/integration-actions-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:b1b31ed35025d8def1177457e3d58a12285f874c0151737110a36ead607469dc"
---

# Интеграция действий в приложении

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции Android](add-android-integration.md)
- [Настройка точек интеграции iOS](add-ios-integration.md)
- [Добавление SDK в приложение](add-sdk-flutter.md)
- [Инициализация SDK](flutter-sdk-initialization.md)

Для передачи данных о действиях клиента нужно завести «операции». Подробно о них [в разделе «Операции и интеграции» на help.mindbox.ru](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F).

Для вызова операций из мобильного приложение Mindbox SDK предлагает 2 метода:

- `executeAsyncOperation` — передача данных в систему;
- `executeSyncOperation` — получение данных из системы.

Для создания тела запроса при вызове операции нужно использовать конструктор `OperationBodyRequest`.

[Пример вызова операций](https://github.com/mindbox-cloud/flutter-sdk/blob/develop/example/flutter_example/lib/view_model/view_model.dart#L12-L37)

## Техническое задание на интеграцию

Эта страница — пример того, как вызывать API SDK для передачи данных.

Для передачи данных в Mindbox сначала надо настроить нужные методы API. Это делается индивидуально для каждого проекта.

Менеджер проекта со стороны Mindbox настраивает нужные методы и описывает их в специальном документе.

Не приступайте к этому разделу, если у вас нет документа с описанием всех нужных методов.

Ниже приведены примеры того, как некоторые запросы могут быть интегрированы из мобильного приложения. **Если просто скопировать код из этих примеров, то интеграция не заработает.**

## Пример реализации вызовов по сценариями

### Авторизация в приложении (только для тестов)

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: "Mobile.CreateCustomer",
  operationBody: {
    "customer": {
      "mobilePhone": "<Мобильный телефон>",
    },
  },
);
```

### Передача действий просмотра продуктов и категорий

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: "CheckGuide.viewProduct",
  operationBody: {
    "product": {
      "ids": {
        "website": "",
      },
    },
  },
);

Mindbox.instance.executeAsyncOperation(
  operationSystemName: "CheckGuide.viewProduct",
  operationBody: {
    "viewProductCategory": {
      "productCategory": {
        "ids": {
          "website": "",
        },
      },
    },
  },
);
```

### Передача действий добавления и установки списка товаров

Для работы со списком товаров Mindbox предлагает 2 варианта подхода:

- добавление/удаление по 1 шт;
- установка списка одним запросом.

Популярные списки продуктов: «корзина» и «избранное».

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: "CheckGuide.addProductToCart",
  operationBody: {
    "addProductToList": {
      "product": {
        "ids": {
          "website": "",
        },
      },
      "pricePerItem": "",
    },
  },
);

Mindbox.instance.executeAsyncOperation(
  operationSystemName: "CheckGuide.addProductToCart",
  operationBody: {
    "productList": [
      {
        "product": {
          "ids": {
            "website": "",
          },
        },
        "count": "",
        "priceOfLine": "",
      },
    ],
  },
);
```

### Пример проверки клиента в сегменте

Данный запрос проверяет принадлежность клиента к заранее настроенному сегменту в системе.

```
Mindbox.instance.executeSyncOperation(
  operationSystemName: "CheckGuide.checkSegment",
  operationBody: {},
  onSuccess: (success) => print(success),
  onError: (error) => print(error),
);
```

### Пример получения персональных рекомендаций

Данный запрос возвращает список товаров, подобранных клиенту на основе одного из настроенных алгоритмов товарных рекомендаций.

```
Mindbox.instance.executeSyncOperation(
  operationSystemName: "CheckGuide.getReco",
  operationBody: {
    "recommendation": {
      "limit": "3",
    },
  },
  onSuccess: (success) => print(success),
  onError: (error) => print(error),
);
```

### Как прошла ваша интеграция SDK Mindbox?

Мы подготовили [короткий опрос](https://forms.gle/HDwuBd8oYVTL2pvY9), чтобы вы могли поделиться своим опытом интеграции SDK Mindbox. Ваши ответы помогут нам сделать продукт и процесс интеграции лучше!
