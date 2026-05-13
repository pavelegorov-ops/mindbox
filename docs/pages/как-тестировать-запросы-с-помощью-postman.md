---
title: Как тестировать запросы с помощью Postman
slug: "как-тестировать-запросы-с-помощью-postman"
source_url: "https://help.mindbox.ru/docs/как-тестировать-запросы-с-помощью-postman"
vcs_path: "как-тестировать-запросы-с-помощью-postman.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:c1e0ed4089c017e8bfc65d56c617d1c57f8abd82f6efc32f41f3692ca8c24db1"
---

# Как тестировать запросы с помощью Postman

**Postman** — это инструмент для тестирования и разработки API, который позволяет удобно отправлять запросы и получать ответы от серверов. Так как у Mindbox открытое API, вы можете отправить любой тестовый запрос самостоятельно, не прибегая к помощи вашей команды разработки.

## Как начать работу

Установите Postman и зарегистрируйтесь по кнопке «Sign up for free»:

![postman-sign-up](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-sign-up.png)

Пропустите выбор плана и нажмите «Continue with Free Plan»:

![postman-sign-up-free](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-sign-up-free.png)

После установки и регистрации можно приступать к тестированию вызовов.

## Как собрать запрос

Чтобы создать новый запрос, нажмите на `+` в панели запросов:

![postman-add-new-request](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-add-new-request.png)

Запрос к API Mindbox состоит из трех частей:

- URL запроса,
- заголовки (headers),
- тело запроса (body).

### URL запроса

Перейдите в [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md), которую надо протестировать. Данные для запроса хранятся в описании операции:

![postman-operation](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation.png)

Скопируйте URL и метод запроса:

![postman-operation-description-url](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-description-url.png)

Далее нужно отредактировать URL:

1. **Метод запроса**: укажите метод из описания операции.
2. **Тип вызова**: `sync`(синхронно) или `async`(асинхронно) без фигурных скобок. Способ вызова зависит от настроек вашей операции — подробнее о синхронных и асинхронных вызовах операций можно прочитать в [статье](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sinhronnye-i-asinhronnye-vyzovy-operacij).

   Если в вашей операции не нужно получать в ответ данные от Mindbox или результат выполнения операции — укажите `async`.
3. `endpointId`: после знака `=` пропишите системное имя той точки интеграции, через которую будет вызываться операция.

   - Чтобы узнать идентификатор точки интеграции, вернитесь к настройкам операции и посмотрите, в каких точках интеграции она доступна:

   ![postman-operation-endpoint](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-endpoint.png)

   - Далее зайдите в раздел «Интеграции» и найдите эту точку интеграции. Системное имя будет в колонке «Точка интеграции»:

   ![postman-operation-endpoint-integration](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-endpoint-integration.png)
4. `transactionID`: необходим для ряда операций, которые могут быть вызваны только с [ключом идемпотентности](idempotentnost.md) (например, операций с шагом «Заказ — Процессинг — Создать или обновить заказ»).

   `transactionID` передается в виде *GUID*. Для тестовых запросов можете воспользоваться [генератором GUID](https://www.guidgenerator.com/).

Пример

Так будет выглядеть URL для операции WebsiteCreateOrder с шагом «Заказ — Процессинг — Создать или обновить заказ»:

- Метод: POST
- URL: `https://api.mindbox.ru/v3/operations/sync?endpointId=demo.Website&operation=WebsiteCreateOrder&transactionId=966e4287-4858-4504-aba9-b0398bc4e4e4`

![postman-url-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-url-example.png)

### Заголовки запроса

1. Скопируйте заголовки из описания операции:

   ![postman-operation-description-headers](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-description-headers.png)
2. Перейдите во вкладку «Headers» в Postman и нажмите «Bulk Edit».

   ![postman-operation-postman-headers](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-postman-headers.png)
3. Вставьте скопированные данные в текстовое окно:

   ![postman-operation-postman-headers-example](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-postman-headers-example.png)
4. Если операция требует передачи [секретного ключа](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md#sekretnye-klyuchi), замените {Секретный ключ} на секретный ключ вашей точки интеграции.

   - Перейдите в точку интеграции, которая была выбрана при заполнении URL.
   - В блоке «Секретные ключи» скопируйте основной или тестовый ключ.

### Тело запроса

Далее необходимо собрать тело запроса с тестовыми данными. Воспользуйтесь одним из вариантов:

- Соберите новый запрос из доступных параметров в описании операции.
- Скопируйте уже готовое тело запроса из [лога операции](operation-logs.md).

Перейдите в раздел «Body» и выберите вариант «raw». Вставьте скопированное тело запроса в текстовое поле:

![postman-operation-postman-body](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-postman-body.png)

Чтобы сделать вложенность элементов запроса более понятной, воспользуйтесь функцией «Beautify»:

![postman-operation-postman-beautify](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-postman-beautify.png)

Когда запрос собран, можно нажимать кнопку «Send» для его отправки. В поле «Response» вернется ответ от сервера Mindbox.

![postman-operation-postman-response](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/postman-operation-postman-response.png)

Если в ответе вернулось 200 и Success, то можно вернуться в Mindbox и проверить выполнение нужного действия в карточке клиента. А о кодах ошибок пишем [тут](https://developers.mindbox.ru/docs/error_processing#/).

При наличии синтаксических ошибок в JSON, воспользуйтесь любым сервисом для валидации JSON.

[Работа с API без навыков программирования](https://mindbox.ru/academy/education/kak-rabotat-s-api/) — интегрируем друг с другом разные сервисы типа банкинга, телефонии и CRM-систем.

Статически уникальный идентификатор, состоящий из 32 символов, разделенных дефисом.
