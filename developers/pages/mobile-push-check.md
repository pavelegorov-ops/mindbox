---
title: "Проверка корректной работы мобильных push-уведомлений"
slug: "mobile-push-check"
source_url: "https://developers.mindbox.ru/docs/mobile-push-check"
breadcrumb:
  - Мобильные приложения
  - Справочное
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:50e75824e8ae42c3cec786794dc9c5e79023ae5f1a13f99b11c8fd3bd600fdd8"
---

# Проверка корректной работы мобильных push-уведомлений

Дебаг стандартных ошибок — [здесь](sdk-integration-checklist.md).

## Проверить, что мобильное push-уведомление отправляется

### Результат проверки:

Пуш должен отправиться и отобразиться на вашем телефоне

Найдите клиента по deviceUUID и откройте страницу с подробной информацией:

Статус разрешения на уведомления (Notifications permission status): **Разрешены (Allowed)**  
Статус устройства (Device status): **Активировано (Activated)**

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/55885c7-5d18424-1.png "5d18424-1.png")

## Отправка тестового пуша

1. Запустите приложение на физическом телефоне (эмулятор не умеет получать пуши)
2. Получите в консоли deviceUUID
3. [Создайте рассылку](https://help.mindbox.ru/docs/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BF%D1%83%D1%88%D0%B5%D0%B9) мобильных пушей в системе и заполните в ней заголовок и текст
4. Нажмите кнопку «отправить тестовое» и введите в поле поиска deviceUUID

Если вы тестируете пуши в iOS приложении в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/31ed09b-5f71d52-2.png "5f71d52-2.png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/5a6193b-af9b394-3.png "af9b394-3.png")

5. Отправьте сообщение;
6. Откройте список тестовых сообщений и проверьте, что у последнего пуша статус «отправлено».

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/719ea24-a113c6f-5.png "a113c6f-5.png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/2f259fb-e52eb0b-6.png "e52eb0b-6.png")

Пуш должен отправиться и отобразиться на вашем телефоне.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/fbc0d0c-2e41222-7.png "2e41222-7.png")

## Проверить, что мобильное push-уведомление с картинкой отправляется корректно

1. Запустите приложение на физическом телефоне (эмулятор не умеет получать пуши)
2. Получите в консоли deviceUUID
3. Создайте рассылку мобильных пушей в системе и заполните в ней заголовок, текст и укажите URL картинки или загрузите картинку на наш сервер.
4. Нажмите кнопку «отправить тестовое» и введите в поле поиска deviceUUID

Если вы тестируете пуши в iOS приложении в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/fea3186-db60478-11.png "db60478-11.png")

## Проверить, что кнопки отрисовались при клике на пуш

1. Запустите приложение на физическом телефоне (эмулятор не умеет получать пуши)
2. Получите в консоли deviceUUID
3. Создайте рассылку мобильных пушей в системе и заполните в ней заголовок, текст, укажите URL картинки или загрузите картинку на наш сервер и заполните поля для кнопок с текстом и URL.
4. Нажмите кнопку “отправить тестовое” и введите в поле поиска deviceUUID

Если вы тестируете пуши в iOS приложении в окружении Sandbox, не забудьте поставить галочку "Тестовое сообщение Sandbox" в профиле рассылки "Вручную".  
[Подробнее про Sandbox-окружение](sandbox-integration-setup.md)

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7ce757c-Untitled_6.png "Untitled (6).png")

## Проверить, что клики приходят в систему

1. Запустите приложение на физическом телефоне (эмулятор не умеет получать пуши)
2. Получите в консоли deviceUUID
3. [Создайте](https://help.mindbox.ru/docs/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BF%D1%83%D1%88%D0%B5%D0%B9) рассылку мобильных пушей в системе и заполните в ней заголовок и текст
4. Нажмите кнопку “отправить тестовое” и введите в поле поиска deviceUUID

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/7c449a0-Untitled_1.png "Untitled (1).png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/a0ac388-Untitled_2.png "Untitled (2).png")

5. Отправьте сообщение
6. Нажмите на полученный пуш
7. Откройте список тестовых сообщений и проверьте, что у последнего пуша статус “**Доставлено клиенту - Клик по ссылке**”.

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/41993ab-Untitled_3.png "Untitled (3).png")

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/161d2d6-Untitled_4.png "Untitled (4).png")
