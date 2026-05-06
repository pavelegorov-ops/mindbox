---
title: Сценарий «Ваш заказ оформлен»
slug: "workflow-order-created"
source_url: "https://help.mindbox.ru/docs/workflow-order-created"
vcs_path: "workflow-order-created.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:aeddfdb01f15683df5896c3af04e102eae8de8a2324649220effe5e71bd829a0"
---

# Сценарий «Ваш заказ оформлен»

**Задача**: сообщить клиенту о создании заказа.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md);
  - Так как отправляется техническое сообщение о статусе заказа, установите профиль рассылки «Транзакционный»
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода информации о заказе — [Order](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7-%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](new-email-builder-order.md)

Создаем сценарий:

1. Запуск — по событию [Новый заказ](workflow-events.md#novyj-zakaz):

![workflow-order-created-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-order-created-event.png)

Особенности события

---

- На заказе, добавленном задним числом, сценарий срабатывает, если он попадает в актуальность группы шагов и если нет изменений по заказу с более поздней датой.

---

2. Событие срабатывает при создании заказа в базе с любым статусом, поэтому можно добавить проверку [статуса заказа](workflow-conditions.md):

![Снимок экрана 2024-05-14 в 00.05.46.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-14%20%D0%B2%2000.05.46%281%29.png)

Если механика должна запускаться только при переходе **в определенный статус**, используйте событие [Статус заказа изменен](workflow-events.md#zakaz-dobavlen-ili-izmenen).

3. Отправляем письмо:

![Снимок экрана 2022-07-31 в 17.21.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-31%20%D0%B2%2017.21.01.png)

> Клиент обязательно должен получить данную рассылку, поэтому у нее транзакционный статус и проверка на валидность и подписку клиента не нужна.

4. [Транзакционный сценарий](workflow-transactional.md) готов, можно запускать:

![Снимок экрана 2023-12-27 в 12.14.18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-27%20%D0%B2%2012.14.18%281%29.png)

[Что такое автоматическая рассылка](https://mindbox.ru/academy/education/chto-takoe-triggernaya-rassylka/) и чем она отличается от массовой
