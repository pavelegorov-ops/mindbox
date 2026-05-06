---
title: Сценарий для подтверждения подписки
slug: "workflow-welcome-double-opt-in"
source_url: "https://help.mindbox.ru/docs/workflow-welcome-double-opt-in"
vcs_path: "workflow-welcome-double-opt-in.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Приветственные кампании
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:fadcdb83388c3829270fddc7aab8658213e868d4c34cdc6217f655595122d8f6"
---

# Сценарий для подтверждения подписки

**Задача:** после того, как клиент оставил свой email, отправить рассылку для [подтверждения подписки](doi-turn-on.md); при необходимости напомнить через сутки.  
После подтверждения отправить welcome-письмо.

Для решения задачи настроим [сценарии](what-is-workflow.md).

Перед созданием сценариев:

- Добавьте автоматические [email-рассылки](email-trigger.md) для запроса подтверждения и напоминания (с профилем opt-in) и для письма после подписки (со стандартным профилем):
  - Чтобы клик подтверждал подписку клиента, добавьте соответствующую [настройку для ссылок](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BF%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BD%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83.md) (обратите внимание, что рассылки должны быть с профилем opt-in).

В механике подразумевается два запускающих [события](workflow-events.md) — появление клиента и подтверждение подписки. Для каждого из них нужно создать свой сценарий.

## Сценарий для запроса подтверждения подписки

1. Запуск — по [изменению подписки](workflow-events.md#izmenilsya-status-podpiski):

![workflow-double-opt-in-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-double-opt-in-event.png)

Особенности события

---

Запускается, когда у клиента появляется выбранный статус подписки в канале или тематике.

Что входит:- статус стал нужным, в том числе [неявным](subscriptions.md#yavnaya-i-neyavnaya-podpiski);
- статус сразу стал нужным;
- клиент появился сразу с нужным статусом;
- статус повторно стал нужным.

Что не входит:- неявный нужный статус стал таким же, но явным;
- после объединения основной клиент получил нужный статус.

---

Другие возможные события в зависимости от бизнес-задачи:

- [Выдано действие](workflow-events.md#vydano-dejstvie) с шаблонами из конкретных [операций](steps-create-client.md);
- [Клиент зарегистрировался](workflow-events.md#klient-zaregistrirovalsya) — для вызова по любым операциям с регистрацией;
- [Новый клиент](workflow-events.md#novyj-klient) — для отработки по новым клиентам из любых источников.

2. Ограничиваем [срабатывание по клиенту](workflow-limit-per-customer.md) в стартовом блоке одним разом:

![запрос7.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%817.png)

3. Проверяем наличие и валидность контакта:

![запрос2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%812.png)  
*В данном случае не проверяем подписку, так как она задается в событии. При использовании других событий нужно будет добавить фильтр «Подписка — Требует подтверждения в канале Email».*

4. Отправляем рассылку для подтверждения почты:

![запрос3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%813.png)

5. Ждем сутки:

![запрос4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%814.png)

6. Если подписку всё ещё не подтвердили:

![запрос5.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%815.png)

7. Отправляем напоминание:

![запрос6.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%816.png)

Сценарий готов, можно запускать:

![запрос8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%818.png)

## Welcome-сценарий после подтверждения подписки

1. При подтверждении подписки в письме [клиенту выдается](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BF%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BD%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83.md#chto-proishodit-s-klientom) автоматически сгенерированное действие «Подписка клиента на канал» (или «Подписка клиента на тематику» при использовании ссылки по тематике). Запускаем сценарий по этому [действию](workflow-events.md#vydano-dejstvie) и ограничиваем срабатывание по клиенту одним разом:

![велком1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D0%B5%D0%BB%D0%BA%D0%BE%D0%BC1.png)

2. Проверяем, что был клик в рассылке и что клиент подписан и с валидным контактом:

![Снимок экрана 2024-08-05 в 09.42.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-05%20%D0%B2%2009.42.29.png)*При наличии одного сценария с подтверждением можно не ставить дополнительные проверки, но такой подход может пригодиться при использовании нескольких кампаний, в том числе для подписки на разные тематики — ведь в таком случае выдается одинаковый шаблон действия.*

3. Отправляем welcome-письмо:

![велком3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D0%B5%D0%BB%D0%BA%D0%BE%D0%BC3.png)

Что отправить в рассылке

- Чтобы подсказать пользователям, с чего начать, можно порекомендовать им в welcome-письме [популярные продукты](recommendations-bestsellers.md#populyarnye-produkty) или, при наличии, [просмотренные ими продукты](recommendation-algorithms.md#poslednie-prosmotrennye-produkty);
- Для дополнительной мотивации можно выдавать [промокоды](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md) или начислять [баллы](balances-create.md) за подписку;
- [Параметры](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) рассылки:
  - для вывода рекомендаций — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) (или через [новый конструктор](new-email-builder-recommendations.md));
  - для вывода промокода — [Recipient.LastReceivedPromoCode.WithType{название пула}.Value](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md) (или через [новый конструктор](new-builder-personalize.md));
  - для вывода даты сгорания баллов — [функцией AddDays](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85?highlight=AddDays.md) добавьте к дате отправке рассылки (Message.SendingDateTime) нужное количество дней.

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

Сценарий готов, можно запускать:

![велком5.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D0%B5%D0%BB%D0%BA%D0%BE%D0%BC5.png)

## Дополнительные материалы

- +3% к выручке за год. Мобильные пуши [Делимобиля](https://mindbox.ru/journal/cases/delimobil/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) ведут к 10-й поездке, пересаживают на комфорт-класс и возвращают отток
- 40% → 65% — конверсия в первую покупку. Как [«КуулКлевер»](https://mindbox.ru/journal/cases/coolclever/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) превращает лида в покупателя
- + 10 п. п. к retention rate рассылок за счет работы с базой: как в [Бизнес-секретах](https://mindbox.ru/journal/cases/secrets-t-bank/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) удерживают и реактивируют читателей
- Ставки, лоты, 2 пуша! Интернет-аукцион [Auction.ru](https://mindbox.ru/journal/cases/auction/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) онбордит новых клиентов в email и приложении: 15% → 21% доля новичков в GMV
- [Подборка механик](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in). Триггерные рассылки для роста конверсии в индустриях красоты и одежды
- Формы на сайте и welcome-письма магазина [«Ведьмино счастье»](https://mindbox.ru/journal/cases/vedmino-schaste/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in): 6700 подписчиков и 500 заказов от новых клиентов за 5 месяцев
- ИТ-компания [Jivo](https://mindbox.ru/journal/cases/jivo-uvelichila-konversiyu/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) на 35,5% увеличила конверсию welcome-цепочки в покупку платной версии
- 8,8% — доля выручки email-канала. [imkosmetik](https://mindbox.ru/journal/cases/imkosmetik/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) запускает автоматические рассылки с персональными рекомендациями
- 14,6% — доля GMV от CRM-коммуникаций. Как mobile first маркетплейс [KazanExpress](https://mindbox.ru/journal/cases/kazan-express/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) развивает мобильные пуши
- 0,8% → 5% — доля CRM в общем обороте [«Купибилета»](https://mindbox.ru/journal/cases/kupibilet-crm/) за год. Секрет: много тестов, новые триггеры и шутки про джиннов
- [«Магнит Доставка»](https://mindbox.ru/journal/cases/magnit-dostavka/?utm_source=help&utm_campaign=workflow-welcome-double-opt-in) получает 20% выручки из CRM-канала: мобильные пуши, каскадные сценарии, AB-тесты и NPS-опросы
