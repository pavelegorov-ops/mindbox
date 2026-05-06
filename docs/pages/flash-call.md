---
title: Flash Call — авторизация по звонку
slug: "flash-call"
source_url: "https://help.mindbox.ru/docs/flash-call"
vcs_path: "flash-call.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Взаимодействие со сторонними системами
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:014c4deeb7ccd970bc08fa9960f7692cfca03e514d9a82708220b324553f5af8"
---

# Flash Call — авторизация по звонку

## Как это работает

Технология Flash Call позволяет подтвердить личность клиента с помощью телефонного звонка: пользователь получает звонок с номера, последние 4 цифры которого — специальный код для авторизации.

Плюсы механики:

- экономия по сравнению с SMS — в 4-5 раз;
- звонки могут осуществляться на номера любых операторов по всему миру.

Добавление в механику отправки SMS покрывает риск не доставить код клиентам, до которых не удалось дозвониться.

## Как настроить

1. Выберите провайдера для Flash Call.

Важный критерий выбора — возможность настройки через SMPP-соединение. От этого зависит, как будет происходить отправка кода из Mindbox в сервис:

- при поддержке SMPP-протокола можно отправлять коды [через SMPP-соединение](flash-call.md#integraciya-flash-call-po-smpp) из [транзакционного сценария](workflow-transactional.md);
- альтернативный способ — [HTTP-запрос через вебхуки](flash-call.md#integraciya-flash-call-po-http).

Ниже рассматриваем оба варианта интеграции.

Примеры сервисов: [terasms](https://terasms.ru/services-flashcall.html), [Rapporto](https://rapporto.ru/flashcall), [Devino Telecom](https://www.devinotele.com/),

2. Настройте соединение с сервисом и получите спецификации для получения кода авторизации из Mindbox.
3. Подключите [SMS-соединение](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md) для отправки SMS при невозможности выполнения звонка.

### Интеграция Flash Call по SMPP

1. Создайте [SMPP-соединение](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md) для Flash-звонков.  
   Пример настройки:

![Снимок экрана 2023-08-03 в 13.09.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.09.29.png)

2. Настройте отправку кода авторизации в сервис Flash Call.  
   Так как интеграция происходит через SMPP-соединение, в платформе Mindbox отправка настраивается через автоматическую [SMS-рассылку](sms-campaign-automated.md) с нужным подключением:

![Снимок экрана 2023-08-03 в 13.14.20.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.14.20.png)

Отправки сообщения клиенту при этом не происходит, код отправляется в сторонний сервис, который запускает звонок клиенту с нужного номера.

Параметр кода авторизации — `${Recipient.AuthentificationCode}`

Если на проекте уже заведены представленные ниже кампании, можете их переиспользовать для данной механики.

3. Создайте автоматическую [SMS-рассылку](sms-campaign-automated.md), которая будет отправляться при невозможности совершить звонок, с рабочим соединением **для SMS-отправок**:

![Снимок экрана 2023-08-03 в 11.01.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2011.01.41.png)

Код авторизации — `${Recipient.AuthentificationCode}`

4. Создайте [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md) для генерации кода:

![Снимок экрана 2023-11-16 в 19.03.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-16%20%D0%B2%2019.03.15.png)

5. Создайте операцию, с помощью которой будет проверяться введенный клиентом код:

![Снимок экрана 2023-12-12 в 22.47.05.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-12%20%D0%B2%2022.47.05.png)

6. Создайте операцию для запроса SMS по кнопке без ожидания звонка:

![Снимок экрана 2023-12-16 в 15.04.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.04.19.png)

Отдельная операция позволит настроить ручной запуск SMS, когда опция звонка не подходит клиенту.

7. Создайте сценарий:

7.1. Запуск — по [запросу кода](workflow-events.md#zaproshen-kod-avtorizacii):

![Снимок экрана 2023-11-16 в 19.18.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-16%20%D0%B2%2019.18.41.png)

7.2. Если запрос на Flash Call:

![Снимок экрана 2023-12-16 в 15.23.20.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.23.20.png)

7.3. Отправляем код в сервис для Flash Call:

![Снимок экрана 2023-12-12 в 23.18.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-12%20%D0%B2%2023.18.52.png)

7.4. Через минуту:

![Снимок экрана 2023-12-16 в 15.25.34.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.25.34.png)

7.5. Проверяем, были ли проблемы с отправкой кода:

![Снимок экрана 2024-08-06 в 08.13.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-06%20%D0%B2%2008.13.48.png)

7.6. В таком случае отправляем SMS клиенту:

![Снимок экрана 2023-08-03 в 13.04.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.04.26.png)

7.7. В ветке «Нет» от первого условия:

![Снимок экрана 2023-12-16 в 15.39.44.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.39.44.png)

Проверяем, был ли запрос на SMS:

![Снимок экрана 2023-12-16 в 15.24.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.24.38.png)

В данном случае также отправляем SMS.

[Транзакционный сценарий](workflow-transactional.md) готов:

![Снимок экрана 2023-12-16 в 15.26.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.26.04%281%29.png)

### Интеграция Flash Call по HTTP

1. Создайте [точку интеграции для вебхуков](webhooks.md#sozdanie-tochki-integracii).

Заполнение полей зависит от выбранного сервиса.  
Пример настройки:

![Снимок экрана 2023-08-03 в 10.10.25.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2010.10.25.png)

2. Создайте [вебхук](webhooks.md#sozdanie-vebhuka) для отправки кода авторизации.

Требования к формату могут различаться в зависимости от выбранного оператора.  
[Параметры](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md), которые понадобятся для отправки клиенту:

- мобильный номер — `${Recipient.MobilePhone}`
- код авторизации — `${Recipient.AuthentificationCode}`

![Снимок экрана 2023-08-03 в 10.20.34.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2010.20.34.png)

Вебхук должен принимать ответы:

![Снимок экрана 2023-08-03 в 10.22.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2010.22.01.png)

Если на проекте уже заведены представленные ниже кампании, можете их переиспользовать для данной механики.

3. Создайте автоматическую [SMS-рассылку](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md), которая будет отправляться при невозможности совершить звонок:

![Снимок экрана 2023-08-03 в 11.01.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2011.01.41.png)

Код авторизации — `${Recipient.AuthentificationCode}`

4. Создайте [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md) для генерации кода и запуска механики:

![Снимок экрана 2023-11-16 в 19.03.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-16%20%D0%B2%2019.03.15.png)

5. Создайте операцию, с помощью которой будет проверяться введенный клиентом код:

![Снимок экрана 2023-11-16 в 19.11.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-16%20%D0%B2%2019.11.22.png)

6. Создайте операцию для запроса SMS по кнопке без ожидания звонка:

![Снимок экрана 2023-12-16 в 15.04.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.04.19.png)

Отдельная операция позволит настроить ручной запуск SMS, когда опция звонка не подходит клиенту.

7. Создайте сценарий:

7.1. Запуск — по [запросу кода](workflow-events.md#zaproshen-kod-avtorizacii):

![Снимок экрана 2023-11-16 в 19.18.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-16%20%D0%B2%2019.18.41.png)

7.2. Если запрос на Flash Call:

![Снимок экрана 2023-12-16 в 15.23.20.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.23.20.png)

7.3. Отправляем вебхук в сервис для Flash Call:

![flashcall-webhook.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/flashcall-webhook.png)

7.4. Проверяем, успешность вызова:

![Снимок экрана 2023-08-03 в 12.59.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2012.59.45.png)

- Если сервис ответит на вызов HTTP-кодом 2xx, событие уйдет в ветку «Да».
- Если в ответе придет код 5xx или 429, вебхук попробует отправиться ещё 3 раза с промежутком в 5 минут. После трех неудачных попыток отправки событие уйдет в ветку «Нет».
- Если вернется ответ с кодами 4xx (кроме 429), либо вебхук не удастся сформировать из-за ошибок в шаблонизаторе, событие также уйдет в ветку «Нет».

Ответ сервиса и ошибки можно проверить в [логах вызова вебхуков](webhook-logs).

7.5. Отправляем SMS, если не удалось успешно вызвать вебхук:

![Снимок экрана 2023-08-03 в 13.04.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.04.26.png)

7.6. В ветке «Нет» от первого условия:

![Снимок экрана 2023-12-16 в 15.49.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.49.59.png)

Проверяем, был ли запрос на SMS:

![Снимок экрана 2023-12-16 в 15.24.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.24.38.png)

В данном случае также отправляем SMS.

Сценарий готов:

![Снимок экрана 2023-12-16 в 15.50.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-16%20%D0%B2%2015.50.19.png)

### Подтверждение контакта

Тот же принцип подтверждения можно использовать для подтверждения контакта клиента:

![Снимок экрана 2023-08-03 в 13.32.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.32.56.png)

![Снимок экрана 2023-08-10 в 12.05.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-10%20%D0%B2%2012.05.45.png)

Особенности:

- для генерации кода не нужно будет дополнительных шагов в операции или сценарии, достаточно указать параметр `${Recipient.MobilePhoneConfirmationCode}`
- для подтверждения используйте операцию с шагом «Подтвердить мобильный телефон на стороне клиента»:

![Снимок экрана 2023-08-03 в 13.30.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2013.30.45.png)

[Авторизация по звонку](https://mindbox.ru/journal/education/flash-call-vs-sms/): как экономить на SMS
