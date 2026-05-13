---
title: Как отправить рассылку с вложением
slug: "email-with-attachment"
source_url: "https://help.mindbox.ru/docs/email-with-attachment"
vcs_path: "email-with-attachment.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Дополнительные возможности рассылок
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:5531795c4e49bbff7c61313f20a877bba25bdbf94498ffd27059ffb151294e5f"
---

# Как отправить рассылку с вложением

Отправить рассылку с вложением можно через вызов операции API.

Как это работает:

1. Файл загружается на сервер, в результате чего формируется его **уникальный идентификатор**.
2. Далее рассылка отправляется через операцию, в вызове к которой указывается полученный идентификатор в вызове этот идентификатор. Таким образом, к письму прикрепляется нужное вложение.

Рассмотрим шаги подробнее.

## 1. Загрузите вложение на сервер

Общий метод загрузки вложения описан в [инструкции](https://developers.mindbox.ru/docs/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0-%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B4%D0%BB%D1%8F-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%B0%D1%85#/). В этом разделе расскажем, как это сделать самостоятельно через Postman.

[Как начать работу с Postman](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-postman).

### Подготовка запроса

1. Выберите метод `POST`
2. Скопируйте общий адрес URL и отредактируйте его под данные вашего проекта.

**Общий вид URL:**

```
https://api.mindbox.ru/v3/files/upload?endpointId={уникальный идентификатор точки интеграции}&fileKind=attachment
```

**Какие части URL необходимо отредактировать:**

- [api.mindbox.ru](http://api.mindbox.ru) — домен запроса. Он может отличаться в зависимости от вашего проекта.

  **Как определить домен API Mindbox**

  1. Перейдите в раздел Кампании — Операции проекта
  2. Откройте любую операцию
  3. Нажмите «Посмотреть описание»
  4. Скопируйте домен из URL.

  ![api_url_domen](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/api_url_domen.png)

  На примере этого скриншота `api.mindbox.ru` нужно заменить на `api.s.mindbox.ru`.
- `endpointId`: после знака `=` пропишите системное имя той точки интеграции, через которую будет вызываться операция.

  Вы можете использовать любую точку интеграции из раздела раздел «Интеграции». Системное имя будет в колонке «Точка интеграции»:

  ![postman-operation-endpoint-integration](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-endpoint-integration.png)

**Пример готового URL:**

```
https://api.s.mindbox.ru/v3/files/upload?endpointId=demo.Website&fileKind=attachment
```

### Заголовки

Скопируйте и вставьте заголовки ниже во вкладку «Headers» по [инструкции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-postman#zagolovki-zaprosa). Эта операция требует передачи [секретного ключа](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8#sekretnye-klyuchi) - замените `{Секретный ключ}` на секретный ключ точки интеграции, которая указана в `endpointId` адреса URL.

```
Accept: application/json  
Content-Type: multipart/form-data  
Authorization: SecretKey {Секретный ключ}
```

![email-attachment-headers-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-attachment-headers-example.png)

### Добавление файла к запросу

1. Перейдите в раздел «Body» и выберите «form-data»:

![email-attachment-body](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-attachment-body.png)

2. Далее выберите `File` в поле `Key` и нажмите `Select Files` в поле «Value». В появившемся системном окне выберите файл, который хотите приложить к рассылке.

![email-attachment-body-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-attachment-body-example.png)

### Отправление запроса

Нажмите «Send». Скопируйте полученное значение `fileId`:

![email-attachment-send](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-attachment-send.png)

## 2. Создайте автоматическую email-рассылку

[Инструкция](email-trigger.md)

![Снимок экрана 2022-11-02 в 19.32.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-02%20%D0%B2%2019.32.41.png)

## 3. Добавьте операцию с шагом отправки созданной рассылки

[Инструкция](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md)

Пример настройки:

![Снимок экрана 2022-10-27 в 00.08.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-10-27%20%D0%B2%2000.08.51.png)

### Соберите вызов

Перейдите в описание операции. При использовании в операции шага «Отправить Email», в спецификацию его запроса добавляется контракт для прикрепления файла:

![Снимок экрана 2022-10-27 в 00.14.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-10-27%20%D0%B2%2000.14.08.png)

- `fileId` — идентификатор файла, полученный на первом шаге;
- `fileName` — как файл будет называться в отправленном письме.

Оба поля обязательны для отправки вложения.

Пример тела запроса:

```
<operation>
  <customer>
    <email>test@mindbox.ru</email>
  </customer>
  <emailMailing>
    <attachments>
      <attachment>
        <fileName>Док</fileName>
        <body>
          <fileId>4d238d4e-20a8-4a44-9388-b16bf206978a</fileId>
        </body>
      </attachment>   
    </attachments>
  </emailMailing>
</operation>
```

---

Отображение в почтовом сервисе:

![Снимок экрана 2022-11-02 в 19.31.18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-02%20%D0%B2%2019.31.18.png)

## Частые вопросы

### Какие файлы можно прикреплять?

Поддерживаются форматы:

```
application/msword
application/pdf
application/rtf
application/vnd.ms-excel
application/vnd.ms-powerpoint
application/vnd.oasis.opendocument.graphics
application/vnd.oasis.opendocument.presentation
application/vnd.oasis.opendocument.spreadsheet
application/vnd.oasis.opendocument.text
application/vnd.openxmlformats-officedocument.presentationml.presentation
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
application/vnd.openxmlformats-officedocument.wordprocessingml.document
application/x-7z-compressed
application/x-rar-compressed
application/zip
image/gif
image/jpeg
image/pjpeg
image/png
image/svg+xml
image/tiff
image/vnd.microsoft.icon
text/calendar
text/html
text/plain
video/mp4
video/mpeg
```

### Есть ли ограничения по размеру файла?

Максимальный размер письма вместе со всеми вложениями — 25Мб.

### Есть ли ограничения по количеству файлов?

Количество вложений не ограничено.

### Как посмотреть вложения в отправленных письмах

Просмотр вложений из интерфейса проекта невозможен. Для этого нужно переслать себе письмо из **карточки клиента**:

![Снимок экрана 2022-11-02 в 17.43.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-11-02%20%D0%B2%2017.43.36.png)

Переслать рассылку с вложением можно только при наличии пермиссии «Переотправка вложений из писем». Изначально она есть только у группы «Владельцы», можно [выдать дополнительно](staff-add-permissions-and-groups.md).

При отсутствии прав у персонала письмо будет отправлено без вложения.

[4 сервиса для тестирования HTML-писем](https://mindbox.ru/academy/education/servisy-dlya-testirovaniya-pisem/) — узнайте, как будет выглядеть письмо у подписчиков
