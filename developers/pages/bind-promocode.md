---
title: Выдача промокода
slug: "bind-promocode"
source_url: "https://developers.mindbox.ru/docs/bind-promocode"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:7b0145fd6df57e021a3ede78c839b513384f3f22129dee78f77c4d696412dd9f"
---

# Выдача промокода

## Описание метода

Осуществляется с помощью POST-запроса. Название операции и набор принимаемых полей настраиваются в системе Майндбокс. Подробней про вызов метода можно прочитать [здесь](v3.md).

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpoint={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}&{transactionId}={Id транзакции в вашей системе}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

<operation>
    <customer>
        <ids>
            <webSiteUserId>{Идентификатор клиента}webSiteUserId>
        ids>
    customer>
    <promoCode>
        <ids>
            <value>{Значение промокода}value>
        ids>
        <pool>
            <ids>
                <externalId>{Внешний идентификатор}externalId>
            ids>
        pool>
        <availableFromDateTimeUtc>{Дата, с которой доступен промокод в формате YYYY-MM-DD hh:mm:ss.fff}availableFromDateTimeUtc>
        <availableTillDateTimeUtc>{Дата, до которой доступен промомкод в формате YYYY-MM-DD hh:mm:ss.fff }availableTillDateTimeUtc>
    promoCode>
    <executionDateTimeUtc>{Дата и время привязки промокода (для выполнения запроса задним числом)}executionDateTimeUtc>
operation>
```

Параметр transactionId используется только для асинхронных вызовов. Подробнее в [статье](https://help.mindbox.ru/docs/idempotentnost).  
Обязательность узлов promoCode/ids и promoCode/pool зависит от настроек шага операции:

| Получение промокода | promoCode/ids | promoCode/pool |
| --- | --- | --- |
| По значению, создание запрещено | Обязателен | Запрещен |
| По значению, создание разрешено | Обязателен | Обязателен, если не указан в настройках шага операции, иначе запрещен. |
| Получить доступный из пула | Запрещен | Обязателен, если не указан в настройках шага операции, иначе запрещен. |

```
<result>
	<status>{Результат выполнения запроса: Success в случае успеха, ValidationError в случае ошибки пользователя, ProtocolError в случае ошибки интеграции, InternalServerError в случае недоступности сервера.}status>
	<promoCode>
		<issueStatus>{Статус выдачи}issueStatus>
		<ids>
			<mindboxId>{Идентификатор промокода}mindboxId>
			<value>{Значение промокода}value>
		ids>
		<pool>
			<ids>
				<externalId>{Внешний идентификатор}externalId>
			ids>
			<name>{Имя}name>
			<description>{Описание}description>
		pool>
		<availableFromDateTimeUtc>{Дата, с которой доступен промокод в формате YYYY-MM-DD hh:mm:ss.fff}availableFromDateTimeUtc>
		<availableTillDateTimeUtc>{Дата, до которой доступен промомкод в формате YYYY-MM-DD hh:mm:ss.fff }availableTillDateTimeUtc>
		<isUsed>{Погашен ли промокод, значение true или false}isUsed>
		<usedPointOfContact>
			<ids>
				<externalId>{Внешний инденнтификатор}externalId>
			ids>
			<name>{Название точки контакта}name>
		usedPointOfContact>
		<usedDateTimeUtc>{Дата гашения промокода в формате YYYY-MM-DD hh:mm:ss.fff}usedDateTimeUtc>
		<issuedPointOfContact>
			<ids>
				<externalId>{Внешний инденнтификатор}externalId>
			ids>
			<name>{Название точки контакта}name>
		issuedPointOfContact>
		<issuedDateTimeUtc>{Дата выдачи промокода в формате YYYY-MM-DD hh:mm:ss.fff}issuedDateTimeUtc>
		<blockedDateTimeUtc>{Дата блокировки промокода в формате YYYY-MM-DD hh:mm:ss.fff}blockedDateTimeUtc>
	promoCode>
result>
```

| Статус выдачи | Описание |
| --- | --- |
| PromoCodeNotFound | Промокод не найден |
| PromoCodePoolNotFound | Пул промокодов не найден |
| NoAvailablePromoCodesInPool | В пуле отсутствуют доступные к выдаче промокоды |
| NotAvailableForIssue | Не может быть выдан |
| Issued | Выдан |
| NotInIssueDateTimeRange | Дата выдачи не входит в сроки выдачи промокода |
