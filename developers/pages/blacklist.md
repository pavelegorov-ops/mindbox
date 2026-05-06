---
title: Черный список контактов
slug: blacklist
source_url: "https://developers.mindbox.ru/docs/blacklist"
breadcrumb:
  - Клиент
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e00314293ee94dd0eb44bf7565b75665a5143d9a8b2504bd930dc89e3ab29fa6"
---

# Черный список контактов

Изменение списка некорректных контактов.

## Описание метода

Осуществляется с помощью POST-запроса. Адрес запроса и набор принимаемых полей настраиваются в системе Майндбокс.

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=ImportFakeContacts&csvCodePage=65001&transactionId={Значение ключа идемпотентности в формате GUID}
Content-Type: text/csv;charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}
```

**Параметры запроса**

- endpointId - точка доступа, из которой будут взяты настройки интеграции. Значение настраивается в системе.
- transactionId - ключ идемпотентности, позволяющий избежать повторного выполнения запроса. Ключ идемпотентности обязательно создавать в формате GUID (рекомендуется версия 4). Для повторных запросов c повторяющимся ключом в ответ вернется статус `TransactionAlreadyProcessed`.

## Описание полей

| Заголовок | Описание |
| --- | --- |
| ContactType | Тип контакта. Возможные варианты:  - Email — email - MobilePhone — мобильный номер - ExternalIdentity — уникальный идентификатор; его системное имя задается в CustomFieldSystemName - Device — идентификатор устройства - DiscountCardNumber — номер дисконтной карты |
| Contact | Сам контакт |
| CustomFieldSystemName | Системное имя идентификатора; обязательное поле для типа контакта ExternalIdentity |

## Пример запроса внесение контактов в черный список

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=ImportFakeContacts&csvCodePage=65001
Content-Type: text/csv;charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}
Contact;ContactType;CustomFieldSystemName
1@1.RU;Email;
fale@fake.ru;Email;
77777777777;MobilePhone;
78888888888;MobilePhone;
111111;ExternalIdentity;WebsiteID
844fcf8b-783c-4297-a0ad-ec5ee966a962;Device;
```

## Пример запроса удаления контактов из черного списка

```
POST https://api.mindbox.ru/v3/operations/bulk?endpointId={уникальный идентификатор сайта и т.п.}&operation=DeleteFakeContacts&csvCodePage=65001
Content-Type: text/csv;charset=utf-8
Accept: application/json
Authorization: SecretKey {Секретный ключ}
Contact;ContactType;CustomFieldSystemName
1@1.RU;Email;
fale@fake.ru;Email;
78005553535;MobilePhone;
78004453535;MobilePhone;
111111;ExternalIdentity;WebsiteID
844fcf8b-783c-4297-a0ad-ec5ee966a962;Device;
```
