---
title: "Как найти клиентов, которые взаимодействовали с рассылкой"
slug: "filter-clients-mailing"
source_url: "https://help.mindbox.ru/docs/filter-clients-mailing"
vcs_path: "filter-clients-mailing.md"
toc_path:
  - Фильтры
  - "Рассылки: фильтры по клиентам с рассылками"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:0945f570498204a8df6c48c3fa4ea18cdef513d42c7070051d37cb4220dcb1f2"
---

# Как найти клиентов, которые взаимодействовали с рассылкой

Как работают [Статусы рассылки](customer-message-statuses.md).

В качестве примера рассмотрим взаимодействия с рассылкой:

![Снимок экрана 2024-07-26 в 09.16.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.16.50.png)

## Поиск клиентов

Перейдите на вкладку **Данные** → **Клиенты**:

![Снимок экрана 2024-07-26 в 10.33.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2010.33.45.png)

В разделе фильтров **'Рассылки'** выберите условие с нужным статусом:

![Снимок экрана 2024-07-26 в 09.31.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.31.50.png)

В каждом из них есть [вложенное условие](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B2-%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%85.md) «Рассылки» — в нем выберите интересующую кампанию:

![Снимок экрана 2024-07-26 в 09.34.25.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.34.25.png)

- Найти клиентов, которым была отправлена рассылка:

![Снимок экрана 2024-07-26 в 09.40.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.40.54.png)

- Найти клиентов, которым не удалось отправить рассылку:

![Снимок экрана 2024-07-26 в 09.41.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.41.22.png)

- Найти клиентов, которым не удалось доставить рассылку:

![Снимок экрана 2024-07-26 в 09.41.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.41.50.png)

- Найти клиентов, которые были в выборке рассылки, но не смогли ее получить (не удалось отправить или доставить сообщение):

![Снимок экрана 2024-07-26 в 11.01.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2011.01.29.png)

- Найти клиентов, которым была доставлена рассылка.

Отдельного статуса «Доставлено» нет. Для поиска таких клиентов нужно задать два условия: есть отправка письма + нет недоставки:

![Снимок экрана 2024-07-26 в 11.04.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2011.04.40.png)

- Найти клиентов, которые открыли рассылку:

![Снимок экрана 2024-07-26 в 09.43.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.43.54.png)

- Найти клиентов, которые не открыли рассылку.

Важно: не забудьте задать наличие отправки. Иначе фильтр будет выдавать и тех клиентов, которые не были в списке получателей рассылки — ведь действия открытия у них тоже нет:

![Снимок экрана 2024-07-26 в 09.49.12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.49.12.png)

- Найти клиентов, которые кликнули по ссылке в письме:

![Снимок экрана 2024-07-26 в 09.49.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.49.51.png)

- Найти клиентов, которые не кликнули в письме:

![Снимок экрана 2024-07-26 в 11.02.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2011.02.15.png)

- Найти клиентов, которые кликнули по ссылке [отписки](how-to-unsubscribe.md) в письме:

![Снимок экрана 2024-07-26 в 09.51.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.51.26.png)

- Найти участников рассылки, то есть всех клиентов, которые были в заложенном списке ее получателей:

![Снимок экрана 2024-07-26 в 09.33.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.33.38.png)

### Поиск по времени взаимодействия

- Найти клиентов, которые открывали письмо в июне 2024 года:

![Снимок экрана 2024-07-26 в 09.55.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.55.42.png)

- Найти клиентов, которые открывали письмо за последний час:

![Снимок экрана 2024-07-26 в 09.56.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.56.36.png)

### Поиск по количеству взаимодействий

- Найти клиентов, которые кликали в рассылке от двух раз:

![Снимок экрана 2024-07-26 в 09.57.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.57.31.png)

- Найти клиентов, которым отправляли рассылку три раза за последние полгода:

![Снимок экрана 2024-07-26 в 09.59.17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2009.59.17.png)

### Интерактивное демо

## Поиск изменений статусов рассылки

Перейдите на вкладку **Данные** → **Статусы рассылок**:

![Снимок экрана 2024-08-06 в 19.15.18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-08-06%20%D0%B2%2019.15.18.png)

- Найти все отправки рассылки:

![Снимок экрана 2024-07-26 в 10.02.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2010.02.52.png)

- Найти все открытия рассылки:

![Снимок экрана 2024-07-26 в 10.03.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2010.03.46.png)

- Найти все клики в рассылке за последние сутки:

![Снимок экрана 2024-07-26 в 10.04.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-07-26%20%D0%B2%2010.04.56.png)

Узнать больше о работе фильтров и попрактиковаться в их составлении можно на [курсе](https://stepik.org/course/130156/info).

[Лучшее время для отправки email- и SMS-рассылок](https://mindbox.ru/academy/education/luchshee-vremya-dlya-rassylok/). Данные об эффективности рассылок 60 клиентов Mindbox
