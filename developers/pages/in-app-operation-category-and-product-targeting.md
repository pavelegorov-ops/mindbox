---
title: Настройка операций в приложении для таргетинга на экран категории и экран продукта
slug: "in-app-operation-category-and-product-targeting"
source_url: "https://developers.mindbox.ru/docs/in-app-operation-category-and-product-targeting"
breadcrumb:
  - Мобильные приложения
  - "In-App"
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:be6026b8e89325f2738a78e01e4855433ff48d60f0735a53cf0ce31d53b23044"
---

# Настройка операций в приложении для таргетинга на экран категории и экран продукта

Данный тип таргетинга доступен в версиях SDK 2.6.0 и выше для нативных приложений на [iOS](https://github.com/mindbox-cloud/ios-sdk/releases/tag/2.6.1) и [Android](https://github.com/mindbox-cloud/android-sdk/releases/tag/2.6.1); в версии 2.6.0 и выше для приложений на [Flutter](https://github.com/mindbox-cloud/flutter-sdk/releases)

Таргетинг на экраны категории и продукта позволяет настроить отображение in-app’а при переходе пользователя в определенную категорию или продукт. При этом, настраивается по одной операции на категорию и на продукт, в них передается только id.

Если в приложении уже вызываются нужные операции, то настраивать дополнительно в приложении ничего не нужно. Вы можете использовать их в таргетинге in-app'ов.

### Android

1. Настройте [передачу действия](android-integration-of-actions.md) просмотра продукта/категории в админке.
2. В момент, когда нужно показать инапп, вызвать метод executeSyncOperation или executeAsyncOperation с параметром operationName, соответствующим названию операции, которая в админке выбрана как просмотр продукта/категории и телом операции, соответствующим просмотру продукта/категории (ViewProductRequest/ViewProductCategoryRequest)

Пример вызова 1:

```
val bodyRequest = OperationBodyRequest(
                viewProductCategory = ViewProductCategoryRequest(
                    productCategory = ProductCategoryRequest(Ids("website" to "12345f")),
                    customerAction = CustomerActionRequest(CustomFields("string" to "test"))
                )
            )
                )
            )
Mindbox.executeAsyncOperation(applicationContext, "ProsmotrKategorii", bodyRequest)
```

Пример вызова 2:

```
val bodyRequest = OperationBodyRequest(
                viewProductRequest = ViewProductRequest(
                    product = ProductRequest(Ids("website" to "test-1")),
                    customerAction = CustomerActionRequest(CustomFields("string" to "test"))
                )
            )
Mindbox.executeSyncOperation(applicationContext, "ProsmotrProdukta, bodyRequest, {}, {})
```

### iOS

1. Настройте [передачу действия](ios-integration-actions.md) просмотра продукта/категории в админке.
2. В момент, когда нужно показать инапп, вызвать метод executeSyncOperation или executeAsyncOperation с параметром operationName, соответствующим названию операции, которая в админке выбрана как просмотр продукта/категории и телом операции, соответствующим просмотру продукта/категории(ViewProductRequest/ViewProductCategoryRequest)

Пример вызова 1:

```
let json = """
{ "viewProduct": { "product": { "ids": { "website": "49" } } } }
"""

Mindbox.shared.executeSyncOperation(operationSystemName: "some operation name",
                           json: json) { result in

}
```

Пример вызова 2:

```
let json = """
{ "viewCategory": { "productCategory": { "ids": { "test-site": "100" } } } }
"""

Mindbox.shared.executeAsyncOperation(operationSystemName: "some operation name",
                                     json: json)
```

### Flutter

1. Настройте [передачу действия](integration-actions-flutter.md) просмотра продукта/категории в админке.
2. В момент, когда нужно показать инапп, вызвать метод executeSyncOperation или executeAsyncOperation с параметром operationName, соответствующим названию операции, которая в админке выбрана как просмотр продукта/категории и телом операции, соответствующим просмотру продукта/категории(ViewProductRequest/ViewProductCategoryRequest)

Пример вызова 1:

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: '<системное имя операции>',
  operationBody: { < объект с данными в формате  Map<String, dynamic>> },
);
```

Пример вызова 2:

```
Mindbox.instance.executeSyncOperation(
  operationSystemName: '<системное имя операции>',
  operationBody: { < объект с данными в формате  Map<String, dynamic>> },
  onSuccess: (data)  { <метод обработки успешного ответа> },
  onError: (error) { <метод обработки ответа с ошибкой> },
);
```

### React Native

1. Настройте [передачу действия](integration-actions-flutter.md) просмотра продукта/категории в админке.
2. В момент, когда нужно показать инапп, вызвать метод executeSyncOperation или executeAsyncOperation с параметром operationName, соответствующим названию операции, которая в админке выбрана как просмотр продукта/категории и телом операции, соответствующим просмотру продукта/категории(ViewProductRequest/ViewProductCategoryRequest)

```
MindboxSdk.executeAsyncOperation({
  operationSystemName: '<системное имя операции>',
  operationBody: {  },
});
```

```
MindboxSdk.executeSyncOperation({
  operationSystemName: '<системное имя операции>',
  operationBody: {  },
  onSuccess: (data) => { ... },
  onError: (error) => { ... },
});
```
