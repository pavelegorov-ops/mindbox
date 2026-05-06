---
title: Правила верстки попапов и встроенных форм
slug: "popup-markdown-how-to"
source_url: "https://help.mindbox.ru/docs/popup-markdown-how-to"
vcs_path: "popup-markdown-how-to.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:31f51b1be43fbbc6308399a628f5ddca12d8a9dc7a39f944012ba7f3a31f01a6"
---

# Правила верстки попапов и встроенных форм

Верстка формы зависит от выбранного типа: будет ли она [для сбора контактов](popup-markdown-contacts.md) или [для сбора кликов](popup-markdown-inform.md). Также есть общие принципы, одинаковые для всех видов форм.

## HTML

### Общие правила

- В начало верстки не требуется вставлять `<!DOCTYPE html>` или `<header>`. верстка **начинается сразу с** `<div>`, с классом `"popmechanic-reset"` и `id="popmechanic-form”`.
- **Главный экран** формы подписки оборачивается классом `"popmechanic-main"`
- Используйте `"data-popmechanic-close"` во всех элементах, при клике на которые, форма должна **закрываться**. Никаких дополнительных скриптов прописывать не нужно:

```
<!-- Вся форма обернута в отдельный div с классом "popmechanic-reset" и id="popmechanic-form" -->
<div class="popmechanic-reset" id="popmechanic-form">
    <div class="popmechanic-main">
        <div class="popmechanic-content">
            <div class="popmechanic-title">
                Заголовок
            </div>
            <div class="popmechanic-sub-title">
                Текст
            </div>
				</div>
		</div>
		<!-- Отдельный класс для элементов закрытия формы: -->
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
</div>
```

### Для форм сбора контактов

- Форма сбора контактов по определению должна передавать некоторые данные клиента в Mindbox, поэтому в ней должно быть как минимум одно **поле ввода и кнопка подтверждения**:

```
<div class="popmechanic-inputs">
		<input type="email" class="popmechanic-input" data-popmechanic-input="email" placeholder="Email" required>
		<button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
</div>
```

[Подробнее о полях ввода и валидации.](popup-input.md)

- В форме сбора контактов можно добавить **экран благодарности** и обернуть его классом `"popmechanic-thankyou"`

```
<div class="popmechanic-thankyou">
		<div class="popmechanic-title">Спасибо!</div>
    <div class="popmechanic-sub-title">Уже отправили вам письмо</div>
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
</div>
```

#### Пример готового кода

```
<!-- Вся форма обернута в отдельный div с классом "popmechanic-reset" и id="popmechanic-form" -->
<div class="popmechanic-reset" id="popmechanic-form">
    <div class="popmechanic-main">
        <div class="popmechanic-content">
            <div class="popmechanic-title">
                Заголовок
            </div>
            <div class="popmechanic-sub-title">
                Текст
            </div>
						<!-- Поле ввода и кнопка формы: -->
						<div class="popmechanic-inputs">
					    <input type="email" class="popmechanic-input" data-popmechanic-input="email" placeholder="Email" required>
					    <button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
						</div>
				</div>
		</div>
		<!-- Отдельный класс для элементов закрытия формы: -->
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
    <div class="popmechanic-thankyou">
        <div class="popmechanic-title">Спасибо!</div>
        <div class="popmechanic-sub-title">Уже отправили вам письмо</div>
		<!-- Отдельный класс для элементов закрытия формы: -->
        <div class="popmechanic-close" data-popmechanic-close>×
        </div>
    </div>
</div>
```

### Для информационных форм

- Если ваша форма предполагает наличие ссылки или кнопки, клики по которым нужно считать, то добавьте в них `"data-popmechanic-submit"`

```
<button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
```

Если в форме будет несколько кнопок с этим параметром, в отчете все клики будут объединены.

#### Пример готового кода

```
<!-- Вся форма обернута в отдельный div с классом "popmechanic-reset" и id="popmechanic-form" -->
<div class="popmechanic-reset" id="popmechanic-form">
    <div class="popmechanic-main">
        <div class="popmechanic-content">
            <div class="popmechanic-title">
                Заголовок
            </div>
            <div class="popmechanic-sub-title">
                Текст
            </div>
					  <!-- На элементы, клики по которым нужно считать добавляйте data-popmechanic-submit -->
					  <button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
				</div>
		</div>
		<!-- Отдельный класс для элементов закрытия формы -->
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
</div>
```

## Стили CSS

### Параметры стилей для разного размера экранов

Не используйте медиазапросы, если верстаете попап-форму. Скрипт Mindbox вешает на контейнер формы классы `"popmechanic-desktop"`, `"popmechanic-tablet"`, `"popmechanic-mobile"` для адаптации внешнего вида под устройство.

Наши зарезервированные классы для стилей:

- *#popmechanic-form* — все экраны формы
- *.popmechanic-mobile* — мобильная версия формы
- *.popmechanic-tablet* — планшетная версия формы
- *.popmechanic-thankyou* — экран благодарности за подписку

Для кастомных стилей в CSS формы используйте `#popmechanic-form` в начале селектора как в примерах ниже:

```
<!-- Стили для ссылок в форме в целом: -->
#popmechanic-form a {
    display: block;
}

<!-- Стили для элемента закрытия в форме в целом: -->
#popmechanic-form .popmechanic-close {
    font-size: 20px;
}

<!-- Стили для мобильной версии формы: -->
.popmechanic-mobile #popmechanic-form {
    width: 300px;
}

<!-- Стили для картинок мобильной версии формы: -->
.popmechanic-mobile #popmechanic-form img {
    width: 200px;
}
```

### Добавление кастомных шрифтов в форму

Рекомендуемый вариант:

```
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&subset=cyrillic");
@import url("https://fonts.googleapis.com/css?family=Roboto:400,700&subset=cyrillic-ext");
```

### Добавление видео в форму

Не добавляйте GIF анимацию размером больше 2 МБ

Используйте видеоформат для фона, если это необходимо:

```
<video autoplay loop muted class="popmechanic-video popmechanic-video-desktop">
    <source src="https://static.popmechanic.ru/media/fridays-video/video/desktop_bg.mp4" type="video/mp4">
</video>
```

Больше информации по использованию видео в форме в [статье](pop-up-with-video.md).

### Для многоэкранных форм

Если форма многоэкранная или содержит экран благодарности, нужно скрыть все экраны кроме первого при отрисовке формы.

```
<!-- Экран благодарности скрыт при показе формы -->
#popmechanic-form .popmechanic-thankyou {
    display: none; }

<!-- Первый экран скрывается, когда данные успешно отправлены и показывается экран благодарности -->
.popmechanic-success #popmechanic-form .popmechanic-main {
    display: none; }

.popmechanic-success #popmechanic-form .popmechanic-thankyou {
    display: block; }
```

```
<!-- Аналогично скрываются все экраны кроме первого в многоэкранной форме -->
#popmechanic-form .second-screen {
  display: none;
}
```

### Пример

В качестве примера опишем стили кнопки формы

```
<!-- Общие стили кнопки для ПК, мобильного вида -->
#popmechanic-form .popmechanic-button {
width: 110px;
height: 30px;
background: #4fad00;
color: #fff;
font-size: 13px;
font-weight: 700;
display: flex;
align-items: center;
justify-content: center;
border-radius: 30px;
cursor: pointer;
outline: none;
border: none;
text-decoration: none;
-webkit-transition: all .3s;
transition: all .3s;
}
<!-- Изменение стиля кнопки при наведении -->
#popmechanic-form .popmechanic-button:hover {
color: #4fad00;
background: #fff;
}
<!-- Изменение стиля кнопки при отрисовке на мобильном устройстве -->
.popmechanic-mobile #popmechanic-form .popmechanic-button {
width: 120px;
height: 25px;
font-size: 12px;
line-height: 10px;
}
```

[Как использовать попапы, не раздражая клиентов](https://mindbox.ru/academy/education/kak-ispolzovat-popapy/). Какие ошибки совершают бренды при создании попапов и как сделать, чтобы этот инструмент приносил пользу и клиенту, и компании.
