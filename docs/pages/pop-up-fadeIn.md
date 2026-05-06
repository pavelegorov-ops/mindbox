---
title: Настроить плавное появление попапа
slug: "pop-up-fadeIn"
source_url: "https://help.mindbox.ru/docs/pop-up-fadeIn"
vcs_path: "pop-up-fadeIn.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Попапы и встроенные блоки
  - Собственная верстка форм
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:c844edd533117a173a137e7be71e1a818c45bbd59c061bf8c9edefbb575dc323"
---

# Настроить плавное появление попапа

![pop-up-fadein-example5.gif](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/pop-up-fadein-example5.gif)

Чтобы настроить плавное появление попапа:

1. В редактировании формы откройте код, вкладку CSS:

![pop-up-fadein-code.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/pop-up-fadein-code.png)

2. Добавьте в стили `#popmechanic-form` следующие строки:

```
animation-name: popmechanic-fadeIn;
animation-duration: Ns;
```

где N — количество секунд до полного отображения попапа.

![pop-up-fadein-animation-added.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/pop-up-fadein-animation-added.png)

Если CSS уже заложена анимация, но она не подходит для решения задачи, закомментируйте ее с помощью символов `//`:

![pop-up-fadein-animation-commented.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/pop-up-fadein-animation-commented.png)

Учтите, что при слишком долгой отрисовке клиент может уйти со страницы до появления формы.
