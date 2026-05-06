---
title: Сценарий для реактивации по открытиям писем
slug: "workflow-reactivate-open"
source_url: "https://help.mindbox.ru/docs/workflow-reactivate-open"
vcs_path: "workflow-reactivate-open.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ecce88b4cdc93414021f2d402fd826ef99a910f6e47bab26138884d48ff98079"
---

# Сценарий для реактивации по открытиям писем

**Задача**: вернуть подписчиков, которые давно не открывали письма.

**Решение**: отправить с помощью [сценария](what-is-workflow.md) рассылки, мотивирующие неактивных пользователей вновь читать письма от бренда.

Перед созданием сценария:

- Добавьте автоматические рассылки в [email-канале](email-trigger.md).

Создаем сценарий:

1. Запуск — [по расписанию](workflow-schedule.md), раз в сутки.

Проверяем, что раньше клиент открывал письма, но в последнее время перестал, хотя отправки были; а также валидность контакта и подписку [в канале](workflow-check-subscription.md):

![Снимок экрана 2024-09-05 в 08.11.00](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2008.11.00.png)

2. Отправляем первую рассылку:

![Снимок экрана 2024-09-05 в 08.12.20](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2008.12.20.png)

Что отправить в рассылке

Подписчиков можно заинтересовать полезным контентом, маркетинговыми играми, подарками.  
Если отписываете неактивных пользователей, сообщите об этом в письме — это может мотивировать клиентов, которые хотят и дальше получать рассылки от бренда.

Для открытия письма важны в первую очередь тема и прехедер — **определите лучший вариант с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md)**.

3. Ждем 3 дня:

![Снимок экрана 2024-09-05 в 08.13.08](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2008.13.08.png)

4. Проверяем, были ли открытия, и что клиенту ещё можно отправлять письма:

![Снимок экрана 2024-09-05 в 09.07.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2009.07.02.png)

5. Отправляем вторую рассылку:

![Снимок экрана 2024-09-05 в 08.15.14](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2008.15.14.png)

Для дополнительной мотивации можно выдать [промокод](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md) или начислить [баллы](balances-create.md) и указать эту информацию в теме.

В таком случае нужно будет добавить третье письмо с напоминанием о сгорании бонусов, если ими ещё не воспользовались.

6. В стартовом блоке ограничиваем [частоту срабатываний](workflow-limit-per-customer.md) по клиенту:

![Снимок экрана 2024-09-05 в 08.22.05](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2008.22.05.png)

В фильтре расписания условия заданы таким образом, что клиенты могут повторно попадать в сценарий только при открытии рассылки и только через 180 дней. Поэтому задавать частоту применений необязательно.

Но при других настройках механики это ограничение может быть необходимым, чтобы она не запускалась несколько дней подряд.

Сценарий готов, можно запускать:

![Снимок экрана 2024-09-05 в 09.09.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2009.09.26.png)

## Дополнительные материалы

- [Как составить кликабельную тему письма путем компонентного анализа](https://mindbox.ru/journal/experts/klikabelnaya-tema-pisma/?utm_source=help&utm_campaign=workflow-reactivate-open)
- [Как написать письмо для продающей рассылки, которое клиент захочет открыть](https://mindbox.ru/journal/education/prodayushee-pismo-dlya-rassylki/?utm_source=help&utm_campaign=workflow-reactivate-open)
- [Геймификация в бизнесе: как маркетинговые игры увеличивают продажи](https://mindbox.ru/journal/education/gejmifikaciya-v-biznese/?utm_source=help&utm_campaign=workflow-reactivate-open)
- + 10 п. п. к retention rate рассылок за счет работы с базой: как в [Бизнес-секретах](https://mindbox.ru/journal/cases/secrets-t-bank/?utm_source=help&utm_campaign=workflow-reactivate-open) удерживают и реактивируют читателей
- Продавать не продавая: как [VIVA LA VIKA](https://mindbox.ru/journal/cases/massovaja-rassylka-viva-la-vika/?utm_source=help&utm_campaign=workflow-reactivate-open) увеличила конверсию с помощью массовых информационных рассылок
- [ZARINA](https://mindbox.ru/journal/cases/zarina-mailings/?utm_source=help&utm_campaign=workflow-reactivate-open) зарабатывает с контентной рассылки в 2,5 раза больше, чем с акционной
- 6 AB-тестов [Synergetic](https://mindbox.ru/journal/experts/synergetic-ab-test/?utm_source=help&utm_campaign=workflow-reactivate-open) для роста open rate, CTR и конверсии в заказ
- Контент вместо скидок, сегменты по интересам. Экологичный email-маркетинг приносит [«Аудиомании»](https://mindbox.ru/journal/cases/audiomania-email/?utm_source=help&utm_campaign=workflow-reactivate-open) 7% выручки

[Механики персонализации](https://mindbox.ru/academy/mechanics/unikalnye-mehaniki-personalizaczii-sajta/) — используйте идеи механик персонализации сайта наших клиентов из разных индустрий.
