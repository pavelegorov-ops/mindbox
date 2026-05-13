---
title: Обновление информации о категории
slug: "update-product-category"
source_url: "https://developers.mindbox.ru/docs/update-product-category"
breadcrumb:
  - Номенклатура
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6a14643d5775f1d52f411c8c5b8c4250fe2d2bdb2ab20fa06e62232d7a4e6e71"
---

# Обновление информации о категории

## Описание метода

Осуществляется с помощью POST-запроса. Название операции настраивается в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

#### XML

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <productCategory>
    <ids>
      <{Наименование идентификатора}>{Идентификатор категории в системе }
    ids>
    <parentCategory>
      <ids>
        <{Наименование идентификатора}>{Идентификатор родительской категории в системе }
      ids>
    parentCategory>
    <name>{Наименование категории}name>
  productCategory>
operation>
```

#### JSON

## Пример операции

#### Пример вызова XML

```
POST https://api.mindbox.ru/v3/operations/sync?endpointId=MindboxRu&operation=SaveCategory

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey D061p764m85bklq

<operation>
  <productCategory>
    <ids>
      <webSiteId>10webSiteId>
    ids>
    <parentCategory>
      <ids>
        <webSiteId>1webSiteId>
      ids>
    parentCategory>
    <name>Категория 10name>
  productCategory>
operation>
```

#### Пример вызова JSON

## Ответ

#### XML

```
<result>
<status>Successstatus>
result>
```

#### JSON
