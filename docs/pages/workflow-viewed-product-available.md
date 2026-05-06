---
title: Сценарий «Просмотренный продукт снова в наличии»
slug: "workflow-viewed-product-available"
source_url: "https://help.mindbox.ru/docs/workflow-viewed-product-available"
vcs_path: "workflow-viewed-product-available.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:5c6938c6315141fc608e915701de8ffaf754efb244764eae26c41e12b2fe6e6e"
---

# Сценарий «Просмотренный продукт снова в наличии»

**Задача**: отправить коммуникацию о возврате просмотренного продукта в наличие.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода продукта — [ProductView](parameters-productview-available.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](email-editor-productview.md).

Создаем сценарий:

1. Установите запуск — по событию [Просмотренный продукт изменился — Продукт вернулся в наличие](workflow-events.md#produkt-vernulsya-v-nalichie1) и ограничьте [количество срабатываний](workflow-limit-per-customer.md) по клиенту, чтобы не отправлять разом несколько рассылок:

![Снимок экрана 2024-02-12 в 19.04.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2019.04.27.png)

Особенности события

---

Просмотренный клиентом продукт, который ранее был не в наличии или о наличии которого не было данных, стал доступен.

- Работает каждый раз: при очередном переходе в недоступность и возврате в наличие сценарий вновь запустится.
- Работает на каждый продукт: если два продукта из списка стали доступны, сценарий сработает два раза.

Для клиентов с заполненной [зоной](regional-yml-import.md):

- если у продукта есть региональные данные по доступности в зоне клиента, сценарий запускается по изменениям продукта в регионе клиента;
- если у продукта не заполнены региональные данные о наличии в зоне клиента, сценарий срабатывает по изменениям в основном фиде.

---

2. Ограничиваем выход из блока, чтобы не отправлять письмо ночью:

![Снимок%20экрана%202023-11-21%20в%2016.11.20](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-21%20%D0%B2%2016.11.20.png)

Если на проекте также настроена отправка рассылок [на доступность продукта в списке](workflow-product-available.md), поставьте задержку, чтобы сначала отрабатывала более приоритетная механика по списку.

3. Проверяем, что просмотр произошел недавно и что продукт на данный момент в наличии:

![Снимок%20экрана%202023-11-21%20в%2016.13.20](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-21%20%D0%B2%2016.13.20.png)

4. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2024-08-05 в 10.13.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-05%20%D0%B2%2010.13.56.png)

5. Отправляем письмо:

![Снимок%20экрана%202023-11-21%20в%2016.17.09](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-21%20%D0%B2%2016.17.09.png)

Что отправить в рассылке

- К продукту можно добавить [сопутствующие товары](recommendations-related.md) или [персональные рекомендации](recommendations-personal.md);
  - параметр [для вывода рекомендаций](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) к товару — ProductListItem.Product.Recommendations.{название алгоритма}, для персональных — Recipient.Recommendations.{название алгоритма} (или через новый конструктор — для [товара](email-editor-product-recommendations.md) и [клиента](new-email-builder-recommendations.md))

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

6. Сценарий готов, можно запускать:

![Снимок экрана 2023-11-21 в 16.18.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-21%20%D0%B2%2016.18.42%281%29.png)

### Интерактивное демо

## Дополнительные материалы

- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-viewed-product-available): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках
