---
title: Интеграция с Shopify
slug: "shopify-integration"
source_url: "https://help.mindbox.ru/docs/shopify-integration"
vcs_path: "shopify-integration.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:324ae05baaaad1dd78103acbafc45a52be165f2c9ec771b36d1b2675d09372e9"
---

# Интеграция с Shopify

## Интеграция Shopify

[Shopify](https://www.shopify.com/) — платформа для создания собственного интернет-магазина.  
Возможности интеграции:

- создание и обновление данных по клиенту;
- создание и обновление данных по заказу;
- передача авторизации клиента в личном кабинете на сайте;
- передача событий просмотра товаров и категорий;
- передача событий удаления и добавления товаров в корзину;
- передача продуктов и категорий из Shopify, если нет товарной номенклатуры в [yml-формате](https://developers.mindbox.ru/docs/prodimportxml).

## Настройки в Mindbox

Нужно завести в Mindbox:

- [статусы позиций заказов](%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-shopify.md#sozdanie-statusov-pozicij-zakazov), которые будут приходить из Shopify;
- [список корзины](%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-shopify.md#sozdanie-spiska-produktov%D0%B2):
- [идентификаторы клиентов и заказов](%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-shopify.md#sozdanie-identifikatorov-klientov-i-zakazov);
- [точку интеграции Shopify](%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-shopify.md#sozdanie-tochki-integracii);
- [операции для передачи данных](%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%81-shopify.md#sozdanie-operacij).

Если на проекте уже созданы сущности с нужными настройками и именами, **их можно переиспользовать**.

### Создание статусов позиций заказов

Добавьте [статусы позиций заказов](how-to-add-the-status-of-an-order-item.md) с системными именами **Created**, **Canceled**, **Paid**, **Delivered**.

![Снимок экрана 2023-08-22 в 10.37.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-22%20%D0%B2%2010.37.35.png)

### Создание списка продуктов

Добавьте [список продуктов](personal-list.md) «Корзина»:

![Снимок экрана 2023-08-22 в 10.25.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-22%20%D0%B2%2010.25.36%281%29.png)

### Создание идентификаторов клиентов и заказов

Добавьте [дополнительные поля](additional-data.md) нужного типа с указанными системными именами:

- Для клиентов — **ShopifyCustomerId**:

![image15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image15%281%29.png)

- Для заказов — **ShopifyOrderId**:

![image6.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image6%284%29.png)

### Создание точки интеграции

Добавьте отдельную [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) с системным названием в формате «название проекта.Shopify».

![image20.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image20%281%29.png)

![image13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image13%282%29.png)

### Создание операций

Для операций Shopify можно создать отдельную [папку](folders.md) или добавить точку интеграции Shopify в уже существующие операции с нужными настройками.

- Передача просмотра категорий.

Системное имя операции — в формате «системное имя проекта.ViewCategory».

![image12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image12%281%29.png)

- Передача просмотра продукта.

Системное имя операции — в формате «системное имя проекта.ViewProduct».

![image1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image1%286%29.png)

- Передача корзины продуктов.

Системное имя операции — в формате «системное имя проекта.SetCart».

![image3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image3%284%29.png)

- Передача клиентов и обновление информации по ним.

Системное имя операции — в формате «системное имя проекта.ImportClientOperation».

![image4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image4%284%29.png)

- Передача заказов и обновление информации по ним.

Системное имя операции — в формате «системное имя проекта.IdentifyCustomerAndUpdateOrder».

![image10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image10%281%29.png)

- Передача авторизаций клиента в личном кабинете на сайте.

Системное имя операции — в формате «системное имя проекта.Authorize».

![image11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image11%282%29.png)

## Настройки в Shopify

1. В кабинете Shopify перейдите на страницу «App and sales channel settings» в раздел «Develop apps».

![image8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image8%282%29.png)

![image17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image17%281%29.png)

2. Создайте приложение в кабинете — нажмите на «Create an app».

![image5.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image5%283%29.png)

3. Введите название приложения «Mindbox integration» и нажмите «Создать приложение».

![image7.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image7%285%29.png)

4. В созданном приложении перейдите в «Configure Admin API scopes» и укажите доступы по списку ниже. Сохраните.

- write_customers
- read_draft_orders
- read_orders
- read_products
- read_product_feeds
- read_products_listing
- read_customers

![image24.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image2%284%29%281%29.png)

![image19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image19%281%29.png)

5. Дальше перейдите в «API credentials» и установите приложение по кнопке «Install app».

![image16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image16%283%29.png)

![image18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image18%282%29.png)

6. Сформируется токен, который нужен для подключения. Нажмите на «Reveal token once», чтобы посмотреть его.

**Важно:** обязательно запишите токен. Второй раз токен нельзя будет посмотреть и скопировать.

![image92.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image9%282%29%281%29.png)

7. Предайте токен установки в поддержку Mindbox или вашему менеджеру. После этого коллеги настроят интеграцию в течение пяти рабочих дней.

Пример формата токена: `shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
