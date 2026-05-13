---
title: Объединение клиентов по запросу
slug: "on-demand-customer-merging"
source_url: "https://developers.mindbox.ru/docs/on-demand-customer-merging"
breadcrumb:
  - Клиент
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:2d5a380953cd33c7374312fc8f8c6273c964abfad9a8ad33ba0522d9cc0f291a"
---

# Объединение клиентов по запросу

В инструкции описаны **примеры** POST-запросов. Интеграция с Mindbox не будет работать, если использовать запросы из примеров ниже без редактирования.

Операции именно под вашу задачу создает и описывает в техническом задании менеджер проекта, если у вас нет такого документа, то обратитесь к вашему менеджеру.

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <customersToMerge>
    <customer>
      <ids>
        <webSiteId>{Id первого клиента}webSiteId>
      ids>
    customer>
    <customer>
      <ids>
        <webSiteId>{Id второго клиента}webSiteId>
      ids>
    customer>
  customersToMerge>
  <resultingCustomer>
    <ids>
      <webSiteId>{Id результирующего клиента}webSiteId>
    ids>
  resultingCustomer>
operation>
```

В `resultingCustomer` надо передавать клиента, в которого хотим объединить. В `customersToMerge` - остальных клиентов, которых надо объединить с `resultingCustomer`. Все переданные клиенты уже должны быть в БД, чтобы произошло объединение.

## Пример операции

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=MergeCustomer

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <customersToMerge>
    <customer>
      <ids>
        <webSiteId>11webSiteId>
      ids>
    customer>
    <customer>
      <ids>
        <webSiteId>22webSiteId>
      ids>
    customer>
  customersToMerge>
  <resultingCustomer>
    <ids>
      <webSiteId>33webSiteId>
    ids>
  resultingCustomer>
operation>
```

В результате выполнения данной операции клиенты с идентификаторами 11 и 22 будут объединены в клиента с идентификатором 33.

## Ответ

#### Ответ, если все клиенты есть

```
Content-Type: application/xml

<result>
  <status>Successstatus>
  <customersToMerge>
    <customer>
      <processingStatus>FoundprocessingStatus>
      <ids>
        <webSiteId>11webSiteId>
      ids>
    customer>
    <customer>
      <processingStatus>FoundprocessingStatus>
      <ids>
        <webSiteId>22webSiteId>
      ids>
    customer>
  customersToMerge>
  <resultingCustomer>
    <processingStatus>MergedprocessingStatus>
    <ids>
      <webSiteId>33webSiteId>
    ids>
  resultingCustomer>
result>
```

#### Ответ, если некоторых клиентов нет
