---
title: Получение источника установки мобильного приложения
slug: "ios-get-app-install-source"
source_url: "https://developers.mindbox.ru/docs/ios-get-app-install-source"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:789832b0bee6a1170366c761c5af7b03eeb0bbbe2838b231fa3cfe19422b5a70"
---

# Получение источника установки мобильного приложения

Для того чтобы отслеживать, из какого источника пользователь установил ваше мобильное приложение, оценивать эффективность рекламных кампаний и выстраивать дальнейшую коммуникацию на основе этих данных, выполните следующие шаги:

1. Установите библиотеку [AppsFlyer](https://dev.appsflyer.com/hc/docs/install-ios-sdk).

```
pod 'AppsFlyerFramework'
```

2. Интегрируйте AppsFlyer в ваш проект [по инструкции](https://dev.appsflyer.com/hc/docs/integrate-ios-sdk).
3. Добавьте субдомен в разделе "Signing & Capabilities" под настройкой "Associated Domains". Субдомен должен быть создан вами на этапе формирования шаблона.
4. Реализуйте метод **onConversionDataSuccess** из протокола **AppsFlyerLibDelegate**. Этот метод вызывается при первой установке приложения по ссылке и предоставляет важные данные о пользователе, включая информацию об установке, источнике и рекламной кампании. Используйте предоставленный ниже код в качестве шаблона для реализации метода.

```
func onConversionDataSuccess(_ data: [AnyHashable: Any]) {
        print("onConversionDataSuccess data:")
        for (key, value) in data {
            print(key, ":", value)
        }

        if let status = data["af_status"] as? String {
            if status == "Non-organic" {
                if let sourceID = data["media_source"],
                   let campaign = data["campaign"] {
                    print("This is a Non-Organic install. Media source: \(sourceID)  Campaign: \(campaign)")
                }
            } else {
                print("This is an organic install.")
            }
            if let is_first_launch = data["is_first_launch"] as? Bool,
               is_first_launch {
                print("First Launch")
            } else {
                print("Not First Launch")
            }
        }
    }
```

5. Создайте [операцию](https://help.mindbox.ru/docs/%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F#sozdanie-operacii-v3) с выдачей действия и/или заполнением дополнительного поля
6. Полученную строку **sourceID** нужно отправить в кастомное поле действия в Mindbox.

```
Mindbox.shared.executeAsyncOperation(operationSystemName:"" json: "{<тело запроса с передачей полученого sourceId>}")
```
