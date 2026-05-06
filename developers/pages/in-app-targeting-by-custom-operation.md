---
title: "Настройка операций в приложении для таргетинга in-app на операцию"
slug: "in-app-targeting-by-custom-operation"
source_url: "https://developers.mindbox.ru/docs/in-app-targeting-by-custom-operation"
breadcrumb:
  - Мобильные приложения
  - "In-App"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:d26613554802dd562716bc2368a872622df68c6d7aff9ef255bc17b2192b9425"
---

# Настройка операций в приложении для таргетинга in-app на операцию

Данный тип таргетинга доступен в версиях SDK 2.5.0 и выше для нативных приложений [iOS](https://github.com/mindbox-cloud/ios-sdk/releases/tag/2.5.0) и [Android](https://github.com/mindbox-cloud/android-sdk/releases/tag/2.5.0); в версии 2.6.0 и выше для приложений на [Flutter](https://github.com/mindbox-cloud/flutter-sdk/releases) и [React Native](https://github.com/mindbox-cloud/react-native-sdk/releases).

Таргетинг по операции позволяет настроить in-app таким образом, что он будет показан в определенном месте приложения или при совершении пользователем действия. Для этого в приложении необходимо настроить операции, при вызове которых будет показываться in-app.

Если в приложении уже вызываются нужные операции, то настраивать дополнительно в приложении ничего не нужно. Вы можете использовать их в таргетинге in-app'ов.

1. Выберите в приложении активности (например, клик по кнопке, переход на экран), в момент которых вы хотите показать пользователю in-app. Составьте список этих активностей. Желательно, чтобы активности в приложении iOS и Android совпадали. Иначе нужно будет создавать разные in-app'ы для разных приложений.
2. Создайте операции по [инструкции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-in-app%D0%B0-%D0%B2-%D0%BB%D1%8E%D0%B1%D0%BE%D0%BC-%D0%BC%D0%B5%D1%81%D1%82%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F) или обратитесь со списком активностей к менеджеру Mindbox.
3. Настройте операции в приложении, используя системные имена операций в Mindbox.

### Android

В приложении в момент, когда хотите показать in-app вызовите метод Mindbox.executeSyncOperation (исполнит синхронную операцию) или метод Mindbox.executeAsyncOperation (исполнит асинхронную операцию). В обоих методах в параметре operationName должна быть строка, соответствующая названию системной операции на которую таргетится in-app. Пример вызова:

```
Mindbox.executeSyncOperation(
	context = applicationContext,
	operationSystemName = "some operation name",
	operationBodyJson = "some operation body in json format", 
	onSuccess = { 
		// Success Callback 
	},
	onError = {
		// Error callback
	}
)
```

```
Mindbox.executeAsyncOperation(         
	context = applicationContext,
	operationSystemName = "some operation name",
	operationBodyJson = "some operation body in json format"
)
```

После того, как внутри приложении произошел переход на экран, на котором вы хотите показать in-app, можно вызвать любую из операций с соответствующим именем в методах жизненного цикла activity onCreate, onStart или onResume. Если навигация работает на фрагментах, то операцию можно вызывать в методе жизненного цикла onViewCreated. Если для навигации используется jetpack compose, то операцию можно вызвать из любой composable функции.

Если вызывать операцию в методах жизненного цикла, отвечающих за уход с экрана, то in-app может либо успеть показаться на мгновение перед уходом, либо будет показан уже на след экране, в этом случае все решит гонка, делать так опасно.

Сейчас in-app по умолчанию покажется на старте приложения. Создавать отдельную операцию активности “старт приложения” не нужно.

### iOS

В приложении в момент, когда хотите показать in-app вызовите метод Mindbox.shared.executeSyncOperation (исполнит синхронную операцию) или метод Mindbox.shared.executeAsyncOperation (исполнит асинхронную операцию). В обоих методах в параметре operationName должна быть строка, соответствующая названию системной операции на которую таргетится in-app. Пример вызова:

```
Mindbox.shared.executeSyncOperation(operationSystemName: "some operation name",
                           json: "some operation body in json format") { result in
            
}
```

```
Mindbox.shared.executeAsyncOperation(operationSystemName: "some operation name",
                                     json: "some operation body in json format")
```

### Flutter

В приложении в момент, когда хотите показать in-app вызовите метод Mindbox.executeSyncOperation (исполнит синхронную операцию) или метод Mindbox.executeAsyncOperation (исполнит асинхронную операцию). В обоих методах в параметре operationName должна быть строка, соответствующая названию системной операции на которую таргетится in-app. Пример вызова:

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: '',
  operationBody: { < объект с данными в формате  Map <String, dynamic>  > },
);
```

```
Mindbox.instance.executeSyncOperation(
  operationSystemName: '',
  operationBody: { < объект с данными в формате  Map <String, dynamic>  > },
  onSuccess: (data)  { <метод обработки успешного ответа> },
  onError: (error) { <метод обработки ответа с ошибкой> },
);
```

Сейчас in-app по умолчанию покажется на старте приложения. Создавать отдельную операцию активности “старт приложения” не нужно.

Можно вызывать в любой из этапов жизненного цикла ViewController, так как создается отдельное окно.

### React Native

В приложении в момент, когда хотите показать in-app вызовите метод Mindbox.executeSyncOperation (исполнит синхронную операцию) или метод Mindbox.executeAsyncOperation (исполнит асинхронную операцию). В обоих методах в параметре operationName должна быть строка, соответствующая названию системной операции на которую таргетится in-app. Пример вызова:

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

Сейчас in-app по умолчанию покажется на старте приложения. Создавать отдельную операцию активности “старт приложения” не нужно.

Можно вызывать в любой из этапов жизненного цикла ViewController, так как создается отдельное окно.
