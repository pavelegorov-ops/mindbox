---
title: Передача событий через iOS SDK
slug: "ios-sdk-events"
source_url: "https://developers.mindbox.ru/docs/ios-sdk-events"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:3cc0bb61fecb0ce1e0af224f60ad1d0c53a18162b0db0944f51d46639ff442f2"
---

# Передача событий через iOS SDK

## Передача данных через асинхронное выполнение операций

Для передачи данных в Mindbox через асинхронные операции, можно использовать метод SDK `Mindbox.shared.executeAsyncOperation`

Этот метод принимает:

- системное имя операции
- тело запроса в Mindbox

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

## Передача и получение данных через синхронное выполнение операций

Для выполнения синхронных операций можно использовать следующие метод `Mindbox.shared.executeSyncOperation`

Этот метод принимает:

- системное имя операции
- тело запроса в Midnbox
- коллбек, который надо вызвать, если операция выполнится успешно
- колбек, который надо вызвать, если операция выполнится с ошибкой

В колбеки передается типизированный объект, в который парсится ответ от Mindbox.

Если по каким-то причинам ответ от Mindbox не может обработаться структурами, которые заложен в SDK, вы можете реализовать собственный класс для обработки ответа.  
Он передается отдельным параметром в вызов функции

## Использование готового класса

### Описание метода

```
public func executeSyncOperation<T>(
  operationSystemName: String,
  operationBody: T,
  completion: @escaping (Result<OperationResponse, MindboxError>) -> Void
) where T: OperationBodyRequestType {}
```

В таком случае, для запроса используется параметры `operationSystemName`  и `operationBody`. Ответом на запрос является сущность `Result`.

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

## Используя собственного класс для ответа

В таком случае, для запроса используется параметры `operationSystemName`  и `operationBody`, а также `customResponseType`, который должен реализовывать протокол `OperationResponseType`. Ответом на запрос является сущность `Result`.

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

`OperationResponse` - модель, которая имеет в себе перечисление всех возможных полей ответа от сервера. Все поля опциональны.

`MindboxError` - модель ошибки, которую возвращает `Mindbox`. Возможные вариации ошибок от сервера:

- `validationError` содержит в себе модель `ValidationError`. Указывает на поля, которые были заполнены неправильно.
- `protocolError` - содержит в себе модель `ProtocolError`. Возвращается в случае ответа от сервера со статусами `4XX` а также некоторые ошибки `5XX`.
- `serverError` - возвращается в случае `5ХХ` статуса без данных от сервера.
- `connectionError` - ошибка запроса по причине соединения.
- `invalidResponse` - возвращается в случае невалидного ответа от сервера.
- `internalError` - указывает на ошибки конфигурации `Mindbox`, ошибки декодирования ответа и прочие.
- `unknown` - возвращается в случае непредвиденного поведения со вложенным типом `Error`.

Для отладки ошибок используйте параметр `errorDescription`.

## Конструктор тела запроса

Для создания тела запроса в Mindbox нужно использовать структуру `OperationBodyRequestType`

Для упрощения интеграции в SDK есть конструктор тела запроса `OperationBodyRequest`, который реализует эту структуру и дает возможность заполнить все стандартные поля запроса

### Пример использования конструктора

```
let body = OperationBodyRequest()

body.viewProduct = .init(
    productGroup: .init(ids: ["website": "test-1"]),
    customerAction: .init(customFields: ["string": "test"])
)
```

### Подробный пример с данными клиента

```
func createCustomer(
  email: String,
  phone: String,
  userId: String
) -> OperationBodyRequest {
  let body = OperationBodyRequest()
  let dateFormatter = DateFormatter()

  dateFormatter.dateFormat = "dd.MM.yyyy"
  let birthDate = dateFormatter.date(from: "12.01.1998")

  body.customer = .init(
    birthDate: birthDate?.asDateOnly,
    sex: .male,
    firstName: "<Имя>",
    email: email,
    mobilePhone: phone,
    ids: ["websiteId": userId],
    customFields: [
      "firstField": "<первое доп поле>", 
      "secondField": "<второе доп поле>"
    ],
    subscriptions: [
      .init(
        brand: "<Бренд>",
        pointOfContact: .email,
        isSubscribed: true
      ),
      .init(
        brand: "<Бренд>",
        pointOfContact: .sms,
        topic: "<Тематика подписки>",
        isSubscribed: true
      ),
    ]
  )

  return body
}

Mindbox.shared.executeAsyncOperation(
  operationSystemName: name.rawValue, 
  operationBody: createCustomer("test@email.com", "79045678901", "Тест")
)
```

## [Подробное описание структуры конструктора запроса](ios-sdk-request-constructor.md)

Если в конструкторе тела запроса нет нужных полей, вы можете объявить свой класс-наследник от `OperationBodyRequest` и сделать override метода encode

```
class CustomOperationBodyRequest: OperationBodyRequest {
  var field: String?

  // override this method when using inheritance
  override func encode(to encoder: Encoder) throws {
    // call super.encode(to:)
    try super.encode(to: encoder)
    var container = encoder.container(keyedBy: Keys.self)

    // encode to container new fields
    try container.encode(field, forKey: .field)
  }

  // provide keys for encoding
  enum Keys: String, CodingKey {
    case field
  }
}
```
