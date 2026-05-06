---
title: Как удалить категории
slug: "product-categories-delete-bulk"
source_url: "https://help.mindbox.ru/docs/product-categories-delete-bulk"
vcs_path: "product-categories-delete-bulk.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Продукты
  - Удаление продуктов и категорий
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:1502416010717a87327f68ab46e90f3c5e8cf3ceee43976c703fd7a2a9f8fca2"
---

# Как удалить категории

Нельзя удалить категорию, если:

- Она или ее дочерняя категория связаны с действием;
- Ей или ее дочерней категории принадлежит какой-либо продукт;
- Она или ее дочерняя категория добавлены в [персональные предложения](personal-offers.md) с типом «категория» как любимые.

Перед постановкой задачи может понадобиться [удалить действия](actions-delete.md), редактировать или [удалить продукты](products-delete-bulk.md).

---

Задача: удалить ненужные категории продуктов:

![Снимок экрана 2023-03-07 в 06.43.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2006.43.02.png)

Чтобы удалить категории:

1. Перейдите в раздел **Данные** → **Продукты**:

![Снимок экрана 2021-08-24 в 14.37.32.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2014.37.32.png)

2. В меню страницы нажмите «Удалить продукты»:

![Снимок экрана 2023-03-06 в 23.12.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-06%20%D0%B2%2023.12.03.png)

3. Выберите операцию «Удаление категорий». Для скачивания доступен шаблон файла с примером:

![Снимок экрана 2023-03-07 в 13.16.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2013.16.19.png)

4. Заполните файл.

В файл нужно добавить столбец со списком удаляемых категорий. Для идентификации используйте идентификаторы во внешних системах. Определить их можно [по выгрузке](product-categories-export.md).

При удалении родительской категории удаляются и все её дочерние категории.

Поэтому в файле достаточно указать идентификаторы родительских категорий, не перечисляя все вложенные.

Пример:

![Снимок экрана 2023-03-07 в 14.20.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2014.20.36.png)

Подгрузите файл в операцию.

5. Нажимите «Добавить задачу»:

![Снимок экрана 2023-03-07 в 07.49.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2007.49.30.png)

- Появляется ссылка на нее:

![Снимок экрана 2023-03-07 в 14.13.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2014.13.33.png)

- Убедитесь, что задача успешно завершилась:

![Снимок экрана 2023-03-07 в 14.23.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2014.23.29.png)

- Готово — категории удалены:

![Снимок экрана 2023-03-07 в 07.51.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-07%20%D0%B2%2007.51.58.png)
