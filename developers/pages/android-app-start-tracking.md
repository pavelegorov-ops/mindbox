---
title: 5. Получение источника установки мобильного приложения
slug: "android-app-start-tracking"
source_url: "https://developers.mindbox.ru/docs/android-app-start-tracking"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:4dad1d14af3efdd02a44484f4e0de006ecbdaa210bb5f27c3b33953d0d49e616"
---

# 5. Получение источника установки мобильного приложения

Есть два способа получения источника установки: через Google Play и через AppsFlyer.

#### AppsFlyer

1. Добавьте библиотеку [AppsFlyer](https://dev.appsflyer.com/hc/docs/install-android-sdk)

```
dependencies {
    ...
    implementation 'com.appsflyer:af-android-sdk:6.3.2'
    implementation "com.android.installreferrer:installreferrer:2.2"
}
```

2. Интегрируйте AppsFlyer по инструкции [здесь](https://dev.appsflyer.com/hc/docs/integrate-android-sdk)
3. Реализуйте методы протокола **AppsFlyerConversionListener**, а именно **onConversionDataSuccess**. Данный метод вызывается при первичной установке приложения по ссылке, и предоставляет данные по установкам / источнику / кампании и т.д.

```
AppsFlyerConversionListener conversionListener = new AppsFlyerConversionListener() {
    @Override
    public void onConversionDataSuccess(Map<String, Object> conversionDataMap) {
        String status = Objects.requireNonNull(conversionDataMap.get("af_status")).toString();
        
        if (status.equals("Non-organic")) {
            String sourceID = (String) conversionData.get("media_source");
            String campaign = (String) conversionData.get("campaign");
            if (Objects.requireNonNull(conversionDataMap.get("is_first_launch")).toString().equals("true")) {
                Log.d(LOG_TAG, "Conversion: First Launch");
            } else {
                Log.d(LOG_TAG, "Conversion: Not First Launch");
            }
        } else {
            Log.d(LOG_TAG, "Conversion: This is an organic install.");
        }
    }
}
```

4. Создайте [операцию](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F) с выдачей действия и/или заполнением дополнительного поля
5. Полученную строку **sourceID** нужно отправить в кастомное поле к действию в Mindbox.

```
Mindbox.executeAsyncOperation(applicationContext, "", "{<тело запроса с передачей полученого sourceId>}")
```

#### GooglePlay
