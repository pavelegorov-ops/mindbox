---
title: Как удалить версию сценария
slug: "workflow-delete-version"
source_url: "https://help.mindbox.ru/docs/workflow-delete-version"
vcs_path: "workflow-delete-version.md"
toc_path:
  - Сценарии
  - Разные настройки сценария
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ea4f2d458d725ba9ac19b6c28c39bad564fba2c12df8c5a2bd8c6ed2cc17ec8b"
---

# Как удалить версию сценария

При удалении сущностей работает валидация, которая проверяет, что они не используются в механиках, в том числе в сценариях.

Чтобы обойти это ограничение, нужно удалить либо сам сценарий, либо затронутую версию.

## Удалить старую версию

1. Перейдите в нужную версию:

![Снимок экрана 2024-09-09 в 11.06.36](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.06.36.png)

2. Нажмите в настройках «Удалить версию»:

![Снимок экрана 2024-09-09 в 11.07.06](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.07.06.png)

Готово:

![Снимок экрана 2024-09-09 в 11.07.30](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.07.30.png)

## Удалить текущую версию

Удалить текущую версию сценария нельзя — можно только создать новую, а дальше убрать старую по описанному выше принципу.

1. Создайте новый черновик:

![Снимок экрана 2024-09-09 в 11.08.08](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.08.08.png)

2. Замените удаляемую сущность, чтобы убрать валидацию, и запустите сценарий:

![Снимок экрана 2024-09-09 в 11.11.18](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.11.18.png)

Чтобы сценарий не успел отработать по новым событиям до его остановки, можно настроить [начало его работы](what-is-workflow.md#vremya-raboty-scenariya) в будущем или задать невыполнимые [условия](workflow-conditions.md).

Далее после запуска сразу остановите сценарий.

3. Удалите [старую версию](workflow-delete-version.md#udalit-staruyu-versiyu):

![Снимок экрана 2024-09-09 в 11.12.08](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2011.12.08.png)
