---
title: Как импортировать региональные данные по продуктам
slug: "products-import-regional-data"
source_url: "https://help.mindbox.ru/docs/products-import-regional-data"
vcs_path: "products-import-regional-data.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Продукты
  - Добавление продуктов и категорий
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:f641cda4c2fdae49e7ec5f472d9820f897788ad30620c4ae7d719f4833174ed2"
---

# Как импортировать региональные данные по продуктам

На проекте возможно добавление разных [зон](areas-import.md).  
Это удобно, когда один и тот же продукт имеет, например, разную стоимость в Москве и Самаре: мы можем загрузить данные в карточку одного продукта и выводить жителю каждого города актуальную информацию.

#### Как добавить региональные данные:

1. Переходим на вкладку **Данные** → **Продукты**:

![Снимок экрана 2021-08-24 в 14.37.32.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2014.37.32.png)

2. Нажимаем «Импорт» → «Импорт продуктов»:

![Снимок экрана 2021-08-24 в 16.21.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-24%20%D0%B2%2016.21.09.png)

3. Выбираем операцию «Импорт региональных данных» и скачиваем шаблон файла:

![Снимок экрана 2021-05-19 в 19.31.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.31.41.png)

4. Подготавливаем файл.

Под ссылкой на скачивание шаблона перечислены названия колонок для импорта с описанием и подробностями.

Обязательно нужно заполнить внешние идентификаторы [зоны](%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%B7%D0%BE%D0%BD.md) и продукта.

Из основного фида в региональные данные автоматически попадет категория. Остальные данные (название, описание, цена и т.д.) надо продублировать, иначе они останутся пустыми в зоне:

![Снимок экрана 2021-05-19 в 19.55.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.55.29.png)

5. Добавляем файл в импорт и ставим задачу:

![Снимок экрана 2021-05-19 в 19.33.44.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.33.44.png)

- Появляется ссылка на задачу:

![Снимок экрана 2021-05-19 в 19.34.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.34.07.png)

- Ждём завершения задачи:

![Снимок экрана 2021-05-19 в 19.35.12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.35.12.png)

- У продукта появляются данные по зоне:

![Снимок экрана 2021-05-19 в 19.57.17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-05-19%20%D0%B2%2019.57.17.png)

[Гайд по LTV](https://mindbox.ru/journal/experts/ltv-prognoz-metriki/): прогноз метрики с помощью машинного обучения
