---
title: Сценарий для мотивации на повторный заказ
slug: "workflow-next-order"
source_url: "https://help.mindbox.ru/docs/workflow-next-order"
vcs_path: "workflow-next-order.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:2a4d463368468a125a76b6704ae0bd1a56fc8c447355144ac72aa8e8071649d9"
---

# Сценарий для мотивации на повторный заказ

**Задача**: увеличить количество повторных заказов.

**Решение**: отправим сопутствующие товары к заказу, а затем подборку из новинок с помощью [сценария](what-is-workflow.md).

Также удержать клиентов помогут механики:

- [Напоминание о товарах повторного спроса](workflow-product-expire.md)
- [Опрос об удовлетворенности последним заказом](workflow-feedback.md)

Перед созданием сценария:

- Добавьте автоматические рассылки в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md)

Создаем сценарий:

1. Запуск — по событию [Статус заказа изменен](workflow-events.md#status-zakaza-izmenen):

![мотивация-событие.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5.png)

Особенности события

---

Заказ перешел в выбранный статус. В том числе сразу пришел в нужном статусе.

- На заказе, добавленном задним числом, сценарий срабатывает, если он попадает в актуальность группы шагов и если нет изменений по заказу с более поздней датой.
- В статус должны перейти все позиции, которые пришли с созданием заказа. То есть, если одна позиция отменилась, сценарий не запустится. В режиме «Любая позиция заказа перешла» такого ограничения нет.
- Позиции необязательно должны переходить в указанный статус в рамках одного действия. Если изменения по позициям приходят постепенно, сценарий запустится, когда все позиции получат нужный статус.
- Можно дополнительно ограничить количество срабатываний в рамках заказа.
- Количество переходов в нужный статус считается с момента запуска сценария. Например, если сценарий должен применяться к заказу один раз и нужный переход произошел до включения сценария, повторное изменение статуса заказа запустит сценарий.

---

2. Ставим [задержку](workflow-delay.md) и ограничиваем выход из блока ожидания, чтобы не отправлять письма ночью:

![мотивация-ожидание1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%B6%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B51.png)

3. Проверяем, что [заказ](workflow-conditions.md) не отменен:

![мотивация-заказ.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7.png)

4. Проверяем, что у клиента есть подписка и валидный контакт [в канале рассылки](workflow-check-subscription.md):

![мотивация-клиент1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%821.png)

5. Отправляем рассылку:

![мотивация-сопутка.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D1%81%D0%BE%D0%BF%D1%83%D1%82%D0%BA%D0%B0.png)

Для отправки рекомендаций

- Используйте алгоритм [Сопутствующие продукты к последнему заказу](recommendations-related.md) или [Ручное соответствие категорий к последнему заказу](recommendations-custom.md);
  - Параметр для вывода в рассылке — [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](new-email-builder-recommendations.md)

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

6. Ставим ожидание после письма:

![мотивация-ожидание2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%B6%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B52.png)

7. Проверяем, были ли у клиента заказы за время работы цепочки и рассылки за последние сутки:

![Снимок экрана 2024-08-05 в 10.27.18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-05%20%D0%B2%2010.27.18.png)

8. Отправляем вторую рассылку:

![мотивация-новинки.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%BA%D0%B8.png)

Что отправить в рассылке

- продукты из [пересчитываемого](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статического](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегмента (параметр [Products.GetBySegment()](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md));
  - дополнительно можно ограничить выборку [по любимому признаку](parameters-products-by-computed-field.md) клиента (цвет, стиль и т.д.);
- рекомендации по алгоритму [Популярные продукты](recommendations-bestsellers.md);
- [персональные рекомендации](recommendations-personal.md).

9. В стартовом блоке ограничиваем [частоту срабатываний](workflow-limit-per-customer.md) по клиенту:

![мотивация-огр.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%B3%D1%80.png)

10. Сценарий готов, можно запускать:

![мотивация-готово.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BE.png)

## Дополнительные материалы

- [Удержание клиентов](https://mindbox.ru/journal/education/uderzhanie-klientov/?utm_source=help&utm_campaign=workflow-next-order): советы и инструменты
- [Как повысить повторные продажи](https://mindbox.ru/journal/education/kak-povysit-povtornye-prodazhi/?utm_source=help&utm_campaign=workflow-next-order): подборка эффективных методов и инструментов
- 7,92% — инкрементальный прирост из CRM-канала. Как в [«Много лосося»](https://mindbox.ru/journal/cases/mnogolososya/?utm_source=help&utm_campaign=workflow-next-order) сегментируют базу, выбирают офферы и автоматизируют рассылки
- ×4,4 выручка от CRM-канала. Как [Колесо.ру](https://mindbox.ru/journal/cases/koleso-ru/?utm_source=help&utm_campaign=workflow-next-order) удерживает клиентов и увеличивает выручку в бизнесе с яркой сезонностью
- Как [«Снежная Королева»](https://mindbox.ru/journal/cases/snezhnaya-koroleva/?utm_source=help&utm_campaign=workflow-next-order) удвоила конверсию в покупку из email-канала
- Контент вместо скидок, сегменты по интересам. Экологичный email-маркетинг приносит «[Аудиомании](https://mindbox.ru/journal/cases/audiomania-email/?utm_source=help&utm_campaign=workflow-next-order)» 7% выручки
- 7 эффективных триггеров [KANZLER](https://mindbox.ru/journal/cases/kanzler/?utm_source=help&utm_campaign=workflow-next-order) в email и SMS. Конверсия в покупку — в 2,5 раза выше, чем у стандартных механик
- 0,8% → 5% — доля CRM в общем обороте «[Купибилета](https://mindbox.ru/journal/cases/kupibilet-crm/?utm_source=help&utm_campaign=workflow-next-order)» за год: информационные претрипы, предложение купить обратный билет или слетать в новую локацию при длительной поездке
- 9% → 14% доля email в выручке интернет-магазина. Как «[Галерея косметики](https://mindbox.ru/journal/cases/galereya-kosmetiki/?utm_source=help&utm_campaign=workflow-next-order)» восстановила показатели CRM
- [Подборка механик](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-next-order). Триггерные рассылки для роста конверсии в индустриях красоты и одежды
- [Сопутствующие товары](https://mindbox.ru/journal/education/podborka-soputstvuyushhih-tovarov-k-zakazu/?utm_source=help&utm_campaign=workflow-next-order): 5 причин, почему их стоит предлагать в интернет-магазине или рассылках
