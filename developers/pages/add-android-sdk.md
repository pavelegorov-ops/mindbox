---
title: 1. Добавление SDK в приложение
slug: "add-android-sdk"
source_url: "https://developers.mindbox.ru/docs/add-android-sdk"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:96d0c3031a71c488a4373ab876087f98818a24ece3bad865e4a1b3402deacb80"
---

# 1. Добавление SDK в приложение

### Результат шага «Добавление SDK в приложение»:

В навигаторе по проекту, в разделе External Libraries можно найти строчку `Gradle: cloud.mindbox.mobile-sdk:{версия}@arr`.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/5dbc923-1.png)

Для работы Mindbox SDK нужно добавить зависимость в файл app/build.gradle в блок dependencies (Module: app). Лучше указать фиксированную версию, чтобы контролировать обновление. Актуальную версию вы можете посмотреть [на странице библиотеки в Maven Central](https://central.sonatype.com/namespace/cloud.mindbox).

```
dependencies {
    ...
    implementation 'cloud.mindbox:mobile-sdk:{версия}'  
    //если вы планируете интегрировать мобильные пуши Firebase, Huawei, RuStore
	  //то можете сразу добавить зависимости ниже
    implementation 'cloud.mindbox:mindbox-firebase'  # since 2.10.0
    implementation 'cloud.mindbox:mindbox-huawei'  # since 2.10.0
    implementation 'cloud.mindbox:mindbox-rustore'  # since 2.12.0
   ...
}
```

Нажмите «Sync Now» после изменения файла.

### Implementation @aar

Не используйте implementation `'cloud.mindbox:mobile-sdk:{версия}@aar'`. Это приведет к ошибкам `NoClassDefFoundError` в Runtime
