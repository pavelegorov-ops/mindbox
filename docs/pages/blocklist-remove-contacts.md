---
title: Удаление из черного списка
slug: "blocklist-remove-contacts"
source_url: "https://help.mindbox.ru/docs/blocklist-remove-contacts"
vcs_path: "blocklist-remove-contacts.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Клиенты
  - Контакты и идентификаторы
  - Черный список контактов
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:e8f93be39d69c3d1506a9be8cdc334e875f15682cb01e84c896dc2f04e207850"
---

# Удаление из черного списка

Чтобы убрать контакт из [черного списка](blocklist.md):

1. На вкладке **Данные** → **Клиенты** нажмите «Импорт» → «Импорт клиентов»:

![Снимок экрана 2022-06-08 в 19.26.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-08%20%D0%B2%2019.26.45.png)

2. Выберите операцию «Удаление из черного списка»:

![Снимок экрана 2024-10-10 в 14.57.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-10-10%20%D0%B2%2014.57.33.png)*Для скачивания доступен шаблон с примером. Также на странице появляются данные по всем возможным полям для загрузки: их название, описание и обязательность с примерами принимаемых форматов.*

3. Подготовьте файл.

Формат — .csv  
Кодировка — по умолчанию utf-8. Можно проверить кодировку своего файла с помощью редакторов вроде Notepad++, VS Code и т.д.

Поля для заполнения:

- **ContactType** — тип контакта, который будет удален из списка; обязательное поле. Доступные типы:
  - Email — email-адрес;
  - MobilePhone — мобильный номер;
  - ExternalIdentity — [идентификатор клиента](additional-data.md); его системное имя задается в CustomFieldSystemName;
  - Device — [идентификатор устройства](deviceuuid.md);
  - DiscountCardNumber — номер дисконтной карты;
- **Contact** — сам контакт; обязательное поле;
- **CustomFieldSystemName** — системное имя идентификатора; обязательное поле для типа контакта ExternalIdentity.

Пример заполненного файла:

![Снимок экрана 2022-11-23 в 15.56.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-23%20%D0%B2%2015.56.41.png)

4. Загрузите файл и поставьте задачу:

![blocklist-remove-contacts-launch.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/blocklist-remove-contacts-launch.png)

- Появляется ссылка на задачу:

![Снимок экрана 2022-09-08 в 22.28.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-09-08%20%D0%B2%2022.28.54.png)

После успешного завершения задачи контакты будут удалены из списка.
