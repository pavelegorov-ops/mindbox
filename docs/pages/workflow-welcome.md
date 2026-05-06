---
title: "Welcome-сценарий"
slug: "workflow-welcome"
source_url: "https://help.mindbox.ru/docs/workflow-welcome"
vcs_path: "workflow-welcome.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Приветственные кампании
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:a328abd344dfe5e0a253a7e0e11c5d7c9de82c253153b508140a0e927e6c0593"
---

# Welcome-сценарий

**Задача:** отправить приветственное письмо. Если клиент не совершает заказ за неделю, отправляем рассылку с промокодом.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматические рассылки в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).

Создаем сценарий:

1. Установите запуск по событию ["Новый клиент"](workflow-events.md#novyj-klient) и настройте [количество срабатываний](workflow-limit-per-customer.md) на клиенте одним разом:

![workflow-welcome-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-welcome-event.png)

Особенности события

---

Новый клиент добавлен в базу любым способом: вручную, по API, импортом по файлу. Если появляется новый Mindbox ID — событие срабатывает.

- Даже если новый клиент сразу объединится с карточкой существующего клиента, создание новой карточки произошло. Поэтому сценарий запустится. Чтобы избежать повторного срабатывания в таких случаях, ограничьте срабатывание сценария одним разом к клиенту.
- Обратите внимание, что не всегда импорт создает нового клиента. Если клиент есть в базе, он будет просто отредактирован. В таком случае события попадания в базу не произойдет.

---

Другие возможные события в зависимости от бизнес-задачи:

- [Выдано действие](workflow-events.md#vydano-dejstvie) с шаблонами из конкретных [операций](steps-create-client.md),
- [Клиент зарегистрировался](workflow-events.md#klient-zaregistrirovalsya) — для вызова по любым операциям с регистрацией.

2. Проверяем валидность контакта и наличие подписки [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2022-02-01 в 22.54.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-02-01%20%D0%B2%2022.54.21.png)

Чтобы не срабатывать по клиентам, которые были в базе до создания сценария, нужна дополнительная проверка.  
Например, по времени [первой регистрации](filter-clients-register.md):

![Снимок экрана 2024-09-09 в 10.01.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.01.22.png)

3. Отправляем welcome-рассылку:

![Снимок экрана 2021-09-22 в 18.38.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-22%20%D0%B2%2018.38.13.png)

Что отправить в рассылке

- Чтобы подсказать пользователям, с чего начать, можно порекомендовать им [популярные продукты](recommendations-bestsellers.md#populyarnye-produkty) или, при наличии, [просмотренные ими продукты](recommendation-algorithms.md#poslednie-prosmotrennye-produkty).
  - [параметры](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода рекомендаций — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md)

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

4. Ждем неделю:

![workflow-welcome-wait-week.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-welcome-wait-week.png)

5. Если у клиента всё ещё нет заказов:

![Снимок экрана 2021-10-20 в 17.04.00.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-20%20%D0%B2%2017.04.00.png)

6. Шлем рассылку-напоминание:

![Снимок экрана 2021-10-20 в 17.05.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-20%20%D0%B2%2017.05.51.png)

Что отправить в рассылке

- Можно отправить рекомендации с [популярными продуктами](recommendations-bestsellers.md#populyarnye-produkty).
- Для дополнительной мотивации можно выдавать [промокоды](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md) или начислять [баллы](balances-create.md);
- [Параметры](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) рассылки:
  - для вывода рекомендаций — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) (или через [новый конструктор](new-email-builder-recommendations.md));
  - для вывода промокода — [Recipient.LastReceivedPromoCode.WithType{название пула}.Value](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md) (или через [новый конструктор](new-builder-personalize.md));
  - для вывода даты сгорания баллов — [функцией AddDays](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85?highlight=AddDays.md) добавьте к дате отправке рассылки (Message.SendingDateTime) нужное количество дней.

Сценарий готов. Можно запускать:

![workflow-welcome-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-welcome-start.png)

## Дополнительные материалы

- ×2 выручка от email за год. Как ресейл-платформа [Second Friend Store](https://mindbox.ru/journal/cases/secondfriendstore/?utm_source=help&utm_campaign=workflow-welcome) перестроила автоматические кампании
- 7,92% — инкрементальный прирост из CRM-канала. Как в [«Много лосося»](https://mindbox.ru/journal/cases/mnogolososya/?utm_source=help&utm_campaign=workflow-welcome) сегментируют базу, выбирают офферы и автоматизируют рассылки
- +3% к выручке за год. Мобильные пуши [Делимобиля](https://mindbox.ru/journal/cases/delimobil/?utm_source=help&utm_campaign=workflow-welcome) ведут к 10-й поездке, пересаживают на комфорт-класс и возвращают отток
- 40% → 65% — конверсия в первую покупку. Как [«КуулКлевер»](https://mindbox.ru/journal/cases/coolclever/?utm_source=help&utm_campaign=workflow-welcome) превращает лида в покупателя
- + 10 п. п. к retention rate рассылок за счет работы с базой: как в [Бизнес-секретах](https://mindbox.ru/journal/cases/secrets-t-bank/?utm_source=help&utm_campaign=workflow-welcome) удерживают и реактивируют читателей
- Ставки, лоты, 2 пуша! Интернет-аукцион [Auction.ru](https://mindbox.ru/journal/cases/auction/?utm_source=help&utm_campaign=workflow-welcome) онбордит новых клиентов в email и приложении: 15% → 21% доля новичков в GMV
- [Подборка механик](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-welcome). Триггерные рассылки для роста конверсии в индустриях красоты и одежды
- Формы на сайте и welcome-письма магазина [«Ведьмино счастье»](https://mindbox.ru/journal/cases/vedmino-schaste/?utm_source=help&utm_campaign=workflow-welcome): 6700 подписчиков и 500 заказов от новых клиентов за 5 месяцев
- ИТ-компания [Jivo](https://mindbox.ru/journal/cases/jivo-uvelichila-konversiyu/?utm_source=help&utm_campaign=workflow-welcome) на 35,5% увеличила конверсию welcome-цепочки в покупку платной версии
- 8,8% — доля выручки email-канала. [imkosmetik](https://mindbox.ru/journal/cases/imkosmetik/?utm_source=help&utm_campaign=workflow-welcome) запускает автоматические рассылки с персональными рекомендациями
- 14,6% — доля GMV от CRM-коммуникаций. Как mobile first маркетплейс [KazanExpress](https://mindbox.ru/journal/cases/kazan-express/?utm_source=help&utm_campaign=workflow-welcome) развивает мобильные пуши
- 0,8% → 5% — доля CRM в общем обороте [«Купибилета»](https://mindbox.ru/journal/cases/kupibilet-crm/?utm_source=help&utm_campaign=workflow-welcome) за год. Секрет: много тестов, новые триггеры и шутки про джиннов
- [«Магнит Доставка»](https://mindbox.ru/journal/cases/magnit-dostavka/?utm_source=help&utm_campaign=workflow-welcome) получает 20% выручки из CRM-канала: мобильные пуши, каскадные сценарии, AB-тесты и NPS-опросы

[Как собирать базу email-подписчиков в онлайне](https://mindbox.ru/academy/education/kak-sobirat-bazu-podpischikov/) — 10 реальных механик
