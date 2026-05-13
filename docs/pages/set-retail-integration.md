---
title: Интеграция Set Retail
slug: "set-retail-integration"
source_url: "https://help.mindbox.ru/docs/set-retail-integration"
vcs_path: "set-retail-integration.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:243369ab7071ab9324fcf887baa396046830f13a48437f9783a4aae32d508263"
---

# Интеграция Set Retail

## Как настроить интеграцию с Set Retail

Порядок настройки, ограничения и возможности указаны по ссылке ([Интеграция с Set Retail](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-set-retail))

### Создать [SMS отправителя](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md)

![permissions-sms-smpp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/permissions-sms-smpp.png)

### Создать [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md)

![Снимок экрана 2021-05-12 в 17.29.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-12%20%D0%B2%2017.29.36.png)

### Создать [статусы заказа](how-to-add-the-status-of-an-order-item.md)

- **Sr10Paid**
- **SR10Return**
- **SR10Cancel**
- **Sr10CheckedOut**

![Screenshot 2024-11-21 at 19.06.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Screenshot%202024-11-21%20at%2019.06.41.png)

### Создать [балльный счет](balances-create.md)

![Снимок экрана 2021-05-18 в 18.11.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-18%20%D0%B2%2018.11.22.png)

### Создать [тип карты](discount-card-types.md)

![Снимок экрана 2023-12-21 в 12.21.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2012.21.38.png)

### Создать [внешний идентификатор заказа](additional-data.md)

**offlineTransactionId**

![Снимок экрана 2024-04-09 в 18.23.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-04-09%20%D0%B2%2018.23.41.png)

### Создать [рассылки](sms-campaign-automated.md)

**1. SMS с кодом авторизации**

Шаблон: `Код авторизации: ${Recipient.AuthentificationCode}`

![Снимок экрана 2021-05-12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-12%20%D0%B2%2018.21.33%283%29.png)

**2. SMS с кодом подтверждения номера**

Шаблон: `Код подтверждения: ${Recipient.MobilePhoneConfirmationCode}`

![Снимок экрана 2023-12-21 в 11.53.39.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2011.53.39.png)

### Создать [операции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md)

**1. Offline.GetCustomerInfo**

![Снимок экрана 2021-07-02 в 11.26.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.26.14.png)

**2. Offline.SendMobilePhoneAuthorizationCode**

![set-retail-Offline.SendMobilePhoneAuthorizationCode.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.SendMobilePhoneAuthorizationCode.png)

Отправка рассылки происходит через [транзакционный сценарий](set-retail-integration.md#sozdat-scenarii).

**3. Offline.RegisterCustomer**

![set-retail-Offline.RegisterCustomer.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.RegisterCustomer.png)

Отправка рассылки происходит через [транзакционный сценарий](set-retail-integration.md#sozdat-scenarii).

**4. Offline.ConfirmMobilePhone**

![Снимок экрана 2023-12-21 в 12.08.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2012.08.46.png)

**5. Offline.ResendMobilePhoneConfirmationCode**

![Снимок экрана 2023-12-21 в 11.54.24.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2011.54.24.png)

**6. Offline.ActivateDiscountCard**

![Снимок экрана 2023-12-21 в 12.14.32.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2012.14.32%281%29.png)

**7. Offline.ActivateVirtualDiscountCard**

![Снимок экрана 2023-12-21 в 12.25.25.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2012.25.25%281%29.png)

**8. Offline.Return**

![Снимок экрана 2021-05-12 в 16.05.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-12%20%D0%B2%2016.05.07%281%29.png)

**9. Offline.SaveOfflineOrder**

![Снимок экрана 2021-05-12 в 16.07.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-12%20%D0%B2%2016.07.56%281%29.png)

**10. Offline.AuthorizedPreorder**

![Снимок экрана 2021-07-02 в 11.33.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.33.31.png)

![Снимок экрана 2021-07-02 в 11.33.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.33.58.png)

**11. Offline.UnauthorizedPreorder**

![Снимок экрана 2021-07-02 в 11.35.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.35.47.png)

![Снимок экрана 2021-07-02 в 11.36.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.36.09.png)

**12. Offline.AnonymousPreorder**

![Снимок экрана 2021-05-12 в 17.06.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-12%20%D0%B2%2017.06.46.png)

**13. Offline.CreateAuthorizedOrder**

![set-retail-Offline.CreateAuthorizedOrder.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.CreateAuthorizedOrder.png)

**14. Offline.CreateAnonymousOrder**

![set-retail-Offline.CreateAnonymousOrder.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.CreateAnonymousOrder.png)

**15. Offline.ChangeStatus**

![set-retail-Offline.ChangeStatus.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.ChangeStatus.png)

**16. Offline.CheckMobilePhoneAuthorizationCode**

![Снимок экрана 2021-07-02 в 11.36.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.36.48.png)

### Создать [сценарии](what-is-workflow.md)

[Транзакционные сценарии](workflow-transactional.md) для отправки SMS.

**1. Для отправки кода авторизации**

![set-retail-Offline.SendMobilePhoneAuthorizationCode-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.SendMobilePhoneAuthorizationCode-workflow.png)

- Событие — Клиент запросил код авторизации;
- Условие — проверяем, что был запрос из нужной операции:

![set-retail-Offline.SendMobilePhoneAuthorizationCode-workflow-conditions.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.SendMobilePhoneAuthorizationCode-workflow-conditions.png)

- Группа шагов — отправляем созданную рассылку с кодом авторизации.

**2. Для отправки кода подтверждения номера**

![set-retail-Offline.RegisterCustomer-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.RegisterCustomer-workflow.png)

- Событие — Клиент зарегистрировался;
- Условие — проверяем, что был запрос из нужной операции:

![set-retail-Offline.RegisterCustomer-workflow-conditions.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/set-retail-Offline.RegisterCustomer-workflow-conditions.png)

- Группа шагов — отправляем созданную рассылку c кодом подтверждения.

### Настройка ПО Set Retail

1. Полученную «Точку интеграции» необходимо записать в «Endpoint процессинга»
2. Полученный «Секретный ключ» нужно записать в «Секретный ключ» в формате: **Mindbox secretKey="XXXXXXXXX"**
3. Полученное «Системное имя бонусного счета» нужно записать в «Идентификатор основного бонусного счета»

[Интеграция сайта с платформой Mindbox](https://mindbox.ru/academy/education/5-ehtapov-integracii-mindbox/): получение данных с сайта, из мобильного приложения, лендингов, программы лояльности, офлайн-точек, CRM-систем.
