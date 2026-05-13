---
title: Тикет для авторизации на сайте
slug: "website-authorization-ticket"
source_url: "https://developers.mindbox.ru/docs/website-authorization-ticket"
breadcrumb:
  - Общее
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:6c9ee5eb2b032ffd946429a5d8c6035d4f5e40d9003b5cc3daa359915be412a7"
---

# Тикет для авторизации на сайте

## Алгоритм генерации

Для генерации тикета нужно выполнить следующие шаги:

- Сгенерировать сообщение. Содержание сообщения зависит от типа тикета:
  - тикет с идентификатором клиента;
  - тикет с e-mail адресом;
  - тикет с номером мобильного телефона;
    Виды сообщений в зависимости от типа тикета описаны ниже.
- Вычислить хеш от сообщения по алгоритму hmac (секретный ключ можно скопировать [из точки интеграции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8#sekretnye-klyuchi) или запросить у владельца проекта). В качестве алгоритма хэширования в hmac надо использовать sha512.
- Перевести сообщение и хеш в HEX строки. Для преобразования сообщения в массив байт использовать кодировку UTF-8. Важно, если библиотека хэширования возвращает хэш в виде HEX строки, не надо повторно кодировать ее в HEX.
- Объединение строк через символ "|": |.
- MyWebSite — системное имя поля, в котором хранится идентификатор пользователя на сайте. Настраивается в системе Mindbox.

#### Пример на псевдокоде

```
string secretKey = "PUT_YOUR_SECRET_KEY_HERE"

  string myWebSiteId = "1543"

  DateTime dateTime = GetCurrentDateTime()
  string dateTimeString = dateTime.ToString("yyyy-MM-dd HH:mm:ss")

  string message = "ExternalIdentityAuthentication|MyWebSite|" + myWebSiteId + "|" + dateTimeString 
  byte[] messageBytes = StringToBytesInUTF8(message)

  byte[] hash = hmacSha512(messageBytes, secretKey)

  string messageHexString = ByteArrayToHexString(messageBytes)
  string hashHexString = ByteArrayToHexString(hash)

  string result = messageHexString + "|" + hashHexString
```

#### Пример на PHP

## Частые ошибки

- Убедитесь, что указывайте время в часовом поясе UTC+0 (минус три часа от Московского времени).
- При использовании тикета с идентификатором клиента убедитесь, что заменили ID из примера (MyWebSite) тот, который реально создан в вашем проекте Mindbox.

## Сообщение для тикета c идентификатором

Сообщение следующего формата:  
ExternalIdentityAuthentication|||`<дата и время в часовом поясе UTC+0 в формате yyyy-MM-dd HH:mm:ss>`

- где externalIdentitySystemName — системное имя поля, в котором хранится идентификатор пользователя на сайте. Настраивается в системе Mindbox.
- identity – идентификатор клиента.
- тикет считается валидным в течение получаса с указанной в нем даты и времени.

**Пример:**  
ExternalIdentityAuthentication|MyWebSite|1543|2015-12-10 09:12:25

Обратите внимание, что **MyWebSite** нужно заменить на системное имя идентификатора.

## Сообщение для тикета с email-адресом

Сообщение следующего формата:  
EmailAuthenticationHex||`<дата и время в часовом поясе UTC+0 в формате yyyy-MM-dd HH:mm:ss>`

- тикет считается валидным в течение получаса с указанной в нем даты и времени

**Пример:**  
EmailAuthenticationHex|[test@mail.ru](mailto:test@mail.ru)|2015-12-10 09:12:25

## Сообщение для тикета с номером мобильного телефона

Сообщение следующего формата:  
MobilePhoneAuthenticationHex|`<номер мобильного телефона клиента>`|`<дата и время в часовом поясе UTC+0 в формате yyyy-MM-dd HH:mm:ss>`

- тикет считается валидным в течение получаса с указанной в нем даты и времени
- номер мобильного телефона должен быть в международном формате, без знака выбора страны (+), без пробелов и дефисов.

**Пример:**  
MobilePhoneAuthenticationHex|79000000001|2015-12-10 09:12:25

- при вводе пустой строки, будет использовано текущее значение даты и времени в часовом поясе UTC+0

Для тестирования алгоритма генерации тикета можно воспользоваться консольным приложением для сравнения результатов: [DirectCrmTicketGenerator.exe](https://cdn.document360.io/54e2940a-f593-4b09-a41c-a2d31eebd57d/Images/Documentation/DirectCrmTicketGenerator.exe)
