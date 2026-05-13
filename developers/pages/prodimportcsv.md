---
title: csv
slug: prodimportcsv
source_url: "https://developers.mindbox.ru/docs/prodimportcsv"
breadcrumb:
  - Номенклатура
  - Импорт продуктов
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:b86a0f3c5f5e724589eaf6077f8315918043919dce8396b8560dc7139bfaea4c"
---

# csv

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса можно получить в системе Майндбокс. Идентификаторы товаров в импорте должны совпадать с идентификаторами товаров, передаваемых в заказах и действиях с продуктом.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId=`{уникальный идентификатор сайта и т.п.}`&operation=ImportProducts&csvCodePage=65001&externalSystem=`{Идентификатор внешней системы}`&transactionId=`{Значение ключа идемпотентности в формате GUID}`

Authorization: SecretKey `{Секретный ключ}`
Accept: application/json
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- brand - опциональный параметр, обязательный для передачи на мультибрендовых проектах.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| Пример: WebsiteId | Идентификатор товара. Обязательное поле |
| Name | Наименование |
| Description | Описание |
| Categories (Пример: CategoryWebsiteId) | Идентификатор категории товара. Через запятую можно передать несколько категорий. |
| GroupId | Идентификатор группы товаров |
| IsAvailable | Доступен ли товара в данный момент |
| Url | Ссылка на страницу с описанием товара на сайте |
| PictureUrl | Ссылка на изображение товара |
| Price | Цена продукта |
| OldPrice | Старая цена продукта |
| CostPrice | Себестоимость продукта |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId=Test&operation=ImportProducts&csvCodePage=65001&externalSystem=sap-erp

Authorization: SecretKey ***********
Accept: application/xml
Content-Type: text/csv;charset=utf-8

WebsiteId;Name;CategoriesWebsite;ManufacturerName;IsAvailable;Price;CostPrice;Url;PictureUrl
89;Автомагнитола Kenwood KDC-W707Y;50;Kenwood;;;;
105;Коаксиальная автоакустика Panasonic CJ-A1323N;40;Panasonic;;;;
169;Электрический чайник Philips HD4665/20;27;Philips;1;4390;;
219;Телевизор Rolsen C21SR74NT;3;Rolsen;;;;
242;Стиральная машина Electrolux EWC 1350;18;Electrolux;;;;
274;Автомагнитола Alpine CDA-9857R;50;Alpine;;;;
299;Щипцы Rowenta CF2012;1221;Rowenta;1;1660;;
```
