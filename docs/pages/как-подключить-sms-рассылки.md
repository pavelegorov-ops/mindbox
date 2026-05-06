---
title: "Как подключить SMS-рассылки"
slug: "как-подключить-sms-рассылки"
source_url: "https://help.mindbox.ru/docs/как-подключить-sms-рассылки"
vcs_path: "как-подключить-sms-рассылки.md"
toc_path:
  - Рассылки
  - "SMS-рассылки"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:4fcc45886f0fc1646b9bbf54ee123465a6c7a5e6aebd4622240b478fd04627c1"
---

# Как подключить SMS-рассылки

Mindbox — управляющая маркетинговая система, а провайдер является транспортом для доставки SMS- и Viber-сообщений пользователям через шлюз .  
Протокол SMPP- формат данных для передачи сообщения из Mindbox провайдеру.

Мы работаем со следующими провайдерами SMS-рассылок:

|  |  |  |
| --- | --- | --- |
| - АДВ Медиа Групп - Альфа СМС - Девино Телеком - КазИнфоТех - Мегафон Хаб - ПИР СМС - Простор-СМС - Ростелеком - Связной - СМС Дисконт - СМС УСЛУГИ - СМС-Агент - AtomPark - Beeline SMPP - Beltelecom - DanyTech - Dexatel - Digital-Direct - Easy SMS - edna (бывший MFMS) - ePochta - FunBox - Generic SMPP - GMS | - Green SMS SMPP - i-Digital - i-Digital (UDH) - imobis - Infobip - Intellin - IntelNetCom - Intis Telecom SMPP - MainSMS SMPP - Mediarik - Messaggio - Microsms Smpp - Mir sms - MMD Smart - MTS Marketolog - MTT - P1SMS - Play Mobile UZ - PushSMS SMPP - QTelecom - Rapporto SMPP - RedSMS SMPP - SevenTech - Sigma messaging | - SMS Aero - SMS profi - SMS-ассистент - SMS-Центр - SMS-Центр Казахстан - Sms-Consult.kz - sms-prostoru - Sms-Traffic - Sms SMPP - Smsbliss - SmsGold SMPP - SmsGorod - SMSint - Smstec - soft-line.az - Stream Telecom Smpp - Target SMS - Terasms - TurboSMS - UNIBELL - UtelePro - Voxys - Web sms - Webcom Mobi - Weborama SMPP |

### Шаг 1. Подключите SMPP-соединение.

Если у вас уже подключено SMS SMPP-соединение с провайдером из списка, переходите к шагу 2.  
Выберите шлюз для отправки сообщений. Мы поддерживаем любого оператора, у которого есть SMPP-протокол и прямое подключение к хосту.

**Если вашего подрядчика-шлюза нет в нашем списке, обратитесь к менеджеру на вашем проекте.**

### Шаг 2. Добавьте SMPP-соединение в Mindbox.

2.1. Запросите у провайдера следующие данные:

- host
- port
- логин (или systemId)
- пароль
- имя отправителя

#### IP адреса в Mindbox

Провайдер может потребовать IP-адреса, с которых к ним будут подключаться, чтобы добавить их в список разрешенных.

Внести в список нужно все адреса. Актуальный список — на странице добавления соединения в вашем проекте.

2.2. Перейдите на страницу добавления соединения: **Настройки** → **Рассылки** → **Соединения** → **SMS** → **Все соединения**.

![sms-smpp-1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/sms-smpp-1.png)

Выберите бренд. Если у вас один бренд, то он будет выбран автоматически. Нажмите на «Добавить соединение» и введите данные, полученные от провайдера.

![sms-smpp-2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/sms-smpp-2.png)

Обратите внимание: после введения имени отправителя надо нажать **Enter.**

![Screenshot 2022-10-05 at 14-01-25 Aag SMS SMPP-соединения1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Screenshot%202022-10-05%20at%2014-01-25%20Aag%20SMS%20SMPP-%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%281%29%281%29.png)

Имена отправителя нельзя удалить после сохранения соединения.

### Шаг 3. Включите модуль SMS-рассылок.

В демо-режиме можно отправлять [тестовые сообщения](mailings-test-mode.md), но запуск SMS-рассылок не доступен.

Для этого запросите подключение модуля SMS-рассылок в разделе [Подписка и оплата](billing-modules.md) или обратитесь к менеджеру.

Конечную стоимость за услуги отправок SMS рассылок вы можете уточнить у провайдера.

### Отключить соединение

Неактивное соединение можно отключить. После этого оно не будет пытаться подключиться к провайдеру и [соответствующая проблема](issues-types.md#dkim,-smpp) пропадет. Убирать для этого соединение из отправленных рассылок не нужно, но выбрать его в новых кампаниях будет нельзя.

[10 базовых принципов](https://mindbox.ru/academy/education/tekst-dlya-sms-rassylki/) написания текста для продающей SMS-рассылки
