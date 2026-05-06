---
title: Как настроить каскадную рассылку с помощью сценария
slug: "workflow-cascade"
source_url: "https://help.mindbox.ru/docs/workflow-cascade"
vcs_path: "workflow-cascade.md"
toc_path:
  - Сценарии
  - Разные настройки сценария
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:1da91a0d8f0cf2e4eea18562a8ad1a916dc51fa006b6b9e24adfb0db13b467f4"
---

# Как настроить каскадную рассылку с помощью сценария

## Принцип работы каскада

- каждое последующее сообщение уходит, только если с клиентом не удалось связаться на предыдущих этапах каскада;
- сначала отправляются бесплатные email, мобильный пуш и/или вебпуш, затем — платные Viber и/или SMS;
- цепочка останавливается, как только хотя бы одно сообщение перешло в статус «Доставлено» или клиент выполнил целевое действие.

## Алгоритм настройки каскада

1. Выберите, какие каналы будут использоваться.
2. Определите порядок каналов в каскаде. Учитывайте стоимость сообщений и отклик клиентов в разных каналах.
3. Придумайте логику каскада: корневое событие, которое запускает весь сценарий, и события для перехода на второй и последующий этапы.

Есть несколько вариантов условий для перехода к следующему этапу каскада:

- **Недоставка или неотправка в предыдущем канале.**

Этот способ позволяет отправить сообщение максимальному количеству клиентов на имеющийся у них контакт.

- **Нет открытия в предыдущем канале за X времени.**

Нужно не просто доставить сообщение, а убедиться, что клиент его увидел, возможно, даже перешел по ссылке. Не подходит для каналов без отслеживания открытий (SMS, Viber, MobilePush, и сторонние системы, которые не могут прислать сигнал об открытии).

- **Клиент не совершил целевое действие за X времени.**

Целевым действием может быть заказ, регистрация на сайте, заполнение анкеты. Подходит для задач, в которых нужно провести клиента по длинному процессу покупки или сбора данных.

4. Настройте сценарий — на каждом этапе отправляется сообщение в заданный канал.

### Схема отправки

#### Этап первый: мобильный пуш и/или email

![image](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-02%20%D0%B2%2015.21.45.png)

![image](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-02%20%D0%B2%2015.22.12.png)

#### Этап второй: Viber

![image](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-02%20%D0%B2%2014.43.53.png)

#### Этап третий: SMS

![Снимок экрана 2021-09-02 в 14.44.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-02%20%D0%B2%2014.44.27%281%29.png)

## Пример сценария

Настроим сценарий для отправки уведомления по изменению статуса заказа.  
Используем каналы email, Viber и SMS. Если нет контакта или получаем недоставку, пробуем следующий канал.

![Снимок экрана 2024-09-03 в 19.57.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2019.57.07.png)

#### Этап первый — Email

![Снимок экрана 2024-09-03 в 19.57.07 — копия 1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2019.57.07%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F%201.png)

1. Запуск — после оформления заказа:

![Снимок экрана 2024-09-03 в 19.50.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2019.50.35.png)

2. [Проверяем контакт и подписку](workflow-check-subscription.md) в email:

![Снимок экрана 2024-09-03 в 20.07.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.07.41.png)

3. Отправляем email:

![Снимок экрана 2024-09-03 в 20.11.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.11.26.png)

4. Ждем 5 минут:

![Снимок экрана 2024-09-03 в 20.11.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.11.51.png)

5. Проверяем, [была ли неотправка или недоставка](filter-clients-mailing.md) в канале:

![Снимок экрана 2024-09-03 в 20.12.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.12.43.png)

Если да, переходим ко второму этапу.

#### Этап второй — Viber

В эту ветку попадают клиенты:

- у которых нет почты или подписки в email;
- которым не удалось доставить email.

![Снимок экрана 2024-09-03 в 19.57.07 — копия 2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2019.57.07%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F%202.png)

6. Проверяем контакт и подписку в Viber:

![Снимок экрана 2024-09-03 в 20.16.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.16.02.png)

7. Отправляем Viber:

![Снимок экрана 2024-09-03 в 20.16.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.16.42.png)

8. Ждем 5 минут:

![Снимок экрана 2024-09-03 в 20.17.29.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.17.29.png)

9. Проверяем, была ли неотправка или недоставка в канале:

![Снимок экрана 2024-09-03 в 20.18.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.18.08.png)

Если да, переходим к третьему этапу.

#### Этап третий — SMS

В эту ветку попадают клиенты:

- у которых нет контакта или подписки в Viber;
- которым не удалось доставить Viber.

![Снимок экрана 2024-09-03 в 19.57.07 — копия 3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2019.57.07%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F%203.png)

10. Проверяем контакт и подписку в SMS:

![Снимок экрана 2024-09-03 в 20.23.05.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.23.05.png)

11. Отправляем SMS:

![Снимок экрана 2024-09-03 в 20.24.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-03%20%D0%B2%2020.24.03.png)

---

## Дополнительные материалы

- [Сначала бесплатные email, только затем дорогие SMS: как благодаря каскадным рассылкам сократить расходы на коммуникацию в 2 раза и добиться open rate ~100%](https://mindbox.ru/journal/education/kaskadnye-rassylki/?utm_source=help&utm_campaign=workflow-cascade)
- Как спрогнозировать эффект от внедрения каскадных коммуникаций. Опыт DIY-ритейлера [«Петрович»](https://mindbox.ru/journal/experts/prognoz-effecta-kaskady/?utm_source=help&utm_campaign=workflow-cascade)
- [«Магнит Доставка»](https://mindbox.ru/journal/cases/magnit-dostavka/?utm_source=help&utm_campaign=workflow-cascade) получает 20% выручки из CRM-канала: мобильные пуши, каскадные сценарии, AB-тесты и NPS-опросы
- 40% → 65% — конверсия в первую покупку. Как [«КуулКлевер»](https://mindbox.ru/journal/cases/coolclever/?utm_source=help&utm_campaign=workflow-cascade) превращает лида в покупателя
- 8,7% → 16,2% — доля выручки от CRM-канала. Интернет-магазин [«Акушерство»](https://mindbox.ru/journal/cases/akusherstvo/?utm_source=help&utm_campaign=workflow-cascade) перешел от массовых пушей к сегментации и каскадным сценариям
- [BetBoom](https://mindbox.ru/journal/cases/betboom/?utm_source=help&utm_campaign=workflow-cascade) повысил retention в 2,4 раза с помощью сегментации по жизненному циклу, каскадных рассылок и персонализации

- [Как собирать базу email-подписчиков в онлайне](https://mindbox.ru/academy/education/kak-sobirat-bazu-podpischikov/) — 10 реальных механик
- Сначала бесплатные email, только затем дорогие SMS: как благодаря [каскадным рассылкам](https://mindbox.ru/journal/education/kaskadnye-rassylki/) сократить расходы на коммуникацию в 2 раза и добиться open rate ~100%
