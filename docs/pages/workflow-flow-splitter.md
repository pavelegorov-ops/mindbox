---
title: "«Разделение»: как распределить прохождения по веткам сценария"
slug: "workflow-flow-splitter"
source_url: "https://help.mindbox.ru/docs/workflow-flow-splitter"
vcs_path: "workflow-flow-splitter.md"
toc_path:
  - Сценарии
  - Блоки сценария
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:2d7b96a0a4f01da3b1b5b35b71b870c4b6ca98ae209ecbd61ecdf17675b8d246"
---

# «Разделение»: как распределить прохождения по веткам сценария

В сценариях можно разбить поток прохождений по веткам с заданной вероятностью. Для этого используется блок «Разделение»:

![Снимок экрана 2024-09-09 в 10.21.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.21.21.png)

Блок схож с [АБ-тестом](workflow-ab-tests.md), но, в отличие от него, выполняет только функцию распределения клиентов без проведения тестирования.

## Настройки блока

- В блоке может быть от 2 до 5 выходов.
- Выбор выхода считается для каждого отдельного прохождения с указанной вероятностью.

## Пример использования

**Задача:** клиентам, оставившим контакт в форме, в случайном порядке назначить одного из трех менеджеров.

1. После регистрации разделяем прохождения по трем веткам с одинаковой вероятностью:

![Снимок экрана 2024-09-09 в 10.31.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.31.03.png)

2. Записываем клиентам из первой цепочки значение в заранее созданное [дополнительное поле](additional-data.md):

![Снимок экрана 2024-09-09 в 10.31.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.31.41.png)

3. Дублируем настройки для остальных веток:

![Снимок экрана 2024-09-09 в 10.33.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.33.28.png)

4. В стартовом блоке ограничьте [количество применений](workflow-limit-per-customer.md) одним разом:

![Снимок экрана 2024-09-09 в 10.33.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.33.40.png)

Сценарий готов. Можно запускать:

![Снимок экрана 2024-09-09 в 10.33.57.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2010.33.57.png)
