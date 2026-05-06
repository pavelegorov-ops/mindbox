---
title: Как импортировать категории
slug: "product-categories-import"
source_url: "https://help.mindbox.ru/docs/product-categories-import"
vcs_path: "product-categories-import.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Продукты
  - Добавление продуктов и категорий
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:aa34b199c2636c45225adbe8fe2cea962deb19b01da0c39652bab6e2c2dd70e4"
---

# Как импортировать категории

1. Переходим на вкладку **Данные** → **Продукты**:

![Снимок экрана 2021-08-24 в 14.37.32.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2014.37.32.png)

2. Нажимаем «Импорт» → «Импорт продуктов»:

![Снимок экрана 2021-08-24 в 16.21.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.21.09.png)

3. Выбираем операцию «Импорт категорий продуктов с идентификацией по внешнему ID».

Для скачивания доступен шаблон файла с примером:

![Снимок экрана 2021-08-24 в 16.44.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.44.50.png)

4. Подготавливаем файл.

Пример:

![Снимок экрана 2021-08-24 в 16.54.06.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.54.06.png)

- *CategoryExternalId* — внешний идентификатор категории;
- *Name* — название категории;
- *ParentCategoryExternalId* — внешний идентификатор родительской категории; если не указывать, то категория будет верхнеуровневой.

В нашем примере мы создаём:

- категорию *Верхняя одежда* с дочерними категориями *Куртки* и *Плащи*;
- категорию *Аксессуары* с дочерними категориями *Очки* и *Ремни* (со своей дочерней — *Кожаные* ).

5. Добавляем файл, выбираем [внешнюю систему](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D1%8E%D1%8E-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83.md) и нажимаем «Добавить задачу»:

![Снимок экрана 2021-08-24 в 16.55.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.55.31.png)

6. Появляется ссылка на задачу:

![Снимок экрана 2021-08-24 в 16.55.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.55.46.png)

7. Ждём её завершения:

![Снимок экрана 2021-08-24 в 16.59.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.59.52.png)

8. Проверяем на странице продуктов, что категории появились:

![Снимок экрана 2021-08-24 в 17.07.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2017.07.33.png)

[Гайд по LTV](https://mindbox.ru/journal/experts/ltv-prognoz-metriki/): прогноз метрики с помощью машинного обучения
