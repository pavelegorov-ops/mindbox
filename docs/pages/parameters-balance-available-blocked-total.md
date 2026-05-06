---
title: Как вывести текущий баланс в письме
slug: "parameters-balance-available-blocked-total"
source_url: "https://help.mindbox.ru/docs/parameters-balance-available-blocked-total"
vcs_path: "parameters-balance-available-blocked-total.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Простые параметры и форматирование. Примеры.
  - Баланс клиента и цена
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ac3e5e756103eb888836265233c2cf5df256556b77c99632e9a6c6d222b88182"
---

# Как вывести текущий баланс в письме

Выводим доступные и заблокированные баллы.

Параметр для вывода баллов складывается из:

- **Recipient.GetBonusPointsAccount("Test")**  
  и
- .**Available** — доступно
- .**Blocked** — заблокировано
- .**Total** — всё (доступно + заблокировано)

*"Test" — название балльного счета в нашем примере.*

Например, есть клиент с следующим балансом:

![Снимок экрана 2021-03-18 в 15.17.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-18%20%D0%B2%2015.17.35.png)

В рассылку вставляем код:

```
Ваши баллы:
- доступно ${Recipient.GetBonusPointsAccount("Test").Available}
- заблокированно ${Recipient.GetBonusPointsAccount("Test").Blocked}
- всего ${Recipient.GetBonusPointsAccount("Test").Total}
```

В письме получаем:

> Ваши баллы:  
> - доступно 5000  
> - заблокированно 1000  
> - всего 6000

  
* * *

Для форматирования вывода баллов можно воспользоваться [функцией](как-форматировать-даты-и-целочисленные-параметры) FormatDecimal, для формы слова — [функциями](функции-для-обработки-и-форматирования-данных) Forms или AppendForms.

Пример:

```
- доступно ${FormatDecimal(Recipient.GetBonusPointsAccount("Test").Available, "N0")} б.

- заблокированно ${AppendForms (Recipient.GetBonusPointsAccount("Test").Blocked, "балл", "балла", "баллов")}

- всего ${FormatDecimal(Recipient.GetBonusPointsAccount("Test").Total, "N0")} ${Forms (Recipient.GetBonusPointsAccount("Test").Total, "балл", "балла", "баллов")}
```

> Получаем:  
> - доступно 5 000 б.  
> - заблокированно 1000 баллов  
> - всего 6 000 баллов

[Внедрении программы лояльности в бизнес](https://mindbox.ru/academy/education/kak-zapustit-programmu-loyalnosti-5-shagov-i-sovety-ot-ekspertov-rynka/) — опыт специалистов
