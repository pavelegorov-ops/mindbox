---
title: Создание и редактирование внешней промоакции
slug: "save-external-promotion"
source_url: "https://developers.mindbox.ru/docs/save-external-promotion"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:caa3b53a6ecccad79cb8e6c045595c450d54e1cb8fa969080d8f162759a0a5f3"
---

# Создание и редактирование внешней промоакции

## Описание метода

Операция позволяет создать или отредактировать внешнюю промоакцию в системе Майндбокс. Если промоакции с таким идентификатором еще нет в системе Майндбокс, она будет создана, иначе – отредактирована.

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpoint={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
  <promotion>
    <ids>
      <externalId>{Внешний идентификатор промоакции}externalId>
    ids>
    <type>externaltype>
    <name>{Название внешней промоакции}name>
    <description>{Описание внешней промоакции}description>
    <startDateTimeUtc>{Дата и время начала действия акции в часовом поясе UTC+0}startDateTimeUtc>
    <endDateTimeUtc>{Дата и время окончания акции в часовом поясе UTC+0}endDateTimeUtc>
  promotion>
operation>
```
