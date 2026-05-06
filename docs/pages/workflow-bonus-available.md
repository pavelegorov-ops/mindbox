---
title: Сценарий «Ваши баллы доступны»
slug: "workflow-bonus-available"
source_url: "https://help.mindbox.ru/docs/workflow-bonus-available"
vcs_path: "workflow-bonus-available.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Уведомления о баллах
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:b113ea0d71e7bbba51fbbf679c9337a3b5fe34ab7bf2f4a05c9f5d6a76a3a33e"
---

# Сценарий «Ваши баллы доступны»

Баллы [не всегда доступны](balances-blocked-why.md) с момента начисления. Например, они могут быть заблокированы до истечения срока возврата.

**Задача:** сообщить клиенту, что баллы можно использовать.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода баллов — [CustomerBalanceChange](parametry-bally-dostupny.md)

Создаем сценарий:

1. Запуск — по событию [Бонусные баллы стали доступны](workflow-events.md#bonusnye-bally-stali-dostupny-pereshli-iz-zablokirovannyh):

![Снимок экрана 2024-02-12 в 19.11.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2019.11.08.png)

Особенности события

---

- Если баллы начинают действовать сразу после выдачи, сценарий тоже срабатывает.
- Сценарий должен быть запущен и на момент начисления баллов, и на момент их перехода в доступные.

---

2. Ожидание — можно ограничить выход из блока, чтобы не отправлять письмо ночью:

![Снимок экрана 2022-07-28 в 22.28.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2022.28.38.png)

3. Проверяем, что баллы не потрачены:

![Снимок экрана 2022-07-28 в 22.25.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2022.25.01.png)

4. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2022-07-28 в 22.25.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2022.25.29.png)

5. Отправляем письмо:

![Снимок экрана 2022-07-28 в 22.25.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2022.25.46.png)

Что отправить в рассылке

- подборки товаров, которые клиент может оплатить баллами, в зависимости от текущего баланса — собрать их можно с помощью [пересчитываемых](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статических](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегментов (параметр [Products.GetBySegment](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md));
  - дополнительно можно ограничить выборку [по любимому признаку](parameters-products-by-computed-field.md) клиента (цвет, стиль и т.д.);
- [популярные продукты](recommendations-bestsellers.md) или [персональные рекомендации](recommendations-personal.md) (параметр [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md));
- популярные продукты из [любимой категории](parameters-category-from-computed-field.md);
- чаще всего [просматриваемый или покупаемый продукт](parameters-product-from-computed-field.md) и рекомендации к нему.

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

Сценарий готов, можно запускать:

![Снимок экрана 2022-07-28 в 22.29.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-28%20%D0%B2%2022.29.36.png)

## Дополнительные материалы

- [Подборка механик. Триггерные рассылки для роста конверсии в индустриях красоты и одежды](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-bonus-available)

[Что такое автоматическая рассылка](https://mindbox.ru/academy/education/chto-takoe-triggernaya-rassylka/) и чем она отличается от массовой
