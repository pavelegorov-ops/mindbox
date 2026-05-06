---
title: Сценарий «Цена на самый просматриваемый или покупаемый продукт снизилась»
slug: "workflow-computed-field-lower-price"
source_url: "https://help.mindbox.ru/docs/workflow-computed-field-lower-price"
vcs_path: "workflow-computed-field-lower-price.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:2212d905b24048ac169e3c0d898d87f3660456cbb3f68b68e2e7962b22f29f2b"
---

# Сценарий «Цена на самый просматриваемый или покупаемый продукт снизилась»

**Задача:** отправить коммуникацию о снижении цены на продукт из [вычисляемого поля](computed-fields.md) — чаще всего покупаемый клиентом продукт.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода продукта — [Product](parameters-customfield-computed-field-price.md)

Создаем сценарий:

1. Запуск — по событию [Предпочитаемый продукт изменился](workflow-events.md#predpochitaemyj-produkt-izmenilsya):

![workflow-computed-field-lower-price-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-computed-field-lower-price-event.png)

Особенности события

---

При изменении у продукта поля «Цена» сравнивается, уменьшилась ли она по сравнению с предыдущим значением на заданный процент или сумму.  
Если да, запускается сценарий по клиентам, у которых в указанном вычисляемом поле записан этот продукт.

- Работает каждый раз, в том числе:
  - При ещё большем снижении цены.
  - При подорожании и новом снижении стоимости относительно прошлого значения цены.
- Не реагирует на заполнение цены. Если у продукта ранее не было данных о стоимости, его цена должны вновь поменяться после заполнения, чтобы сценарий запустился.

Для клиентов с заполненной [зоной](https://help.mindbox.ru/docs/regional-yml-import):

- если у продукта есть региональные данные по цене в зоне клиента, сценарий запускается по изменениям продукта в регионе клиента;
- если у продукта есть какие-либо региональные данные, но не по зоне клиента, сценарий не запускается;
- если у продукта есть региональные данные по зоне клиента, но информация о цене в ней не заполнена, сценарий реагирует на изменения в основном фиде;
- если у продукта нет никаких региональных данных, сценарий срабатывает по изменениям в основном фиде.

---

2. Ограничьте [количество срабатываний](workflow-limit-per-customer.md) по клиенту, чтобы не отправлять разом несколько рассылок:

![workflow-computed-field-lower-price-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-computed-field-lower-price-frequency.png)

3. Задержку не ставим, но ограничиваем выход из блока, чтобы не отправлять письмо ночью:

![workflow-computed-field-lower-price-delay.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-computed-field-lower-price-delay.png)

4. Проверяем, что продукт известный и в наличии:

![workflow-cf3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/aa/workflow-cf3.png)

5. Проверяем валидность контакта и наличие подписки [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-09-29 в 18.53.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.53.02.png)

При наличии других механик по снижению цены ([в списке](workflow-product-lower-price.md) или [по просмотрам](workflow-viewed-product-price-down.md)) поставьте задержку, чтобы сначала отрабатывала более приоритетная механика, а в остальных задайте проверку на отсутствие коммуникаций за последнее время.

6. Отправляем письмо:

![workflow-cf4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/aa/workflow-cf4.png)

Что отправить в рассылке

- К продукту можно добавить [сопутствующие](recommendations-related.md) или [похожие](recommendations-similar.md) товары;
  - параметр для вывода рекомендаций — [ProductListItem.Product.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md)

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

7. Сценарий готов, можно запускать:

![workflow-computed-field-lower-price-launch.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-computed-field-lower-price-launch.png)
