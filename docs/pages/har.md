---
title: "Как записать har-файл"
slug: har
source_url: "https://help.mindbox.ru/docs/har"
vcs_path: har.md
toc_path:
  - Администрирование
  - "Проблемы, ошибки и невалидные данные"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:79dd0fb861b468d6b41c3bbfe64097afc0b848eb2e5b0995e7812ddb6b711305"
---

# Как записать har-файл

1. Откройте страницу, на которой возникает проблема.
2. В меню Chrome выберите "Дополнительные инструменты" → "Инструменты разработчика":

![Снимок экрана 2021-08-25 в 12.52.06.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-25%20%D0%B2%2012.52.06.png)

Или используйте горячие клавиши: **Ctrl+Shift+J** (для Windows / Linux) или **Cmd+Opt+J** (для Mac)

3. Откройте вкладку **Network**:

![Снимок экрана 2021-08-25 в 13.05.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-08-25%20%D0%B2%2013.05.52.png)

4. Убедитесь, что запись включена, сбросьте существующие логи и включите опции **Preserve log** и **Disable cache**:

![har-record.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/har-record.png)

5. Обновите страницу и воспроизведите проблему.
6. Кликните по кнопке **Export HAR**:

![har-export.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/har-export.png)

7. Укажите имя файла и сохраните его на диск.

[Для чего нужен email-маркетинг](https://mindbox.ru/academy/education/kakie-zadachi-reshaet-email-marketing/): обзор основных задач
