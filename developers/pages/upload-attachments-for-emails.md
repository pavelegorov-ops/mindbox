---
title: Загрузка вложений для использования в письмах
slug: "upload-attachments-for-emails"
source_url: "https://developers.mindbox.ru/docs/upload-attachments-for-emails"
breadcrumb:
  - Рассылки
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:66cf67898793548d109a113fcd0729fd50075891192bac22b6a105b8d6dc0261"
---

# Загрузка вложений для использования в письмах

## Описание метода

Осуществляется с помощью POST-запроса. В ответе возвращается идентификатор файла

```
POST https://api.mindbox.ru/v3/files/upload?endpointId={уникальный идентификатор сайта/мобильного приложения/и т.п.}&fileKind=attachment

Accept: application/json
Content-Type: multipart/form-data
Authorization: SecretKey {Секретный ключ}
```

- секретный ключ — уточнить у менеджера

Максимальный размер загружаемого файла — 25 МБ

В запросе всегда передается заголовок Content-Type: multipart/form-data. Для такого типа обязателен параметр boundary, который определяет границы вложений. При тестировании через postman он добавляется автоматически:

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/4f35d77-__2022-06-19__20.22.28.png)

При загрузке каждого файла отдельно передается его Content-Type.

Список поддерживаемых Content-Type'ов файлов:  
application/msword,  
application/pdf,  
application/rtf,  
application/vnd.ms-excel,  
application/vnd.ms-powerpoint,  
application/vnd.oasis.opendocument.graphics,  
application/vnd.oasis.opendocument.presentation,  
application/vnd.oasis.opendocument.spreadsheet,  
application/vnd.oasis.opendocument.text,  
application/vnd.openxmlformats-officedocument.presentationml.presentation,  
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,  
application/vnd.openxmlformats-officedocument.wordprocessingml.document,  
application/x-7z-compressed,  
application/x-rar-compressed,  
application/zip,  
image/gif,  
image/jpeg,  
image/pjpeg,  
image/png,  
image/svg+xml,  
image/tiff,  
image/vnd.microsoft.icon,  
text/calendar  
text/html,  
text/plain,  
video/mp4,  
video/mpeg,

## Пример запроса

```
POST https://api.mindbox.ru/v3/files/upload?endpointId=test.test&fileKind=attachment

Accept: application/json
Content-Type: multipart/form-data;
				boundary="gc0p4Jq0M2Yt08jU534c0p"
Authorization: SecretKey ***********
```

## Пример ответа

```
{
  "fileId": "065773e7-4eef-4b32-8306-db5103bb3e9f"
}
```

Для отправки рассылки с вложением нужно передать в контракте операции уникальный ключ вложения. Специальных настроек в интерфейсе рассылок делать не нужно.

## Что дальше

- [Отправка рассылок по API](api-mailings-send.md)
- [Как отправить рассылку с загруженным вложением](https://help.mindbox.ru/docs/email-with-attachment)
