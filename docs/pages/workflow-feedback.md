---
title: Сценарий «Пройдите опрос / оставьте отзыв»
slug: "workflow-feedback"
source_url: "https://help.mindbox.ru/docs/workflow-feedback"
vcs_path: "workflow-feedback.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:a32633e8685456c0af43717eb25825299e52d3a4bd7783f2c1746dfc2f930076"
---

# Сценарий «Пройдите опрос / оставьте отзыв»

**Задача**: отправить коммуникацию после доставки с просьбой оценить заказ или оставить отзыв на стороннем ресурсе.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md);
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода информации о заказе — [Order](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7-%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](new-email-builder-order.md)

Создаем сценарий:

1. Запуск — по событию [Статус заказа изменен](workflow-events.md#status-zakaza-izmenen):

![Снимок экрана 2024-02-12 в 19.07.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2019.07.23.png)

Особенности события

---

Заказ перешел в выбранный статус. В том числе сразу пришел в нужном статусе.

- На заказе, добавленном задним числом, сценарий срабатывает, если он попадает в актуальность группы шагов и если нет изменений по заказу с более поздней датой.
- В статус должны перейти все позиции, которые пришли с созданием заказа. То есть, если одна позиция отменилась, сценарий не запустится. В режиме «Любая позиция заказа перешла» такого ограничения нет.
- Позиции необязательно должны переходить в указанный статус в рамках одного действия. Если изменения по позициям приходят постепенно, сценарий запустится, когда все позиции получат нужный статус.
- Можно дополнительно ограничить количество срабатываний в рамках заказа.
- Количество переходов в нужный статус считается с момента запуска сценария. Например, если сценарий должен применяться к заказу один раз и нужный переход произошел до включения сценария, повторное изменение статуса заказа запустит сценарий.

---

2. Ставим [задержку](workflow-delay.md), чтобы клиент успел воспользоваться товаром, и ограничиваем выход из блока ожидания, чтобы не отправлять письма ночью:

![Снимок экрана 2021-09-29 в 18.37.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.37.08.png)

3. Проверяем, что у клиента есть подписка и валидный контакт [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-09-29 в 18.38.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.38.30.png)

4. Отправляем письмо, если клиент подходит под условия:

![Снимок экрана 2021-09-29 в 18.40.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.40.50.png)

5. В стартовом блоке ограничьте [частоту срабатываний](workflow-limit-per-customer.md) по клиенту:

![Снимок экрана 2021-09-29 в 18.42.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.42.10.png)

6. Сценарий готов, можно запускать:

![Снимок экрана 2021-09-29 в 18.42.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.42.27.png)

## Дополнительные материалы

- [Опросы клиентов](https://mindbox.ru/journal/education/oprosy-klientov/?utm_source=help&utm_campaign=workflow-feedback): для чего они нужны и как использовать полученные данные. 11 примеров с рынка
- Как эффективно работать с [отзывами](https://mindbox.ru/journal/education/rabota-s-negativnymi-otzyvami/?utm_source=help&utm_campaign=workflow-feedback): как отрицательными, так и положительными
- [Отток клиентов](https://mindbox.ru/journal/education/ottok-klientov/?utm_source=help&utm_campaign=workflow-feedback): как контролировать уход пользователей
- Как собственник отошел от операционки, но сохранил контроль над процессами с помощью обратной связи от клиентов. История [Flor2U](https://mindbox.ru/journal/experts/flor2u/?utm_source=help&utm_campaign=workflow-feedback)
- Как автоматизировать сбор обратной связи и сделать его инструментом трансформации компании. Рассказывают head of digital marketing и head of customer experience «[Детского мира](https://mindbox.ru/journal/cases/detskij-mir/?utm_source=help&utm_campaign=workflow-feedback)»
- «[ВсеИнструменты.ру](https://mindbox.ru/journal/cases/vseinstrumenty-ru/?utm_source=help&utm_campaign=workflow-feedback)» удвоили доход на клиента в email-канале и собирают в шесть раз больше отзывов в месяц
- [XCOM-SHOP](https://mindbox.ru/journal/cases/xcom/?utm_source=help&utm_campaign=workflow-feedback) построил CRM-маркетинг и повысил выручку email-канала на 4,84% год к году: просьба оставить отзыв — самая конверсионная механика
- «[Сплав](https://mindbox.ru/journal/cases/splav/?utm_source=help&utm_campaign=workflow-feedback)» меняет восприятие бренда с помощью персонализации коммуникаций: NPS-опрос для реактивации после заказа
- 4% → 8% — доля выручки email-канала. Исполнительный директор магазина техники [Quke](https://mindbox.ru/journal/cases/quke/?utm_source=help&utm_campaign=workflow-feedback) — о том, как работа с базой помогает не зависеть от маркетплейсов
- 7,92% — инкрементальный прирост из CRM-канала. Как в [«Много лосося»](https://mindbox.ru/journal/cases/mnogolososya/?utm_source=help&utm_campaign=workflow-feedback) сегментируют базу, выбирают офферы и автоматизируют рассылки

[Как собирать базу email-подписчиков в онлайне](https://mindbox.ru/academy/education/kak-sobirat-bazu-podpischikov/) — 10 реальных механик
