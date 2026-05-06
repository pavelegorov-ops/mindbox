---
title: Как вывести информацию по сгорающим баллам
slug: "parametry-bally-sgoryat"
source_url: "https://help.mindbox.ru/docs/parametry-bally-sgoryat"
vcs_path: "parametry-bally-sgoryat.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Простые параметры и форматирование. Примеры.
  - Баланс клиента и цена
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:0bcfffdbff66ace010899971839065ae8c274bda14dee89008dc9e3a0cb8f3d0"
---

# Как вывести информацию по сгорающим баллам

Со сгоранием баллов можно работать двумя способами:

- вывести информацию по конкретному начислению с помощью параметра CustomerBalanceChange - его можно использовать только в определённых сценариях;
- вывести сгорающие за следующие N дней баллы с балльного счёта с помощью функции GetExpirationBalanceChanges - можно использовать и в массовых рассылках.

## I. CustomerBalanceChange

Параметр доступен в письмах, отправляемых в сценариях по событию "изменение баланса" и "баланс клиента стал отрицательным".  
Для нашей задачи важно первое событие.

Для вывода данных добавим к **CustomerBalanceChange** один из параметров:

- **ChangeAmount** - сколько было начислено баллов изначально (часть из них может быть уже потрачена);
- **CustomerAction** - открывает параметры по действию, с которым начислили баллы;
- **ExpirationDateTime** - дата сгорания по московскому времени;
- **RemainingAmount** - сколько осталось от начисления.

*Для форматирования вывода данных даты и баллов можно воспользоваться [функциями](как-форматировать-даты-и-целочисленные-параметры) Formatdatetime (со [стандартными](стандартные-форматы-даты-и-времени) или [пользовательскими](настраиваемые-форматы-даты-и-времени) форматами) и FormatDecimal, для формы слова - [функциями](функции-для-обработки-и-форматирования-данных) Forms или AppendForms.*

### Пример.

Настроен [сценарий](workflow-bonus-expire.md) для отправки рассылки за семь дней до сгорания баллов.

#### **Запускающее событие:**

![Снимок экрана 2021-10-12 в 15.04.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-12%20%D0%B2%2015.04.42.png)

Обратите внимание на то, что часть баллов уже потрачена.

#### **Вёрстка письма:**

```
${Formatdatetime(CustomerBalanceChange.CustomerAction.DateTime, "d")}
было начислено ${CustomerBalanceChange.ChangeAmount}приветственных 
${Forms(CustomerBalanceChange.ChangeAmount, "балл", "балла", "баллов")}.

${AppendForms(CustomerBalanceChange.RemainingAmount, "балл", "балла", "баллов")}из них сгорят 
${Formatdatetime(CustomerBalanceChange.ExpirationDateTime, "d.MM.yyyy")}
```

#### **Клиент получает в письме:**

> 12.10.2021 было начислено 100 приветственных баллов.  
> 45 баллов из них сгорят 18.10.2021

## II. GetExpirationBalanceChanges

Параметр доступен во всех письмах.

- Вывод с помощью коллекции  
  **Recipient.GetBonusPointsAccount("Test").GetExpirationBalanceChanges(14)**, в которой:

  - **GetBonusPointsAccount** - функция, которая отбирает нужный балльный счёт;
  - **Test** - пример системного имени балльного счёта;
  - **GetExpirationBalanceChanges** - функция, которая принимает количество дней (N)  
    и возвращает сгораемые в эти дни начисления баллов
- С помощью функции **Take** можно ограничить количество начислений, которые выводим. Например, Recipient.GetBonusPointsAccount("Test").GetExpirationBalanceChanges(100).Take(1) вернёт коллекцию с самым "старым" начислением баллов.
- Для вывода суммы сгорающих баллов используется [**set**](как-работать-с-элементами-коллекции-с-помощью-цикла-for-end-for-и-set)  и параметр RemainingAmount.

Для этого задаём переменной значение 0, открываем цикл по коллекции начислений, в котором к этой же переменной прибавляем RemainigAmount, закрываем цикл и выводим сумму.

Например,

```
@{set sum=0}
@{for balanceChange in Recipient.GetBonusPointsAccount("Test").GetExpirationBalanceChanges(14)}
@{set sum = sum + balanceChange.RemainingAmount}
@{end for}
${sum}
```

- Для вывода данных добавим к параметру:
  - **ChangeAmount** - количество баллов, которое изначально было начислено (часть из них может быть уже потрачена)
  - **CustomerAction** - открывает параметры по действию, с которым начислили баллы
  - **ExpirationDateTime** - дата сгорания по московскому времени
  - **RemainingAmount** - сколько осталось от начисления

*Для форматирования вывода данных даты и баллов можно воспользоваться [функциями](как-форматировать-даты-и-целочисленные-параметры) Formatdatetime (с [стандартными](стандартные-форматы-даты-и-времени) или [пользовательскими](настраиваемые-форматы-даты-и-времени) форматами) и FormatDecimal, для формы слова - [функциями](функции-для-обработки-и-форматирования-данных) Forms или AppendForms.*

#### Пример.

**Изменения баланса:**

![Снимок экрана 2021-10-12 в 15.22.24.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-12%20%D0%B2%2015.22.24.png)

Обратите внимание на даты сгорания и на то, что часть баллов уже потрачена.

**Вёрстка письма:**

```
За следующие две недели сгорят следующие начисления:
@{set sum=0}
@{for balanceChange in Recipient.GetBonusPointsAccount("Test").GetExpirationBalanceChanges(14)}
${AppendForms(balanceChange.RemainingAmount, "балл", "балла", "баллов")}
${Formatdatetime(balanceChange.ExpirationDateTime, "d")}
@{set sum = sum + balanceChange.RemainingAmount}
@{end for}
Сумма баллов: 
${sum}
```

**Клиент получает в письме:**

За следующие две недели сгорят следующие начисления:  
20 баллов 06.11.2019  
3 балла 02.11.2019  
15 баллов 08.11.2019  
60 баллов 09.11.2019  
Сумма баллов: 98

[Внедрении программы лояльности в бизнес](https://mindbox.ru/academy/education/kak-zapustit-programmu-loyalnosti-5-shagov-i-sovety-ot-ekspertov-rynka/) — опыт специалистов
