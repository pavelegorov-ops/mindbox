---
title: Механики для интеграции приложения «Кошелёк» для отправки пушей
slug: "cardsmobile-integration-mechanics-for-loyalty-module"
source_url: "https://developers.mindbox.ru/docs/cardsmobile-integration-mechanics-for-loyalty-module"
breadcrumb:
  - Стандартные интеграции
  - Интеграция с приложением «Кошелёк»
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8078049d1691d3da9c63c59e52bb7cacc2562362bed1f77da65430b0c5eff432"
---

# Механики для интеграции приложения «Кошелёк» для отправки пушей

Инструкция для интеграции приложения «Кошелёк» при использовании [внешней лояльности](koshelek-app-integration.md#создание-интеграции-для-cdp-и-внешней-лояльности-доставка-пушей).

## Создать точку контакта

**PrilozhenieKoshelek**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/5a1a2c6-.png)

## Создать точку интеграции

Если у вас уже создана точка интеграции с другими настройками для интеграции с приложением «Кошелёк» в рамках программы лояльности, используйте её же.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/74affa2-__2021-12-30__13.04.09.png)

## Создать шаблоны действий

#### Кошелёк. Промо пуш доставлен

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/cf1aacd-__2022-01-12__19.35.10.png)

#### Кошелёк. Промо пуш открыт

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/0b70355-2.png)

#### Кошелёк. Транзакционный пуш доставлен

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/284900d-__2022-01-12__19.34.58.png)

#### Кошелёк. Транзакционный пуш открыт

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/08833de-4.png)

## Создать операции

Операции необходимо создавать с теми настройками и именами, которые указаны в инструкции:

### Кошелёк. Промо пуш доставлен

**CardsMobile.PromoPushDelivered**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/6cc0318-5.png)

### Кошелёк. Промо пуш открыт

**CardsMobile.PromoPushOpened**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ee82165-6.png)

### Кошелёк. Транзакционный пуш доставлен

**CardsMobile.TransactionalPushDelivered**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/5d1b230-7.png)

### Кошелёк. Транзакционный пуш открыт

**CardsMobile.TransactionalPushOpened**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/30871bb-8.png)

## Создать дополнительные поля

Для выделения клиентов, у которых есть приложение, при использовании сторонней программы лояльности.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/f5cbf6f-__2022-01-25__17.48.24.png)

**CardsmobileMessageID**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/61f838d-__2023-07-27__11.18.56.png)

**CardsmobileMessageHeader**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ec7c105-__2023-07-27__11.20.03.png)

**CardsmobileMessageBody**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/b1a2fee-__2023-07-27__11.22.38.png)

**CardsmobileMessageUtmSource**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9b99cab-__2023-07-27__11.23.48.png)

**CardsmobileMessageUtmMiddle**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/8d8f3c0-__2023-07-27__11.24.34.png)

**CardsmobileMessageUtmCampaign**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/ef5100a-__2023-07-27__11.25.04.png)
