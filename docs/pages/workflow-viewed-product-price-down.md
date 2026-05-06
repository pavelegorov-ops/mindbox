---
title: Сценарий «Цена на просмотренный продукт снизилась»
slug: "workflow-viewed-product-price-down"
source_url: "https://help.mindbox.ru/docs/workflow-viewed-product-price-down"
vcs_path: "workflow-viewed-product-price-down.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:6448d2f614a7ddac48db85053b5101a93360df1c8f4646bb0258846812cd95a4"
---

# Сценарий «Цена на просмотренный продукт снизилась»

**Задача**: отправить коммуникацию о снижении цены на просмотренный продукт.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода продукта — [ProductView](parameters-productview-price.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](email-editor-productview.md)

Создаем сценарий:

1. Запуск — по событию [Просмотренный продукт изменился — Цена на продукт снизилась](workflow-events.md#cena-na-produkt-snizilas1):

![Снимок экрана 2024-02-12 в 19.02.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2019.02.58.png)

Особенности события

---

Текущая цена продукта меньше цены, с которой клиент просматривал продукт.

- Работает каждый раз, в том числе:
  - При ещё большем снижении цены.
  - При подорожании и новом снижении стоимости относительно цены в списке.
- Работает на каждый продукт. Если два продукта из списка стали дешевле, сценарий сработает два раза.
- Не реагирует на заполнение цены. Если у продукта ранее не было данных о стоимости, его цена должны вновь поменяться после заполнения, чтобы сценарий запустился.

Для клиентов с заполненной [зоной](regional-yml-import.md):

- если у продукта есть региональные данные по доступности в зоне клиента, сценарий запускается по изменениям продукта в регионе клиента;
- если у продукта не заполнены региональные данные о цене в зоне клиента, сценарий срабатывает по изменениям в основном фиде.

---

2. Ограничьте [количество срабатываний](workflow-limit-per-customer.md) по клиенту, чтобы не отправлять разом несколько рассылок:

![Снимок экрана 2023-11-20 в 11.46.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2011.46.13.png)

3. Ограничиваем выход из блока, чтобы не отправлять письмо ночью:

![Снимок экрана 2023-11-20 в 11.43.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2011.43.29.png)

Если на проекте также настроена отправка рассылок [по снижению цены в списке](workflow-product-lower-price.md), поставьте задержку, чтобы сначала отрабатывала более приоритетная механика по списку.

4. Проверяем, что просмотр произошел недавно и что продукт на данный момент в наличии:

![Снимок экрана 2023-11-20 в 12.42.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2012.42.38.png)

5. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2024-08-05 в 10.14.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-05%20%D0%B2%2010.14.51.png)

6. Отправляем письмо:

![Снимок экрана 2023-11-20 в 11.45.24.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2011.45.24.png)

Что отправить в рассылке

- К продукту можно добавить [сопутствующие товары](recommendations-related.md) или [персональные рекомендации](recommendations-personal.md);
  - параметр [для вывода рекомендаций](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) к товару — ProductListItem.Product.Recommendations.{название алгоритма}, для персональных — Recipient.Recommendations.{название алгоритма} (или через новый конструктор — для [товара](email-editor-product-recommendations.md) и [клиента](new-email-builder-recommendations.md))

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

7. Сценарий готов, можно запускать:

![Снимок экрана 2023-11-20 в 12.48.53 — копия.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2012.48.53%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F.png)

### Интерактивное демо

## Дополнительные материалы

- +40% к доходу триггерных рассылок. 8 тестов интернет-магазина [«МегаФон»](https://mindbox.ru/journal/cases/megafon/?utm_source=help&utm_campaign=workflow-viewed-product-price-down) с ML-рекомендациями: подтвердили эффективность самой механики и рекомендаций с помощью АБ-тестов
- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-viewed-product-price-down): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках
