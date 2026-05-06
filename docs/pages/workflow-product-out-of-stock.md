---
title: Сценарий «Продукта из списка нет — предложить альтернативы»
slug: "workflow-product-out-of-stock"
source_url: "https://help.mindbox.ru/docs/workflow-product-out-of-stock"
vcs_path: "workflow-product-out-of-stock.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:e581acf9d6cf66aa644c8c1a50c2b6dbc8787c6f49b7ffc5fe6870cef44a49df"
---

# Сценарий «Продукта из списка нет — предложить альтернативы»

**Задача:** пользователь откладывает товар, которого сейчас нет в наличии. Нужно отправить рассылку с похожими товарами, которые доступны уже сейчас.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

1. Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md);
2. Создайте рекомендации по алгоритму [Похожие продукты](recommendations-similar.md#pohozhie-produkty);
3. Добавьте [параметры](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) в рассылку:

- для вывода добавленного продукта — параметр [ProductListItem](parameters-productlistitem-available.md);
- для вывода рекомендаций к нему — [ProductListItem.Product.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md).  
  Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — инструкции для [продукта](email-editor-productlistitem.md)/[рекомендаций](email-editor-product-recommendations.md).

Создаем сценарий:

1. Установите запуск по [добавлению в список](workflow-events.md#spisok-produktov-izmenilsya) и ограничьте [количество срабатываний](workflow-limit-per-customer.md) по клиенту:

![тов1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%BE%D0%B21.png)

Особенности события

---

Запускается, когда в список клиента добавлена новая линия.

На увеличение количества продукта в уже имеющейся линии событие не реагирует.

---

2. Проверяем, что товар не в наличии:

![тов2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%BE%D0%B22%282%29.png)

3. Проверяем валидность контакта и наличие подписки [в канале рассылки](workflow-check-subscription.md):

![тов3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%BE%D0%B23.png)

4. Отправляем рассылку с рекомендациями:

![тов4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%BE%D0%B24.png)

Сценарий готов, можно запускать:

![тов6.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%BE%D0%B26.png)

## Дополнительные материалы

- [Present & Simple](https://mindbox.ru/journal/cases/present-simple/?utm_source=help&utm_campaign=workflow-product-out-of-stock): цепочка уведомлений о появлении товара в наличии дает до 40% выручки от рассылок
- 7 эффективных триггеров [KANZLER](https://mindbox.ru/journal/cases/kanzler/?utm_source=help&utm_campaign=workflow-product-out-of-stock) в email и SMS. Конверсия в покупку — в 2,5 раза выше, чем у стандартных механик
- ROI 1696%: [«Сплав»](https://mindbox.ru/journal/cases/splav/?utm_source=help&utm_campaign=workflow-product-out-of-stock) меняет восприятие бренда с помощью персонализации коммуникаций
