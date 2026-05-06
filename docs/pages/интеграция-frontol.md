---
title: Интеграция Frontol
slug: "интеграция-frontol"
source_url: "https://help.mindbox.ru/docs/интеграция-frontol"
vcs_path: "интеграция-frontol.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:6ba11fbd82cb44dc3403719fd74bbadfc045fb2f371784c13c5084e10747ac5d"
---

# Интеграция Frontol

## Как настроить интеграцию с Frontol

Порядок настройки, ограничения и возможности указаны по ссылке ([Интеграция с Frontol](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-frontol))

## Настройка SMS отправителя

Добавьте SMPP-соединение по [инструкции](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md).

![permissions-sms-smpp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/permissions-sms-smpp.png)

## Создание точки интеграции

[Создайте точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) с типом «Другое»:

![frontol-endpoint.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-endpoint.png)

## Создание рассылки

### Авторизация Frontol

Создайте [автоматическую SMS-рассылку](sms-campaign-automated.md). Шаблон кода авторизации — `${Recipient.AuthentificationCode}`:

![frontol-email-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-email-text.png)

Установите транзакционный профиль рассылки:

![frontol-email-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-email-settings.png)

## Настройка операций

Создайте операции [по инструкции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sozdanie-operacii-v3) и перейдите к настройкам ниже.

### Frontol.AnonymousPreorder

![frontol-anonymous-preorder.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-anonymous-preorder.png)

### Frontol.AuthorizedPreorder

![frontol-authorized-preorder-1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-authorized-preorder-1.png)

![frontol-authorized-preorder-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-authorized-preorder-2.png)

### Frontol.BeginAnonymousOrderTransaction

![frontol-begin-anonymous.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-begin-anonymous.png)

### Frontol.BeginAuthorizedOrderTransaction

![frontol-begin-authorized.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-begin-authorized.png)

### Frontol.CancelOrder

![frontol-cancel-order.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-cancel-order.png)

### Frontol.CommitRegisterCustomer

![Снимок экрана 2021-05-06 в 16.51.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-06%20%D0%B2%2016.51.35.png)

### Frontol.GetCustomerInfo

![frontol-getcustomerinfo-1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-getcustomerinfo-1.png)

![frontol-getcustomerinfo-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-getcustomerinfo-2.png)

### Frontol.RegisterCustomer

![frontol-register-customer-1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-register-customer-1.png)

![frontol-register-customer-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-register-customer-2.png)

![frontol-register-customer-3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-register-customer-3.png)

### Frontol.Return

![frontol-return.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-return.png)

### Frontol.SendMobilePhoneAuthorizationCode

![frontol-send-code-1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-send-code-1.png)

![frontol-send-code-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/frontol-send-code-2.png)

## Передача данных

Менеджер проекта Mindbox передает данные в разработку для выполнения настроек.

## Добавить данные в ПО Frontol

**1. Перейдите в настройки платежной системы**  
**2. Добавьте новую платежную систему**  
**3. Укажите в свойствах «Frontol Priority API»**  
**4. Перейдите в «Параметры АС»**  
**5. Заполните поля**

- «Веб-адрес сервера лояльности» - https://frontol-gateway.mindbox.ru
- «Идентификатор организации» берется из системного имени точки интеграции.

  **Пример**:

  - Системное имя: Demo.Frontol
  - Идентификатор организации: Demo
- «Ключ доступа» — cекретный ключ точки интеграции.
- *Идентификатор магазина и идентификатор кассы* — настраивает клиент
- Если необходимо работать с клиентами без дисконтной карты — установите галочку *«Отправлять документы продажи и возврата без карты лояльности»*

**6. Перейти в назначение платежной системы и выбрать «Бонусы и скидки».**

[Интеграция сайта с платформой Mindbox](https://mindbox.ru/academy/education/5-ehtapov-integracii-mindbox/): получение данных с сайта, из мобильного приложения, лендингов, программы лояльности, офлайн-точек, CRM-систем.
