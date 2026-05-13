---
title: Cинхронизация deviceUUID между Flutter mobile SDK и JS SDK в приложении с WebView
slug: "sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-flutter"
source_url: "https://developers.mindbox.ru/docs/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:333c327f07ccfc2961216ad2a28f91adc3e7412d9d653f7a345aed971f1ecc64"
---

# Cинхронизация deviceUUID между Flutter mobile SDK и JS SDK в приложении с WebView

### Результат шага:

- В административной панели Mindbox создается 1 карточка клиента, в которую попадают действия и из мобильного SDK, и с сайта использующего JS SDK.

[Пример реализации](https://github.com/mindbox-cloud/flutter-sdk/blob/webView_integration/example/flutter_example/lib/view/main_page/main_page.dart)

Если ваше приложение использует WebView с сайтом на котором используется [JS трекер](https://developers.mindbox.ru/v3.0_Flutter-SDK/docs/%D1%82%D1%80%D0%B5%D0%BA%D0%B5%D1%80#/), при установке моб. приложения, в mindbox будет создаваться по 2 карточки одного и того же клиента с разными deviceUUID: одна из JS SDK и другая из mobile SDK. Чтобы этого избежать и хранить все данные в одной карточке клиента, нужно выполнить следующие действия:

### Добавьте в приложение метод по получению deviceUUID

```
// Таймаут ожидания для получения deviceUUID.
// Страница не начнет загружаться, пока не истечет этот таймаут.
// Во время первой инициализации получение может занять несколько секунд,
// последующие попытки обычно занимают менее 250 мс.
static const fetchDeviceUuidTimeout = Duration(milliseconds: 4000);

// Получает deviceUUID в пределах указанного таймаута.
// Примечание: fetchDeviceUuidTimeout не должен быть меньше 250 мс,
// иначе deviceUUID может не успеть быть получен.
Future<String> _fetchDeviceUUIDWithTimeout() async {
  final completer = Completer<String>();

  if (fetchDeviceUuidTimeout.inMilliseconds < 250) {
    throw ArgumentError("Timeout must be at least 250 milliseconds.");
  }

  final timer = Timer(fetchDeviceUuidTimeout, () {
    if (!completer.isCompleted) {
      completer.completeError(
        TimeoutException("Timeout while fetching Device UUID."),
      );
    }
  });

  Mindbox.instance.getDeviceUUID((deviceUUID) {
    if (!completer.isCompleted) {
      if (deviceUUID.isNotEmpty) {
        completer.complete(deviceUUID);
      } else {
        completer.completeError(Exception("DeviceUUID is empty"));
      }
    }
  });

  return completer.future.whenComplete(() => timer.cancel());
}
```

### При первой инициализации mindbox SDK deviceUUID может быть получен от провайдера в течение нескольких секунд.

При следующих инициализациях deviceUUID будет получен в течение 100-200 мсек

### Использование third-party cookie

По умолчанию, начиная с Android API 21 и IOS 12, использование third-party cookies отключено.

При использовании third-party cookies, вам обязательно надо дождаться получения deviceUUID при первой инициализации.

---

### Добавьте в`initState` метод ожидания получения deviceUUID и инициализации`WebViewController`

```
@override
void initState() {
  super.initState();

  _initializeDeviceUUIDAndWebView();

  // Этот вызов гарантирует, что даже если получение deviceUUID
  // завершилось по таймауту в момент первоначальной загрузки,
  // синхронизация произойдет при следующих загрузках страницы или запусках приложения.
  Mindbox.instance.getDeviceUUID((uuid) {
    deviceUUID = uuid;
  });

  // ваш остальной код
}

// Пытается получить deviceUUID в пределах указанного таймаута (fetchDeviceUuidTimeout).
// Страница начнёт загружаться либо после получения UUID, либо после истечения таймаута.
// Если UUID не был получен, синхронизация произойдёт при следующем запуске или загрузке страницы.
Future<void> _initializeDeviceUUIDAndWebView() async {
  try {
    final uuid = await _fetchDeviceUUIDWithTimeout();
    deviceUUID = uuid;
    print('DeviceUUID initialized: $deviceUUID');
  } catch (e) {
    print('Failed to initialize DeviceUUID: $e');
  } finally {
    _initializeWebViewController();
    setState(() {
      _isWebViewInitialized = true;
    });
  }
}
```

---

### Продублируйте получение deviceUUID в initState, если не хотите ждать несколько секунд во время первой инициализации. В этом случае синхронизация произойдёт при следующей загрузке страницы.

```
// Добавление этого метода гарантирует, что даже если получение deviceUUID
   // завершится по таймауту во время начальной загрузки страницы,
   // синхронизация произойдет при последующих загрузках страницы или запусках приложения
    Mindbox.instance.getDeviceUUID((uuid) {
      deviceUUID = uuid;
    });
```

---

### Добавьте метод инициализации`WebViewController` и метод синхронизации deviceUUID

```
// Инициализирует WebView. Синхронизация выполняется в колбэке onPageStarted.
Future<void> _initializeWebViewController() async {
  _controller = WebViewController()
    ..setJavaScriptMode(JavaScriptMode.unrestricted)
    ..setNavigationDelegate(
      NavigationDelegate(
        onPageStarted: (String url) async {
          if (deviceUUID != null) {
            await _waitForJavaScriptReady(_controller);
            await _synchronizeDeviceUUID(_controller, deviceUUID!);
          }
        },
      ),
    )
    ..loadRequest(Uri.parse(url));
}

// Синхронизирует deviceUUID с JS SDK.
Future<void> _synchronizeDeviceUUID(
  WebViewController controller,
  String uuid,
) async {
  await controller.runJavaScript('''
    document.cookie = "mindboxDeviceUUID=$uuid";
    window.localStorage.setItem('mindboxDeviceUUID', '$uuid');
  ''');

  Mindbox.instance.writeNativeLog(
    message: "Device UUID synchronized with deviceUUID: $uuid",
    logLevel: LogLevel.info,
  );
}
```

---

### Добавьте метод ожидания доступности контекста JS при старте загрузки страницы

На iOS в callback onPageStarted некоторое время недоступен контекст JS и до появления доступа к контексту JS нельзя выполнять JS скрипты

```
// Метод для ожидания готовности JavaScript-контекста.
Future<void> _waitForJavaScriptReady(WebViewController controller) async {
  const int maxRetries = 10;
  int attempts = 0;
  const Duration retryInterval = Duration(milliseconds: 10);

  while (attempts < maxRetries) {
    // Добавляет небольшую задержку перед первой проверкой, чтобы дать
    // JavaScript-контексту время для инициализации.
    await Future.delayed(retryInterval);

    try {
      final isReady = await controller.runJavaScriptReturningResult('''
        (function() {
          return typeof document.cookie !== "undefined" &&
                 typeof localStorage !== "undefined";
        })();
      ''');

      if (isReady == true) {
        print("JavaScript context is ready.");
        return;
      }

      print("JavaScript context not ready, retrying... [$attempts]");
    } catch (e) {
      print("Error during JavaScript readiness check: $e");
    }

    await Future.delayed(retryInterval);
    attempts++;
  }

  throw TimeoutException(
    "JavaScript context not ready after $maxRetries retries.",
  );
}
```

---

## Пример готового файла

### Пример
