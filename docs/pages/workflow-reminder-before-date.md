---
title: "Сценарий-напоминание о начале занятия или лекции"
slug: "workflow-reminder-before-date"
source_url: "https://help.mindbox.ru/docs/workflow-reminder-before-date"
vcs_path: "workflow-reminder-before-date.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:03184c03e8ec2c97a5dcdcb44ff31ca1ddf848806acec3bb03a4266b6269f7aa"
---

# Сценарий-напоминание о начале занятия или лекции

**Задача**: на сайте можно записаться к преподавателям; нужно отправлять напоминание ученикам за день и за 15 минут до занятий.

Для решения задачи настроим [сценарий](what-is-workflow.md).

**Реализация механики**: предметы добавлены на проект как продукты, запись на занятия передается как заказ, а время начала каждого занятия — [дополнительное поле](additional-data.md) по позиции.

![Снимок экрана 2023-07-24 в 12.13.57.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2012.13.57.png)

Если время занятия передается в дополнительном поле **заказа**, а не позиции, настройте сценарий по аналогии с [инструкцией](workflow-after-travel.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода предмета (продукта) — [OrderItem](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82-%D0%B8%D0%B7-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0-%D1%81%D0%BA%D0%BE%D1%80%D0%BE-%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD%D1%87%D0%B8%D1%82%D1%81%D1%8F.md)

Создаем сценарий:

1. Запуск — по событию [«Продукт в заказе доставлен»](workflow-events.md#produkt-v-zakaze-dostavlen):

![workflow-reminder-before-date-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-reminder-before-date-start.png)

Особенности события

---

- Запускается **только** по статусу доставки. Для отработки по другим статусам оно не подходит.
- Срабатывает по позиции, даже если она сразу пришла в данном статусе.
- Запускается на каждую доставленную позицию, даже если они пришли в одном заказе. То есть доставка заказа с двумя позициями запустит сценарий два раза.
- Работает **повторно** по позиции, если что-то в ней поменялось (цена, количество, дополнительные поля).
- На заказах, добавленных задним числом, сценарий срабатывает, но действие должно попадать в актуальность группы шагов и не должно быть изменений по позиции с более поздней датой.
- Событие можно дополнительно ограничить по статусу заказа в категории «Доставлено» и по сегментам доставленного продукта.

---

Если время занятия передается дополнительным полем не к позиции, а **к заказу**, настройка сценария будет отличаться в двух моментах:

- событие — [Новый заказ](workflow-events.md#novyj-zakaz), [Данные заказа изменены](workflow-events.md#dannye-zakaza-izmeneny) или [Статус заказа изменен](workflow-events.md#status-zakaza-izmenen);
- ожидание — по дополнительному полю заказа.

2. [Ожидание](workflow-delay.md#dinamicheskoe) — за сутки до начала занятия:

![workflow-reminder-before-date-1h-delay.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-reminder-before-date-1h-delay.png)

3. Проверяем, что занятие не отменено:

![Снимок экрана 2023-07-24 в 11.31.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2011.31.30.png)

4. И что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2023-07-24 в 11.36.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2011.36.31.png)

Если рассылка об оплаченном занятии транзакционная, проверять подписку и контакт не надо.

5. Отправляем письмо:

![Снимок экрана 2023-07-24 в 12.16.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2012.16.01.png)

6. Второе «ожидание» — за 15 минут до начала:

![workflow-reminder-before-date-15m-delay.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-reminder-before-date-15m-delay.png)

7. [Дублируем](what-is-workflow.md#massovoe-kopirovanie-i-udalenie-blokov) проверки:

![Снимок экрана 2023-07-24 в 11.31.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2011.31.30.png)

![Снимок экрана 2023-07-24 в 11.36.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2011.36.31.png)

8. Отправляем финальное напоминание:

![Снимок экрана 2023-07-24 в 12.17.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-24%20%D0%B2%2012.17.28.png)

9. Сценарий готов, можно запускать:

![workflow-reminder-before-date-result.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/workflow-reminder-before-date-result.png)
