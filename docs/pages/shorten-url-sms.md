---
title: Как сократить ссылки в SMS и дополнительных каналах для сбора статистики
slug: "shorten-url-sms"
source_url: "https://help.mindbox.ru/docs/shorten-url-sms"
vcs_path: "shorten-url-sms.md"
toc_path:
  - Рассылки
  - "SMS-рассылки"
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:587990075c00952fb5429369101e19e495468974eb15ad33f912e7e4b4989323"
deprecation_hint:
  - устаревш
---

# Как сократить ссылки в SMS и дополнительных каналах для сбора статистики

## Зачем сокращать ссылки

1. Сокращение количества символов: меньше оплачиваемых частей SMS и более аккуратный вид сообщения.
2. Сбор статистики по кликам из рассылок.

## Сокращатель на домене Mindbox

### Преимущества

- Ссылка сокращается до 16 знаков для SMS и до 24 знаков для каналов [модуля «Уведомления и мессенджеры»](notifications-and-messangers.md).
- Для отслеживания не нужна установка трекера — вся настройка происходит в Mindbox.
- Можно сокращать ссылки на внешние сайты (например, на опрос в Google Forms).

Важно

При истечении *срока жизни ссылки*, она может быть выдана повторно для другой ссылки на любом проекте.

### Где можно использовать

- SMS
- Любые каналы модуля «Уведомления и мессенджеры». Исключение — каналы, настроенные через FastTrack (аналитика приходит со стороны провайдера).

Сокращение ссылки в разных каналах

**Оригинальная ссылка:** `https://example.com/promo/12345/?utm_source=mindbox&utm_medium=sms&utm_campaign=promo08.03.2023`

- **SMS:** `mbxg.ru/=6jOi25m`
- **Каналы «Уведомления и мессенджеры»:** `https://mbxg.ru/=6jOi25m`

### Как подключить

- На новых проектах сокращатель на домене Mindbox подключен автоматически.
- Если у вас подключен старый сокращатель, напишите менеджеру вашего проекта или [в техническую поддержку](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support.md).

Обратите внимание

Если на вашем проекте используется несколько брендов, то подключение нового сокращателя переведет на него все бренды.

### Что произойдет при клике по ссылке

Клиент переходит по сокращенной ссылке. К ней будет добавлен:

- тикет авторизации `UniversalAuthenticationCustomizableTimeTicket` для определения клиента с максимальным сроком жизни 3 месяца.

  По истечении 3 месяцев тикет перестанет работать для авторизации, но ссылка продолжит собирать клики до истечения своего *срока*.
- `mindbox-click-id` для выдачи клиенту клика.

Ссылка из рассмотренного примера примет вид:

`https://example.com/promo/12345/?mindbox-click-id=8caf42da-1526-468b-8f11-dba452fd1844&utm_source=mindbox&utm_medium=sms&utm_campaign=promo08.03.2023&direct-crm-ticket=PGRpcmVjdENybVRpY2tldCB0eXBlPSJFbWFpbEF1dGhlbnRpY2F0aW9uVGlja2V0IiBjdXN0b21lcklkPSIyNzE2NDk1IiBwYXNzd29yZD0iIiB0ZW1wUGFzc3dvcmQ9IiIgZW1haWw9IkExOEMyODU1NjMyODc1NDQwNEY3QjBFNjkyMDhFNTM2RjAyQjlEOTgiIHNpZ25hdHVyZT0iM0E0RTQ3RjUzODNDMkMxNTgzQzk2OUQ5MTFEOURCREFBOTc2NjkxQTgzMzdDNzVFMDk1NUY0OTM3QTU1RkVBMTE5NzA0NUI3QkJFQjg5RDRGNTAxQzdDQ0E5RTM3NjYzQTdDREU4N0JBNzYwMkYxNEVEQTg3M0M5RjJBMjI4NDciIC8`

## Старый сокращатель (устаревшее)

Особенности и настройка

### Ограничения

1. Не сокращайте ссылки в SMS, которые ведут на сайты, на которых не установлен трекер Mindbox, так как в таком случае не получится открыть сокращенную ссылку. Например, не нужно сокращать ссылку, ведущую на стороннюю форму опроса в Google Forms.
2. Убедитесь, что ссылка не сокращалась в сторонних сервисах и при переходе на ваш сайт нет дополнительных редиректов. Это помешает работе сокращенных ссылок, так как они обрабатываются внутренним редиректом трекера Mindbox.
3. Если вы сократите ссылку с непопулярным доменом первого уровня, то в зависимости от ОС мобильного устройства, ссылка может быть некликабельной на устройстве получателя, так как при сокращении для экономии символов убирается протокол http(s).

### Как сократить ссылки

1. На целевом сайте создайте пустую страницу по адресу http(s)://yourdomain.com**/s** и убедитесь, что на этой странице установлен [трекер](https://developers.mindbox.ru/docs/%D1%82%D1%80%D0%B5%D0%BA%D0%B5%D1%80) Mindbox.

На странице может быть содержимое, но всё же рекомендуем оставлять ее пустой, чтобы редирект происходил максимально быстро. Дополнительно на сайте ничего настраивать не надо.

При использовании ссылки на поддомен, на нем также должна быть страница `.../s` с трекером.

Например, чтобы отслеживать клики по ссылке вида `https://blog.yourdomain.com/articles/shorten-url-sms`, должна быть создана страница с трекером Mindbox по адресу `https://blog.yourdomain.com/s`

### Какую ссылку получит клиент

Путь ссылки на целевом сайте преобразуется в уникальный в рамках клиентов 15-ти символьный код.  
Целиком ссылка принимает вид `yourdomain.com/s?s={15-ти символьный код}`

Например, ссылка `https://yourdomain.com/promo/12345/?utm_source=mindbox&utm_medium=sms&utm_campaign=promo08.03.2023` сокращается до вида `yourdomain.com/s?s=5peQW0cg4BGjkMT`

### Что произойдет при клике по ссылке

Перед открытием целевой страницы пользователь на несколько секунд увидит страницу `https://yourdomain.com/s`.

Затем его перенаправит на целевую страницу.  
При этом к ней будут добавлены:

- тикет авторизации (PermanentAuthenticationTicket) для определения клиента,
- mindbox-click-id для выдачи клиенту клика.

Ссылка из рассмотренного примера примет вид:

`https://yourdomain.com/promo/12345/?mindbox-click-id=8caf42da-1526-468b-8f11-dba452fd1844&utm_source=mindbox&utm_medium=sms&utm_campaign=promo08.03.2023&direct-crm-ticket=PGRpcmVjdENybVRpY2tldCB0eXBlPSJFbWFpbEF1dGhlbnRpY2F0aW9uVGlja2V0IiBjdXN0b21lcklkPSIyNzE2NDk1IiBwYXNzd29yZD0iIiB0ZW1wUGFzc3dvcmQ9IiIgZW1haWw9IkExOEMyODU1NjMyODc1NDQwNEY3QjBFNjkyMDhFNTM2RjAyQjlEOTgiIHNpZ25hdHVyZT0iM0E0RTQ3RjUzODNDMkMxNTgzQzk2OUQ5MTFEOURCREFBOTc2NjkxQTgzMzdDNzVFMDk1NUY0OTM3QTU1RkVBMTE5NzA0NUI3QkJFQjg5RDRGNTAxQzdDQ0E5RTM3NjYzQTdDREU4N0JBNzYwMkYxNEVEQTg3M0M5RjJBMjI4NDciIC8`

## Как сократить ссылку в рассылке

1. Создайте рассылку в нужном канале ([SMS](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-sms-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md) или [в дополнительном канале](notifications-and-messangers.md)).
2. В шаблоне SMS-рассылки укажите ссылку для перехода на целевую страницу сайта.

   Например:

   ```
   https://example.com/promo/12345/?utm_source=mindbox&utm_medium=sms&utm_campaign=promo08.03.2023
   ```

   Обязательно используйте префикс `http://` или `https://`, иначе ссылка не будет сокращена.

   Если ОС устройства не распознает домен и ссылка некликабельна, то вы можете добавить протокол в ссылку с помощью параметра шаблонизатора таким образом:

   ```
   @{set a="https://"} ${a}https://YourSiteDomainName.market/
   ```
3. В блоке «Сокращение ссылок» рассылки включите «Отслеживание кликов»:

   ![mass-sms-shorten.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-sms-shorten.png)

Сокращение происходит непосредственно при формировании сообщения клиенту, поэтому ссылка в шаблоне останется прежней.

## Как тестировать

В предпросмотре можно посмотреть, как внешне будет выглядит сообщение клиенту со сформированной ссылкой:

![sms-url-shorten-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/sms-url-shorten-test.png)

Для точного определения количества частей в SMS нужно отправить тестовое сообщение.

Важно

В предпросмотре и при формировании сообщений в тестовом режиме рассылки редирект и отслеживание клика не работает. Вместо этого ссылка ведет на пустую страницу или выдает ошибку 404.

Чтобы протестировать корректность редиректа, нужно отправить тестовое сообщение. Отслеживание перехода и выдачу действия клика можно проверить только при отправке боевой SMS-рассылки на номер.

## Ссылки с параметрами

Ссылки можно персонализировать под клиента с помощью [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md).

Например, подставить в ссылку трек-номер заказа:

```
https://yourdomain.com/${Order.CustomField.TrackingURL}
```

**Тикеты**

К любой сокращенной ссылке автоматически добавляется тикет аутентификации для определения клиента:

- Сокращатель на домене Mindbox: `UniversalAuthenticationCustomizableTimeTicket`
- Старый сокращатель: `PermanentAuthenticationTicket`

Можно использовать и другие [тикеты авторизации клиента](%D1%82%D0%B8%D0%BA%D0%B5%D1%82.md), которые представлены на странице *https://projectname.mindbox.ru/mailing-parameters-help/Ticket* (вместо *projectname* — название вашего проекта), прописав нужный вручную. PermanentAuthenticationTicket/UniversalAuthenticationCustomizableTimeTicket в таком случае добавлен не будет.

**Пример:**

```
https://yourdomain.com/?ticket=${Ticket.MobilePhoneAuthenticationHexTicket}
```

Чтобы авторизация по тикету работала, на вашем сайте необходимо реализовать его обработку силами разработчиков.

[SMS-рассылки](https://mindbox.ru/academy/education/SMS-rassylki-s-vysokim-open-rate/): как настроить и запустить канал с самым высоким open rate

Срок жизни ссылки составляет 5 лет.
