---
title: Вывод просмотренных в сессии продуктов (новый конструктор)
slug: "new-email-builder-viewed-products-in-session"
source_url: "https://help.mindbox.ru/docs/new-email-builder-viewed-products-in-session"
vcs_path: "new-email-builder-viewed-products-in-session.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Механики в новом конструкторе
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:56e434623e51702695b5f0f8bd3ecc2ce3df8399d27b0fe992702dc075b2769c"
---

# Вывод просмотренных в сессии продуктов (новый конструктор)

[Новый конструктор](email-editor.md) email-рассылок позволяет настроить динамический вывод просмотренных в сессии продуктов без использования кода и [параметров](parameters-session-productviews.md).

Чтобы вывести просмотры из сессии:

1. Выберите блок по продуктам с динамическим заполнением:

![Снимок экрана 2023-12-05 в 00.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-05%20%D0%B2%2000.12.59.png)  
2. Настройте блок:

- **Заполнение контента** — «Динамическое»
  - **Какие продукты отображать** — «Просмотренные продукты в сессии»
  - Можно ограничить выборку сегментом продуктов ([пересчитываемый](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статический](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md)) и зоной клиента.
- Правила вывода продуктов:
  - Задайте **количество строк и колонок** в товарной сетке. Неполные строки выводятся с выравниванием по середине.
  - **Если нет продуктов для отображения, то** — не отображать блок или не отправлять письмо.

![email-editor-viewed-products-in-session.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-viewed-products-in-session.png)

3. Настройте карточку продукта. Изменения в одной карточке автоматически дублируются на остальные:

![Снимок экрана 2024-07-13 в 13.31.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-13%20%D0%B2%2013.31.46.png)

4. Сохраните изменения в шаблоне.

---

Пример сформированного письма:

![Снимок экрана 2024-07-13 в 13.56.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-13%20%D0%B2%2013.56.58.png)
