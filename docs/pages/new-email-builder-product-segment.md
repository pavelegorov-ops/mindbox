---
title: Вывод продуктов из сегмента (новый конструктор)
slug: "new-email-builder-product-segment"
source_url: "https://help.mindbox.ru/docs/new-email-builder-product-segment"
vcs_path: "new-email-builder-product-segment.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Механики в новом конструкторе
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ab9e9d73b72a4f5652d249d2c7cb8ef26a00381aae01391838397b583da5a3d6"
---

# Вывод продуктов из сегмента (новый конструктор)

[Новый конструктор](email-editor.md) email-рассылок позволяет настроить динамический вывод продуктов из пересчитываемого или статического [сегмента](segments-products.md) без использования кода и [параметров](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md).

Чтобы вывести сегмент:

1. Выберите блок из категории "Продукты":

![Снимок экрана 2023-12-05 в 00.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-05%20%D0%B2%2000.12.59.png)

2. Настройте блок:

- **Заполнение контента** — «Подобрать автоматически»

  - **Какие продукты отображать** — «Сегмент продуктов»
  - **Сегмент** — выберите [пересчитываемый](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статический](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегмент продуктов.
  - Можно ограничить выборку зоной клиента.
- **Если нет продуктов для отображения, то**:

  - не отображать блок,
  - не отправлять письмо.
- Задайте **расположение продуктов** по строкам и колонкам в товарной сетке. Неполные строки выводятся с выравниванием по середине.

  ![email-editor-product-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-product-segment.png)

3. Настройте карточку продукта. Изменения в одной карточке автоматически дублируются на остальные:

![Снимок экрана 2023-12-28 в 03.13.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-28%20%D0%B2%2003.13.58.png)

4. Сохраните изменения в шаблоне.

---

Пример сформированного письма:

![Снимок экрана 2023-12-28 в 03.29.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-28%20%D0%B2%2003.29.47.png)
