---
title: Получение источника установки мобильного приложения
slug: "ios-app-start-tracking-react-native"
source_url: "https://developers.mindbox.ru/docs/ios-app-start-tracking-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:bd6e95162a816fde7da1847266a62099b7cc25eaab580a659c83dd92b98b1d16"
---

# Получение источника установки мобильного приложения

## AppsFlyer

Если вам нужно отслеживать источник установки приложения (например, для оценки эффективности рекламных кампаний), выполните следующие шаги:

### 1. Установите библиотеку AppsFlyer SDK

Следуйте официальной инструкции: [GitHub — AppsFlyer￼](https://github.com/AppsFlyerSDK/appsflyer-react-native-plugin/tree/master?tab=readme-ov-file#-getting-started).

### 2. Инициализируйте AppsFlyer SDK

Создайте экземпляр AppsFlyerSdk и выполните инициализацию в initState() вашего виджета. Это позволит SDK начать обработку атрибуции сразу после запуска приложения.

```
import appsFlyer from 'react-native-appsflyer';

const handleConversionData = (data) => {
  console.log('onInstallConversionData data:');
  for (const key in data) {
    if (data.hasOwnProperty(key)) {
      console.log(`${key} : ${data[key]}`);
    }
  }

  const status = data.af_status;
  if (status) {
    if (status === 'Non-organic') {
      const sourceID = data.media_source;
      const campaign = data.campaign;
      console.log(`Неорганическая установка. Источник: ${sourceID} Кампания: ${campaign}`);
    } else {
      console.log('Органическая установка.');
    }

    const isFirstLaunch = data.is_first_launch === 'true' || data.is_first_launch === true;
    if (isFirstLaunch) {
      console.log('Первый запуск приложения.');
    } else {
      console.log('Повторный запуск приложения.');
    }
  }
};

const initializeAppsFlyer = () => {
  const options = {
    devKey: 'YOUR_AF_DEV_KEY',
    appId: 'YOUR_APP_ID',
    isDebug: true,
    onInstallConversionDataListener: true,
    timeToWaitForATTUserAuthorization: 3,
  };

  appsFlyer.initSdk(
    options,
    (result) => {
      console.log('AppsFlyer SDK инициализирован:', result);
    },
    (error) => {
      console.error('Ошибка инициализации AppsFlyer SDK:', error);
    }
  );

  // Подписка на события конверсии
  const unsubscribe = appsFlyer.onInstallConversionData(handleConversionData);
  return () => unsubscribe();
};

useEffect(() => {
  const cleanup = initializeAppsFlyer();
  return () => cleanup();
}, []);
```

### 3. Передача sourceID в Mindbox

1. Создайте [операцию](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) в Mindbox с действием и/или заполнением дополнительного поля. Инструкция представлена в документации Mindbox.
2. После получения sourceID из AppsFlyer отправьте его в кастомное поле операции:

```
MindboxSdk.executeAsyncOperation({
  operationSystemName: '',
  operationBody: {<тело запроса с передачей полученого sourceId>}
})
```

Более подробную информацию можно найти в [примере AppsFlyer SDK для React Native](https://github.com/AppsFlyerSDK/appsflyer-react-native-plugin/tree/master).

---

## Общая информация

Ошибки:

1. **404** — указан неверный afDevKey или appID.
2. **403** — план AppsFlyer Zero не позволяет просматривать данные об установках.
