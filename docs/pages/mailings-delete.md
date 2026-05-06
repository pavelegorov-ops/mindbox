---
title: Как удалить рассылку
slug: "mailings-delete"
source_url: "https://help.mindbox.ru/docs/mailings-delete"
vcs_path: "mailings-delete.md"
toc_path:
  - Рассылки
  - Общие настройки рассылок
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:29176a82aaea72f3f2fc84cdb1d9355c6f90e6a4cb1f11f17e9097c532586e9a"
deprecation_hint:
  - не используется
---

# Как удалить рассылку

Удалить можно любую рассылку, которая не используется в механиках. При этом есть валидация как на использование самой рассылки в шагах отправки, так и на ее [шаблоны действия](mailings-action-templates.md) в сохраненных фильтрах.

Посмотреть все использования рассылки можно через соответствующую кнопку:

![Снимок экрана 2023-03-22 в 03.57.21.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-22%20%D0%B2%2003.57.21.png)

Для удаления рассылки все связанные механики нужно либо поправить, либо удалить.

Вместе с рассылкой удаляются и её действия вместе с статистикой.

1. На странице редактирования рассылки нажимаем на кнопку «Удалить»:

![Снимок экрана 2023-03-22 в 03.57.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-22%20%D0%B2%2003.57.31.png)

2. Подтверждаем:

![Снимок экрана 2021-10-06 в 22.44.06.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-06%20%D0%B2%2022.44.06.png)

3. Появляется сообщение, что рассылка удалена.

- Если удаляется рассылка рассылка в разработке, она сразу исчезает.
- Если удаляется завершённая рассылка, она сначала переходит в статус «Ожидает удаления»:

![Снимок экрана 2021-10-06 в 22.53.05.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-06%20%D0%B2%2022.53.05.png)

И ставится задача:

![Снимок экрана 2021-10-06 в 22.53.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-06%20%D0%B2%2022.53.53.png)

После успешного завершения задачи рассылка удалена.

[Шаблон email-рассылки](https://mindbox.ru/academy/education/shablon-email-rassylok/): как создать и зачем использовать
