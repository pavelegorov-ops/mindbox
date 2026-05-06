---
title: Сценарий для опроса после поездки
slug: "workflow-after-travel"
source_url: "https://help.mindbox.ru/docs/workflow-after-travel"
vcs_path: "workflow-after-travel.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:d5b49c673c5dd8e60013c2b361167451291a862cb07d78ea00c23c063d3d23ca"
---

# Сценарий для опроса после поездки

**Задача**: запросить отзыв после завершения поездки.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Отличие от [сценария с опросом](workflow-feedback.md) после доставки в том, что время использования услуги не зависит от времени покупки: билеты могут быть приобретены как за день до поездки, так и за несколько месяцев.  
Поэтому сценарий с рассылкой должен ориентироваться не на дату совершения заказа, а на [время, переданное в заказе](workflow-delay.md#dinamicheskoe). ![Снимок экрана 2024-05-14 в 00.56.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-14%20%D0%B2%2000.56.45.png)

Для реализации механики нужно передавать дату в [дополнительное поле](additional-data.md) заказа, позиции заказа или продукта.  
Выбор зависит от специфики проекта и интеграции.

- Передача даты к заказу позволяет реагировать на переход в любой статус; «ожидание» по позиции доступно только при доставке.
- По заказу указывается одна дата для всего заказа; при использовании доп. поля по позиции можно передавать разные значения для отдельных позиций и запускать для каждой свою цепочку.

В данной статье рассмотрим механику **с передачей даты к заказу**. Сценарий по позиции заказа настраивается по аналогии с [инструкцией](workflow-reminder-before-date.md).

Перед созданием сценария:

- Добавьте автоматическую рассылку в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md).
  - [Параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) для вывода данных по заказу — [Order](%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7-%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD.md). Или используйте [новый конструктор](email-editor.md) для вывода без параметров и кода — [инструкция](new-email-builder-order.md)

Создаем сценарий:

1. Запуск — по событию [Статус заказа изменен](workflow-events.md#status-zakaza-izmenen). [Частота применения](workflow-limit-per-customer.md) к заказу по умолчанию ограничена одним разом — оставляем настройку:

![после поездки-событие.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4%D0%BA%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5.png)

Особенности события

---

Заказ перешел в выбранный статус. В том числе сразу пришел в нужном статусе.

- На заказе, добавленном задним числом, сценарий срабатывает, если он попадает в актуальность группы шагов и если нет изменений по заказу с более поздней датой.
- В статус должны перейти все позиции, которые пришли с созданием заказа. То есть, если одна позиция отменилась, сценарий не запустится. В режиме «Любая позиция заказа перешла» такого ограничения нет.
- Позиции необязательно должны переходить в указанный статус в рамках одного действия. Если изменения по позициям приходят постепенно, сценарий запустится, когда последняя позиция получит нужный статус.
- Можно дополнительно ограничить количество срабатываний в рамках заказа.
- Количество переходов в нужный статус считается с момента запуска сценария. Например, если сценарий должен применяться к заказу один раз и нужный переход произошел до включения сценария, повторное изменение статуса заказа запустит сценарий.

---

2. Ставим динамическое [ожидание](workflow-delay.md#dinamicheskoe):

![после поздки-ожидание.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B7%D0%B4%D0%BA%D0%B8-%D0%BE%D0%B6%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5.png)

3. Проверяем, что [заказ](workflow-conditions.md) актуален и не был отменен:

![после поездки-заказ.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4%D0%BA%D0%B8-%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7.png)

4. Проверяем, что клиент с подпиской и валидным контактом [в канале рассылки](workflow-check-subscription.md):

![после поездки-клиент.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4%D0%BA%D0%B8-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82.png)

5. Отправляем письмо:

![после поездки-шаги.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4%D0%BA%D0%B8-%D1%88%D0%B0%D0%B3%D0%B8.png)

6. Сценарий готов, можно запускать:

![после поздки-готово.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%B7%D0%B4%D0%BA%D0%B8-%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BE.png)

## Дополнительные материалы

- [Опросы клиентов](https://mindbox.ru/journal/education/oprosy-klientov/?utm_source=help&utm_campaign=workflow-after-travel): для чего они нужны и как использовать полученные данные. 11 примеров с рынка
- Как эффективно работать с [отзывами](https://mindbox.ru/journal/education/rabota-s-negativnymi-otzyvami/?utm_source=help&utm_campaign=workflow-after-travel): как отрицательными, так и положительными
- [Отток клиентов](https://mindbox.ru/journal/education/ottok-klientov/?utm_source=help&utm_campaign=workflow-after-travel): как контролировать уход пользователей
- Как собственник отошел от операционки, но сохранил контроль над процессами с помощью обратной связи от клиентов. История [Flor2U](https://mindbox.ru/journal/experts/flor2u/?utm_source=help&utm_campaign=workflow-after-travel)
- Как автоматизировать сбор обратной связи и сделать его инструментом трансформации компании. Рассказывают head of digital marketing и head of customer experience «[Детского мира](https://mindbox.ru/journal/cases/detskij-mir/?utm_source=help&utm_campaign=workflow-after-travel)»
- «[ВсеИнструменты.ру](https://mindbox.ru/journal/cases/vseinstrumenty-ru/?utm_source=help&utm_campaign=workflow-after-travel)» удвоили доход на клиента в email-канале и собирают в шесть раз больше отзывов в месяц
- [XCOM-SHOP](https://mindbox.ru/journal/cases/xcom/?utm_source=help&utm_campaign=workflow-after-travel) построил CRM-маркетинг и повысил выручку email-канала на 4,84% год к году: просьба оставить отзыв — самая конверсионная механика
- «[Сплав](https://mindbox.ru/journal/cases/splav/?utm_source=help&utm_campaign=workflow-after-travel)» меняет восприятие бренда с помощью персонализации коммуникаций: NPS-опрос для реактивации после заказа
- 4% → 8% — доля выручки email-канала. Исполнительный директор магазина техники [Quke](https://mindbox.ru/journal/cases/quke/?utm_source=help&utm_campaign=workflow-after-travel) — о том, как работа с базой помогает не зависеть от маркетплейсов
