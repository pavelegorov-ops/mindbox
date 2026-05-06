---
title: "Как создать чат-бота в Telegram через BotFather"
slug: "chat-bots-telegram"
source_url: "https://help.mindbox.ru/docs/chat-bots-telegram"
vcs_path: "chat-bots-telegram.md"
toc_path:
  - "Чат-боты"
  - "Создание чат-ботов"
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:246de2321f678144a65849e1b1f62dbde6d08d9af39ed020d7a70183b86e35c1"
---

# Как создать чат-бота в Telegram через BotFather

Для работы с чат-ботами необходимо подключить модуль «**Боты и чаты»**.

Для консультации по поводу подключения модуля обратитесь к менеджеру проекта или консультанту по внедрению: [selickiy@mindbox.cloud](mailto:selickiy@mindbox.cloud).

## Создание бота

1. Откройте мессенджер Telegram.
2. Найдите бота `@botfather` через поиск и откройте чат с ним.

   ![chat-bots-botfather-search.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-search.jpg)
3. Нажмите кнопку «СТАРТ», чтобы начать разговор.

   ![chat-bots-botfather-start.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-start.jpg)
4. В нижней части экрана появится кнопка мини‑приложения. Нажмите на кнопку «Open».

   ![chat-bots-botfather-open.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-open.jpg)
5. Нажмите кнопку «Create a New Bot»:

   ![chat-bots-botfather-create.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-create.jpg)
6. Заполните данные:

   - **Name** — отображаемое имя бота (например, «Интернет‑магазин Example»).
   - **Username** — укажите уникальное имя бота на латинице, которое **заканчивается на bot** (например, example_shop_bot).

   ![chat-bots-botfather-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-settings.png)
7. Подтвердите создание бота. BotFather создаст бота и сгенерирует для него API-токен. Скопируйте токен по кнопке «Copy».

## Как получить API-токен бота

Важно

Токен используется для подключения бота к Mindbox. Не передавайте токен третьим лицам.

1. Откройте мини‑приложение BotFather.
2. В списке выберите нужного бота. Откроется его карточка с настройками.

   ![chat-bots-botfather-list.jpeg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-list.jpeg)
3. Скопируйте токен по кнопке «Copy»:

   ![chat-bots-botfather-token-copy.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-token-copy.jpg)

## Как перевыпустить токен

Перевыпуск токена может понадобиться в случае его компрометации или утери. **После перевыпуска старый токен перестанет работать.**

1. Откройте карточку бота в мини-приложении BotFather.
2. В блоке с токеном нажмите **Revoke**.
3. Подтвердите действие. Будет сгенерирован новый токен, а старый перестанет работать.

![chat-bots-botfather-token-revoke.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-botfather-token-revoke.jpg)
