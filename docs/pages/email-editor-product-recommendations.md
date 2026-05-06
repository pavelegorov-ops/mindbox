---
title: Вывод рекомендаций к продукту (новый конструктор)
slug: "email-editor-product-recommendations"
source_url: "https://help.mindbox.ru/docs/email-editor-product-recommendations"
vcs_path: "email-editor-product-recommendations.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Механики в новом конструкторе
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ec9e4cd01f21206f0e69b9131cfd8ea899103d777021b7e5a8f9bac8dabf3eb3"
---

# Вывод рекомендаций к продукту (новый конструктор)

[Новый конструктор](email-editor.md) позволяет настроить динамический вывод [рекомендаций](recommendation-algorithms.md) без использования кода и [параметров](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md).

Инструкция подходит для вывода алгоритмов к продукту:

- Сопутствующие продукты
- Похожие продукты
- Ручное соответствие категорий

---

Чтобы вывести рекомендации:

1. Выберите блок по продуктам с динамическим заполнением:

![Снимок экрана 2023-12-05 в 00.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-05%20%D0%B2%2000.12.59.png)  
2. Настройте блок:

- **Заполнение контента** — «Динамическое»
  - **Какие продукты отображать** — «Рекомендации к продукту»
  - **Алгоритм рекомендаций** — выберите подходящий алгоритм.
- Правила вывода продуктов:
  - Задайте **количество строк и колонок** в товарной сетке. Неполные строки выводятся с выравниванием по середине.
  - **Если нет продуктов для отображения, то** — не отображать блок или не отправлять письмо.

![email-editor-product-recommendations.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-product-recommendations.png)

3. Настройте карточку продукта. Изменения в одной карточке автоматически дублируются на остальные:

![email-editor-product-recommendations-product.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-product-recommendations-product.png)

4. Сохраните изменения в шаблоне.

---

Пример сформированного письма:

![MostViewedProduct-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/MostViewedProduct-example.png)
