---
title: Сценарий «Цена на продукт в списке снизилась»
slug: "workflow-product-lower-price"
source_url: "https://help.mindbox.ru/docs/workflow-product-lower-price"
vcs_path: "workflow-product-lower-price.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:48fe8014000c0ce4f2adee079be6888a628a1441c547883e6948ac8cf94252c0"
---

# Сценарий «Цена на продукт в списке снизилась»

**Задача:** отправить коммуникацию о снижении цены на продукт в [списке клиента](personal-list.md).

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода продукта — [ProductListItem](parameters-productlistitem-price.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](email-editor-productlistitem.md).

Создаем сценарий:

1. Запуск — по событию [Продукт в списке продуктов изменился — Цена на продукт снизилась](workflow-events.md#cena-na-produkt-snizilas):

![Снимок экрана 2024-02-12 в 18.55.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2018.55.35.png)

Особенности события

---

Текущая цена продукта меньше цены, с которой клиент добавлял его в список.

- Работает каждый раз, в том числе:
  - При ещё большем снижении цены.
  - При подорожании и новом снижении стоимости относительно цены в списке.
- Работает на каждый продукт. Если два продукта из списка стали дешевле, сценарий сработает два раза.
- Не реагирует на заполнение цены. Если у продукта ранее не было данных о стоимости, его цена должны вновь поменяться после заполнения, чтобы сценарий запустился.

Для клиентов с заполненной [зоной](regional-yml-import.md):

- если у продукта есть региональные данные по цене в зоне клиента, сценарий запускается по изменениям продукта в регионе клиента;
- если у продукта есть какие-либо региональные данные, но не по зоне клиента, сценарий не запускается;
- если у продукта есть региональные данные по зоне клиента, но информация о цене в ней не заполнена, сценарий реагирует на изменения в основном фиде;
- если у продукта нет никаких региональных данных, сценарий срабатывает по изменениям в основном фиде.

---

2. В стартовом блоке ограничиваем [количество срабатываний](workflow-limit-per-customer.md), чтобы не отправлять разом несколько рассылок:

![Снимок экрана 2023-11-09 в 13.08.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2013.08.58.png)

3. Ожидание не ставим, но ограничиваем выход из блока, чтобы не отправлять письмо ночью:

![Снимок экрана 2023-11-09 в 13.07.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2013.07.19.png)

4. Проверяем, что продукт в наличии:

![Снимок экрана 2021-09-29 в 18.52.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.52.11.png)

5. Проверяем валидность контакта и наличие подписки [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-09-29 в 18.53.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.53.02.png)

6. Отправляем письмо:

![Снимок экрана 2021-09-29 в 18.53.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.53.52.png)

Что отправить в рассылке

- К продукту можно добавить [сопутствующие товары](recommendations-related.md) или [персональные рекомендации](recommendations-personal.md);
  - параметр [для вывода рекомендаций](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) к товару — ProductListItem.Product.Recommendations.{название алгоритма}, для персональных — Recipient.Recommendations.{название алгоритма} (или через новый конструктор — для [товара](email-editor-product-recommendations.md) и [клиента](new-email-builder-recommendations.md))

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

7. Сценарий готов, можно запускать:

![Снимок экрана 2023-11-09 в 13.09.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2013.09.10.png)

### Интерактивное демо

## Дополнительные материалы

- Мобильные пуши приносят [«ВсеИнструменты.ру»](https://mindbox.ru/journal/cases/vseinstrumenty-push/?utm_source=help&utm_campaign=workflow-product-lower-price) более 150 млн рублей выручки в месяц: механики по снижению цены в избранном и в корзине — одни из самых эффективных с точки зрения выручки.
- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-product-lower-price): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках
- 27% выручки — от рассылок. Как в [Lassie](https://mindbox.ru/journal/cases/lassie/?utm_source=help&utm_campaign=workflow-product-lower-price) выстроили CRM-маркетинг за 1,5 года

[Механики персонализации](https://mindbox.ru/academy/mechanics/unikalnye-mehaniki-personalizaczii-sajta/) — используйте идеи механик персонализации сайта наших клиентов из разных индустрий.
