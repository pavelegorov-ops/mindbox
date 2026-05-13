---
title: Механики для интеграции приложения «Кошелёк» с модулем лояльность на Mindbox
slug: "create-integration-for-cdp-and-loyalty-module"
source_url: "https://developers.mindbox.ru/docs/create-integration-for-cdp-and-loyalty-module"
breadcrumb:
  - Стандартные интеграции
  - Интеграция с приложением «Кошелёк»
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:0bc82209f820f556c6932a7ccfac47f5c4a21cb3d77c70be0b879b9f3543dc12"
---

# Механики для интеграции приложения «Кошелёк» с модулем лояльность на Mindbox

Инструкция для интеграции приложения «Кошелёк» при использовании [лояльности Mindbox](koshelek-app-integration.md#создание-интеграции-для-cdp-и-модуля-лояльность-на-mindbox).

## Создать точку контакта

**PrilozhenieKoshelek**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9b59e11-.png "тк.png")

## Создать точку интеграции

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1d41780-.png "ти.png")

## Создать сегменты действий

### Изменение баланса

**CustomerBalanceChange**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/74c6c2a--.png "сегмент-баланс.png")

### Все заказы

**AllOrders**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/9ffd2e3--.png "сегмент-заказы.png")

## Создать тип дисконтных карт

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/74b247d-__2022-04-27__11.02.27.png "Снимок экрана 2022-04-27 в 11.02.27.png")

## Создать дополнительное поле

### Город

**City**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1c0d9f9-__2022-02-22__18.10.22.png "Снимок экрана 2022-02-22 в 18.10.22.png")

## Создать операции

Операции необходимо создавать с теми настройками и именами, которые указаны в инструкции:

### Активация карты в приложении "Кошелёк"

**CardsMobile.ActivateCard**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/8d584a3-1.png "оп1.png")

### Выгрузить дисконтные карты

**CardsMobile.GetDiscountCards**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/fe6e394-2.png "оп2.png")

### Выдача новой карты в приложении "Кошелёк"

**CardsMobile.BindCard**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/86cfd00-4.png "оп4.png")

### Получение доступных промоакций в приложении "Кошелёк"

**CardsMobile.GetAvailablePromotions**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/8c954c9-__2021-12-29__21.38.59.png "Снимок экрана 2021-12-29 в 21.38.59.png")

### Получение информации о покупателе в приложении "Кошелёк"

**CardsMobile.GetCustomerInfo**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/51d56a7-10.png "оп10.png")

### Получение информации по карте

**CardsMobile.GetDiscountCard**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a1e1599-11.png "оп11.png")

### Получение истории заказов в приложении "Кошелёк"

**CardsMobile.GetCustomerOrders**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/4d4910e-12.png "оп12.png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/2d91caa-121.png "оп121.png")

### Получение истории изменений баланса в приложении "Кошелёк"

**CardsMobile.GetCustomerBalanceHistory**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/22d6dd8-13.png "оп13.png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d23e7de-__2021-12-29__22.08.37.png "Снимок экрана 2021-12-29 в 22.08.37.png")

### Проверка наличия покупателя в приложении "Кошелёк"

**CardsMobile.CheckCustomer**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/677728d-14.png "оп14.png")

### Регистрация в приложении "Кошелёк"

**CardsMobile.RegisterCustomer**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/c7febe6-15.png "оп15.png")

### Редактирование потребителя в приложении "Кошелёк"

**CardsMobile.EditCustomer**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/dd6eed7-__2022-02-22__18.08.11.png "Снимок экрана 2022-02-22 в 18.08.11.png")

### Подтверждение мобильного телефона в приложении "Кошелёк"

**CardsMobile.ConfirmPhone**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/e565ad3-__2022-02-22__17.36.50.png "Снимок экрана 2022-02-22 в 17.36.50.png")
