---
title: Как строить фильтр с двумя и более шаблонами действий
slug: "filters-action-templates"
source_url: "https://help.mindbox.ru/docs/filters-action-templates"
vcs_path: "filters-action-templates.md"
toc_path:
  - Фильтры
  - Регистрация и действия клиента
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:5efc2e032ac0bc6ef8d483469d762779fff1321a2fa9076e45abaf1b16b11dd3"
---

# Как строить фильтр с двумя и более шаблонами действий

Действия клиентов связаны с участием в рассылках, просмотром продуктов, оформлением заказа и т.д.  
По всем действиям можно фильтровать информацию, выбрав верный шаблон.

В статье будем использовать [шаблоны действия](mailings-action-templates) по участию в рассылке.

Для примера используем рассылки с названиями «**Рассылка первая**» и «**Вторая рассылка**».

Есть «Рассылка первая»:

![Снимок экрана 2021-04-02в 20.43.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.43.01.png)

Есть «Вторая рассылка»:

![Снимок экрана 2021-04-02в 20.43.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.43.15.png)

## Примеры использования:

- Найти клиентов, у которых есть **хотя бы одно** из действий:

![Снимок экрана 2021-04-02в 20.42.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.42.36.png)

- Найти клиентов, у которых есть **только «Рассылка первая»**, нет второй:

![Снимок экрана 2021-04-02в 20.45.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.45.10.png)

- Найти клиентов, у которых есть **только одно** из действий:

![Снимок экрана 2021-04-02в 20.46.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.46.01.png)

- Найти клиентов, у которых есть **оба действия** :

![Снимок экрана 2021-04-02в 20.43.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.43.36.png)

- Найти клиентов, у которых **нет ни одного** из действий:

![Снимок экрана 2021-04-02в 20.47.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.47.21.png)

Также корректно искать так:

![Снимок экрана 2021-04-02в 20.47.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.47.04.png)

- Исключить тех клиентов, у которых есть оба действия одновременно:

![Снимок экрана 2021-04-02в 20.48.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-02%20%D0%B2%2020.48.45.png)

Узнать больше о работе фильтров можно в курсе [«Фильтры Mindbox»](https://stepik.org/course/130156/info).

В видеоуроках собрана вся основная информация о фильтрах, которая может понадобиться в работе, а после каждого урока идет закрепление материала в практических заданиях.

[Урок по шаблонам действия:](https://stepik.org/lesson/838624/step/1?unit=842288)

Урок также доступен [на youtube.](https://www.youtube.com/embed/iMe4R5eNn5M?rel=0)

[Персонализация рекламы](https://mindbox.ru/academy/education/personalizaciya-reklamy/) — эффективные способы привлечь клиентов
