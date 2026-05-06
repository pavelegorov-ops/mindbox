---
title: Как обработать события в прошлом в сценарии с большим ожиданием
slug: "workflow-events-before-launch"
source_url: "https://help.mindbox.ru/docs/workflow-events-before-launch"
vcs_path: "workflow-events-before-launch.md"
toc_path:
  - Сценарии
  - Разные настройки сценария
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:b2cd3d73081e74286bf3bdcd8433fca9f4036719c981c91567b409ba6f5ce44f"
---

# Как обработать события в прошлом в сценарии с большим ожиданием

Сценарий применяется только к тем событиям, которые пришли, [пока он был запущен](workflow-client-flow.md#sobytijnyj-scenarij).  
Если в сценарии используется длительное ожидание, то первые срабатывания по клиентам появятся лишь через заложенное время.

> ![Снимок экрана 2024-09-03 в 15.54.17](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.54.17.png)  
> *После запуска сценария первые письма начнут отправляться не раньше чем через год.*

**Задача:** настроить сценарий с длительным ожиданием и также отработать по подходящим событиям, которые произошли до включения сценария.

**Решение:** параллельно с основным сценарием запустить временный периодический — для отработки по старым событиям.

В качестве примера настроим механику для ежегодного напоминания о прохождении техобслуживания.

## Основной сценарий

![Снимок экрана 2024-09-03 в 15.54.17](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.54.17.png)

1. Запуск — после оплаты:

![Снимок экрана 2024-09-03 в 15.50.44](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.50.44.png)

2. Проверяем, что в заказе есть нужный товар:

![Снимок экрана 2024-09-03 в 15.51.02](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.51.02.png)

3. Ожидание — 365 дней:

![Снимок экрана 2024-09-03 в 15.51.36](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.51.36.png)

4. Проверяем, что заказ не был отменен:

![Снимок экрана 2024-09-03 в 15.51.53](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.51.53.png)

5. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md) и ещё не совершил повторный заказ:

![Снимок экрана 2024-09-03 в 15.52.39](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.52.39.png)*Дополнительно можно добавить условие, что клиент не получал напоминания за последние сутки, чтобы избежать пересечения со вторым сценарием.*

6. Отправляем рассылку:

![Снимок экрана 2024-09-03 в 15.52.54](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.52.54.png)

7. Ограничиваем частоту применений:

![Снимок экрана 2024-09-03 в 15.53.35](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.53.35.png)

## Сценарий для обработки исторических событий

![Снимок экрана 2024-09-03 в 15.54.42](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.54.42.png)

1. Запуск — [по расписанию](workflow-schedule.md).

Проверяем, что у клиента:

- есть заказ с нужным товаром 365 дней назад;
- нет повторного заказа;
- не было отправки напоминания за последние сутки (чтобы избежать пересечения с основным сценарием);
- есть подписка и контакт [в канале рассылки](workflow-check-subscription.md).

![Снимок экрана 2024-09-03 в 16.22.44.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2016.22.44.png)

2. Отправляем ту же рассылку:

![Снимок экрана 2024-09-03 в 15.52.54](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.52.54.png)

3. Задаем дату [окончание работы](what-is-workflow.md#vremya-raboty-scenariya) сценария (через 366 дней) и ограничиваем частоту применений к клиенту:

![Снимок экрана 2024-09-03 в 15.54.55](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2015.54.55.png)

Данный сценарий остановится автоматически.
