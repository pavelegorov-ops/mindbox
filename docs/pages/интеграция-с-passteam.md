---
title: Интеграция с Passteam
slug: "интеграция-с-passteam"
source_url: "https://help.mindbox.ru/docs/интеграция-с-passteam"
vcs_path: "интеграция-с-passteam.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:29539caea3e7b742ad3609b52157e5540beb463900f94b5e68abd3be158dd25d"
---

# Интеграция с Passteam

Порядок настройки, ограничения и возможности указаны по ссылке [(Интеграция с Passteam)](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-passteam).

## Шаг 1 — создаем [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md)

![Снимок экрана 2021-11-30 в 19.19.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.19.21.png)

## Шаг 2 — создаем [операции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md)

1. Passteam.ExportCustomers. Позволяет экспортировать клиентов при синхронизации с Passteam:

![Снимок экрана 2021-11-30 в 18.45.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2018.45.40.png)

![Снимок экрана 2021-11-30 в 18.45.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2018.45.56.png)

После вызова операции создается задание на генерацию JSON файла, запуск синхронизации возможен только после того, как задание выполнится.

2. Passteam.CreateCustomer. Операция позволяет импортировать клиентов на стороне MB, при создании в Passteam карты:

![Снимок экрана 2021-11-30 в 18.48.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2018.48.26.png)

3. Passteam.GetCustomerByPhone. Позволяет находить в Mindbox клиента по номеру телефона. В интеграции используется как метод дедубликации, чтобы не возникал случай повторного создания клиента в Mindbox:

![Снимок экрана 2021-11-30 в 18.49.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2018.49.48.png)

4. Passteam.UpdateCustomer. Позволяет находить в MB клиента по номеру телефона, после чего обновляет его данными, переданными из запроса при установке карты в Passteam:

![Снимок экрана 2021-11-30 в 18.51.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2018.51.08.png)

## Шаг 3 — создаем [веб-хук](webhooks.md)

![Снимок экрана 2022-02-17 в 23.08.37 — копия.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-02-17%20%D0%B2%2023.08.37%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F.png)

Тип: POST  
Url : https://app.passteam.io/integrations/mindbox/webhook  
Content-Type: application/json  
MindboxKey - secretKey для подключаемой точки интеграции  
companyId – идентификатор, который получает менеджер – id компании в Passteam

Тело запроса:

```
{
	"companyId":"...",
	"action":"customerUpdated",
	"fields":{
	    "%NAME%":"${Recipient.FirstName}",
	    "%SURNAME%":"${Recipient.LastName}",
	    "%EMAIL%":"${Recipient.Email}",
	    "%PHONE%":"${Recipient.MobilePhone}",
        "%_BALANCE%":"${Recipient.GetBonusPointsAccount("Main").Available}",
	    "%CARDCODE%": "${Recipient.Card.AnyType.Number}"
	}
}
```

Набор полей в теле запроса индивидуален для каждого клиента.

**Синтаксис:** %название_переменной_Passteam%: “поле в Mindbox“

Переменные в Passteam:

| Passteam | Значение |
| --- | --- |
| %NAME% | Имя |
| %SURNAME% | Фамилия |
| %PATRONYMIC% | Отчество |
| %EMAIL% | Адрес электронной почты |
| %PHONE% | Номер телефона |
| %BIRTHDAY% | День рождения |
| %SEX% | Пол - возможные значения: male, female |
| %NEXTBURNBALANCE% | Сумма баллов к сгоранию |
| %DISCOUNT% | Скидка |
| %NEXTBURNDATE% | Дата сгорания баллов |
| %BONUS% | Кэшбэк |
| %_BALANCE% | Бонусы |

Если этих переменных недостаточно, пожалуйста, сообщите менеджеру Passteam, и он добавит необходимые.

## Шаг 4 — создаем [сценарии](what-is-workflow.md)

#### Сценарий 1.

Сценарий срабатывает после изменения клиента/ создания и вызывает созданный раннее вебхук:

- блок 1 — событие — «Данные клиента изменены». [Частота применения](workflow-limit-per-customer.md) - каждый раз.
- блок 2 — группа шагов — отправить созданный веб-хук

![Снимок экрана 2021-11-30 в 19.43.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.43.43.png)

#### Сценарий 2.

Сценарий срабатывает после активации карты и вызывает созданный раннее вебхук:

- блок 1 — событие — выдано действие «Активация карты». [Частота применения](workflow-limit-per-customer.md) - каждый раз.
- блок 2 — группа шагов — отправить созданный веб-хук

![Снимок экрана 2021-11-30 в 19.46.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.46.26.png)

#### Сценарий 3.

Сценарий срабатывает после изменения баланса у клиента Mindbox и отправляет созданный раннее вебхук:

- блок 1 — изменение заданного баланса — по любому балансу. [Частота применения](workflow-limit-per-customer.md) - каждый раз.
- блок 2 — группа шагов — отправить созданный веб-хук

![Снимок экрана 2021-11-30 в 19.48.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.48.26.png)

## Шаг 5 — создаем [дополнительные поля](additional-data.md)

- passteamInstalledStatus: Для хранения статуса установки:

![Снимок экрана 2021-11-30 в 19.12.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.12.27.png)

- passteamQrCodeUrl: Ссылка на QR-код карты:

![Снимок экрана 2021-11-30 в 19.14.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-30%20%D0%B2%2019.14.13.png)

[Интеграция сайта с платформой Mindbox](https://mindbox.ru/academy/education/5-ehtapov-integracii-mindbox/): получение данных с сайта, из мобильного приложения, лендингов, программы лояльности, офлайн-точек, CRM-систем.
