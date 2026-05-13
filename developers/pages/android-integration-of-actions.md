---
title: 6. Интеграция действий в приложении
slug: "android-integration-of-actions"
source_url: "https://developers.mindbox.ru/docs/android-integration-of-actions"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:39d12e3098369dafd3319c6315211aa5c675f97216aa0ebe98feb4a49fac0614"
---

# 6. Интеграция действий в приложении

### Убедитесь, что эти шаги выполнены успешно:

- [Настройка точек интеграции для Android приложения](add-android-integration.md)
- [Добавление SDK в приложение](add-android-sdk.md)
- [Инициализация SDK](android-sdk-initialization.md)

[Пример вызова асинхронного запроса "Просмотр продукта"](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/Operations.kt#L31) и [Пример вызова синхронного запроса "Получение персаональных рекомендаций"](https://github.com/mindbox-cloud/android-sdk/blob/develop/example/app/src/main/java/com/mindbox/example/Operations.kt#L31)

Для передачи данных о действиях клиента нужно завести «операции» Подробно о них [в разделе “Операции и интеграции” на help.mindbox.ru](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F).

Для вызова операций из мобильного приложение Mindbox SDK предлагает 2 метода:

- `executeAsyncOperation` — передача данных в систему;
- `executeSyncOperation` — получение данных из системы.

Для создания тела запроса при вызове операции нужно использовать конструктор `OperationBodyRequest`.

## Техническое задание на интеграцию

Эта страница — пример того, как вызывать API SDK для передачи данных.

Для передачи данных в Mindbox сначала надо настроить нужные методы API. Это делается индивидуально для каждого проекта.

Менеджер проекта со стороны Mindbox настраивает нужные методы и описывает их в специальном документе.

Не приступайте к этому разделу, если у вас нет документа с описанием всех нужных методов.

## Пример реализации вызовов по сценариями

## Авторизация в приложении

```
fun authorizeCustomer() {
    Mindbox.executeAsyncOperation(
        context,
        operationSystemName = "CheckGuide.auth",
        operationBody = OperationBodyRequest(
            customer = CustomerRequest(
                mobilePhone = "79060948798"
            )
        )
    )
}
```

## Передача действий просмотра продуктов и категорий

```
fun viewProduct() {
    Mindbox.executeAsyncOperation(
        context,
        operationSystemName = "CheckGuide.viewProduct",
        operationBody = OperationBodyRequest(
            viewProductRequest = ViewProductRequest(
                product = ProductRequest(
                    ids = Ids(
                        "website" to "123"
                    )
                )
            )
        )
    )
}

fun viewProductCategory() {
    Mindbox.executeAsyncOperation(
        context,
        operationSystemName = "CheckGuide.viewCategory",
        operationBody = OperationBodyRequest(
            viewProductCategory = ViewProductCategoryRequest(
                productCategory = ProductCategoryRequest(
                    Ids(
                        "website" to "123"
                    )
                )
            )
        )
    )
}
```

## Передача действий добавления и установки списка товаров

Для работы со списком товаров Mindbox предлагает 2 варианта подхода:

- добавление/удаление по 1 шт;
- установка списка одним запросом

Популярные списки продуктов: «корзина» и «избранное».

```
fun addProductToCart() {
    Mindbox.executeAsyncOperation(
        context,
        operationSystemName = "CheckGuide.addProductToCart",
        operationBody = OperationBodyRequest(
            addProductToList = ProductListItemRequest(
                product = ProductRequest(
                    Ids(
                        "website" to ""
                    )
                ),
                pricePerItem = 10.0

            )
        )
    )
}

fun setCart() {
    Mindbox.executeAsyncOperation(
        context,
        operationSystemName = "CheckGuide.setUpCart",
        operationBody = OperationBodyRequest(
            productList = arrayListOf(
                ProductListItemRequest(
                    count = 2.0, // <Количество продуктов>
                    product = ProductRequest(
                        Ids(
                            "website" to ""
                        )
                    ),
                    isPricePerItem = false, // если передается цена за единицу товара
                    price = 10.0
                ),
                ProductListItemRequest(
                    count = 2.0, // <Количество продуктов>
                    product = ProductRequest(
                        Ids(
                            "website" to ""
                        )
                    ),
                    isPricePerItem = true, // если передается цена за линию в корзине
                    price = 10.0
                ),
                ProductListItemRequest(
                    count = 2.0, // <Количество продуктов>
                    productGroup = ProductGroupRequest(
                        Ids(
                            "website" to ""
                        )
                    ),
                    isPricePerItem = true, // если передается цена за линию в корзине
                    price = 10.0
                ),
            )
        )
    )
}
```

## Пример проверки клиента в сегменте

Данный запрос проверяет принадлежность клиента к заранее настроенному сегменту в системе.

```
fun checkSegment() {
    Mindbox.executeSyncOperation(
        operationSystemName = "CheckGuide.checkSegment",
        context = context,
        operationBody = OperationBodyRequest(),
        onSuccess = { response -> Log.i("Success ", response.toString())},
        onError = {error -> Log.i("Error", error.toString())}
    )
}
```

## Пример получения персональных рекомендаций

Данный запрос возвращает список товаров, подобранных клиенту на основе одного из настроенных алгоритмов товарных рекомендаций.

```
fun getReco() {
    Mindbox.executeSyncOperation(
        operationSystemName = "CheckGuide.getReco",
        context = context,
        operationBody = OperationBodyRequest(
            recommendation = RecommendationRequest(
                limit = 3
            )
        ),
        onSuccess = { response -> Log.i("getReco Success", response.toString())},
        onError = {error -> Log.i("getReco Error", error.toString())}
    )
}
```

## Подробное описание вызова `executeAsyncOperation`

Для передачи данных в Mindbox через асинхронные операции, можно использовать метод SDK `Mindbox.executeAsyncOperation`.

Этот метод принимает:

- системное имя операции;
- тело запроса в Mindbox.

## Инструкция по вызову Mindbox.executeAsyncOperation

### Описание метода

```
Mindbox.executeAsyncOperation<T>(
  context: Context,
  operationSystemName: String,
  operationBody: T
)
```

### Пример вызова

```
val customerRequestBody = OperationBodyRequest(
  customer = CustomerRequest(
    email = "meAwesome@email.site",
    mobilePhone = "89023234456",
    customFields = CustomFields(
      "myField" to "myString"
    ),
    subscriptions = arrayListOf(
      SubscriptionRequest(
        isSubscribed = true,
        pointOfContact = PointOfContactRequest.EMAIL
      )
    )
  )
)

Mindbox.executeAsyncOperation(
  context = context,
  operationSystemName = "MyOperation",
  operationBody = CustomerRequestBody
)
```

## Проверка выполнения инструкции

1. Создайте операцию в админке;
2. Интегрируйте вызов `Mindbox.executeAsyncOperation` в вашем приложении, например, по нажатию кнопки;
3. Запустите приложение и выполните целевое действие;
4. Найдите своего пользователя в системе и проверьте, что у него в «действиях» появилась ожидаемая запись.

Дебаг стандартных ошибок — [здесь](sdk-integration-checklist.md).

## Подробное описание вызова `executeSyncOperation`

Для выполнения синхронных операций можно использовать метод `Mindbox.executeSyncOperation`.

Этот метод принимает:

- системное имя операции;
- тело запроса в Midnbox;
- коллбек, который надо вызвать, если операция выполнится успешно;
- коллбек, который надо вызвать, если операция выполнится с ошибкой.

В коллбеки передается типизированный объект, в который парсится ответ от Mindbox.

Если по каким-то причинам ответ от Mindbox не может обработаться структурами, которые заложен в SDK, вы можете реализовать собственный класс для обработки ответа.

Он передается отдельным параметром в вызов функции.

## Использование готового класса

### Описание метода

```
Mindbox.executeSyncOperation(
  context: Context,
  operationSystemName: String,
  operationBody: T,
  onSuccess: (OperationResponse) -> Unit,
  onError: (MindboxError) -> Unit
)
```

В таком случае, для запроса используется параметры `operationSystemName` и `operationBody`.

Ответом на запрос является сущность `Result`.

### Пример

```
Mindbox.executeSyncOperation(
      operationSystemName = "CheckGuide.getReco",
      context = context,
      operationBody = OperationBodyRequest(
          recommendation = RecommendationRequest(
              limit = 3
          )
      ),
      onSuccess = { response -> Log.i("getReco Success", response.toString())},
      onError = {error -> Log.i("getReco Error", error.toString())}
  )
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

### Как прошла ваша интеграция SDK Mindbox?

Мы подготовили [короткий опрос](https://forms.gle/HDwuBd8oYVTL2pvY9), чтобы вы могли поделиться своим опытом интеграции SDK Mindbox. Ваши ответы помогут нам сделать продукт и процесс интеграции лучше!
