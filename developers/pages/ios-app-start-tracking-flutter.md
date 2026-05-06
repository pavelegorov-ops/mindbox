---
title: Получение источника установки мобильного приложения
slug: "ios-app-start-tracking-flutter"
source_url: "https://developers.mindbox.ru/docs/ios-app-start-tracking-flutter"
breadcrumb:
  - Мобильные приложения
  - Flutter SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:5da60ce96c8865c8797d501045cc8d73c02917ac32a21bf3ddd399c826eb7714"
---

# Получение источника установки мобильного приложения

## AppsFlyer

Если вам нужно отслеживать источник установки приложения (например, для оценки эффективности рекламных кампаний), выполните следующие шаги:

### 1. Установите библиотеку AppsFlyer SDK

Следуйте официальной инструкции: [GitHub — AppsFlyer Flutter Plugin￼](https://github.com/AppsFlyerSDK/appsflyer-flutter-plugin?tab=readme-ov-file#-guides).

### 2. Инициализируйте AppsFlyer SDK

Создайте экземпляр AppsFlyerSdk и выполните инициализацию в initState() вашего виджета. Это позволит SDK начать обработку атрибуции сразу после запуска приложения.

```
import 'package:appsflyer_sdk/appsflyer_sdk.dart';

late AppsflyerSdk _appsflyerSdk;

@override
void initState() {
  super.initState();
  _initAppsFlyerSdk();
}

void _initAppsFlyerSdk() async {
  // Настройки SDK
  final AppsFlyerOptions options = AppsFlyerOptions(
    afDevKey: 'YOUR_AF_DEV_KEY',           // Ваш AppsFlyer Dev Key
    appId: 'YOUR_IOS_APP_ID',              // ID приложения (только iOS)
    showDebug: true,
  );

  _appsflyerSdk = AppsflyerSdk(options);

  // Инициализация SDK
  await _appsflyerSdk.initSdk(
    registerConversionDataCallback: true,
    registerOnAppOpenAttributionCallback: true,
    registerOnDeepLinkingCallback: true,
  );

  // Обработка данных о конверсии
  _appsflyerSdk.onInstallConversionData((data) {
    print("onInstallConversionData data:");
    data.forEach((key, value) {
      print('$key : $value');
    });

    final status = data['af_status'];

    if (status == 'Non-organic') {
      final sourceID = data['media_source'];
      final campaign = data['campaign'];
      print('Неорганическая установка. Источник: $sourceID Кампания: $campaign');
    } else if (status == 'Organic') {
      print('Органическая установка.');
    }

    final isFirstLaunch =
        data['is_first_launch'] == 'true' || data['is_first_launch'] == true;

    if (isFirstLaunch) {
      print('Первый запуск приложения.');
    } else {
      print('Не первый запуск приложения.');
    }
  });
}
```

### 3. Передача sourceID в Mindbox

1. Создайте [операцию](ios-get-app-install-source.md) в Mindbox с действием и/или заполнением дополнительного поля. Инструкция представлена в документации Mindbox.
2. После получения sourceID из AppsFlyer отправьте его в кастомное поле операции:

```
Mindbox.instance.executeAsyncOperation(
  operationSystemName: "",
  operationBody: {
    // передайте полученный sourceID
  },
);
```

Более подробную информацию можно найти в [примере AppsFlyer SDK для Flutter.](https://github.com/AppsFlyerSDK/appsflyer-flutter-plugin)

---

## Общая информация

Ошибки:

1. **404** — указан неверный afDevKey или appID.
2. **403** — план AppsFlyer Zero не позволяет просматривать данные об установках.
