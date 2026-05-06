---
title: Отменить гашение промокода
slug: "cancel-promocode-redemption"
source_url: "https://developers.mindbox.ru/docs/cancel-promocode-redemption"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0024099d81d25ed74c18a11599723d2863f5eeebf5be104b148b511cc4068484"
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
