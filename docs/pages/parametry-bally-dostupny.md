---
title: Как вывести доступные баллы
slug: "parametry-bally-dostupny"
source_url: "https://help.mindbox.ru/docs/parametry-bally-dostupny"
vcs_path: "parametry-bally-dostupny.md"
toc_path:
  - Рассылки
  - "Шаблонизатор, подстановка параметров в рассылки"
  - Простые параметры и форматирование. Примеры.
  - Баланс клиента и цена
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:d3c4947c88bda7e527534609b5f0aedf48ba4da716a82f6117d3d1d38b142044"
---

# Как вывести доступные баллы

Задача: вывести баллы, которые стали доступны.

Используем базовый параметр CustomerBalanceChange. Он доступен для использования в автоматических рассылках, отправляемых в [сценариях по событию](workflow-bonus-available.md) "Бонусные баллы стали доступны".

Для вывода данных добавим к CustomerBalanceChange один из параметров:

- **ChangeAmount** - сколько было начислено баллов изначально (часть из них может быть уже потрачена);
- **CustomerAction** - открывает параметры по действию, с которым начислили баллы;
- **ExpirationDateTime** - дата сгорания по московскому времени;
- **RemainingAmount** - сколько осталось от начисления.

Для форматирования вывода данных даты и баллов можно воспользоваться [функциями](%D0%BA%D0%B0%D0%BA-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B4%D0%B0%D1%82%D1%8B-%D0%B8-%D1%86%D0%B5%D0%BB%D0%BE%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B.md) Formatdatetime и FormatDecimal, для формы слова — [функциями](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.md) Forms или AppendForms.

Пример верстки:

```
Доступно: ${AppendForms(CustomerBalanceChange.RemainingAmount, "балл", "балла", "баллов")}
Дата сгорания: ${FormatDateTime(CustomerBalanceChange.ExpirationDateTime, "m")}
```

Получаем:

> Доступно: 15 баллов  
> Дата сгорания: 5 июля

[Внедрении программы лояльности в бизнес](https://mindbox.ru/academy/education/kak-zapustit-programmu-loyalnosti-5-shagov-i-sovety-ot-ekspertov-rynka/) — опыт специалистов
