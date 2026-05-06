---
title: Сценарий «Ваши баллы скоро сгорят»
slug: "workflow-bonus-expire"
source_url: "https://help.mindbox.ru/docs/workflow-bonus-expire"
vcs_path: "workflow-bonus-expire.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Уведомления о баллах
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:9d5594b5affbd84ad526985157540a37921ac5f154fb2cacd24904285abd1644"
---

# Сценарий «Ваши баллы скоро сгорят»

**Задача:** отправить коммуникацию о скором сгорании начисленных баллов.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода баллов — [CustomerBalanceChange](parametry-bally-sgoryat.md)

Создаем сценарий:

1. Запуск — по событию [Изменение заданного баланса](workflow-events.md#izmeneniya-zadannogo-balansa):

![Снимок экрана 2024-02-12 в 19.09.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%C2%A0%D0%B2%2019.09.13.png)

2. Ожидание — [за 7 суток](workflow-delay.md#dinamicheskoe) до сгорания баллов:

![Снимок экрана 2022-05-27 в 19.18.08](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-05-27%20%D0%B2%2019.18.08.png)

3. Проверяем, что баллы доступны и не потрачены:

![Снимок экрана 2022-05-27 в 19.19.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-05-27%20%D0%B2%2019.19.09.png)

4. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2022-07-28 в 20.18.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2020.18.08.png)

5. Отправляем письмо:

![Снимок экрана 2022-07-28 в 20.36.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2020.36.15.png)

Что отправить в рассылке

- подборки товаров, которые клиент может оплатить баллами, в зависимости от текущего баланса — собрать их можно с помощью [пересчитываемых](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статических](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегментов (параметр [Products.GetBySegment](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md));
  - дополнительно можно ограничить выборку [по любимому признаку](parameters-products-by-computed-field.md) клиента (цвет, стиль и т.д.);
- [популярные продукты](recommendations-bestsellers.md) или [персональные рекомендации](recommendations-personal.md) (параметр [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md));
- популярные продукты из [любимой категории](parameters-category-from-computed-field.md);
- чаще всего [просматриваемый или покупаемый продукт](parameters-product-from-computed-field.md) и рекомендации к нему.

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

Сценарий готов, можно запускать:

![Снимок экрана 2022-07-28 в 20.25.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2020.25.21.png)

## Дополнительные материалы

- [Подборка механик. Триггерные рассылки для роста конверсии в индустриях красоты и одежды](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-bonus-expire)

[Что такое автоматическая рассылка](https://mindbox.ru/academy/education/chto-takoe-triggernaya-rassylka/) и чем она отличается от массовой
