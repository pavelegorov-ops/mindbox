---
title: Интеграция формы персонализации сайта с Sendsay
slug: "mindbox-popup-blocks-intergration-with-sendsay"
source_url: "https://help.mindbox.ru/docs/mindbox-popup-blocks-intergration-with-sendsay"
vcs_path: "mindbox-popup-blocks-intergration-with-sendsay.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:1425ed912850bf211faa58af65f8d3416c66a9211583e684d845f6338b931228"
---

# Интеграция формы персонализации сайта с Sendsay

**Задача:** настроить передачу лидов из форм персонализации сайта Mindbox в Sendsay.

#### Для настройки понадобится:

- Настроить веб-хук
- Настроить сценарий

Перед началом настройки убедитесь, что создали нужную форму в Mindbox и после регистрации в этой форме новый клиент создается в базе.

Как создать нового клиента в Mindbox после регистрации в форме можно прочитать по [ссылке](%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D0%B5%D1%81%D1%82%D1%8C-%D0%B4%D0%B5%D0%B8%D1%81%D1%82%D0%B2%D0%B8%D1%8F-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D1%84%D0%BE%D1%80%D0%BC%D1%8B.md#sozdat-novogo-klienta-ili-redaktirovat-sushestvuyushego).

## Настройка веб-хука

Для настройки нужно получить на стороне Sendsay общий логин проекта, ключ апи для отправки API запроса и id сегмента.

Где найти общий логин и API ключ можно подробнее прочитать по [ссылке](https://docs.google.com/document/d/1srO1FXdCO6ylaBEYDYSXzs_eDnomnJmywuhm5oAajiY/edit?usp=sharing).

Чтобы узнать id сегмента, нужно перейти на страницу сегмента в Sendsay и скопировать id из URL страницы.

```
https://app.sendsay.ru/subscribers/segments/здесь будет id сегмента/summary
```

Полученные данные нужно подставить в соответствующие поля при настройке веб-хука, как показано на скриншоте.

![Снимок экрана 2022-08-31 в 11.43.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-31%20%D0%B2%2011.43.47.png)

Пример URL запроса:

```
https://api.sendsay.ru/general/api00/json/подставить общий логин проекта Sendsay/
```

Пример тела запроса:

```
{
 "apikey" : "подставить API ключ",
  "action" : "member.set",
  "email": "${Recipient.Email}",
   "obj" : {
     "-group" : {
"подставить id сегмента в Sendsay":"1"
     }
   }

}
```

Подробнее о настройке веб-хуков в Mindbox можно узнать по [ссылке](webhooks.md).

## Настройка сценария

Сценарий нужно запускать по событию регистрации в форме и следующим шагом отправлять веб-хук. Будет выглядеть так:

![Снимок экрана 2022-08-31 в 10.43.52.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-31%20%D0%B2%2010.43.52.png)

![Снимок экрана 2022-08-31 в 10.35.03.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-08-31%20%D0%B2%2010.35.03.png)

Подробнее о том, как создать сценарий можно прочитать в статье по [ссылке](what-is-workflow.md).

[Что такое вебхуки](https://mindbox.ru/academy/education/pro-veb-huki/) и как они используются, где их можно настроить, примеры использования в Mindbox.
