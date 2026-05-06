---
title: Статус подтверждения контакта
slug: "email-and-mobile-confirmation"
source_url: "https://help.mindbox.ru/docs/email-and-mobile-confirmation"
vcs_path: "email-and-mobile-confirmation.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Клиенты
  - Контакты и идентификаторы
  - Подтверждение контактов
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:9fc098126058e052a8180202062804599f7ec9e8e7265fafe93c3987d27e6993"
---

# Статус подтверждения контакта

## Что такое «Подтверждение контакта»

**Подтверждение контакта** позволяет убедиться, что телефон или почта действительно принадлежат клиенту.

Не путайте с [подтверждением подписки (DOI)](doi-turn-on.md): оно означает согласие получать рассылки и напрямую связано с [подписками](subscriptions.md).

## Как включить подтверждение контактов

Подтверждение email и мобильного телефона настраивается на уровне [интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) в разделе «Настройки подтверждения контактов»:

![Снимок экрана 2023-06-20 в 12.07.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-06-20%20%D0%B2%2012.07.56.png)

После этого, контакты, проходящие через данную интеграцию, будут иметь признак подтверждения и учитывать его при обработке запросов.

Включение настройки не влияет на уже имеющиеся в базе контакты.

## После включения

### Как выглядят контакты

У email’ов и мобильных номеров появляются иконки:

- ожидающий подтверждения контакт:

![email-and-mobile-confirmation-notconfirmed.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-notconfirmed.png)

- подтвержденный контакт:

![email-and-mobile-confirmation-confirmed.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-confirmed.png)

У контактов без данных по подтверждению остается отображение без иконок.

#### Основной и ожидающий подтверждения контакты

На проектах с включенным подтверждением контакты делятся на основные и ожидающие подтверждения.

- **Основной контакт** может быть подтвержденным или ожидать подтверждения. Он обладает всеми свойствами обычного контакта: должен быть уникальным в рамках проекта, на него можно отправлять стандартные рассылки, его значение можно использовать в фильтрах и запросах и т.д.;
- **Неосновной контакт — всегда ожидающий подтверждения.** Его применение сильно ограничено: на него можно отправлять только рассылки [с определенными настройками](email-and-mobile-confirmation.md#na-kakie-kontakty-mozhno-otpravlyat-rassylki). Требования по уникальности нет, то есть он может дублировать чей-то основной контакт или быть одинаковым у нескольких клиентов.

С этим связаны описанные ниже особенности.

#### Почему у клиента два email-адреса или телефона?

![email-and-mobile-confirmation-two-contacts.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-two-contacts.png)

При попытке изменить подтвержденный контакт, старый, подтвержденный, контакт остается основным, пока не будет подтвержден новый.  
На ожидающий email или номер можно отправить только сообщение с кодом или ссылкой подтверждения. То есть он не является вторым полноценным контактом.

Таких клиентов можно найти с помощью фильтра:

![email-and-mobile-confirmation-two-contacts-filter.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-two-contacts-filter.png)

#### Почему у клиента ожидающий подтверждения контакт не основной?

![email-and-mobile-confirmation-only-notconfirmed.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-only-notconfirmed.png)

Основной контакт, будь он подтвержденным или нет, должен быть уникальным в рамках проекта. Поэтому, если один клиент подтвердил определенный email, у другого клиента этот контакт перейдет в неосновной, ожидающий подтверждения.

Таких клиентов можно найти с помощью фильтра:

![email-and-mobile-confirmation-only-notconfirmed-filter.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-only-notconfirmed-filter.png)

#### Почему у двух клиентов одинаковый контакт?

![email-and-mobile-confirmation-same-contact1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-same-contact1.png)  
![email-and-mobile-confirmation-same-contact2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-same-contact2.png)

Неосновной контакт не имеет требований по уникальности. Поэтому, если несколько клиентов указали один контакт, то он может быть у всех записан в неосновные. Даже если один из клиентов подтвердит этот email или телефон, он всё равно останется у остальных пользователей с возможностью его подтвердить.

### Как записывается статус подтверждения у контакта

На проектах с подтверждением у контакта может быть одно из трех состояний:

- ожидает подтверждения
- подтвержден
- без данных по подтверждению

Статус зависит от того, как контакта попал в базу.

**Точка интеграции с подтверждением email или мобильного**

- контакт заполнили → *ожидает подтверждения*;
- ожидающий подтверждения контакт отредактировали → *ожидает подтверждения*;
- контакт без подтверждения отредактировали → *ожидает подтверждения*;
- контакт без подтверждения не редактировали, но передали в импорте или вызове → *ожидает подтверждения*;
- подтвержденный контакт отредактировали → старый контакт остается основным, новый ожидает подтверждения.

Исключение:

Шаг «Создать и подписать» в операции игнорирует настройки интеграции — контакт приходит без данных по подтверждению.

**Точка интеграции без подтверждения**

- контакт заполнили → *без подтверждения*;
- любой контакт отредактировали → *без подтверждения*;
- контакт с подтверждением не редактировали, но передали в импорте или вызове → остается прежний статус.

**Добавление клиента или контакта вручную**

- контакт добавили при создании клиента → *ожидает подтверждения*;
- контакт заполнили у существующего клиента → *без подтверждения*;
- контакт без подтверждения отредактировали → *без подтверждения*;
- ожидающий подтверждения контакт отредактировали → *ожидает подтверждения*;
- подтвержденный контакт отредактировали → старый контакт остается основным, новый ожидает подтверждения.

### На какие контакты можно отправлять рассылки

На **основной** контакт, будь он подтвержденным или ожидающим подтверждения, можно отправлять рассылки как на любой другой контакт: значение имеет только [валидность](email-validity.md).

На **неосновной неподтвержденный** контакт можно отправлять только транзакционные кампании через сценарий или операцию, указав нужный тип контакта:

![email-and-mobile-confirmation-mailing.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-mailing.png)

## Как подтвердить контакт клиента

### Подтверждение Email

#### Из рассылки

В ссылку подтверждения нужно добавить [тикет](%D1%82%D0%B8%D0%BA%D0%B5%D1%82.md) `Ticket.EmailConfirmationLinkTicket`  
Клик по ней подтвердит контакт и, если на проекте включено DOI, подписку.

Пример ссылки с тикетом:

`https://mysite/?direct-crm-ticket=${Ticket.EmailConfirmationLinkTicket}`

#### Через сценарий

В [сценарии](what-is-workflow.md) нужно использовать шаг «Подтвердить email»:

![Снимок экрана 2022-06-10 в 17.28.27.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-10%20%D0%B2%2017.28.27.png)

#### Через импорт

В задаче [импорта](clients-import.md) или [редактирования](clients-import-edit.md) нужно добавить поле `IsEmailConfirmed` с любым положительным значением `(1 / true / yes)`:

![Снимок экрана 2023-02-07 в 16.52.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-02-07%20%D0%B2%2016.52.01.png)

Обязательно используйте интеграцию, в которой установлен [флаг подтверждения](email-and-mobile-confirmation.md#kak-podklyuchit-podtverzhdenie-kontakta-na-proekteе) соответствующего контакта:

![Снимок экрана 2023-10-13 в 14.14.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-13%20%D0%B2%2014.14.36.png)

### Подтверждение мобильного телефона

#### Из операции

Нужно вызвать операцию **с одним из шагов**:

- «Подтвердить мобильный телефон и подписку на SMS»
- «Подтвердить мобильный телефон на стороне клиента»

#### Через импорт

В задаче [импорта](clients-import.md) или [редактирования](clients-import-edit.md) нужно добавить поле `IsMobilePhoneConfirmed` с любым положительным значением `(1 / true / yes)`:

![Снимок экрана 2023-02-07 в 16.56.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-02-07%20%D0%B2%2016.56.19.png)

Обязательно используйте интеграцию, в которой установлен [флаг подтверждения](email-and-mobile-confirmation.md#kak-podklyuchit-podtverzhdenie-kontakta-na-proekte) соответствующего контакта.

![Снимок экрана 2023-10-13 в 14.14.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-13%20%D0%B2%2014.14.36.png)

### Если несколько клиентов подтвердили один контакт

Карточки таких клиентов объединятся. У контактов, дающих доступ к аккаунту, есть [особенности при дедубликации](%D0%BE%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%BE%D0%B2-%D1%81-%D0%BF%D0%BE%D0%BC%D0%B5%D1%82%D0%BA%D0%BE%D0%B9-%D0%B4%D0%B0%D0%B5%D1%82-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%83.md).

### После подтверждения

Подтверждение фиксируется в [истории изменений](who-is-the-client.md#istoriya-izmenenij):

![email-and-mobile-confirmation-history.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-and-mobile-confirmation-history.png)

По этому событию можно настроить сценарий для [email](workflow-events.md#pervoe-podtverzhdenie-email) и [мобильного телефона](workflow-events.md#pervoe-podtverzhdenie-mobilnogo-telefona).

[Рассылки попали в спам](https://mindbox.ru/academy/education/rassylki-popali-v-spam/): как исправить ситуацию и вернуть их во «входящие»
