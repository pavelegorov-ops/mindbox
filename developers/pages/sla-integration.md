---
title: Интеграция с сервисом SLA
slug: "sla-integration"
source_url: "https://developers.mindbox.ru/docs/sla-integration"
breadcrumb:
  - Разное
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6e44250c707d910d59e5577b6386736cc1603e120942fa6b8ef1e8a6f2131a66"
---

# Интеграция с сервисом SLA

### Ограничения по использованию сервиса

Сервис поддерживает только последнюю версию SLA, размещенную на сайте mindbox.ru

Получить информацию о нарушении SLA можно по адресам:

- <https://sla.mindbox.ru/v1/client> - для клиентов в РФ
- <https://sla.mindbox.cloud/v1/client> - для зарубежных клиентов

Схема авторизации - `Basic`.

```
GET https://sla.mindbox.ru/v1/client

Authorization: Basic <base64 encoded string>
```

Где `base64 encoded string` - строка вида `username:password`, закодированная в `base64`.

Для авторизации нужно указать любую точку интеграции (Endpoint) вашего проекта Mindbox, где:  
`username` - внешний идентификатор точки интеграции (обязателен)  
`password` - секретный ключ точки интеграции (обязателен)

Ответ сервиса содержит информацию об нарушении SLA в формате метрик `prometheus`.

```
# HELP sla_violation 
# TYPE sla_violation gauge
sla_violation{feature="Personalization",tenant="mindbox-client"} 0
sla_violation{feature="CalculationDiscounts",tenant="mindbox-client"} 0
sla_violation{feature="CalculationDiscountsDegradation",tenant="mindbox-client"} 0
sla_violation{feature="PersonalArea",tenant="mindbox-client"} 0
sla_violation{feature="OrderProcessing",tenant="mindbox-client"} 0
sla_violation{feature="OrderProcessingDegradation",tenant="mindbox-client"} 0
sla_violation{feature="DisplayingWidgets",tenant="mindbox-client"} 0
sla_violation{feature="MailingsSendingSpeed", tenant="mindbox-client"} 0
sla_violation{feature="TransactionalWorkflow", tenant="mindbox-client"} 0
```

Если значение одной из метрик равно 1 - то, в данный момент, SLA нарушается.

Сервис возможно интегрировать с `prometheus`, см. инструкцию <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config>

На данный момент, сервис возвращает нарушения SLA только для синхронных интеграций (sync при вызове операции Mindbox):

- `Personalization` - синхронные вызовы операций персонализации
- `CalculationDiscounts` - синхронные вызовы расчета скидок и баллов в корзине
- `CalculationDiscountsDegradation` - синхронные вызовы расчета скидок и баллов в корзине (деградация)
- `PersonalArea` - синхронные вызовы операций, требуемых для отображения клиентских интерфейсов
- `OrderProcessing` - синхронные вызовы операций для процессинга заказов
- `OrderProcessingDegradation` - синхронные вызовы операций для процессинга заказов (деградация)
- `DisplayingWidgets` - отображения виджетов рекомендаций
- `MailingsSendingSpeed` - скорость массовых рассылок
- `TransactionalWorkflow` - транзакционные сообщения после заказа из сценариев

Нарушения `CalculationDiscountsDegradation` и `OrderProcessingDegradation` соответствуют следующему пункту SLA:

- Error Rate синхронных вызовов Операций для расчета скидок и баллов в корзине и Операций для процессинга заказов больше 0,005 при T = 4 сек за сутки; ошибка — код ответа 500 или 503

см. <https://mindbox.ru/documents/sla/>
