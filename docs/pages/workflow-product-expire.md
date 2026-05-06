---
title: Сценарий «Продукт из заказа скоро закончится»
slug: "workflow-product-expire"
source_url: "https://help.mindbox.ru/docs/workflow-product-expire"
vcs_path: "workflow-product-expire.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:5aa83482b29e0aa34e39149dd7f6e629b182773e01e92f30a83fa4dc2202c083"
---

# Сценарий «Продукт из заказа скоро закончится»

**Задача**: напомнить клиентам, что купленный ими товар заканчивается и пора обновить запасы.  
Например, шампунь, подгузники, капсулы для стирки — любой продукт, который нужно покупать с примерно одинаковой периодичностью.

Для решения задачи настроим [сценарий](what-is-workflow.md).

**Особенности механики и альтернативы**

- **Нужно будет дополнить товарный фид** и передавать в нем срок годности продуктов.

Способ реализации без изменения фида — передавать дату следующей покупки в дополнительном поле позиции заказа и ориентироваться на нее. Сценарий настроить по аналогии с [инструкцией](workflow-reminder-before-date.md).

- **Механика работает по позициям, а не заказам.**  
   Это означает, что в рассылке для вывода будет доступна информация по конкретной позиции, а не всему заказу.

Также, две подходящие позиции из одного заказа — два отдельных события и, соответственно, два отдельных уведомления.

Чтобы повторно отправлять клиентам весь заказ через заданный интервал, настройте сценарий по аналогии с [инструкцией](workflow-feedback.md).

Перед созданием сценария:

1. Дополните YML-фид параметром `<expiry>` внутри элемента `<offer>`. Пример файла фида в [документации](https://developers.mindbox.ru/docs/prodimportxml#%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0).

Примеры заполнения параметра:

- 1 год: P1Y
- 2 месяца: P2M
- 3 суток: P3D
- 4 часа: PT4H
- 1 год 2 месяца 3 суток 4 часа: P1Y2M3DT4H

Теперь у продуктов с этим параметром есть значение срока годности. На проекте пока нет возможности увидеть значение этого поля, оно отображается только в фиде.

2. Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md);

- [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода информации о продукте — [OrderItem](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82-%D0%B8%D0%B7-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0-%D1%81%D0%BA%D0%BE%D1%80%D0%BE-%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD%D1%87%D0%B8%D1%82%D1%81%D1%8F.md)

Создаем сценарий:

1. Запуск — по событию [«Продукт в заказе доставлен»](workflow-events.md#produkt-v-zakaze-dostavlen):

![workflow-product-expire-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-product-expire-start.png)

Особенности события

---

- Запускается **только** по статусу доставки. Для отработки по другим статусам оно не подходит.
- Срабатывает по позиции, даже если она сразу пришла в данном статусе.
- Запускается на каждую доставленную позицию, даже если они пришли в одном заказе. То есть доставка заказа с двумя позициями запустит сценарий два раза.
- Работает **повторно** по позиции, если что-то в ней поменялось (цена, количество, дополнительные поля).
- На заказах, добавленных задним числом, сценарий срабатывает, но действие должно попадать в актуальность группы шагов и не должно быть изменений по позиции с более поздней датой.
- Событие можно дополнительно ограничить по статусу заказа в категории «Доставлено» и по сегментам доставленного продукта.

---

2. Ставим [срабатывание на дату](workflow-delay.md), например, за неделю до окончания срока службы продукта. Ограничиваем выход из блока, чтобы не отправлять рассылку ночью:

![workflow-product-expire-delay.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-product-expire-delay.png)

3. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-11-05 в 23.45.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-05%20%D0%B2%2023.45.26.png)

4. Отправляем рассылку:

![Снимок экрана 2021-11-05 в 23.42.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-05%20%D0%B2%2023.42.14.png)

Что отправить в рассылке

- Дополнительно к заканчивающемуся продукту можно выводить [аналоги](recommendations-similar.md) — в таком случае пользователь может обновить понравившийся товар или попробовать что-то новое.
  - Параметр для вывода рекомендаций — [Product.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md)

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

6. В стартовом блоке ограничиваем [частоту срабатываний](workflow-limit-per-customer.md) по клиенту:

![workflow-product-expire-limit.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-product-expire-limit.png)

7. Сценарий готов, можно запускать:

![workflow-product-expire-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-product-expire-result.png)

## Дополнительные материалы

- [Удержание клиентов](https://mindbox.ru/journal/education/uderzhanie-klientov/?utm_source=help&utm_campaign=workflow-product-expire): советы и инструменты
- 9% → 14% доля email в выручке интернет-магазина. Как «[Галерея косметики](https://mindbox.ru/journal/cases/galereya-kosmetiki/?utm_source=help&utm_campaign=workflow-product-expire)» восстановила показатели CRM
- 14,6% — доля GMV от CRM-коммуникаций. Как mobile first маркетплейс [KazanExpress](https://mindbox.ru/journal/cases/kazan-express/?utm_source=help&utm_campaign=workflow-product-expire) развивает мобильные пуши
- «[Магнит Доставка](https://mindbox.ru/journal/cases/magnit-dostavka/?utm_source=help&utm_campaign=workflow-product-expire)» получает 20% выручки из CRM-канала: мобильные пуши, каскадные сценарии, AB-тесты и NPS-опросы
- «[ВсеИнструменты.ру](https://mindbox.ru/journal/cases/vseinstrumenty-ru/?utm_source=help&utm_campaign=workflow-product-expire)» удвоили доход на клиента в email-канале и собирают в шесть раз больше отзывов в месяц
- [Подборка механик](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-product-expire). Триггерные рассылки для роста конверсии в индустриях красоты и одежды

[Механики персонализации сайта в разном бизнесе](https://mindbox.ru/academy/mechanics/tovarnye-rekomendacii-v-raznyh-industriyah/): товарные рекомендации
