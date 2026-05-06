---
title: Интеграция OSMI Cards
slug: "интеграция-osmi-cards"
source_url: "https://help.mindbox.ru/docs/интеграция-osmi-cards"
vcs_path: "интеграция-osmi-cards.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:174ed0e875deaa14dcc8b63fbca43ee28c643519f317b153bcd5c5520820124b"
---

# Интеграция OSMI Cards

## **Как настроить интеграцию OSMI Cards**

Порядок настройки, ограничения и возможности указаны по ссылке [(Интеграция с OSMI Cards)](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-osmi-cards).

### Создать [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md)

Тип пресета — «**Другое**». Для создания и настройки интеграции с внешней системой.

![Снимок экрана 2023-03-21 в 07.35.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-21%20%D0%B2%2007.35.43.png)

### Создать [шаблон действия](template-create.md)

**1. UpdateCard**  
Обновление электронной карты

![osmi-cards-action.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/osmi-cards-action.png)

### Создать [балльный счет](balances-create.md)

**Если бальный счет создан, то этот шаг можно пропустить.**

![Снимок экрана 2021-05-28 в 15.18.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-28%20%D0%B2%2015.18.01.png)

### Создать [дополнительные поля](additional-data.md)

**1. WalletCardLink**

Ссылка на установку электронной карты

![Снимок экрана 2021-04-28 в 15.40.25.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-28%20%D0%B2%2015.40.25.png)

**2. WalletCardSubscription**

Подписан на рассылки

![Снимок экрана 2021-04-28 в 15.41.16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-28%20%D0%B2%2015.41.16.png)

**3. WalletCardQrCodeLink**

Ссылка на qr-код установки карты

![Снимок экрана 2021-04-28 в 15.41.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-28%20%D0%B2%2015.41.50.png)

### Создать [тип дисконтных карт](discount-card-types.md)

![Снимок экрана 2023-03-21 в 08.26.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-21%20%D0%B2%2008.26.04.png)

### [Импортировать](discount-cards-import.md) дисконтные карты

В файле укажите для карт созданный в предыдущем пункте тип.

![Снимок экрана 2024-09-11 в 22.35.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-11%20%D0%B2%2022.35.30.png)

### Создать [вебхуки](webhooks.md)

Создать вебхук необходимо **после** того, как менеджер OSMI Cards передаст вам шаблон.

**1. Создание карты OSMI**

POST

```
https://[URL полученный от OSMI или клиента]/v2t/passes/${Recipient.Card.[тип карты].Number}/[название шаблона дизайна дисконтной карты полученный от OSMI или клиента]?withValues=true&transactionId=${WebhookRequest.TransactionalId}
```

Content-Type

```
application/json
```

Authorization

```
Bearer xxxxx где xxxxx это токен, который получен от менеджера OSMI
```

Тело запроса

```
{
"values": [
    {
    "label": "[название поля "клиент" полученное от OSMI или клиента]",
    "value": "@{if IsEmpty(Recipient.OnlyStandardFirstName)}@{ else }${Recipient.FirstAndLastName}@{end if}"
    },
    {
    "label": "["название поля "баллы" полученное от OSMI или клиента]",
    "value": "${Recipient.GetBonusPointsAccount("[название бального счета в Mindbox]").Available}"
    }
],
   "barcode": {
        "show": true,
        "showSignature": true,
        "message": "${Recipient.Card.AnyType.Number}",
        "signature": "${Recipient.Card.AnyType.Number}"
    }
}
```

**2. Обновление баланса карты OSMI**

PUT

```
https://[URL полученный от OSMI или клиента]/v2t/passes/${Recipient.Card.[тип карты].Number}?transactionId=${WebhookRequest.TransactionalId}&push=true
```

Content-Type

```
application/json
```

Authorization

```
Bearer xxxxx где xxxxx это токен, который получен от менеджера OSMI
```

Тело запроса

```
{
"values": [
    {
    "label": "[название поля "клиент" полученное от OSMI или клиента]",
    "value": "@{if IsEmpty(Recipient.OnlyStandardFirstName)}@{ else }${Recipient.FirstAndLastName}@{end if}"
    },
    {
    "label": "[название поля "баллы" полученное от OSMI или клиента]",
    "value": "${Recipient.GetBonusPointsAccount("[название бального счета в Mindbox]").Available}"
    }
],
   "barcode": {
        "show": true,
        "showSignature": true,
        "message": "${Recipient.Card.AnyType.Number}",
        "signature": "${Recipient.Card.AnyType.Number}"
    }
}

В теле запроса могут быть дополнительные параметры полей, в зависимости от потребностей клиента.
```

### Создать [сценарии](what-is-workflow.md)

**1. OSMI - Изменение баланса**

- Событие — «Изменение заданного баланса» в выбранном счете:

![Снимок экрана 2023-03-21 в 07.53.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-21%20%D0%B2%2007.53.26%281%29.png)

- Группа шагов — вызвать вебхук:

![osmi-webhook.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/osmi-webhook.png)

Ответ сервиса и ошибки можно проверить в [логах вызова вебхуков](webhook-logs).

**2. OSMI - Создание карты**

- Событие — зависит от выборки, которая должна получить карты. Это может быть любое попадание в базу или регистрация через определенную операцию, например.
- [Частота применения](workflow-limit-per-customer.md) - одним разом на клиента.

![Снимок экрана 2023-05-25 в 18.12.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-05-25%20%D0%B2%2018.12.30.png)

- Проверяем, что нет карт OSMI:

![Снимок экрана 2023-05-25 в 18.14.17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-05-25%20%D0%B2%2018.14.17.png)

- Выдаем карту и вызываем вебхук:

![Снимок экрана 2023-05-25 в 18.16.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-05-25%20%D0%B2%2018.16.30.png)

### Создать [операции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md)

Операции необходимо создавать с теми настройками и именами, которые указаны в инструкции:

**1. Wallet.BindCard**

![Снимок экрана 2021-04-21 в 16.12.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-21%20%D0%B2%2016.12.46.png)

**2. Wallet.CheckCustomer**

![Снимок экрана 2021-07-02 в 11.12.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.12.13.png)

**3. Wallet.EditCustomer**

![Снимок экрана 2021-07-02 в 11.11.25.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.11.25.png)

**4. Wallet.RegisterCustomer**

![Снимок экрана 2021-07-02 в 11.10.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.10.30.png)

**5. Wallet.SubscribeCard**

![Снимок экрана 2021-07-02 в 11.09.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.09.53.png)

**6. Wallet.UnsubscribeCard**

![Снимок экрана 2021-07-02 в 11.08.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.08.52.png)

**7. Wallet.UpdateCard**

![Снимок экрана 2023-05-25 в 17.56.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-05-25%20%D0%B2%2017.56.40.png)

**8. Wallet.SetCardLink**

![Снимок экрана 2021-07-02 в 11.07.55.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-02%20%D0%B2%2011.07.55.png)

[Интеграция сайта с платформой Mindbox](https://mindbox.ru/academy/education/5-ehtapov-integracii-mindbox/): получение данных с сайта, из мобильного приложения, лендингов, программы лояльности, офлайн-точек, CRM-систем.
