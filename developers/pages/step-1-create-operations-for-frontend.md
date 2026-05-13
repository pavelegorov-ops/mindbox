---
title: 1. Создание операций для работы с фронтенда
slug: "step-1-create-operations-for-frontend"
source_url: "https://developers.mindbox.ru/docs/step-1-create-operations-for-frontend"
breadcrumb:
  - Персонализация сайта
  - Расширенная интеграция
  - Фронтенд
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:a100c8a361f6db1f84799b61c41a7e0ab940a69b1961cd2467fe61e11e57564e"
---

# 1. Создание операций для работы с фронтенда

1. Перейдите в раздел **Кампании** -> **Список кампаний**
2. Выберите **Создать кампанию** -> **Операция**
3. В настройках поставьте галочку напротив *Операция требует передачи deviceUUID* и выберите соотвествующий шаг:

- Просмотр страницы продукта: Продукт - Просмотреть ([подробнее](prodactionjson.md))
- ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/0a8c3d3-image.png)

  Просмотр страницы категории: Продукт - Просмотреть категорию ([подробнее](catactionjson.md))
- ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/706dee5-image.png)

  Изменение состава корзины: Продукт - Установить список ([подробнее](prodlistactionjson.md))

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/d22b77d-image.png)

### Важно

- Идентификаторы продукта и категории настраиваются в системе Майндбокс.
- Значения идентификаторов должны соответствовать тем, что уже добавлены в базу Майндбокс.
- Список продуктов настраивается в системе Майндбокс. Должен быть публичным.
- Если операции уже созданы и работают, пожалуйста, проверьте, верный ли у них выбран шаг и подходят ли они.
