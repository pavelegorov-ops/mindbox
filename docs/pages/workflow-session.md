---
title: Сценарий «Брошенная сессия»
slug: "workflow-session"
source_url: "https://help.mindbox.ru/docs/workflow-session"
vcs_path: "workflow-session.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:30326727c4c8e378898937be6595da64fcebbb2c104f7081e6e5aefc3417ee7e"
---

# Сценарий «Брошенная сессия»

**Задача:** отправить коммуникацию после окончания сессии по брошенной корзине / просмотру продукта / просмотру категории в указанном приоритете.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматические рассылки в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md);
  - Настройте вывод продуктов с помощью [параметров](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md):
    - для брошенной корзины — [Session.GetAddedToListProducts()](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0.md)
    - для брошенной категории — [Session.ProductCategoryViews](parameters-session-productcategoryviews.md)
    - для брошенного просмотра — [Session.ProductViews](parameters-session-productviews.md)
  - Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — инструкции для [брошенной корзины](email-editor-added-products-in-session.md)/[продукта](new-email-builder-viewed-products-in-session.md)/[категории](email-editor-products-from-viewed-categories-in-session.md)

Создаем сценарий:

1. Указываем запуск по событию [«Клиент покинул сайт или приложение»](workflow-events.md#klient-pokinul-sajt-ili-prilozhenie) и ограничиваем [количество срабатываний](workflow-limit-per-customer.md) раз в 3 дня:

![workflow-session-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-settings.png)

Особенности события

---

Сессией считается непрерывная цепочка действий на сайте ([с трекером Mindbox](https://developers.mindbox.ru/docs/%D1%82%D1%80%D0%B5%D0%BA%D0%B5%D1%80)) или в приложении ([c SDK Mindbox](https://developers.mindbox.ru/docs/mindbox-sdk)). Она автоматически закрывается через полчаса после бездействия клиента.

---

Настройки события

---

**В сессии были действия**

Доступные действия:

- Добавления в список продуктов
- Просмотр продукта
- Просмотр категории продукта

Если выбрано **одно или несколько типов действий**, сценарий будет срабатывать только на те сессии клиентов, в которых были эти действия.

Если не выбрано **ни одно из действий**, то сценарий будет учитывать все сессии.

**Заказы в сессии**  
Позволяет ограничить сессии по наличию или отсутствию в них оформленных заказов.

---

1. Ждем полчаса:

![workflow-session-delay.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-delay.png)

Также ограничиваем выход из блока, чтобы не отправлять письма ночью.

3. Проверяем, что у клиента не было заказов и отправок рассылок последние сутки, есть подписка и валидный контакт [в канале рассылки](workflow-check-subscription.md):

![workflow-session-client-conditions.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-client-conditions.png)

4. Фильтруем по сессии — есть добавление продукта в корзину, и продукт ещё в списке:

![workflow-session-cart.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-cart.png)

5. В таком случае отправляем брошенную корзину:

![workflow-session-cart-send.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-cart-send.png)

Что отправить в рассылке

- К перечислению продуктов из корзины можно добавить рекомендации:
  - [сопутствующие товары к списку](recommendations-related.md) — чтобы помочь собрать заказ;
  - [похожие товары к списку](recommendations-similar.md) — аналоги, которые могут больше подойти;
- [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода рекомендаций к списку — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md). Или используйте новый конструктор — [инструкция](new-email-builder-recommendations.md).

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

6. Если добавления в корзину нет:

![workflow-session-cart-no.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-cart-no.png)

7. Но при этом есть просмотр продукта:

![workflow-session-product.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-product.png)

8. Отправляем брошенный просмотр продукта:

![workflow-session-productview-send.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-productview-send.png)

Что отправить в рассылке

- Можно добавить рекомендации — [похожие продукты на просмотренные в последней сессии](recommendations-similar.md) — аналоги, которые могут больше подойти;
  - Параметр — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) (или через [новый конструктор](new-email-builder-recommendations.md))

9. Если нет просмотра продукта:

![workflow-session-product-no.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-product-no.png)

10. Но есть просмотр категории:

![workflow-session-product-category.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-product-category.png)

11. Отправляем брошенный просмотр категории:

![workflow-session-productcategory-send.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-productcategory-send.png)

Что отправить в рассылке

- Можно добавить рекомендации — [популярные продукты в просмотренных категориях в последней сессии](recommendations-bestsellers.md);
  - Параметр — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) (или через [новый конструктор](new-email-builder-recommendations.md)).

12. Сценарий готов. Можно запускать:

![workflow-session-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-session-result.png)

## Дополнительные материалы

- Триггерная рассылка [«брошенная корзина»](https://mindbox.ru/journal/education/triggernaya-rassylka-broshennaya-korzina-instrukciya-po-zapusku-dlya-marketologa/?utm_source=help&utm_campaign=workflow-session): инструкция по запуску для маркетолога
- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-session): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках
- [Опросы клиентов](https://mindbox.ru/journal/education/oprosy-klientov/?utm_source=help&utm_campaign=workflow-session): для чего они нужны и как использовать полученные данные. 11 примеров с рынка
- ×2 выручка от email за год. Как ресейл-платформа [Second Friend Store](https://mindbox.ru/journal/cases/secondfriendstore/?utm_source=help&utm_campaign=workflow-welcome) перестроила автоматические кампании
- 4% → 8% — доля выручки email-канала. Исполнительный директор магазина техники [Quke](https://mindbox.ru/journal/cases/quke/?utm_source=help&utm_campaign=workflow-session) — о том, как работа с базой помогает не зависеть от маркетплейсов
- 14,6% — доля GMV от CRM-коммуникаций. Как mobile first маркетплейс [KazanExpress](https://mindbox.ru/journal/cases/kazan-express/?utm_source=help&utm_campaign=workflow-session) развивает мобильные пуши
- Мобильные пуши приносят [«ВсеИнструменты.ру»](https://mindbox.ru/journal/cases/vseinstrumenty-push/?utm_source=help&utm_campaign=workflow-session) более 150 млн рублей выручки в месяц
- Аудит коммуникаций [Charuel и Calista](https://mindbox.ru/journal/cases/charuel-audit/?utm_source=help&utm_campaign=workflow-session) увеличил долю выручки CRM-канала на 8 п. п.
- [Gulliver Market](https://mindbox.ru/journal/cases/gulliver-market/?utm_source=help&utm_campaign=workflow-session) запустил приложение и за год вырастил его долю в обороте до 49%
- +40% к доходу триггерных рассылок. 8 тестов интернет-магазина [«МегаФон»](https://mindbox.ru/journal/cases/megafon/?utm_source=help&utm_campaign=workflow-session) с ML-рекомендациями
- 7 эффективных триггеров [KANZLER](https://mindbox.ru/journal/cases/kanzler/?utm_source=help&utm_campaign=workflow-session) в email и SMS. Конверсия в покупку — в 2,5 раза выше, чем у стандартных механик
- B2B-маркетплейс [«на_полке»](https://mindbox.ru/journal/cases/na-polke-research/?utm_source=help&utm_campaign=workflow-session) исследовал клиентов и увеличил долю заказов из CRM-канала до 11,9%

[Что такое брошенная корзина](https://mindbox.ru/academy/education/broshennaya-korzina-zapusk/): инструкция по запуску для маркетолога
