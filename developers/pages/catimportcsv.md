---
title: csv
slug: catimportcsv
source_url: "https://developers.mindbox.ru/docs/catimportcsv"
breadcrumb:
  - Номенклатура
  - Импорт категорий продуктов
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e085ec4e063e740a174da4309fa243f3827d69ef33061a30b86a7a648f61e9b8"
---

# csv

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса можно получить в системе Майндбокс. Идентификаторы категорий в импорте должны совпадать с идентификаторами категорий, передаваемых в действиях с категориями.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DirectCrm.Retail.ImportProductCategories&csvCodePage=65001&externalSystem={Идентификатор внешней системы}&transactionId={Значение ключа идемпотентности в формате GUID}

Authorization: SecretKey {Секретный ключ}
Accept: application/xml
Content-Type: text/csv;charset=utf-8
```

- csvCodePage - идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter - символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier - символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.
- данный сервис разрешает поставить не более 60 импортов в час. После превышения порога вы будете получать 429 Too Many Requests до тех пор, пока количество поставленных задач за час не опустится ниже 60.
- максимальный размер принимаемого файла 200мб. В случае, если необходимо загрузить больший объем данных, данные нужно разбить на несколько файлов.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| CategoryExternalId | Идентификатор категории |
| ParentCategoryExternalId | Идентификатор родительской категории |
| Name | Название категории |

## Пример запроса

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId=Test&operation=DirectCrm.Retail.ImportProductCategories&csvCodePage=65001&externalSystem=sap-erp

Authorization: SecretKey *********
Accept: application/xml
Content-Type: text/csv

CategoryExternalId;ParentCategoryExternalId;Name
1;;Аудио, видео
2;1;ЭЛТ телевизоры
3;1;Телевизоры
4;1157;DVD плееры
5;1156;Домашние кинотеатры
6;1155;Наушники
7;1158;Кронштейны для телевизоров
8;1156;Музыкальные центры
9;1155;MP3-плееры
10;1156;Акустика
12;1156;Магнитолы
```
