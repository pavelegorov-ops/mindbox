---
title: Выгрузка черного списка
slug: "blocklist-export-contacts"
source_url: "https://help.mindbox.ru/docs/blocklist-export-contacts"
vcs_path: "blocklist-export-contacts.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Клиенты
  - Контакты и идентификаторы
  - Черный список контактов
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:360c9a52274d8b95cc2160f0a5370bcda0ebe476b2e323a656a9125a70e871bb"
---

# Выгрузка черного списка

Чтобы выгрузить [черный список](blocklist.md):

1. На вкладке **Данные** → **Клиенты** в меню нажмите «Выгрузить черный список»:

![Снимок экрана 2022-11-23 в 15.58.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-23%20%D0%B2%2015.58.19.png)

2. Создается задача на экспорт:

![Снимок экрана 2022-11-23 в 16.01.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-23%20%D0%B2%2016.01.43.png)

3. По ссылке — файл с данными:

![Снимок экрана 2022-11-23 в 16.02.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-23%20%D0%B2%2016.02.08.png)

Поля в файле выгрузки:

- **FakeContactContact** — некорректный контакт;
- **FakeContactContactType** — тип контакта:
  - Email — email-адрес;
  - MobilePhone — мобильный номер;
  - ExternalIdentity — [идентификатор клиента](additional-data.md);
  - Device — [идентификатор устройства](deviceuuid.md);
  - DiscountCardNumber — номер дисконтной карты.
- **FakeContactCustomFieldSystemName** — системное имя идентификатора для типа контакта ExternalIdentity;
- **FakeContactCreationDateTimeUtc** — дата и время попадания в список;
- **FakeContactDescription** — [причина](blocklist.md#prichiny-popadaniya-v-chs) попадания в список:
  - *«Базовый список некорректных контактов»*
  - *«Превышение лимита редактирований или объединений (N раз за час)»*
  - *«Массовая операция — Импорт черного списка. ID задачи N»*

Если не указаны время или причина

- У контактов, попавших в список до 20 декабря 2023 года через импорт или превышение лимита, время и причина попадания не отображаются.
- У некорректных контактов в базовом списке причина выводится всегда. Время попадания соответствует созданию проекта и отображается только на проектах, созданных после 20 декабря 2023 года.

Пример файла экспорта:

![Снимок экрана 2024-02-07 в 11.28.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-07%20%D0%B2%2011.28.13%281%29.png)
