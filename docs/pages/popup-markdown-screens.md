---
title: Как создать собственную форму с несколькими экранами для опроса
slug: "popup-markdown-screens"
source_url: "https://help.mindbox.ru/docs/popup-markdown-screens"
vcs_path: "popup-markdown-screens.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:b71b26942f7eda444240685f605e9fe334dea83a42c9e1048f5414eee9921792"
---

# Как создать собственную форму с несколькими экранами для опроса

Для того, чтобы собрать информацию от клиентов на сайте вам потребуется форма типа «Сбор контактов». В данном случае вы можете собирать контакты или работать с уже идентифицированными клиентами на сайте, не требуя ввести телефон или емейл, но только этот тип формы передает информацию из формы в Mindbox.

Чтобы создать шаблон для опроса:

1. На странице выбора шаблонов нажмите «Загрузить собственную верстку»:

![Untitled 2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%282%29.png)

2. Заполните настройки:

a. В настройках выберите тип формы «Сбор контактов»:

![Untitled 3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%283%29.png)

После создания попапа тип формы уже нельзя будет поменять.

b. Выберите, как форма будет размещаться на экране: на его части, горизонтально или вертикально растянется по экрану клиента или заполнит весь экран:

![Untitled 4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%284%29.png)

c. Укажите, что в форме будет несколько экранов и уточните, нужен ли экран благодарности:

![Снимок экрана 2022-11-09 в 00.23.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2000.23.28.png)

**Форма многоэкранная** — форма, состоящая из несколькиих экранов, кроме экрана, который появляется после отправки контактов (экран благодарности).

**Экран благодарности** — экран, который появляется после отправки контактов или другой информации, которую заполнил клиент.

3. Введите код верстки.

[Общие правила верстки форм](popup-markdown-how-to.md)

**Правила верстки многошаговых попапов**

В ссылку кнопки первого экрана поставьте идентификатор экрана, который должен быть показан при нажатии на кнопку.

- Например, задаем ссылку перехода для первого экрана `href="#popmechanic-second-screen"`:

```
<!-- Вся форма обернута в отдельный div с классом "popmechanic-reset" и id="popmechanic-form" -->
<div class="popmechanic-reset" id="popmechanic-form">
    <div class="popmechanic-screen first-screen" id="popmechanic-first-screen">
        <div class="popmechanic-content">
            <button type="button" name="button" class="popmechanic-button-first" data-target="screen" href="#popmechanic-second-screen">Оставить свой контакт</button>
        </div>
    </div>
		<!-- Отдельный класс для элементов закрытия формы: -->
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
</div>
```

- У второго экрана задаем идентификатор с тем же значением — `id="popmechanic-second-screen"`:

```
<div class="popmechanic-screen second-screen" id="popmechanic-second-screen">
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
```

- В итоге получаем код для двух экранов:

```
<!-- Вся форма обернута в отдельный div с классом "popmechanic-reset" и id="popmechanic-form" -->
<div class="popmechanic-reset" id="popmechanic-form">
    <div class="popmechanic-screen first-screen" id="popmechanic-first-screen">
        <div class="popmechanic-content">
            <button type="button" name="button" class="popmechanic-button-first" data-target="screen" href="#popmechanic-second-screen">Оставить свой контакт</button>
        </div>
    </div>
		<div class="popmechanic-screen second-screen" id="popmechanic-second-screen">
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
</div>
```

![Untitled 14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%2814%29.png)

**Показ разных блоков с учетом предыдущего выбора пользователя (условие ЕСЛИ)**

```
<!-- 1. Помечаем варианты выбора разными значениями: "PopMechanic.customs.questionN = 'adidas'" и "PopMechanic.customs.questionN = 'deha'": -->

<div class="popmechanic-title">Choose the colors you like</div>
    <ul class="popmechanic-options">
        <li class="popmechanic-option" rel="screen" href="#popmechanic-third" onclick="PopMechanic.customs.questionN = 'adidas'"> </li>
        <li class="popmechanic-option" rel="screen" href="#popmechanic-third"onclick="PopMechanic.customs.questionN = 'deha'"></li> </div>

<!-- 2. Используем условие IF для выбора, какой блок показывать пользователю: -->

<div class="popmechanic-promocode_block" data-popmechanic-if="PopMechanic.customs.questionN === 'adidas'">
<div class="popmechanic-promocode_text">We give <strong>5% promo code</strong> to all brand collections</div>
<div class="popmechanic-promocode">ADIDAS636A</div></div>
<div class="popmechanic-promocode_block" data-popmechanic-if="PopMechanic.customs.questionN === 'deha'">
<div class="popmechanic-promocode_text">We give <strong>5% promo code</strong> to all brand collections</div>
<div class="popmechanic-promocode">DEHA1366A</div></div>

<!-- 3. Блок с промокодом ADIDAS636A покажется только тем, кто выбрал ранее вариант со значением "PopMechanic.customs.questionN === 'adidas'"-->Если форма многоэкранная или содержит экран благодарности, нужно скрыть все экраны кроме первого при отрисовке формы
```

4. Добавьте стили, чтобы форма красиво отображалась на сайте.

[Как указать стили](popup-markdown-how-to.md#css)

Важно указать, что второй экран должен быть скрыт при показе формы:

```
#popmechanic-form .second-screen {
  display: none;
}
```

5. Нажмите «Создать попап».

При создании автоматически создается попап/встроенный блок и шаблон, из которого вы в дальнейшем сможете создавать новые попапы/встроенные блоки так же, как из других шаблонов в каталоге.

Все загруженные формы можно найти во вкладке «Ваши шаблоны»:

![Untitled 9.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%289%29.png)

Как сделать [HTML-письмо для рассылки без верстальщика](https://mindbox.ru/academy/education/kak-sdelat-html-pismo-instrumenty-marketologa/): бесплатные инструменты для маркетолога
