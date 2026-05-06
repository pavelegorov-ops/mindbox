---
title: Как создать собственный шаблон формы сбора контактов
slug: "popup-markdown-contacts"
source_url: "https://help.mindbox.ru/docs/popup-markdown-contacts"
vcs_path: "popup-markdown-contacts.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:ccd1f55041a8caf889f3a8c36ef5995bb635b805d6ec83eeadaff8b67c54bf8b"
---

# Как создать собственный шаблон формы сбора контактов

Форма для сбора контактов подходит для сбора email, мобильных номеров, любых другие данных клиента и для проведения опросов.

Отчет по форме сбора контактов показывает, сколько клиентов оставили контакты в форме. Эти данные не атрибутируются к заказам.

Об информационной форме — в [статье](popup-markdown-inform.md).

---

Чтобы создать шаблон сбора контактов:

1. На странице выбора шаблонов нажмите «Загрузить собственную верстку»:

![Untitled 2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%282%29.png)

2. Заполните настройки:

a. В настройках выберите тип формы «Сбор контактов»:

![Untitled 3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%283%29.png)

После создания попапа тип формы уже нельзя будет поменять.

b. Выберите, как форма будет размещаться на экране: на его части, горизонтально или вертикально растянется по экрану клиента или заполнит весь экран:

![Untitled 4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%284%29.png)

c. Укажите, будет ли в форме более одного экрана и нужен ли экран благодарности:

![Снимок экрана 2022-11-09 в 00.23.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-09%20%D0%B2%2000.23.28.png)

**Форма многоэкранная** — форма, состоящая из несколькиих экранов перед экраном благодарности (появляется после отправки контактов). Например, на первом экране собираете email, на втором — любимую категорию, или на первом экране вопрос «Хотите ли получить промокод?» и при нажатии на кнопку «Да» появляется второй экран с промокодом. Подробнее о создании и настройке [многоэкранных форм](popup-markdown-screens.md).

**Экран благодарности** — экран, который появляется после отправки контактов или другой информации, которую заполнил клиент. Обычно на нем содержится текст с благодарностью за подписку и информацией по дальнейшим шагам, например, «Промокод отправлен вам на почту, вы можете найти его там и получить скидку 10% на следующую покупку».

3. Введите код верстки.

[Правила верстки форм](popup-markdown-how-to.md)

Обязательное условие для данной формы — должен быть как минимум один экран с полями ввода и кнопкой отправки данных.

Пример готового кода:

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

![Untitled 8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%288%29.png)

4. Добавитьте стили, чтобы форма красиво отображалась на сайте.

[Как указать стили](popup-markdown-how-to.md#css)

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

Вставьте стили в блок CSS и проверьте, что все экраны формы корректно отображается для всех типов устройств:

![Untitled 8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%288%29%281%29.png)

5. Нажмите «Создать попап».

При создании автоматически создается попап/встроенный блок и шаблон, из которого вы в дальнейшем сможете создавать новые попапы/встроенные блоки так же, как из других шаблонов в каталоге.

Все загруженные формы можно найти во вкладке «Ваши шаблоны»:

![Untitled 9.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%289%29.png)

- [Для чего нужен email-маркетинг](https://mindbox.ru/academy/education/kakie-zadachi-reshaet-email-marketing/): обзор основных задач
- Как [собрать контакты клиентов](https://mindbox.ru/journal/education/kak-sobrat-kontakty-klientov/) для настройки рекламы: 15 способов
