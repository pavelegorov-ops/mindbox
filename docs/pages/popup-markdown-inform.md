---
title: Как создать собственный шаблон формы для сбора кликов или информирования клиентов
slug: "popup-markdown-inform"
source_url: "https://help.mindbox.ru/docs/popup-markdown-inform"
vcs_path: "popup-markdown-inform.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:f95d58364bc3499c9233847cb94fa1b445480335beddcde9e634103bbe99e622"
---

# Как создать собственный шаблон формы для сбора кликов или информирования клиентов

Информационная форма подходит для задач, когда нужно что-то сообщить клиенту — то есть достаточно показа информации, или когда нужно взаимодействие с формой — то есть важны клики по форме.

Не подходят для передачи данных на проект и проведения опросов. Для этих задач используйте тип [сбора контактов](popup-markdown-contacts.md).

---

Чтобы создать информационный шаблон:

1. На странице выбора шаблонов нажмите «Загрузить собственную верстку»:

![Untitled 2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%282%29.png)

2. Заполните настройки:

a. В настройках выберите тип формы «Информационная»:

![Untitled 3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%283%29.png)

После создания попапа тип формы уже нельзя будет поменять.

b. Выберите, как форма будет размещаться на экране: на его части, горизонтально или вертикально растянется по экрану клиента или заполнит весь экран:

![Untitled 4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%284%29.png)

c. Укажите, будет ли в форме более одного экрана:

![Untitled 10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%2810%29.png)

**Форма многоэкранная** — форма, состоящая из несколькиих экранов, кроме экрана, который появляется после отправки контактов (экран благодарности). Например, на первом экране собираете email, на втором — любимую категорию, или на первом экране вопрос «Хотите ли получить промокод?» и при нажатии на кнопку «Да» появляется второй экран с промокодом. Подробнее о создании и настройке [многоэкранных форм](popup-markdown-screens.md).

3. Введите код верстки.

[Правила верстки форм](popup-markdown-how-to.md)

В данной форме нет обязательных элементов.

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
					  <!-- На элементы, клики по которым нужно считать добавляйте data-popmechanic-submit -->
					  <button type="button" name="button" class="popmechanic-button" data-popmechanic-submit>Текст кнопки</button>
				</div>
		</div>
		<!-- Отдельный класс для элементов закрытия формы -->
    <div class="popmechanic-close" data-popmechanic-close>×
    </div>
</div>
```

![Untitled 11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%2811%29.png)

4. Добавитьте стили, чтобы форма красиво отображалась на сайте.

[Как указать стили](popup-markdown-how-to.md#css)

Вставьте стили в блок CSS и проверьте, что форма корректно отображается для всех типов устройств:

![Untitled 12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%2812%29.png)

5. Нажмите «Создать попап».

При создании автоматически создается попап/встроенный блок и шаблон, из которого вы в дальнейшем сможете создавать новые попапы/встроенные блоки так же, как из других шаблонов в каталоге.

Все загруженные формы можно найти во вкладке «Ваши шаблоны»:

![Untitled 13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/Untitled%20%2813%29.png)

Как сделать [HTML-письмо для рассылки без верстальщика](https://mindbox.ru/academy/education/kak-sdelat-html-pismo-instrumenty-marketologa/): бесплатные инструменты для маркетолога
