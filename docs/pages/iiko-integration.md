---
title: Интеграция iiko
slug: "iiko-integration"
source_url: "https://help.mindbox.ru/docs/iiko-integration"
vcs_path: "iiko-integration.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:cc335d37a2da876accf4ec876b061cb783d8af5096458bda49ee54e85ed9e367"
---

# Интеграция iiko

[iiko](https://iiko.ru/solutions) — специализированная система ERP-класса, предназначенная для автоматизации ресторанного бизнеса. Касса, склад, персонал, кухня, финансы, отчетность — все в единой системе.

---

Порядок настройки, ограничения и возможности интеграции указаны [по ссылке](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-iiko).

Ниже приведены сущности, которые должны быть на проекте для интеграции с iiko.

## [Точка интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md)

- Пресет — *Другое*;
- *Настройки подтверждения контактов — Подтверждение мобильного телефона* — включите, если нужно, чтобы в персональных акциях могли участвовать только клиенты с подтвержденным номером.

![endpoint-iiko.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/endpoint-iiko.png)

## [Статусы заказа](how-to-add-the-status-of-an-order-item.md)

Внешние идентификаторы:

- `iikoPaid`
- `iikoReturn`
- `iikoCheckedOut`

![iiko-order-statuses.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-order-statuses.png)

## [Внешняя система](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D1%8E%D1%8E-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83.md)

Допустимы любое название и системное имя.

![iiko-external-system.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-external-system.png)

## [Внешний идентификатор заказа](additional-data.md)

Дополнительное поле:

- *Для сущности* — Заказ;
- *Тип поля* — Внешний идентификатор.

![iiko-externalID.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-externalID.png)

## [Дополнительные поля](additional-data.md)

### Уровень клиента

Если стоит задача выводить уровень программы лояльности посетителя, можно настроить передачу его значения.

Для этого нужно создать сегменты с условиями для каждого уровня и записывать клиенту полученный ранг в дополнительное поле с помощью [сценария](iiko-integration.md#scenarii).

- **Сущность** — Клиент
- **Системное имя** — Rank

![iiko-custom-field.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field.png)

### Официант заказа

iiko может передавать данные об официанте по каждому заказу. С помощью [выгрузки заказов](https://help.mindbox.ru/docs/export-orders) анализируйте подозрительные списания баллов по каждому официанту для построения антифрод-аналитики.

Параметры поля:

- **Сущность** — Заказ
- **Системное имя** — Waiter

![iiko-custom-field-waiter.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field-waiter.png)

## [Балльный счет](balances-create.md)

Допустимы любые настройки.

![iiko-balance.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-balance.png)

## [SMS-соединение](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md)

![permissions-sms-smpp.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/permissions-sms-smpp.png)

## [SMS-рассылки](sms-campaign-automated.md)

**1. SMS с кодом авторизации**

Шаблон: `Код авторизации: ${Recipient.AuthentificationCode}`

![iiko-sms-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-sms-auth.png)

**2. SMS с кодом подтверждения номера**

Шаблон: `Код подтверждения: ${Recipient.MobilePhoneConfirmationCode}`

![Снимок экрана 2023-12-21 в 11.53.39.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2011.53.39.png)

## [Операции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md)

#### 1. Offline.RegisterCustomer

![iiko-operations1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations1.png)

Если в точке интеграции включено подтверждение мобильного телефона, отправляйте SMS с кодом подтверждения через [транзакционный сценарий](iiko-integration.md#scenarii).

#### 2. Offline.SendMobilePhoneAuthorizationCode

Шаг «Сгенерировать код авторизации» используйте, только если нужно отправлять SMS с кодом подтверждения при оплате заказа баллами (в файле конфигурации поле "send_sms_confirm" = true). Отправка рассылки происходит через [транзакционный сценарий](iiko-integration.md#scenarii).

![iiko-operations2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations2.png)

#### 3. Offline.ResendMobilePhoneConfirmationCode

Шаг «Отправить SMS» используйте, только если в точке интеграции включено подтверждение мобильного телефона.

![iiko-operations3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations3.png)

#### 4. Offline.CheckCustomer

В чекбоксе «Баланс клиента» выберите «в выбранных балльных счетах» и укажите балльный счет, работающий с кассой iiko, системное имя которого указано в файле конфигурации.

![iiko-operations4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations4.png)

#### 5. Offline.CheckMobilePhoneAuthorizationCode

![iiko-operations5.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations5.png)

#### 6. Offline.ConfirmMobilePhone

![iiko-operations6.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations6.png)

#### 7. Offline.AuthorizedPreorder

![iiko-operations7.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations7.png)

#### 8. Offline.CreateAuthorizedOrder

![iiko-operations8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations8.png)

#### 9. Offline.AnonymousPreorder

![iiko-operations9.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations9.png)

#### 10. Offline.CreateAnonymousOrder

![iiko-operations10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations10.png)

#### 11. Offline.SaveOfflineOrder

![iiko-operations11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations11.png)

#### 12. Offline.ChangeStatus

![iiko-operations12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations12.png)

#### 13. Offline.Return

![iiko-operations13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations13.png)

#### 14. Offline.EditCustomer

![iiko-operations14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations14.png)

#### 15. Offline.SendProductCatalog

![iiko-operations15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-operations15.png)

## [Сценарии](what-is-workflow.md)

**Для записи уровня ПЛ в дополнительное поле**

![iiko-custom-field-workflow.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field-workflow.png)

- Запуск — попадание в один из сегментов ПЛ:

![iiko-custom-field-workflow-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field-workflow-event.png)

- Условие — наличие в конкретном сегменте:

![iiko-custom-field-workflow-conditions.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field-workflow-conditions.png)

- Группа шагов — записываем значение в поле:

![iiko-custom-field-workflow-steps.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/iiko-custom-field-workflow-steps.png)

По такому же принципу добавляются ветки для остальных рангов.

---

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

- Группа шагов — отправляем созданную рассылку с кодом авторизации.
