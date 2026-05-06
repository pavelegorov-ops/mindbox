---
title: Поля ввода и валидация данных
slug: "popup-input"
source_url: "https://help.mindbox.ru/docs/popup-input"
vcs_path: "popup-input.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:c4c2ae1cd036eac77508edd686e311cfc5077aa23888ad0123666881d53c5430"
---

# Поля ввода и валидация данных

Форма сбора контактов по определению должна передавать некоторые данные клиента в Mindbox, поэтому в ней должно быть как минимум одно **поле ввода и кнопка подтверждения**:

```
<div class="popmechanic-inputs">
		<input type="email" class="popmechanic-input" data-popmechanic-input="email" placeholder="Email" required>
		<button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
</div>
```

### Как обозначить поле ввода

**Поле для email**

```
input type="email" class="popmechanic-input" data-popmechanic-input="email" placeholder="Email"
```

**Поле имени**

```
input type="text" class="popmechanic-input" data-popmechanic-input="first_name" placeholder="Имя"
```

**Поле номера телефона**

```
input type="text" class="popmechanic-input" data-popmechanic-input="phone" placeholder="Ваш номер"
```

**Поле фамилии**

```
input type="text" class="popmechanic-input" data-popmechanic-input="last_name" placeholder="Фамилия"
```

**Поле имени и фамилии**

```
input type="text" class="popmechanic-input" data-popmechanic-input="name" placeholder="Имя и фамилия"
```

**Любое другое кастомное поле**

Вы можете создавать пользовательские поля используя *customs.ваш_параметр*:

```
data-popmechanic-input="customs.year"
data-popmechanic-input="customs.female"
```

Таким образом можно помечать ответы или выделенные категории подписчика.

При отправке данных скрипт считывает поля с атрибутом data-popmechanic-input и в случае, если поле не прошло валидацию, на input вешается класс "popmechanic-invalid".

**Обязательное поле**

Обязательным для заполнения поле можно сделать добавив "data-popmechanic-required" для элемента:

```
input type="email" class="popmechanic-input" data-popmechanic-required data-popmechanic-input="email" placeholder="Email"
```

### Валидация

Примеры реализации валидации можно посмотреть в готовых шаблонах на проекте, например в реализации дополнительных полей Колеса фортуны (поиск <div class="popmechanic-inputs"> в HTML).

![Снимок экрана 2022-11-09 в 20.45.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2020.45.03.png)

**Маска ввода для поля**

Используйте в теге input data-popmechanic-mask="`", где "`" означает 4 знака. Поле ввода data-popmechanic-mask="`.`.####" — ввод полной даты с разделением точками.

### Примеры верстки

- Три поля ввода в форме:

```
<div class="popmechanic-inputs">
    <div class="popmechanic-input">
        <input type="text" class="popmechanic-name" data-popmechanic-input="name" placeholder="Имя">
    </div>
    <div class="popmechanic-input">
        <input type="text" class="popmechanic-phone" data-popmechanic-input="phone" placeholder="Телефон">
    </div>
    <div class="popmechanic-input">
        <input type="email" class="popmechanic-email" data-popmechanic-input="email" placeholder="Email">
    </div>
```

![Снимок экрана 2022-11-09 в 21.02.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2021.02.27.png)

---

- Две кнопки для выбора пола и сохранения данных:

```
<button type="button" class="btn" name="button" data-popmechanic-submit onclick="PopMechanic.customs.gender = 'Male'" data-target="screen">
FOR MEN
</button>

<button type="button" class="btn" name="button" data-popmechanic-submit onclick="PopMechanic.customs.gender = 'Female'" data-target="screen">
FOR WOMEN
</button>
```

![Снимок экрана 2022-11-09 в 21.02.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2021.02.08.png)

---

- Выбор из списка галочек:

```
<h3 class="popmechanic-header-heading">Choose your interests:</h3>

<div class="popmechanic-categories">
    <ul class="popmechanic-categories-list">
        <li class="popmechanic-categories-item popmechanic-categories-item-running">
            <div class="popmechanic-categories-pic popmechanic-categories-pic-running"></div>
            <input id="running" type="checkbox" data-popmechanic-input="customs.running" value="1">
            <label class="popmechanic-categories-label" for="running">Run</label>
        </li>
        <li class="popmechanic-categories-item popmechanic-categories-item">
            <div class="popmechanic-categories-pic popmechanic-categories-pic-training"></div>
            <input id="training" type="checkbox" data-popmechanic-input="customs.training" value="1">
            <label class="popmechanic-categories-label" for="training">Gym</label>
        </li>
        <li class="popmechanic-categories-item popmechanic-categories-item-autosport">
            <div class="popmechanic-categories-pic popmechanic-categories-pic-autosport"></div>
            <input id="autosport" type="checkbox" data-popmechanic-input="customs.auto" value="1">
            <label class="popmechanic-categories-label" for="autosport">Moto</label>
        </li>
```

![Снимок экрана 2022-11-09 в 21.05.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2021.05.28.png)

---

- Сбор даты:

```
<span class="birthday-text">Date of Birth</span>

<div class="popmechanic-input">
    <input data-popmechanic-mask="##" class="popmechanic-day" data-popmechanic-required data-popmechanic-input="customs.day" placeholder="day">
</div>

<div class="popmechanic-input">
    <input data-popmechanic-mask="##" class="popmechanic-month" data-popmechanic-required data-popmechanic-input="customs.month" placeholder="month">
</div>

<div class="popmechanic-input">
    <input data-popmechanic-mask="####" class="popmechanic-year" data-popmechanic-required data-popmechanic-input="customs.year" placeholder="year">
</div>
```

![Снимок экрана 2022-11-09 в 21.07.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2021.07.40.png)

- Чек-бокс политики конфиденциальности с предзаполненной галочкой:

```
<label class="popmechanic-checkbox-block">
    <input type="checkbox" class="popmechanic-checkbox" checked data-popmechanic-input="customs.agreement" data-popmechanic-required value="1">
    <div class="popmechanic-checkbox-check"></div>
    Я согласен с Политикой конфиденциальности компании Н и хочу получать рассылку
</label>
```

![Снимок экрана 2022-11-09 в 21.08.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2021.08.54.png)
