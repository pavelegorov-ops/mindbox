---
title: Выгрузить изменения списков продуктов
slug: "product-list-history-export"
source_url: "https://help.mindbox.ru/docs/product-list-history-export"
vcs_path: "product-list-history-export.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Продукты
  - Списки продуктов
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:0cb28bc0cd5d56bfe7176bf1b63f312fdf5cd52da0c678e9eb60ce5f22d973f6"
---

# Выгрузить изменения списков продуктов

Клиенты могут откладывать продукты в [списки](personal-list.md), например, «Корзину» или «Избранное».

В карточке клиента в виде действий, связанных с продуктом, фиксируются все изменения списков, а именно:

- добавление продукта;
- удаление продукта;
- корректировка данных: изменение стоимости линии или количества продуктов в ней;
- очистка списка.

Для выгрузки этих действий можно использовать стандартный  
экспорт с предустановленными полями или создать собственный экспорт.

## Стандартная выгрузка изменений

1. Выделите нужных клиентов:

![Снимок экрана 2023-12-18 в 17.07.18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-18%20%D0%B2%2017.07.18.png)

2. Нажмите **Экспорт** → **Истории изменения списков продуктов**:

![Снимок экрана 2023-12-18 в 17.07.37.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-18%20%D0%B2%2017.07.37.png)

3. Ставится задача:

![Снимок экрана 2023-12-18 в 17.07.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-18%20%D0%B2%2017.07.48.png)

По ссылке — файл с выгрузкой в формате CSV:

![Снимок экрана 2023-12-18 в 17.15.16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-18%20%D0%B2%2017.15.16.png)

### Какие поля выгружаются

- **ProductListHistoryItemChangeType** — тип изменения.  
  Значения:
  - Add — добавление продукта
  - Remove — удаление продукта
  - Reset — очистка списка
  - Edit — редактирование линии
- **ProductListHistoryItemProductListName**, **ProductListHistoryItemProductListSystemName** — название и системное имя списка продуктов.
- Данные по действию:
  - **ProductListHistoryItemDateTimeUtc** — дата и время.
  - **ProductListHistoryItemChannelIdsMindboxId**, **ProductListHistoryItemChannelName**, **ProductListHistoryItemChannelIdsExternalId**, **ProductListHistoryItemChannelIdsSystemName** — точка контакта (Mindbox Id, название, внешний идентификатор и системное имя).
  - **ProductListHistoryItemBrandIdsSystemName** — бренд.
  - **ProductListHistoryItemChannelUtmCampaign**, **ProductListHistoryItemChannelUtmSource**, **ProductListHistoryItemChannelUtmMedium**, **ProductListHistoryItemChannelUtmContent**, **ProductListHistoryItemChannelUtmTerm** — UTM-метки.
- Данные по клиенту:
  - базовая информация:
    - **ProductListHistoryItemCustomerIdsMindboxId** — ID клиента в Mindbox.
  - **ProductListHistoryItemCustomerIds{Идентификатор}** — внешние идентификаторы клиента.
- Данные по продукту:
  - **ProductListHistoryItemProductIds{Внешняя система}** — внешний идентификатор продукта.

## Пользовательская выгрузка изменений

Пользовательский экспорт создается через заведение операции.

Для этого:

1. На вкладке клиентов нажмите **Экспорт** → **Новый экспорт**:

![Снимок экрана 2023-12-19 в 13.26.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-19%20%D0%B2%2013.26.38.png)

2. Настройте операцию:

![Снимок экрана 2023-12-19 в 23.09.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-19%20%D0%B2%2023.09.43.png)

- точка интеграции — «Административная панель Mindbox»
- шаг «Экспорт — Выгрузить историю изменения списков продуктов»
  - выберите формат экспорта: CSV, JSON или XML
  - выберите данные для экспорта.

Доступные данные для выгрузки и их названия в файле:

- Тип изменения — **ProductListHistoryItemChangeType**  
  Значения:
  - Add — добавление продукта
  - Remove — удаление продукта
  - Reset — очистка списка
  - Edit — редактирование линии
- Список продуктов — **ProductListHistoryItemProductListName**, **ProductListHistoryItemProductListSystemName**
- Данные по действию:
  - Дата и время — **ProductListHistoryItemDateTimeUtc**
  - Точка контакта — **ProductListHistoryItemChannelIdsMindboxId**, **ProductListHistoryItemChannelName**, **ProductListHistoryItemChannelIdsExternalId**, **ProductListHistoryItemChannelIdsSystemName**
  - бренд — **ProductListHistoryItemBrandIdsSystemName**
  - UTM-метки — **ProductListHistoryItemChannelUtmCampaign**, **ProductListHistoryItemChannelUtmSource**, **ProductListHistoryItemChannelUtmMedium**, **ProductListHistoryItemChannelUtmContent**, **ProductListHistoryItemChannelUtmTerm**
- Данные по клиенту:
  - базовая информация
    - ID клиента в Mindbox — **ProductListHistoryItemCustomerIdsMindboxId**
    - ФИО — **ProductListHistoryItemCustomerFirstName**, **ProductListHistoryItemCustomerMiddleName**, **ProductListHistoryItemCustomerLastName**
    - Дата рождения — **ProductListHistoryItemCustomerBirthDate**
    - Пол — **ProductListHistoryItemCustomerSex**
    - Дата последнего редактирования — **ProductListHistoryItemCustomerChangeDateTimeUtc**
    - Таймзона — **ProductListHistoryItemCustomerIanaTimeZone**, **ProductListHistoryItemCustomerTimeZoneSource**
    - Подтвержденность контактов — **ProductListHistoryItemCustomerIsEmailConfirmed**, **ProductListHistoryItemCustomerIsMobilePhoneConfirmed**
    - Валидность контактов — **ProductListHistoryItemCustomerIsEmailInvalid**, **ProductListHistoryItemCustomerIsMobilePhoneInvalid**
    - Зона — **ProductListHistoryItemCustomerAreaName**, **ProductListHistoryItemCustomerAreaIdsExternalId**
  - Email и телефон (в открытом виде, хеш sha256 или md5) — **ProductListHistoryItemCustomerEmail**, **ProductListHistoryItemCustomerMobilePhone**, **ProductListHistoryItemCustomerPendingEmail**, **ProductListHistoryItemCustomerPendingMobilePhone**
  - Внешние идентификаторы клиентов — **ProductListHistoryItemCustomerIds{Идентификатор}**
  - Последняя активированная карта — **ProductListHistoryItemCustomerLastActivatedCardIdsNumber**, **ProductListHistoryItemCustomerLastActivatedCardTypeIdsExternalId**, **ProductListHistoryItemCustomerLastActivatedCardTypeName**, **ProductListHistoryItemCustomerLastActivatedCardStatusIdsSystemName**, **ProductListHistoryItemCustomerLastActivatedCardStatusName**, **ProductListHistoryItemCustomerLastActivatedCardCustomFields{Доп. поле}**
  - Дополнительные поля — **ProductListHistoryItemCustomerCustomFields{Доп. поле}**
- Данные продуктов —
  - Внешние идентификаторы продукта — **ProductListHistoryItemProductIds{Внешняя система}**
  - Базовая информация:
    - Название — **ProductListHistoryItemProductName**
    - Описание — **ProductListHistoryItemProductDescription**
    - Ссылка — **ProductListHistoryItemProductUrl**
    - Ссылка на картинку — **ProductListHistoryItemProductPictureUrl**
    - Цена — **ProductListHistoryItemProductPrice**
    - Старая цена — **ProductListHistoryItemProductOldPrice**
    - Доступность — **ProductListHistoryItemProductIsAvailable**
    - Срок годности — **ProductListHistoryItemProductShelfLife**
    - Код производителя — **ProductListHistoryItemProductVendorCode**
    - Производитель — **ProductListHistoryItemProductVendorIdsExternalId**, **ProductListHistoryItemProductVendorIdsSystemName**, **ProductListHistoryItemProductVendorName**
    - Категории продукта — **ProductListHistoryItemProductCategoriesIds{Внешняя система}**
  - Дополнительные поля — **ProductListHistoryItemProductCustomFields{Доп. поле}**

Данные по продуктам не выгружаются в формате CSV, так как он поддерживает не все типы данных для экспорта. Рекомендуем использовать формат XML или JSON.

3. Сохраните операцию.

Теперь данный экспорт доступен на странице клиентов:

![Снимок экрана 2023-12-19 в 23.14.07.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-19%20%D0%B2%2023.14.07.png)
