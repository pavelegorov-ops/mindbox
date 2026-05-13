---
title: Как вывести в попапе промокод из рассылки
slug: "pop-up-promo-code-from-message"
source_url: "https://help.mindbox.ru/docs/pop-up-promo-code-from-message"
vcs_path: "pop-up-promo-code-from-message.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Дополнительные настройки
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:d37936fd3b8108ec3706aafb5d20c27a52968c995a7eb528cddf1f10ad5b06ce"
---

# Как вывести в попапе промокод из рассылки

**Задача.** Клиент получает рассылку с персональным промокодом. При переходе на сайт из этой рассылки нужно вывести полученный промокод на сайте, чтобы клиент мог его скопировать и использовать.

### Шаг 1. Определите параметр промокода

Используйте тот же параметр, с помощью которого выводите промокод в рассылке.

Вывод одноразового промокода делается через параметр вида `Recipient.LastReceivedPromoCode.WithTypeСистемноеИмяПула.Value`

В качестве примера используем промокод из пула с системным именем Promo500

Его параметр:

```
Recipient.LastReceivedPromoCode.WithTypePromo500.Value
```

Подробнее: [Как вывести в письме промокод.](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md)

---

Вывод многоразового промокода делается через параметр вида `MultiplePromoCodes.WithTypeСистемноеИмяПула.FirstAvailable.Value`

Подробнее: [Как вывести многоразовый промокод.](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D1%81-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D0%B3%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC.md)

### Шаг 2. Добавьте промокод в utm-метки рассылки

Передавайте промокод через любые метки:

- utm_source
- utm_medium
- utm_term
- utm_content
- utm_campaign

Например, используем utm_term

Должны получиться ссылки вида:  
`https://example.ru/?utm_source=mindbox&utm_medium=email&utm_campaign=promik&utm_term=${параметр-промокода}`

В нашем примере получается ссылка:  
`https://example.ru/?utm_source=mindbox&utm_medium=email&utm_campaign=promik&utm_term=${Recipient.LastReceivedPromoCode.WithTypePromo500.Value}`

### Шаг 3. Создайте попап

Подробнее: [Как создать попап.](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md)

При выборе шаблона можно отфильтровать по показу промокода:

![Снимок экрана 2022-08-01 в 23.22.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-01%20%D0%B2%2023.22.01.png)

#### Поправьте код в шаблоне попапа

В коде попапа найдите переменную для вывода промокода:

![Снимок экрана 2022-08-02 в 01.02.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-02%20%D0%B2%2001.02.26.png)

И замените ее на следующий код:

```
<%
  try {
    print(PopMechanic.sbjs.get.current.trm);
  } catch (err) {
    print('(none)');
  }
%>
```

На месте `trm` поставьте метку, которую используете в своем попапе:

- utm_source — `src`
- utm_medium — `mdm`
- utm_campaign — `cmp`
- utm_term — `trm`
- utm_content — `cnt`

![Снимок экрана 2022-08-02 в 01.03.24.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-02%20%D0%B2%2001.03.24.png)

В настройке формы в поле названия промокода можно ничего не вводить, так как промокод берется не оттуда, а из меток в ссылке:

![Снимок экрана 2022-08-15 в 15.04.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-15%20%D0%B2%2015.04.51.png)

#### Ограничьте таргетинг

![Снимок экрана 2022-08-31 в 21.57.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-31%20%D0%B2%2021.57.02.png)  
*Ограничиваем страницы показа метками из рассылки.*

Далее запустите попап и рассылку.

---

Готово!  
Клиент переходит по ссылке из рассылки, попадает на страницу https://example.ru/?utm_source=mindbox&utm_medium=email&utm_campaign=promik&**utm_term=BRTN1412** и видит свой промокод:

![Снимок экрана 2022-08-02 в 01.18.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-02%20%D0%B2%2001.18.51.png)

[Как использовать попапы, не раздражая клиентов](https://mindbox.ru/academy/education/kak-ispolzovat-popapy/). Какие ошибки совершают бренды при создании попапов и как сделать, чтобы этот инструмент приносил пользу и клиенту, и компании.
