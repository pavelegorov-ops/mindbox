---
title: Интеграция действий в приложении
slug: "ios-integration-actions"
source_url: "https://developers.mindbox.ru/docs/ios-integration-actions"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:98da9941588e9af356d9d98b040d16caec3531a74d4a766ab69ad838c92bf304"
---

# Интеграция действий в приложении

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для iOS приложения](add-ios-integration.md)
- [Добавление SDK в приложение](add-sdk-to-app.md#/)
- [Инициализация SDK](ios-sdk-initialization.md#/)

Для передачи данных о действиях клиента нужно завести «операции». Подробно о них в разделе [«Операции и интеграции»](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) на help.mindbox.ru.

Для вызова операций из мобильного приложение Mindbox SDK предлагает 2 метода:

- `executeAsyncOperation` — передача данных в систему;
- `executeSyncOperation` — получение данных из системы.

Для создания тела запроса при вызове операции нужно использовать конструктор `OperationBodyRequest`.

## Техническое задание на интеграцию

Эта страница — пример того, как вызывать API SDK для передачи данных.

Для передачи данных в Mindbox сначала надо настроить нужные методы API. Это делается индивидуально для каждого проекта.

Менеджер проекта со стороны Mindbox настраивает нужные методы и описывает их в специальном документе.

Не приступайте к этому разделу, если у вас нет документа с описанием всех нужных методов.

Ниже приведены примеры того, как некоторые запросы могут быть интегрированы из мобильного приложения. **Если просто скопировать код из этих примеров, то интеграция не заработает.**

## Пример реализации вызовов по сценариями

### Пример авторизации (только для тестов)

Ожидаемый результат:

- по номеру телефона в Mindbox можно найти клиента;
- у этого клиента есть информация о мобильном приложении.

```
private func auth() {
    let body = OperationBodyRequest();
    
    body.customer = .init(
        mobilePhone: "79060948798"
    )
    
    Mindbox.shared.executeAsyncOperation(
        operationSystemName: "CheckGuide.auth",
        operationBody: body
    )
}
```

### Передача действий просмотра продуктов и категорий

Ожидаемый результат:

- у клиента, который находится по deviceUUID, на вкладке действия появляется новая запись «просмотр продукта» и «просмотр категории».

```
private func viewProduct() {
    let body = OperationBodyRequest();
    
    body.viewProduct = .init(
        product: .init(ids: ["website": "123"])
    )
    
    Mindbox.shared.executeAsyncOperation(
        operationSystemName: "CheckGuide.viewProduct",
        operationBody: body
    )
}

private func viewCategory() {
    let body = OperationBodyRequest();
    
    body.viewProductCategory = .init(
        productCategory: .init(ids: ["website": "123"])
    )
    
    Mindbox.shared.executeAsyncOperation(
        operationSystemName: "CheckGuide.viewCategory",
        operationBody: body
    )
}
```

### Передача действий добавления в корзину/удаления из корзины

Для работы со списком товаров Mindbox предлагает 2 варианта подхода:

- добавление/удаление по 1 шт;
- установка списка одним запросом.

Популярные списки продуктов: «корзина» и «избранное».

Ожидаемый результат:

- у клиента, который находится по deviceUUID, на вкладке действия появляются новые записи про добавление и удаление товаров в корзине.

```
private func addProductToCart() {
    let body = OperationBodyRequest();
    
    body.addProductToList = .init(product: .init(ids: ["website": "123"]), pricePerItem: 100)
    Mindbox.shared.executeAsyncOperation(
        operationSystemName: "CheckGuide.addProductToCart",
        operationBody: body
    )
}

private func setUpCart() {
    let body = OperationBodyRequest();
    
    body.productListItems = [
        .init(
            product: .init(ids: ["website": "123"]),
            count: 1,
            priceOfLine: 100
        ),
        .init(
            product: .init(ids: ["website": "321"]),
            count: 1,
            priceOfLine: 100
        )
    ]
    
    Mindbox.shared.executeAsyncOperation(
        operationSystemName: "CheckGuide.setUpCart",
        operationBody: body
    )
}
```

### Пример проверки клиента в сегменте

Данный запрос проверяет принадлежность клиента к заранее настроенному сегменту в системе

Ожидаемый результат:

- в консоли разработчика в Xcode отображается ответ от Mindbox.

```
private func checkSegment() {
    let body = OperationBodyRequest()
    
    Mindbox.shared.executeSyncOperation(
        operationSystemName: "CheckGuide.checkSegment",
        operationBody: body) {
            result in
            switch result {
            case let .success(response):
                print(response.createJSON())
            case let .failure(error):
                print(error.errorDescription)
            }
        }
}
```

### Пример получения персональных рекомендаций

Данный запрос возвращает список товаров, подобранных клиенту на основе одного из настроенных алгоритмов товарных рекомендаций

Ожидаемый результат:

- в консоли разработчика в Xcode отображается ответ от Mindbox.

```
private func getReco() {
    let body = OperationBodyRequest()
    
    body.recommendation = .init(limit: 3)
    
    Mindbox.shared.executeSyncOperation(
        operationSystemName: "CheckGuide.getReco",
        operationBody: body) {
            result in
            switch result {
            case let .success(response):
                print(response.createJSON())
            case let .failure(error):
                print(error.errorDescription)
            }
        }
}
```

## Передача данных в Mindbox — асинхронное выполнение

Для передачи данных в Mindbox через асинхронные операции, можно использовать метод SDK `Mindbox.shared.executeAsyncOperation`

Этот метод принимает:

- системное имя операции;
- тело запроса в Mindbox.

## Описание метода

```
executeAsyncOperation<T: OperationBodyRequestType>(
  operationSystemName: String, 
  operationBody: T
)
```

## Пример вызова

```
let body = OperationBodyRequest()

body.customer =  .init(
  email: "",
  mobilePhone: "<Мобильный телефон>",
  ids:  ["websiteid": "<Идентификатор на сайте>"],
  subscriptions: [
    .init(
      brand: "<Системное имя бренда подписки клиента>",
      pointOfContact: .sms,
      topic: "<Внешний идентификатор тематики подписки>",
      isSubscribed: true
    )
  ]

)

Mindbox.shared.executeAsyncOperation(
  operationSystemName: "Mobile.AuthorizeCustomer",
  operationBody:body
)
```

### Проверка выполнения инструкции

1. Создайте операцию в админке;
2. Интегрируйте вызов `Mindbox.shared.executeAsyncOperation` в вашем приложении, апример, по нажатию кнопки;
3. Запустите приложение и выполните целевое действие;
4. Найдите своего пользователя в системе и проверьте, что у него в «действиях» появилась ожидаемая запись.

Дебаг стандартных ошибок — [здесь](sdk-integration-checklist.md).

## Передача и получение данных от Mindbox — синхронное выполнение

Для выполнения синхронных операций можно использовать метод `Mindbox.shared.executeSyncOperation`.

Этот метод принимает:

- системное имя операции;
- тело запроса в Mindbox;
- коллбэк, который надо вызвать, если операция выполнится успешно;
- коллбэк, который надо вызвать, если операция выполнится с ошибкой.

В коллбэки передается типизированный объект, в который парсится ответ от Mindbox.

Если по каким-то причинам ответ от Mindbox не может обработаться структурами, которые заложен в SDK, вы можете реализовать собственный класс для обработки ответа.

Он передается отдельным параметром в вызов функции.

## Использование готового класса

### Описание метода

```
public func executeSyncOperation<T>(
  operationSystemName: String,
  operationBody: T,
  completion: @escaping (Result<OperationResponse, MindboxError>) -> Void
) where T: OperationBodyRequestType {}
```

В таком случае, для запроса используется параметры `operationSystemName`  и `operationBody`.

Ответом на запрос является сущность `Result`.

### Пример

```
// Create body
let body = OperationBodyRequest()
body.productListItems = ... // fill with data

// Call method
Mindbox.shared.executeSyncOperation(
 operationSystemName: "OperationName",
 operationBody: body
) { result in
  switch result {
    case let .success(response):
      // Handle response here
    case let .failure(error):
      print(error.errorDescription)
  }
}
```

## Используя собственный класс для ответа

В таком случае, для запроса используется параметры operationSystemName и operationBody, а также customResponseType, который должен реализовывать протокол OperationResponseType. Ответом на запрос является сущность Result.

### Описание метода

```
public func executeSyncOperation<T, P>(
  operationSystemName: String,
  operationBody: T,
  customResponseType: P.Type,
  completion: @escaping (Result<P, MindboxError>) -> Void
) where T: OperationBodyRequestType, P: OperationResponseType {}
```

### Пример

```
// Create a new struct/class wich implements OperationResponseType 
struct MyResponse: OperationResponseType {
  var status: Status

  // provide custom fields here
}

...

// Create body
let body = OperationBodyRequest()
body.productListItems = ... // fill with data

// Call method
Mindbox.shared.executeSyncOperation(
  operationSystemName: "OperationName",
  operationBody: body,
  customResponseType: MyResponse.self // type of your custom response model
) { result in
   switch result {
     case let .success(response):
     // handle response here
     // response is type of MyResponse
     case let .failure(error):
     print(error.errorDescription)
   }
  }
```

## Расшифровка ответа

`OperationResponse` — модель, которая имеет в себе перечисление всех возможных полей ответа от сервера. Все поля опциональны.

`MindboxError` — модель ошибки, которую возвращает `Mindbox`. Возможные вариации ошибок от сервера:

- `validationError` содержит в себе модель `ValidationError`. Указывает на поля, которые были заполнены неправильно.
- `protocolError` содержит в себе модель `ProtocolError`. Возвращается в случае ответа от сервера со статусами `4XX` а также некоторые ошибки `5XX`.
- `serverError`  возвращается в случае `5ХХ` статуса без данных от сервера.
- `connectionError` — ошибка запроса по причине соединения.
- `invalidResponse` возвращается в случае невалидного ответа от сервера.
- `internalError` указывает на ошибки конфигурации `Mindbox`, ошибки декодирования ответа и прочие.
- `unknown` возвращается в случае непредвиденного поведения со вложенным типом `Error`.

Для отладки ошибок используйте параметр `errorDescription`.

---

### Как прошла ваша интеграция SDK Mindbox?

Мы подготовили [короткий опрос](https://forms.gle/HDwuBd8oYVTL2pvY9), чтобы вы могли поделиться своим опытом интеграции SDK Mindbox. Ваши ответы помогут нам сделать продукт и процесс интеграции лучше!
