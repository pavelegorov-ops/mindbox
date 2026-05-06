---
title: Экспорт объединений клиентов
slug: "export-customer-merges"
source_url: "https://developers.mindbox.ru/docs/export-customer-merges"
breadcrumb:
  - Экспорты
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:7982947ea8318ff8edb78dd01779f0cce0b291a1ebc420e1fa762f54c4db1d34"
---

# Экспорт объединений клиентов

Данный экспорт работает без постановки задачи на экспорт, а с помощью синхронных запросов с пагинацией.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Mindbox. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customerMergesPage>
    <pageNumber>{Номер страницы, начиная с 1 (не более 2147484)}pageNumber>
    <itemsPerPage>{Количество элементов на странице (не более 10000)}itemsPerPage>
    <sinceDateTimeUtc>{Левая граница времени изменения клиента (включительно)}sinceDateTimeUtc>
    <tillDateTimeUtc>{Правая граница времени изменения клиента (не включительно). Правая граница должна быть как минимум на пять минут меньше текущего времени.}tillDateTimeUtc>
  customerMergesPage>
  <executionDateTimeUtc>{Дата и время выполнения (для выполнения запроса задним числом)}executionDateTimeUtc>
operation>
```

- Такой запрос вернет всех клиентов, которые были объединены с даты 'sinceDateTimeUtc' по дату 'tillDateTimeUtc'.
- Страницы нумеруются с 1.
- Максимальное количество клиентов на страницу - 10000.

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=MergedCustomers

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p664m85bklq

<operation>
  <customerMergesPage>
    <pageNumber>1pageNumber>
    <itemsPerPage>500itemsPerPage>
    <sinceDateTimeUtc>2018-09-16 16:46:58.639sinceDateTimeUtc>
    <tillDateTimeUtc>2018-09-18 16:46:58.639tillDateTimeUtc>
  customerMergesPage>
  <executionDateTimeUtc>2018-10-17 16:46:58.639executionDateTimeUtc>
operation>
```

Запрос вернет первые 500 клиентов, которые были объединены с 16 по 18 сентября 2018 года.

## Ответ

```
Content-Type: application/xml; charset=utf-8

<result>
  <status>Successstatus>
  <customerMerges>
    <customerMerge>
      <resultingCustomer>
        <ids>
          <mindboxId>1810454157mindboxId>
          <tehID>338838091tehID>
          <userwebsiteid>76026058userwebsiteid>
          <vkID>qoaPVvkID>
        ids>
        <changeDateTimeUtc>2018-09-18 20:46:58.670changeDateTimeUtc>
      resultingCustomer>
      <mergedCustomers>
        <mergedCustomer>
          <ids>
            <mindboxId>1289531450mindboxId>
            <tehID>773732863tehID>
            <userwebsiteid>1820856461userwebsiteid>
            <vkID>sZHHbaQjvkID>
          ids>
        mergedCustomer>
        <mergedCustomer>
          <ids>
            <mindboxId>1795392557mindboxId>
            <tehID>338838091tehID>
            <userwebsiteid>1575884755userwebsiteid>
            <vkID>qoaPVvkID>
          ids>
        mergedCustomer>
      mergedCustomers>
    customerMerge>
    <customerMerge>
      <resultingCustomer>
        <ids>
          <mindboxId>1811914583mindboxId>
          <tehID>634419423tehID>
          <userwebsiteid>1205088101userwebsiteid>
          <vkID>PosalSc5IvkID>
        ids>
        <changeDateTimeUtc>2018-09-17 18:46:58.670changeDateTimeUtc>
      resultingCustomer>
      <mergedCustomers>
        <mergedCustomer>
          <ids>
            <mindboxId>285524710mindboxId>
            <tehID>1121596055tehID>
            <userwebsiteid>485794984userwebsiteid>
            <vkID>PosalSc5IvkID>
          ids>
        mergedCustomer>
        <mergedCustomer>
          <ids>
            <mindboxId>40879857mindboxId>
            <tehID>792267062tehID>
            <userwebsiteid>664153368userwebsiteid>
            <vkID>yU9uER8vkID>
          ids>
        mergedCustomer>
      mergedCustomers>
    customerMerge>
  customerMerges>
result>
```
