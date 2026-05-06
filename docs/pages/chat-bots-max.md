---
title: "Создание и подключение чат-бота в Max"
slug: "chat-bots-max"
source_url: "https://help.mindbox.ru/docs/chat-bots-max"
vcs_path: "chat-bots-max.md"
toc_path:
  - "Чат-боты"
  - "Создание чат-ботов"
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:d8bfef6f3cc3fe07c78d04a5ea76451a497ecdbe4a6e1e4540e68cd04fd2107d"
---

# Создание и подключение чат-бота в Max

Для консультации по подключению модуля и завершению настроек обратитесь к менеджеру проекта или консультанту по внедрению: [selickiy@mindbox.cloud](mailto:selickiy@mindbox.cloud).

Чтобы отправлять рассылки в мессенджер Max, необходимо создать чат-бота на платформе Max и подключить его через провайдер Fasttrack. После этого вы сможете настраивать рассылки в Mindbox.

## Что нужно для подключения

- Профиль организации на платформе Max ([зарегистрироваться](http://business.max.ru/self/));
- Личный кабинет в [Fasttrack](https://fstrk.io/);
- Подключенный модуль «Чаты и боты» в Mindbox. [Как подключить модуль](https://help.mindbox.ru/docs/billing-modules#vklyuchit-i-vyklyuchit-modul).

## Создание чат-бота в Max

Следуйте [**официальной инструкции Max**](https://dev.max.ru/docs/chatbots/bots-create) для создания чат-бота.

1. Зарегистрируйтесь на платформе Max;
2. [Подключите организацию](https://dev.max.ru/docs/maxbusiness/connection) к платформе;
3. Перейдите в профиль созданной организации;
4. Нажмите «Создать» в блоке «Чат-боты» на главной странице или перейдите в раздел «Чат-боты»:

   ![chat-bots-max-create.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-max-create.png)
5. Заполните обязательные поля:

   - Имя бота — видно пользователям в Max (до 59 символов)
   - Ник — отображается в ссылке на чат-бота:
     - Должен заканчиваться на `_bot` или `bot`
     - Начинается с маленькой буквы
     - 11 — 60 символов
     - Может содержать только латиницу, цифры и символ `_`
   - Логотип:
     - Размер: 500×500 px.
     - До 5 Мб
     - Допустимые форматы: JPG, JPEG, PNG
   - Описание бота (до 200 символов)

**Модерация**

После создания чат-бота отправляется на проверку. Модерация занимает **до 48 часов в рабочие дни**. После ее завершения будут доступны расширенные настройки и токен доступа.

## Подключение к Fasttrack

Следуйте [документации Fasttrack](https://docs.fstrk.io/knowledge_base/channels/max) для подключения.

1. Перейдите в профиль организации Max в раздел «Чат-боты»;
2. В блоке «Интеграция» нажмите «Получить токен»:

   ![chat-bots-max-token.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-max-token.png)
3. Скопируйте токен из поля «Токен доступа»:

   ![chat-bots-max-token-copy.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-max-token-copy.png)
4. Перейдите [в настройки подключения мессенджера Max](https://my.fstrk.io/account/login/?next=/bots/update/config/max/) в личном кабинете Fasttrack;
5. Вставьте скопированный токен в поле «Токен» и сохраните настройки:

   ![chat-bots-max-token-fasttrack.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-max-token-fasttrack.png)
