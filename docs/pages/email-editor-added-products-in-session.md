---
title: Вывод брошенной корзины (новый конструктор)
slug: "email-editor-added-products-in-session"
source_url: "https://help.mindbox.ru/docs/email-editor-added-products-in-session"
vcs_path: "email-editor-added-products-in-session.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Механики в новом конструкторе
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:64b173d0d3019c9c20b5c20b176b7ca538c83751ad6d1ac6f8cc87cd0b211e0e"
---

# Вывод брошенной корзины (новый конструктор)

[Новый конструктор](email-editor.md) email-рассылок позволяет настроить динамический вывод добавленных за сессию продуктов без использования кода и [параметров](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0.md).

Чтобы вывести брошенную корзину:

1. Выберите блок по продуктам с динамическим заполнением:

![Снимок экрана 2023-12-05 в 00.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-05%20%D0%B2%2000.12.59.png)  
2. Настройте блок:

- **Заполнение контента** — «Динамическое»
  - **Какие продукты отображать** — «Добавленные в список продукты в сессии»
  - **Список продуктов** — выберите нужный список.
  - Можно ограничить выборку сегментом продуктов ([пересчитываемый](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статический](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md)) и зоной клиента.
- Правила вывода продуктов:
  - Задайте **количество строк и колонок** в товарной сетке. Неполные строки выводятся с выравниванием по середине.
  - **Если нет продуктов для отображения, то** — не отображать блок или не отправлять письмо.

![email-editor-added-products-in-session.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-added-products-in-session.png)

3. Настройте карточку продукта. Изменения в одной карточке автоматически дублируются на остальные:

![email-editor-added-products-in-session-product.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-added-products-in-session-product.png)

4. Сохраните изменения в шаблоне.

---

Пример сформированного письма:

![email-editor-added-products-in-session-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-added-products-in-session-result.png)
