---
title: Как удалить зону
slug: "areas-delete"
source_url: "https://help.mindbox.ru/docs/areas-delete"
vcs_path: "areas-delete.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Продукты
  - Зоны/регионы
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:6ddb55f0c1b9f3c22cafe65a05191959af9f9984bb8a1df2052388eb304ad860"
---

# Как удалить зону

Если зона больше не требуется или ошибочно загружена, то ее можно удалить через импорт файла или сервис.

## Удаление зон по файлу

1. Переходим в раздел **Клиенты**:

![клиенты.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D1%8B.png)

2. Нажимаем «Импорт» → «Импорт зон»:

![импорт зон.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82%20%D0%B7%D0%BE%D0%BD.png)

3. Выбираем операцию «Удаление зон».

Для скачивания доступен шаблон с примером:

![Снимок экрана 2021-07-14 в 22.49.32.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-14%20%D0%B2%2022.49.32.png)

4. Заполняем файл:

- *ExternalId* — внешний идентификатор удаляемой зоны.

**Как его найти?**  
[Выгружаем зоны](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B3%D1%80%D1%83%D0%B7%D0%B8%D1%82%D1%8C-%D0%B7%D0%BE%D0%BD%D1%8B.md). В файле будут внешние идентификаторы всех зон в колонке AreaIdsExternalId.

Пример заполненного файла на удаление:

![Снимок экрана 2021-07-14 в 22.50.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-14%20%D0%B2%2022.50.07.png)

5. Заполняем настройки операции:

![Снимок экрана 2021-07-14 в 22.50.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-14%20%D0%B2%2022.50.31.png)

- *Комментарий* — необязателен.
- *Кодировка файла* — utf-8.

Нажимаем на «Добавить задачу».

6. Появляется сообщение о добавлении задачи и ссылка на нее:

![Снимок экрана 2021-07-14 в 22.50.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-14%20%D0%B2%2022.50.41.png)

- Ждем завершения:

![Снимок экрана 2021-07-14 в 22.53.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-07-14%20%D0%B2%2022.53.54.png)

## Удаление зон через сервис

Доступно удаление зон с помощью [POST-запроса](https://developers.mindbox.ru/docs/%D0%BC%D0%B0%D1%81%D1%81%D0%BE%D0%B2%D0%BE%D0%B5-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BE%D0%BD-v3).

## Ограничение на удаление зон

Не будут удалены зоны, которые связаны с клиентами, заказами  
промоакциями, фильтрами, YML-фидами, продуктами.  
В отчете о выполнении задачи будет информация о зонах, которые не были удалены.
