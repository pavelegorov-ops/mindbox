---
title: xml
slug: prodimportxml
source_url: "https://developers.mindbox.ru/docs/prodimportxml"
breadcrumb:
  - Номенклатура
  - Импорт продуктов
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:68ae1cbe9f0ce5a510256095ae532e1a327628a970c77f46af2e8f16410e2d1c"
---

# xml

## Описание формата

Умеем обновлять товарную номенклатуру из yml-файлов раз в несколько часов. YML (Yandex Market Language) — это стандарт, разработанный Яндексом для принятия и размещения информации в базе данных Яндекс.Маркета. YML основан на стандарте XML.
Подробнее о формате можно прочитать [здесь](https://yandex.ru/support/marketplace/ru/assortment/auto/yml)

## Особенности

- Алгоритмы товарных рекомендаций могут работать не более чем с 5 000 000 офферов.
- Категоризация на сайте должна совпадать с категоризацией в yml.
- Идентификаторы товаров и категорий из yml должны совпадать с идентификаторами товаров и категорий в заказах, действиях с продуктами и действиях с категориями.
- Необходимо выгружать всю товарную номенклатуру - товары в наличии и товары не в наличии, передавать с этими статусами нужно в одном фиде.
- Если ранее заполненное в фиде поле не передается при новой загрузке, оно затрется для:
  - дополнительных полей с настройкой «Затирать, если передано пустое значение»;
  - всех системных полей, кроме названия продукта (`name`).
- Если товарная номенклатура в рознице и на сайте отличается - нужно в yml добавить товары из розницы.
- Если цены и доступности в регионах различаются, для каждого региона необходим свой yml-фид.
- В региональных фидах не обрабатываются поля: vendorCode (артикул), shelfLife (срок годности в днях), categories (внешние идентификаторы категорий продукта), groupId (идентификатор группы продуктов).
- Дополнительные поля к продукту добавляются в узлы `значение дополнительного поля` или `значение дополнительного поля`, где `customField` - системное имя дополнительного поля.
- Один продукт может принадлежать к нескольким категориям.
- В случае sku в узле  `id` — идентификатор sku, `group_id` — идентификатор родительского продукта.
- Поле `offer id` не больше 200 символов.
- Поле `description` должно содержать не более 10 000 символов. Если символов больше, продукт не будет добавлен на проект.
- Множественные значения передаются через | . Например, `Вечерние|Коктейльные`.
- Максимальный размер файла 1,5гб.
- Фид должен быть доступен по прямой ссылке, без использования редиректов.
- Доступны только стандартные протоколы http/https и порты 80/443. Если файл защищен авторизацией, обязательно должен использоваться протокол https.
- Поддерживается формат GZIP. Для этого веб-сервер должен вернуть либо заголовки `Content-Encoding: gzip` и `Content-Type: text/xml`, либо заголовок `Content-Type: application/x-gzip`.
- В заголовке `Content-Type` параметр `charset` должен быть задан согласно [стандарту](https://www.iana.org/assignments/character-sets/character-sets.xhtml). Например, utf-8 вместо utf8.

## Виды offer'ов

Существует несколько видов offer'ов в yml. Выделяем упрощенный (1), произвольный (2) и другие (3):

1. Для упрощенного offer'а атрибут  не передается. Название продукта берется из узла .
2. Для произвольного offer'а атрибут `type="vendor.model"`. Название составляется из узлов , , , `< VendorCode >`, например:
   `Смартфон`
   `Apple`
   `iPhone 6s 128gb розовое золото`
   В результате в имени отображается: `Смартфон Apple iPhone 6s 128gb розовое золото`.
   Если после импорта название продукта не соответствует , скорее всего, это произвольный offer, который передается с `type="vendor.model"`. Чтобы это исправить, нужно убрать `type="vendor.model"` из yml-фида.
3. Mindbox поддерживает и другие типы offer'ов: book, audiobook, medicine, event-ticket, tour. Принимаем его как упрощенный (1) и берем имя из . [Подробнее](https://yandex.ru/support/marketplace/ru/assortment/fields/) о типах offer.

## Пример файла

#### Импорт продуктов и категорий

```
</spanxml version="1.0" encoding="UTF-8"?>
<yml_catalog date="2016-02-05 17:22">
<shop>
  <name>ABCname>
  <company>ABC inc.company>
  <url>http://www.abc.ru/url>
  <currencies>
    <currency id="RUR" rate="1"/>
    <currency id="USD" rate="80"/>
  currencies>
  <categories>
    <category id="1278">Электроникаcategory>
    <category id="3761" parentId="1278">Телевизорыcategory>
    <category id="1553" parentId="3761">Медиа-плеерыcategory>
    <category id="3798">Бытовая техникаcategory>
    <category id="1293" parentId="3798">Холодильникиcategory>
  categories>
  <delivery-options>
    <option cost="500" days="0" order-before="15"/>
    <option cost="300" days="1-3"/>
  delivery-options>
  <cpa>1cpa>
  <offers>
    <offer id="158" available="true" bid="80" cbid="90">
      <url>http://www.abc.ru/158.htmlurl>
      <price>55690price>
      <oldprice>56000oldprice>
      <costPrice>53690costPrice>
      <currencyId>RURcurrencyId>
      <categoryId>1293categoryId>
      <categoryId>1278categoryId>
      <picture>http://www.abc.ru/1580.jpgpicture>
      <store>falsestore>
      <delivery>truedelivery>
      <name>Смартфон Apple iPhone 6s 128gb Space Grayname>
      <vendor>Applevendor>
      <model>iPhone 6s 128gb Space Graymodel>
      <description>Описание товара 1description>
      <sales_notes>Необходима предоплата 50%sales_notes>
      <age>0age>
      <manufacturer_warranty>falsemanufacturer_warranty>
      <period-of-validity-days>P10Yperiod-of-validity-days>
      <param name="Тип">моноблокparam>
      <param name="Материал">алюминийparam>
      <param name="Wi-Fi">естьparam>
      <param name="Размер экрана">27param>
      <param name="Размер оперативной памяти">4096param>
      <param name="Объём жесткого диска">1param>
      <param name="Вес">13.8param>
    offer>
    <offer id="159" available="true" cbid="90">
      <url>http://www.abc.ru/159.htmlurl>
      <price>3045.5price>
      <costPrice>2945.0costPrice>
      <currencyId>RURcurrencyId>
      <categoryId>1278categoryId>
      <picture>http://www.abc.ru/1590.jpgpicture>
      <store>falsestore>
      <delivery>truedelivery>
      <name>Наушники Koss Sporta Proname>
      <vendor>Kossvendor>
      <model>Sports Promodel>
      <description>Описание товараdescription>
      <sales_notes>Покупка в день заказаsales_notes>
      <cpa>0cpa>
      <delivery-options>
        <option cost="1000" days="1" order-before="15"/>
      delivery-options>
      <age>0age>
      <manufacturer_warranty>truemanufacturer_warranty>
      <period-of-validity-days>P10Yperiod-of-validity-days>
      <param name="Тип">12344param>
      <param name="Материал">пластикparam>
      <param name="Wi-Fi">даparam>
      <param name="Размер экрана">27param>
      <param name="Размер оперативной памяти">4096param>
      <param name="Объём жесткого диска">1param>
      <param name="Вес">13.8param>
    offer>
  offers>
shop>
yml_catalog>
```

#### Импорт SKU и категорий

## Полезные материалы

[Bitrix - Подключаемся к Яндекс Маркету](https://dev.1c-bitrix.ru/help-assist/yandeks_market/)
