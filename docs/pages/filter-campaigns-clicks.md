---
title: Найти клики по конкретным ссылкам в рассылках
slug: "filter-campaigns-clicks"
source_url: "https://help.mindbox.ru/docs/filter-campaigns-clicks"
vcs_path: "filter-campaigns-clicks.md"
toc_path:
  - Фильтры
  - "Рассылки: фильтры по клиентам с рассылками"
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:7392902e019be192b9f8ddd220ad06f8c688b028e8c1d85904d1bef8c026add9"
---

# Найти клики по конкретным ссылкам в рассылках

С помощью фильтров можно отобрать клики в письмах по конкретным ссылкам.

Для этого выберите условие **Клик в рассылке** — **Клик по ссылке** — **Ссылка**:

![Снимок экрана 2024-07-30 в 08.58.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2008.58.11.png)

Фильтр не поддерживает ссылки, в которых есть символ `?`, якоря (`#abc`) и параметры.

Например, переходы по ссылке `https://demoshop.mindbox.cloud/?utm_source=mindbox&utm_medium=email&utm_campaign=Massovaya` не получится найти, введя ее в поиск целиком:

![Снимок экрана 2024-07-30 в 08.52.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2008.52.19.png)

В фильтре нужно указывать **только часть до символа `?`**:

![Снимок экрана 2024-07-30 в 08.51.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2008.51.47.png)

Такой фильтр найдет переходы по заданной ссылке с любыми параметрами, в том числе с click id и utm-метками.

Вводить искомый адрес целиком необязательно — доступен **поиск по части ссылки**:

![Снимок экрана 2024-07-30 в 09.09.37.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2009.09.37.png)

Также можно указать, клиенты с переходами **из каких рассылок** интересуют:

![Снимок экрана 2024-07-30 в 08.54.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2008.54.28.png)

И за какой **временной промежуток**:

![Снимок экрана 2024-07-30 в 08.55.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2008.55.08.png)

Для **просмотра кликов** постройте фильтр на вкладке **Данные** → **Статусы рассылок**:

![Снимок экрана 2024-07-30 в 09.24.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-30%20%D0%B2%2009.24.09.png)
