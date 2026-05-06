---
title: Вывод продуктов из последней просмотренной категории (новый конструктор)
slug: "email-editor-products-from-viewed-categories-in-session"
source_url: "https://help.mindbox.ru/docs/email-editor-products-from-viewed-categories-in-session"
vcs_path: "email-editor-products-from-viewed-categories-in-session.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Механики в новом конструкторе
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:dc19a8d7c46c6e75ee730f548fa75d4aafe6f2f1ce1801075694ac77b30eafe1"
---

# Вывод продуктов из последней просмотренной категории (новый конструктор)

[Новый конструктор](email-editor.md) email-рассылок позволяет настроить динамический вывод продуктов из последней просмотренной категории без использования кода и [параметров](parameters-session-productcategoryviews.md#vyvesti-produkty-iz-prosmotrennyh-kategorij).

Чтобы вывести продукты из категории:

1. Выберите блок по продуктам с динамическим заполнением:

![Снимок экрана 2023-12-05 в 00.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-05%20%D0%B2%2000.12.59.png)  
2. Настройте блок:

- **Заполнение контента** — «Динамическое»
  - **Какие продукты отображать** — «Продукты из последней просмотренной за сессию категории»
  - Можно ограничить выборку сегментом продуктов ([пересчитываемый](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статический](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md)) и зоной клиента.
- Правила вывода продуктов:
  - Задайте **количество строк и колонок** в товарной сетке. Неполные строки выводятся с выравниванием по середине.
  - **Если нет продуктов для отображения, то** — не отображать блок или не отправлять письмо.

![email-editor-products-from-viewed-categories-in-session.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-products-from-viewed-categories-in-session.png)

3. Настройте карточку продукта. Изменения в одной карточке автоматически дублируются на остальные:

![email-editor-products-from-viewed-categories-in-session-product.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-products-from-viewed-categories-in-session-product.png)

4. Сохраните изменения в шаблоне.

---

Пример сформированного письма:

![email-editor-products-from-viewed-categories-in-session-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-products-from-viewed-categories-in-session-result.png)
