---
title: "Как создать голосование/опрос в email-рассылке"
slug: "how-to-create-a-poll"
source_url: "https://help.mindbox.ru/docs/how-to-create-a-poll"
vcs_path: "how-to-create-a-poll.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Дополнительные возможности рассылок
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:a0deb2cffadcc0e5ca5ae68fe41151094ff867abb4ae6a50d3ffb9abfe7a8c31"
---

# Как создать голосование/опрос в email-рассылке

**Голосования**/опросы в рассылках — это возможность узнать мнение клиента и отследить результаты в системе.

**Ограничения:**

- Голосование работает для клиента только один раз. Даже если оно используется в нескольких рассылках.
- В одной рассылке может быть только одно голосование.
- Клики в тестовых письмах не учитываются. Для тестирования голосования нужно отправить массовую или автоматическую рассылку с помощью сценария.

Если клиент кликнул по варианту из голосования, последующие клики по вариантам учитываться не будут. Не зависит от того, в скольких письмах использовано голосование.  
Например, у вас одно голосование в шести разных рассылках, и клиент кликнул в каждом письме — засчитан будет только первый клик, остальные пять проигнорированы.

Создадим рассылку с голосованием/опросом. Задача состоит из четырех частей:

1. Создание вариантов голосования/опроса
2. Верстка письма
3. Создание рассылки
4. Настройка голосования/опроса

## 1. Создание вариантов голосования/опроса

Создадим шаблоны действий для каждого варианта в голосовании/опросе

1. Перейдите в раздел **Настройки** → **Клиенты и действия** → **Шаблоны действий**:

   ![action-templates-interface.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/action-templates-interface.png)
2. Выберите «Добавить» → «Шаблон действия»:

   ![action-templates-add.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/action-templates-add.png)
3. Создайте шаблон действия для первого варианта в голосовании:

   ![poll-action-yes.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/poll-action-yes.png)
4. Клонируйте шаблон действия для остальных вариантов.

   - Нажмите «Клонировать» в меню напротив шаблона действия:

   ![poll-action-copy.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/poll-action-copy.png)

   - Заполните копию:

   ![poll-action-no.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/poll-action-no.png)

## 2. Создание рассылки

Создайте рассылку [автоматическую](email-trigger.md) или [массовую](email-mass).

## 3. Добавление в письмо

Настроить опрос можно в конструкторе Mindbox или в HTML-редакторе:

- Конструктор Mindbox — собирайте письмо из готовых блоков без знания HTML;
- HTML-редактор — используйте готовую верстку из других сервисов.

### В HTML-редакторе

Добавьте в верстку специальный параметр для каждого варианта ответа:

data-name="системное_имя_шаблона_действия_варианта_ответа"

*Пример для варианта ответа 1:*

```
<a data-name="Da" href="http://vash_site.ru/spasibo-za-vash-otzyv.html">Да</a>
```

Ссылка обязательно должна быть

Она может вести на специальную страницу с благодарностью за участие в опросе, или же просто на главную.

### В конструкторе Mindbox

В конструкторе Mindbox опрос можно настроить двумя способами:

- с помощью готовых стандартных блоков
- или с помощью пустых гибких блоков.

#### Через готовые блоки

1. Добавьте в письмо блок с опросом с вкладки «Стандартные» → «Опрос»:

   ![how-to-create-a-poll-editor-blocks.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/how-to-create-a-poll-editor-blocks.png)
2. Для каждого варианта ответа укажите:

   - Тип ссылки «Опрос» (по умолчанию)
   - **Ссылка перехода по клику:** страница, куда перейдёт клиент. Например, `https://example.ru/`. Для всех вариантов можно использовать одну ссылку;
   - **Метка ссылки:** системное название шаблона действия из шага 1 (например, `Da`, `Net`). Именно метка связывает вариант ответа с действием клиента.

   ![how-to-create-a-poll-editor-link.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/how-to-create-a-poll-editor-link.png)
3. Сохраните рассылку.

#### Через пустой блок

Подробнее о работе с гибкими пустыми блоками в [статье](https://help.mindbox.ru/docs/email-editor#sborka-pisma-iz-blokov).

1. Добавьте в письмо блок из раздела «Пустой блок»:

   ![email-editor-flex-blocks.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-flex-blocks.png)
2. Добавьте колонку для каждого варианта ответа.
3. В каждую из колонок добавьте элемент **«Текст»**:

   ![how-to-create-a-poll-editor-flex-text.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/how-to-create-a-poll-editor-flex-text.png)
4. Введите текст вариантов ответа и настройте оформление (обводка, цвет, шрифт):

   ![how-to-create-a-poll-editor-flex-answers.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/how-to-create-a-poll-editor-flex-answers.png)
5. Выделите текст и добавьте к нему ссылку. В настройках укажите:

   - Тип — Опрос;
   - Ссылка перехода по клику — страница для перехода (например, `https://example.ru/`);
   - Метка ссылки — системное название шаблона действия из шага 1 (например, `Da`, `Net`). Именно метка связывает вариант ответа с действием клиента.

   ![how-to-create-a-poll-editor-flex-link.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/how-to-create-a-poll-editor-flex-link.png)
6. Сохраните рассылку.

При создании голосования в разделе **Кампании → Голосования** варианты ответов подтянутся автоматически из рассылки.

## 4. Настройка голосования

1. Перейдите в раздел **Кампании**:

   ![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)
2. Нажмите на «Создать кампанию» → «Голосование»:

   ![создать-голосование.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B3%D0%BE%D0%BB%D0%BE%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.png)
3. Выберите папку и нажмите «Создать»:

   ![Снимок экрана 2023-01-23 в 00.49.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-01-23%20%D0%B2%2000.49.53.png)
4. Заполните настройки голосования и нажмите «Добавить»:

   ![Снимок экрана 2021-10-08 в 16.51.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-10-08%20%D0%B2%2016.51.36.png)

Клики в тестовых письмах не учитываются. Для тестирования голосования нужно отправить массовую или автоматическую рассылку с помощью сценария.

Подробнее в статье — [«Как протестировать рассылку».](%D0%BA%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md)

[4 сервиса для тестирования HTML-писем](https://mindbox.ru/academy/education/servisy-dlya-testirovaniya-pisem/) — узнайте, как будет выглядеть письмо у подписчиков
