---
title: Отложенное сохранение заказа (процессинг)
slug: "processing-offline-order"
source_url: "https://developers.mindbox.ru/docs/processing-offline-order"
breadcrumb:
  - Заказы
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:4c391560b79c1086988ebdc40693da63e45e893e700c52f9cd982560daa9a87c"
---

# Отложенное сохранение заказа (процессинг)

## Описание метода

Операция для передачи заказа в случае, если во время оформления (пробития чека) Mindbox был недоступен.

При вызове операции:

- Могут быть начислены баллы
- Не применяются скидки Mindbox.
- Невозможно [активировать подарочные карты](gift-cards-in-order-save-operations.md#rabota-s-podarochnymi-kartami-v-operatsiyakh-sokhraneniya-zakazov).

```
{
    "customer": {
        "mobilePhone": "<Мобильный телефон>",
        "ids": {
            "mindboxId": ""
        },
        "discountCard": {
            "ids": {
                "number": "<Номер дисконтной карты>"
            }
        }
    },
    "pointOfContact": "<Внешний идентификатор точки контакта>",
    "executionDateTimeUtc": "<Дата и время расчета заказа. Для новых заказов используется текущее время по умолчанию>",
    "order": {
        "ids": {
            "externalSystemId": "<Идентификатор заказа во внешней системе>"
        },
        "area": {
            "ids": {
                "externalId": "<Внешний идентификатор зоны>"
            }
        },
        "deliveryCost": "<Стоимость доставки>",
        "lines": [
            {
                "product": {
                    "ids": {
                        "testExternalSystem": ""
                    }
                },
                "lineId": "<Идентификатор позиции заказа>",
                "lineNumber": "<Порядковый номер позиции заказа>",
                "quantity": "<Количество товаров>",
                "basePricePerItem": "<Базовая цена товара за единицу товара>",
                "minPricePerItem": "<Минимальная цена товара за единицу товара>",
                "costPricePerItem": "<Себестоимость товара за единицу товара>",
                "customFields": {
                    "lineField1": "<Дополнительное поле1>",
                    "lineField2": "<Дополнительное поле2>"
                },
                "status": {
                    "ids": {
                        "externalId": "<Статус покупки>"
                    }
                },
                "giftCard": {
                    "ids": {
                        "number": "<Номер подарочной карты>"
                    },
                    "getFromPool": "<Выбрать свободную подарочную карту из пула>"
                },
                "requestedPromotions": [
                    {
                        "type": "discount",
                        "promotion": {
                            "ids": {
                                "externalId": "<Внешний идентификатор промоакции>"
                            },
                            "type": "<Тип акции: discount>"
                        },
                        "amount": "<Размер скидки>"
                    }
                ]
            }
        ],
        "totalPrice": "<Сумма заказа с учетом всех скидок, отмен и возвратов>",
        "payments": [
            {
                "type": "<Тип способа оплаты>",
                "amount": "<Размер платежа>"
            },
            {
                "type": "giftCard",
                "giftCard": {
                    "ids": {
                        "number": "<Номер подарочной карты>"
                    }
                },
                "amount": "Размер платежа"
            }
        ],
        "customFields": {
            "orderField1": "<Дополнительное поле1>",
            "orderField2": "<Дополнительное поле2>"
        },
        "cashdesk": {
            "ids": {
                "externalId": "<Идентификатор кассы>"
            }
        }
    }
}
```

## Описание ответа

```
{
    "status": "Success"
}
```
