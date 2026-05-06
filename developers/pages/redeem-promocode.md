---
title: Погасить промокод
slug: "redeem-promocode"
source_url: "https://developers.mindbox.ru/docs/redeem-promocode"
breadcrumb:
  - Промокоды и промоакции
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:8ad4fc3c15c877aad21bc8d5913b24a174a3f50dc1872fafc679e105f925bf2d"
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
