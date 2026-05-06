---
title: Как создать попап с видео
slug: "pop-up-with-video"
source_url: "https://help.mindbox.ru/docs/pop-up-with-video"
vcs_path: "pop-up-with-video.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Дополнительные настройки
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:9279ab2e273b42f2825ace59b27777b401814b8740dde91dd6936a32b292ce34"
---

# Как создать попап с видео

Рассмотрим способ создания попапа с видео:  
[  
](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/попап%20с%20видео.mov)

Добавьте в кампанию [попап](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md):

![создать-попап.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF%D0%B0%D0%BF.png)

Выберите шаблон. Например, информационный с картинкой:

![Снимок экрана 2022-08-05 в 16.14.04.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2016.14.04.png)

После выбора шаблона укажите сайт:

![выбрать сайт.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D1%8B%D0%B1%D1%80%D0%B0%D1%82%D1%8C%20%D1%81%D0%B0%D0%B9%D1%82.png)

В разделе «Попап» нажмите «Изменить», затем — «Редактировать»:

![редактировать попап.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%BF%D0%BE%D0%BF%D0%B0%D0%BF.png)

Откройте код:

![Снимок экрана 2022-08-05 в 22.25.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2022.25.35.png)

Уберите тег <img/>:

![Снимок экрана 2022-08-05 в 22.26.38.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2022.26.38.png)

И вставьте код с ссылкой на видео:

```
<video controls autoplay loop muted class="popmechanic-video popmechanic-video-desktop">
<source src="ссылка на видео" type="video/mp4">
</video>
```

![Снимок экрана 2022-08-05 в 22.55.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2022.55.45.png)

Ссылка должна выдавать конкретный видеофайл, загруженный в хранилище, а не вести на страницу для его скачивания. Поэтому не подходят такие системы как Битрикс24 или Яндекс Диск. Ссылка на видео в YouTube или Rutube также не подойдет.  
Рекомендуем загрузить видео на сайт, на котором будет показана форма.

Используем тег <video> с атрибутами:

- autoplay — видео воспроизводится автоматически после загрузки страницы;
- loop — после завершения видео повторяется с начала;
- controls — добавляет панель управления к видео;
- muted — видео включается без звука.

В последних версиях Google Chrome блокируется автовоспроизведение видео со звуком. Чтобы этого избежать, используйте атрибут muted

В css замените селектор img на video, чтобы свойства прописались нужному тегу:

![Снимок экрана 2022-08-05 в 22.56.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2022.56.14.png)

Протестируйте на сайте:

![Снимок экрана 2022-08-05 в 22.57.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-05%20%D0%B2%2022.57.01.png)

Остальные настройки попапа выполните по [базовой инструкции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md).

[Как использовать попапы, не раздражая клиентов](https://mindbox.ru/academy/education/kak-ispolzovat-popapy/). Какие ошибки совершают бренды при создании попапов и как сделать, чтобы этот инструмент приносил пользу и клиенту, и компании.
