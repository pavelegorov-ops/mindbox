---
title: Сценарий «Продукт в списке стал доступен»
slug: "workflow-product-available"
source_url: "https://help.mindbox.ru/docs/workflow-product-available"
vcs_path: "workflow-product-available.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:9f211bb00b3658425e60a319202159a0fc93a1d1d594a3d9a9ce07ce128347fb"
---

# Сценарий «Продукт в списке стал доступен»

**Задача:** отправить коммуникацию о том, что товар из [списка продуктов](personal-list.md) снова в наличии.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода продукта — [ProductListItem](parameters-productlistitem-price.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](email-editor-productlistitem.md).

Создаем сценарий:

1. Установите запуск по событию [Продукт в списке продуктов изменился — Продукт вернулся в наличие](workflow-events.md#produkt-vernulsya-v-nalichie):

![Снимок экрана 2024-02-12 в 18.57.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2018.57.42.png)

Особенности события

---

Продукт из списка клиента, который ранее был не в наличии или о наличии которого не было данных, стал доступен.

- Работает каждый раз: при очередном переходе в недоступность и возврате в наличие сценарий вновь запустится.
- Работает на каждый продукт: если два продукта из списка стали доступны, сценарий сработает два раза.

Для клиентов с заполненной [зоной](regional-yml-import.md):

- если у продукта есть региональные данные по доступности в зоне клиента, сценарий запускается по изменениям продукта в регионе клиента;
- если у продукта есть какие-либо региональные данные, но не по зоне клиента, сценарий не запускается;
- если у продукта есть региональные данные по зоне клиента, но информация о доступности в ней не заполнена, сценарий реагирует на изменения в основном фиде;
- если у продукта нет никаких региональных данных, сценарий срабатывает по изменениям в основном фиде.

---

2. Ограничьте [количество срабатываний](workflow-limit-per-customer.md):

![Снимок экрана 2023-11-09 в 12.42.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2012.42.15.png)

3. Ограничиваем выход из блока, чтобы не отправлять письмо ночью:

![Снимок экрана 2023-11-09 в 12.38.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2012.38.22.png)

4. Ставим необходимые проверки на продукт:

![Снимок экрана 2021-10-21 в 14.37.20.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-21%20%D0%B2%2014.37.20.png)

5. И что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-10-21 в 14.38.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-21%20%D0%B2%2014.38.14.png)

6. Отправляем письмо. Можно удалить продукт из списка, чтобы не информировать клиента при повторном возврате данного продукта в наличие:

![Снимок экрана 2021-10-21 в 14.41.57.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-21%20%D0%B2%2014.41.57.png)

Что отправить в рассылке

- К продукту можно добавить [сопутствующие товары](recommendations-related.md) или [персональные рекомендации](recommendations-personal.md);
  - параметр [для вывода рекомендаций](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) к товару — ProductListItem.Product.Recommendations.{название алгоритма}, для персональных — Recipient.Recommendations.{название алгоритма} (или через новый конструктор — для [товара](email-editor-product-recommendations.md) и [клиента](new-email-builder-recommendations.md))

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

6. Ограничиваем [количество срабатываний](workflow-limit-per-customer.md), чтобы не отправлять разом несколько рассылок:

![Снимок экрана 2023-11-09 в 12.42.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2012.42.15.png)

Сценарий готов, можно запускать:

![Снимок экрана 2023-11-09 в 12.51.00.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2012.51.00.png)

### Интерактивное демо

## Дополнительные материалы

- Рассылка «Ждем вместе» от [Present & Simple](https://mindbox.ru/journal/cases/mailings-present-simple/?utm_source=help&utm_campaign=workflow-product-available): +8% к доходу от триггерной механики back in stock
- ×2 выручка от email за год. Как ресейл-платформа [Second Friend Store](https://mindbox.ru/journal/cases/secondfriendstore/?utm_source=help&utm_campaign=workflow-welcome) перестроила автоматические кампании
- Производитель косметики [Aravia](https://mindbox.ru/journal/cases/aravia/?utm_source=help&utm_campaign=workflow-product-available) использует нестандартные CRM-механики. +35,56% заказов в интернет-магазине
- ROI 1696%: [«Сплав»](https://mindbox.ru/journal/cases/splav/?utm_source=help&utm_campaign=workflow-product-available) меняет восприятие бренда с помощью персонализации коммуникаций
- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-product-available): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках

[Как собирать базу email-подписчиков в онлайне](https://mindbox.ru/academy/education/kak-sobirat-bazu-podpischikov/) — 10 реальных механик
