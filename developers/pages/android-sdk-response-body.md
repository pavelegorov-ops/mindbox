---
title: Структура конструктора ответа Android SDK
slug: "android-sdk-response-body"
source_url: "https://developers.mindbox.ru/docs/android-sdk-response-body"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:ea11bee6cc1784d1bf36234fa40f3d6bdc81a4f19d8f3a872db2dd296a6b0747"
---

# Структура конструктора ответа Android SDK

Все классы из пакета response имеют переопределенный метод toString() для формирования всех данных класса в виде строки:

1. Класс `OperationResponseBase` - базовый класс для всех ответов, содержит поле `status`
2. Класс `OperationResponse` - содержит в себе стандартные поля-ответы на операции. Метод `catalogProductList()` возвращает `CatalogProductListResponse`, ассоциированный с полем `productList`.  
   Метод `productListItems()` возвращает `List`, ассоциированный с полем `productList`.
3. `Ids` - класс, использующийся для передачи различных идентификатор в виде `Map`.  
   Для передачи MindboxId, необходимо использовать дополнительный конструктор, который на вход принимает Int вместе с `Map` остальных значений.
4. `CustomFields` - класс, использующийся для передачи различных кастомных параметров в виде `Map`. Данный класс имеет метод для преобразования объекта `CustomFields` в любой класс

#### Описание метода

```
/**
  * Convert [CustomFields] value to [T] typed object.
  *
  * @param classOfT Class type for result [CustomFields] object.
  */

fun <T> convertTo(classOfT: Class<T>): T?
```

#### kotlin

#### java

5. `DateOnly` - класс, наследник от Date, используется для передачи на сервер даты в формате "yyyy-mm-dd". При использовании данного класса в качестве типа нового поля при переопределении классов необходимо к полю добавить `@JsonAdapter(DateOnlyAdapter::class)`
6. `DateTime` - класс, наследник от Date, используется для передачи на сервер даты и времени. При использовании данного класса в качестве типа нового поля при переопределении классов необходимо к полю добавить `@JsonAdapter(DateTimeAdapter::class)`

## Классы ошибок

MindboxError - класс, содержащий различные варианты ошибок для ответа:

MindboxError.Validation - ошибка валидации при выполнении операции. Содержит свойство validationMessages, которое хранит информацию об ошибке(ах). Данная ошибка будет возвращена, если поле status от сервера будет содержать ValidationError

MindboxError.Protocol - ошибка протокола, например, может быть возвращена при некорректном названии операции. Данная ошибка будет возвращена, если поле status от сервера будет содержать ProtocolError

MindboxError.InternalServer - внутренняя ошибка сервера. Данная ошибка будет возвращена, если поле status от сервера будет содержать InternalServerError

MindboxError.UnknownServer - остальные ошибки от сервера

MindboxError.Unknown - внутри Mindbox Sdk произошла ошибка. Может содержать в себе Throwable в качестве информации об ошибке.
