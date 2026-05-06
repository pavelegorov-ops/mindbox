---
title: "Как создать AMP-письмо"
slug: "amp-email"
source_url: "https://help.mindbox.ru/docs/amp-email"
vcs_path: "amp-email.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Дополнительные возможности рассылок
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:d942c4f0d036ae9fd6aceef07040cb0b929e99d0e2321e9757a8017510a38f42"
---

# Как создать AMP-письмо

В письма, созданные в формате AMP, можно подставлять интерактивные элементы (игры, карусели и так далее), а также создавать опросники внутри самого письме без переадресации на сторонние ресурсы.

Mindbox поддерживает отправку AMP писем вместе со стандартными шаблонами. При настройке email-рассылки нужно сверстать обычный шаблон HTML или в конструкторе, и добавить AMP версию письма:

![amp-email-add](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/amp-email-add.png)

AMP формат поддерживают:

- Yahoo Mail
- Gmail
- Mail.ru.

Клиенты других почтовых сервисов получат стандартную версию письма.

Первое, что необходимо сделать - это получить разрешения от Google и mail.ru на отправку AMP-писем. На официальном сайте Google есть [инструкция](https://developers.google.com/gmail/ampemail/) по настройке. Такое разрешение нужно получить для каждого домена, с которого будут происходить отправки рассылок, эти домены будут помещены в white-list Gmail. На [официальном сайте](https://help.mail.ru/developers/amp/enable) mail.ru так же есть инструкция и форма для заявки в white-list. То же самое - для [Yahoo Mail](https://developer.verizonmedia.com/mail/amp-for-email/).

И у [Gmail](https://amp.gmail.dev/playground/), и у [mail.ru](https://postmaster.mail.ru/amp/playground.html?lang=ru#hello-world) есть возможность попробовать AMP-письма в "песочнице".

До получения разрешения от почтового сервиса все письма из рассылок (в том числе тестовые) будут приходить в стандартном HTML-формате.

В Gmail есть возможность разрешить отображение AMP-письма для тестирования для одного отправителя в настройках почты (Настройки - Общие - Динамический контент - Настройки для разработчиков).

Пример минимального кода, который имеет необходимую разметку для формирования AMP письма

```
<!doctype html>
<html ⚡4email data-css-strict>
<head>
  <meta charset="utf-8">
  <script async src="https://cdn.ampproject.org/v0.js"></script>
  <style amp4email-boilerplate>body{visibility:hidden}</style>
  <style amp-custom>
    h1 {
      margin: 1rem;
    }
  </style>
</head>
<body>
  <h1>Hello, I am an AMP EMAIL!</h1>
</body>
</html>
```

Всё об [AMP-рассылках](https://mindbox.ru/journal/education/amp-rassylki/)
