---
title: "Интеграция чат-ботов в Telegram через Fasttrack"
slug: "chat-bots-integration"
source_url: "https://help.mindbox.ru/docs/chat-bots-integration"
vcs_path: "chat-bots-integration.md"
toc_path:
  - "Чат-боты"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:999dd0c51686972fc2994e8a67d1cdaadbc99ae70945c58896c8e16bea98422d"
---

# Интеграция чат-ботов в Telegram через Fasttrack

Эта инструкция описывает настройку проекта Mindbox для интеграции с чат-ботами на примере Telegram через сервис [Fasttrack](https://fstrk.io/) — конструктор чат-ботов, который позволяет создавать ботов и отправлять через них рассылки.

Для работы с чат-ботами необходимо подключить модуль «Боты и чаты».

Для консультации по поводу подключения модуля обратитесь к менеджеру проекта или консультанту по внедрению: [selickiy@mindbox.cloud](mailto:selickiy@mindbox.cloud).

## Процесс настройки

**Настройка состоит из двух этапов:**

- **Предварительная настройка** (обязательно) — создание сущностей в Mindbox (точки интеграции, папки, сегментов, шаблонов действий и полей)
- **Настройка операций** — создание операций для взаимодействия с API Mindbox:
  - Работа с клиентами (обязательно)
  - Программа лояльности (опционально в зависимости от настроек проекта)
  - Дополнительные методы (опционально)

## Предварительная настройка

### Точка интеграции

[Создайте](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8) точку интеграции со следующими параметрами:

- **Тип**: «Другое»
- **Название**: Интеграция Fasttrack
- **Системное** **имя**: *проект*.Fasttrack

![chat-bots-fasttrack-endpoint.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-endpoint.png)

### Папка кампаний

[Создайте](https://help.mindbox.ru/docs/folders#kak-sozdat-papku) папку, в которой будут храниться сущности для интеграции Fasttrack:

![chat-bots-fasttrack-folder.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-folder.png)

### Шаблоны действий

[Создайте шаблоны действий](https://help.mindbox.ru/docs/template-create) для выдачи в операциях.

**Действие 1. Старт бота:**

- **Название**: Старт бота
- **Папка**: Fasttrack
- **Категория**: Личные действия → Регистрация, авторизация, заполнение или обновление информации о клиенте → Авторизация

![chat-bots-fasttrack-action-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-action-start.png)

**Действие 2. Событие в боте:**

- **Название**: Событие в боте
- **Папка**: Fasttrack
- **Категория**: Личные действия → Потребление контента и просмотр продуктов → Взаимодействие с разделами сайта или мобильного приложения

![chat-bots-fasttrack-action-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-action-event.png)

### Сегментации

[Создайте](https://help.mindbox.ru/docs/segment-actions) реалтаймовые сегментации по действиям, если таких сегментов на проекте еще нет.

1. **[FT] Заказы** — сегментация для получения всех заказов клиента и отображения их в чат-боте.

   ![chat-bots-fasttrack-segment-orders.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-segment-orders.png)
2. **[FT] Изменения баланса** — сегментация для получения всех действий изменения баланса клиента и отображения их в чат-боте.

   ![chat-bots-fasttrack-segment-points.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-segment-points.png)

### Дополнительные поля

[Создайте](https://help.mindbox.ru/docs/additional-data) дополнительные поля по клиентам и действиям. Поля создаются для каждого мессенджера отдельно. Ниже пример полей для Telegram.

**Поля по сущности «Клиенты»:**

1. **TGID** — идентификатор клиента в Telegram.

   - **Тип:** Идентификатор

   ![chat-bots-fasttrack-field-tgid.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-tgid.png)
2. **inbotTG** — информация о нахождении клиента в боте Telegram.

   - **Тип:** Логический

   ![chat-bots-fasttrack-field-inbotTG.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-inbotTG.png)
3. **subTG** — подписка клиента на рассылки в чат-боте в Telegram.

   - **Тип:** Логический

   ![chat-bots-fasttrack-field-subTG.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-subTG.png)

---

**Поля по сущности «Действия клиента»:**

1. **advertID** — идентификатор акции в чат-боте.

   - **Тип**: Перечисление
   - Включите опцию «Создавать значение перечисления, если не найдено»

   ![chat-bots-fasttrack-field-advertID.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-advertID.png)
2. **ChatBotEventType** — тип события в чат-боте.

   - **Тип**: Перечисление
   - Включите опцию «Создавать значение перечисления, если не найдено»

   ![chat-bots-fasttrack-field-ChatBotEventType.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-ChatBotEventType.png)
3. **BotPlatform** — платформа бота.

   - **Тип**: Перечисление
   - Включите опцию «Создавать значение перечисления, если не найдено»

   ![chat-bots-fasttrack-field-BotPlatform.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-field-BotPlatform.png)

## Настройка операций

### Работа с клиентами

Эти операции необходимы для базовой работы интеграции.

[Старт бота](chat-bots-integration.md#operation-BotStart)

Вызывается при первом запуске чат-бота. Создает профиль клиента с идентификаторами чат-бота и дополнительными полями.

- **Имя:** [FT] Старт бота
- **Системное имя:** ft.BotStart
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-BotStart1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-BotStart1.png)

![chat-bots-fasttrack-operation-BotStart2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-BotStart2.png)

---

[Создание клиента](chat-bots-integration.md#operation-CreateCustomer)

Создает нового клиента в системе с подпиской на рассылки в чат-боте или бренде.

- **Имя:** [FT] Создание клиента
- **Системное имя:** ft.CreateCustomer
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-CreateCustomer.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-CreateCustomer.png)

---

[Дополнить клиента](chat-bots-integration.md#operation-FillUpCustomer)

Обновляет информацию о существующем клиенте.

- **Имя:** [FT] Дополнить клиента
- **Системное имя:** ft.FillUpCustomer
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-FillUpCustomer.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-FillUpCustomer.png)

---

[Получить информацию о клиенте](chat-bots-integration.md#operation-GetCustomer)

Возвращает данные профиля клиента. Шаг «Сегментации — Клиент — Проверить принадлежность» необходим, если в чат-боте нужно выводить информацию по принадлежности к какому-либо сегменту.

- **Имя:** [FT] Получить информацию о клиенте
- **Системное имя:** ft.GetCustomer
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-GetCustomer1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-GetCustomer1.png)  
![chat-bots-fasttrack-operation-GetCustomer2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-GetCustomer2.png)  
![chat-bots-fasttrack-operation-GetCustomer3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-GetCustomer3.png)

### Программа лояльности

Операции ниже необходимы для проектов с программой лояльности.

[Список заказов по номеру телефона](chat-bots-integration.md#operation-GetCustomerOrders)

Возвращает историю заказов клиента.

- **Имя:** [FT] Список заказов по номеру телефона
- **Системное имя:** ft.GetCustomerOrders
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-GetCustomerOrders1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-GetCustomerOrders1.png)

![chat-bots-fasttrack-operation-GetCustomerOrders2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-GetCustomerOrders2.png)

---

[Подтвердить телефон (опционально)](chat-bots-integration.md#operation-ConfirmPhone)

Используется, если на проекте есть [подтверждение номера телефона](https://help.mindbox.ru/docs/email-and-mobile-confirmation). Для этого [в точке интеграции](chat-bots-integration.md#endpoint) должна быть включена настройка «Подтверждение мобильного телефона».

- **Имя:** [FT] Подтвердить телефон
- **Системное имя:** ft.ConfirmPhone
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-confirmphone.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-confirmphone.png)

---

[Генерация QR-кода авторизации (опционально)](chat-bots-integration.md#operation-GenerateLoyaltyCode)

Настройте эту операцию, если на проекте применяется динамический QR-код для авторизации. Подробнее в [инструкции](https://developers.mindbox.ru/docs/chat-bots-qr-authentication) для разработчиков.

- **Имя:** [FT] Генерация QR-кода авторизации
- **Системное имя:** ft.GenerateLoyaltyCode
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-ft.GenerateLoyaltyCode1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-ft.GenerateLoyaltyCode1.png)

![chat-bots-fasttrack-ft.GenerateLoyaltyCode2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-ft.GenerateLoyaltyCode2.png)

### Дополнительные методы

Эти операции расширяют функциональность интеграции в зависимости от потребностей проекта.

[Редактировать клиента](chat-bots-integration.md#operation-EditCustomer)

Изменяет данные профиля клиента.

- **Имя:** [FT] Редактировать клиента
- **Системное имя:** ft.EditCustomer
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-Edit.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-Edit.png)

---

[Получить тикет по клиенту](chat-bots-integration.md#operation-GetTicket)

Необходима для реализации [авторизации клиента по ссылке](https://developers.mindbox.ru/docs/chatbot-authorization).

- **Имя:** [FT] Получить тикет по клиенту
- **Системное имя:** ft.GetTicket
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-getticket.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-getticket.png)

---

[Событие в боте](chat-bots-integration.md#operation-ChatBotEvent)

Отслеживает пользовательские события внутри чат-бота.

- **Имя:** [FT] Событие в боте
- **Системное имя:** ft.ChatBotEvent
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-BotEvent.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-BotEvent.png)

---

[Получить рекомендации](chat-bots-integration.md#operation-GetCustomerRecommendations)

Возвращает персональные рекомендации для клиента на основе [настроенного алгоритма](https://help.mindbox.ru/docs/recommendation#sozdanie-algoritma).

- **Имя:** [FT] Получить рекомендации
- **Системное имя:** ft.GetCustomerRecommendations
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-reco.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-reco.png)

---

[Получить сегменты](chat-bots-integration.md#operation-CheckSegment)

Проверяет принадлежность клиента к сегментам для вывода информации о клиенте в чат-боте. Настройки и сегменты зависят от задач проекта.

- **Имя:** [FT] Получить сегменты
- **Системное имя:** ft.CheckSegment
- Требуется передача секретного сервисного ключа
- Шаги:

![chat-bots-fasttrack-operation-ft.CheckSegment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/chat-bots-fasttrack-operation-ft.CheckSegment.png)

## Что дальше

После завершения настройки передайте разработчикам информацию о созданных операциях для настройки взаимодействия с API Mindbox.

Для разработчиков:

- [Методы интеграции](https://developers.mindbox.ru/docs/chat-bots-methods)
- [Авторизация клиента по ссылке из чат-бота](https://developers.mindbox.ru/docs/chatbot-authorization)
- [Генерация QR-кода для аутентификации клиента на сайте](https://developers.mindbox.ru/docs/chat-bots-qr-authentication)
