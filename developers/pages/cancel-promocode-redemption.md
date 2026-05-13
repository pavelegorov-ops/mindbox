---
title: Отменить гашение промокода
slug: "cancel-promocode-redemption"
source_url: "https://developers.mindbox.ru/docs/cancel-promocode-redemption"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:581679d044489939474a4a2d32d863d58cc2338b4cce86291f2816f24a1f20ad"
---

# Отменить гашение промокода

## Описание метода

В настройках операции при добавлении шага необходимо указать шаблон действия, с которым будет происходить отмена гашения промокода. В операции должен быть шаг “Клиент”.

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
	promoCode>
operation>
```

Параметр transactionId используется только для асинхронных вызовов. Подробнее в [статье](https://help.mindbox.ru/docs/idempotentnost).
