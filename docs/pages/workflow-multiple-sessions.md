---
title: Сценарий «Многократно брошенная сессия»
slug: "workflow-multiple-sessions"
source_url: "https://help.mindbox.ru/docs/workflow-multiple-sessions"
vcs_path: "workflow-multiple-sessions.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Брошенная сессия
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:8bddee5c04a42545379402973bce6808b0fd62184773ca04e3218608b555f495"
---

# Сценарий «Многократно брошенная сессия»

**Задача:** мотивировать клиентов, которые часто посещают сайт, совершить целевое действие.

**Решение:** дополним основной сценарий по [брошенной сессии](workflow-session.md) веткой для клиентов с множественными переходами на сайт.

1. Добавляем блок условия перед проверкой корзины:

![workflow-multiple-sessions.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-multiple-sessions.png)

2. Проверяем, что у клиента:

- за последние 5 дней было 3 сессии;
- заказов за этот период не было;
- рассылка из ветки не отправлялась за последний месяц.

![Снимок экрана 2024-09-05 в 09.42.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2009.42.11.png)

3. Отправляем письмо:

![Снимок экрана 2024-09-05 в 09.33.44.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2009.33.44.png)

Что отправить в рассылке

- [популярные продукты](recommendations-bestsellers.md) или [персональные рекомендации](recommendations-personal.md) (параметр [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) или через [новый конструктор](new-email-builder-recommendations.md));
- [чаще всего просматриваемый](computed-fields.md) [продукт](parameters-product-from-computed-field.md) или [категорию](parameters-category-from-computed-field.md) и рекомендации к ним;
- подборки и советы по поиску подходящих товаров;
- опрос — поможет выявить неудобства для клиентов.

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

Готово:

![workflow-multiple-sessions-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-multiple-sessions-result.png)
