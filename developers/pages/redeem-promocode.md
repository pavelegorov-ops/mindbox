---
title: Погасить промокод
slug: "redeem-promocode"
source_url: "https://developers.mindbox.ru/docs/redeem-promocode"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:f8057c09caa5e5e6ee957c1149e976bb7c8ffd303c6c0e49c8632184431b3d9e"
---

# Погасить промокод

## Описание метода

В настройках операции при добавлении шага необходимо указать шаблон действия, с которым будет происходить гашение промокода. В операции должен быть шаг “Клиент”.

```
POST https://api.mindbox.ru/v3/operations/{синхронная/асинхронная операция}?endpoint={уникальный идентификатор сайта/мобильного приложения/и т.п.}&operation={название операции}&deviceUUID={уникальный идентификатор устройства}&{transactionId}={Id транзакции в вашей системе}

Accept: application/xml
Content-Type: application/xml
Authorization: SecretKey {Секретный ключ, обязательность уточнить у менеджера}

	
		
			{Идентификатор клиента}
		
	
	
		
			{Значение промокода}
		
		{Дата гашения промокода в формате YYYY-MM-DD hh:mm:ss.fff}
```

Параметр transactionId используется только для асинхронных вызовов. Подробнее в [статье](https://help.mindbox.ru/docs/idempotentnost).
