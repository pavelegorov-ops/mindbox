---
title: Интеграция с Segmel
slug: "segmel-integration"
source_url: "https://help.mindbox.ru/docs/segmel-integration"
vcs_path: "segmel-integration.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:8990de28682d827cbcbc17e07afaa6d17998dafcba6f8a1b0eda63c7b90bf707"
---

# Интеграция с Segmel

[**Segmel**](http://segmel.com) — сервис предиктивной аналитики, который помогает оптимизировать затраты на коммуникации и увеличить конверсию в заказ с помощью алгоритмов машинного обучения.

Читайте подробнее о возможностях сервиса и порядке подключения в [статье](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-segmel#/).

Рассмотрим, какие настройки необходимы для интеграции.

## Точка интеграции

[Создайте точку интеграции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8) с типом «Другой». В дальнейшем эта точка будет использоваться для передачи данных между сервисами.

![segmel-endpoint](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-endpoint.png)

## Сегментация клиентов

1. [Создайте](segment-client-static.md) статическую сегментацию.
2. Добавьте первый сегмент:

   - **Имя** — SGMLpred10
   - **Системное имя** — SGMLpred10

   ![segmel-segment](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-segment.png)
3. Повторите п.2 и создайте еще 9 сегментов:

   - SGMLpred20
   - SGMLpred30
   - SGMLpred40
   - SGMLpred50
   - SGMLpred60
   - SGMLpred70
   - SGMLpred80
   - SGMLpred90
   - SGMLpred100
4. Запустите готовую сегментацию в работу:

   ![segmel-segment-start](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-segment-start.png)

## Операции

### Операции для добавления клиентов

Для каждого сегмента нужна своя операция для добавления клиентов.

1. [Создайте](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sozdanie-operacii-v3) новую операцию. Настройте ее аналогично скриншоту ниже и сохраните.

   - **Имя** — AddSGML10
   - **Системное имя** — AddSGML10

   ![segmel-operation](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-operation.png)
2. Создайте операции для оставшихся 9 сегментов:

   - AddSGML20
   - AddSGML30
   - AddSGML40
   - AddSGML50
   - AddSGML60
   - AddSGML70
   - AddSGML80
   - AddSGML90
   - AddSGML100

   Для этого сделайте копию операции из п.1 и замените название и сегмент:

   ![segmel-operation-copy](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-operation-copy.png)

   В итоге получится 10 операций для добавления:

   ![segmel-operation-done](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-operation-done.png)

### Операция для удаления клиента из сегментации

1. Скопируйте одну из операций создания.
2. Переименуйте операцию:

   - **Имя** — ExcludeSGMLpred
   - **Системное имя** — ExcludeSGMLpred
3. Измените шаг добавления в сегментацию на «Сегментации — Исключить клиента из сегментации» и выберите сегментацию:

   ![segmel-operation-delete](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/segmel-operation-delete.png)
