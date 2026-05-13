---
title: Как вывести персональные предложения в рассылке
slug: "personal-offers-variables"
source_url: "https://help.mindbox.ru/docs/personal-offers-variables"
vcs_path: "personal-offers-variables.md"
toc_path:
  - Лояльность и акции
  - Персональные предложения
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:88273755ae1580c213d99892be0ee85986945274de7edfb62433d4fa66a070cd"
---

# Как вывести персональные предложения в рассылке

На проектах есть возможность выводить персональные предложения клиентов в рассылках.

Для этого нужно:

1. [Настроить](personal-offers.md) списки персональных предложений.
2. [Наполнить](https://developers.mindbox.ru/docs/%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9) списки продукцией либо через csv-файл, либо через API.
3. Вывести в письме с помощью параметров шаблонизатора предложения для клиента.

Чтобы вывести персональные предложения для клиента, используйте [параметр](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) вида `Recipient.GetFavoriteList("ListName").Take(N)`, где:

- ListName — системное имя списка;
- N — количество выводимых предложений.

Посмотреть доступные списки для вывода и описание параметров можно в разделе **Помощь → Параметры в шаблонах рассылок**:

![параметры — копия.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B%C2%A0%E2%80%94%20%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F.png)

![Снимок экрана 2023-07-25 в 17.45.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-25%20%D0%B2%2017.45.35.png)

Полученный параметр является коллекцией и доступен во всех письмах.

Для обращения к каждому его элементу (предложению) используйте цикл [for...end for](как-работать-с-элементами-коллекции-с-помощью-цикла-for-end-for-и-set).

![Снимок экрана 2023-03-16 в 19.27.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-16%20%D0%B2%2019.27.53.png)

  

**Пример**

Выведем условия по персональному предложению «Любимый продукт» («LyubimyjProdukt»):

```
Ваша персональная скидка!<br>

@{for offer in Recipient.GetFavoriteList("LyubimyjProdukt").Take(1)}

До ${FormatDateTime(offer.EndDateTime, "d")} на 

@{for prod in offer.Products.Take(1)}
«<a href="${prod.URL}">${prod.Name}@{end for}</a>»

для вас установлена специальная цена — ${offer.Benefit.Amount} руб.<br>

Доступное количество применений: ${offer.Limit.Amount} раз за календарный 

    @{if offer.Limit.PeriodType = "FixedDays"} день.
    @{else if offer.Limit.PeriodType = "FixedWeeks"} неделю.
    @{else if offer.Limit.PeriodType = "FixedMonths"} месяц.
    @{end if}

@{end for}
```

Клиент получит в письме:

> Ваша персональная скидка!  
> До 30.04.2023 на «Шоколадный маффин» для вас установлена специальная цена — 50 руб.  
> Доступное количество применений: 1 раз за календарный день.
