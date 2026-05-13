---
title: Решение частых проблем
slug: "faq-passkey"
source_url: "https://help.mindbox.ru/docs/faq-passkey"
vcs_path: "faq-passkey.md"
toc_path:
  - Администрирование
  - Безопасность
  - Ключи доступа к Mindbox
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:489ec9a2843e062a8a7269fccb3834e17d5f8cbdd44cbda0a3622baea5cd67a8"
---

# Решение частых проблем

В этой статье описаны проблемы, которые могут возникать в процессе настройки ключа доступа или при попытке входа с его помощью.

Если решение проблемы не помогло, напишите [в чат технической поддержки](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support) в нижнем правом углу этой страницы или на почту [support@mindbox.ru](mailto:support@mindbox.ru).

## Общие ошибки

[**После ввода почты появляется ошибка «В аккаунте не настроен ключ доступа»**](faq-passkey.md#no_access)

![faq-passkey-no_access-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-no_access-error.png)

*Вид ошибки в интерфейсе*

Рассмотрим, в каких ситуациях может возникать ошибка и как при этом отображается статус ключей в карточке персонала.

Для проверки статуса обратитесь к сотруднику с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала» или к сотрудникам [технической поддержки](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support).

**В учетной записи были сброшены все ключи доступа.**

Обратитесь к владельцу проекта или другому сотруднику с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала» с просьбой отправить [новую ссылку для настройки ключа](passkey.md#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).

![faq-passkey-no-access1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-no-access1.png)

**Было отправлено письмо с ссылкой на установку ключа, но время работы ссылки истекло.**

Обратитесь к владельцу проекта или другому сотруднику с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала» с просьбой отправить [новую ссылку для настройки ключа](passkey.md#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).

![faq-passkey-no-access2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-no-access2.png)

**Было отправлено письмо с ссылкой на установку ключа, и ссылка еще активна.**

Найдите письмо от Mindbox с темой «Ваша ссылка на установку ключа доступа в Mindbox» в той почте, которая прикреплена к вашему аккаунту, и перейдите по ссылке для настройки.

![faq-passkey-no-access3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-no-access3.png)

---

[**Ошибка «Сервис недоступен. Попробуйте снова и если ошибка повторится — свяжитесь с поддержкой»**](faq-passkey.md#service_unavailable)

![faq-passkey-service-unavailable-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-service-unavailable-error.png)

*Вид ошибки в интерфейсе*

**Варианты возникновения ошибки:**

[Ошибка возникает сразу после перехода по ссылке на настройку ключа доступа до нажатия на кнопку «Настроить»](faq-passkey.md#service_unavailable_link)

Вы уже авторизованы на проекте в другой вкладке браузера.

- Выйдете из профиля Mindbox во всех вкладках браузера:

![faq-passkey-service-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-service-error.png)

- [Очистите кэш в браузере](https://help.mindbox.ru/docs/how-to-clear-cache).
- Перейдите по ссылке из письма еще раз.

---

[Ошибка появляется после нажатия кнопки «Настроить» и выбора варианта хранения ключа](faq-passkey.md#service_unavailable_setting)

Такая ошибка может возникать, если для сохранения ключа доступа выбран ненадежный менеджер паролей.

Выберите другой [менеджер паролей](passkey.md#v-menedzhere-parolej) или вариант сохранения ключа (например, [Windows Hello](passkey.md#v-windows-hello)).

---

[Ошибка появляется после использования специальной ссылки для настройки ключа](faq-passkey.md#service_unavailable_special_link)

Способ настройки ключа по специальной ссылке `https://<имя проекта>.mindbox.ru/login/passkeys/register` доступен только после **авторизации на проекте**.

Авторизуйтесь на проекте и попробуйте использовать ссылку еще раз.

---

[**При переходе по ссылке из письма появляется ошибка «Этой ссылкой на установку ключа уже воспользовались»**](faq-passkey.md#link_already_used)

![faq-passkey-used-link.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-used-link.png)

*Вид ошибки в интерфейсе*

С помощью ссылки на установку ключа можно настроить **только один ключ**.

- Если вы **не использовали ссылку** для настройки ключа, обратитесь к владельцу проекта для [сброса ключей](https://help.mindbox.ru/docs/passkey#kak-udalit-klyuchi-dostupa) в вашей учетной записи в целях безопасности данных проекта.
- Если вам необходимо настроить дополнительный ключ, обратитесь к владельцу проекта для отправки [ссылки для настройки нового ключа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).

Ссылка для настройки ключа **не ведет на страницу авторизации**. Если вы уже настроили ключ и вам необходимо зайти на проект, перейдите на основную страницу `https://<системное имя проекта>.mindbox.ru/login?`.

---

[**Компьютер на Windows просит вставить ключ безопасности в USB-порт и не предлагает другие варианты**](faq-passkey.md#usb)

![faq-passkey-usb.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-usb.png)

*Примеры отображения ошибки на разных устройствах*

**Варианты возникновения ошибки:**

[Окно всплывает после клика по кнопке «Настроить»](faq-passkey.md#usb_setting)

Нажмите на кнопку «Отмена» или «Назад». Если после этого система не предлагает варианты для настройки, значит, что на текущем устройстве не настроены или не поддерживаются другие способы сохранения ключа доступа, кроме физического аппаратного ключа (ключ безопасности).

Чтобы проверить, поддерживаются ли другие способы, попробуйте варианты настроек ниже.

**Для версий Windows 10 и выше:**

- **Google менеджер паролей.** Если вы используете браузер Chrome, то для сохранения ключа можно использовать встроенный менеджер паролей Google. Для этого потребуется авторизация в аккаунте Google. [Подробнее](passkey.md#v-menedzhere-parolej-google).
- **Сохранение ключа на телефоне.** Проверьте, поддерживает ли устройство, на котором появилась ошибка, Bluetooth. При наличии поддержки Bluetooth можно воспользоваться вариантом сохранения ключа на вашем телефоне. [Подробнее](passkey.md#na-telefone-apple-ili-android).
- **Windows Hello.** На устройствах Windows с операционной системной 10+ можно настроить ПИН-код [по инструкции](https://help.mindbox.ru/docs/passkey#winhello), который можно использовать для сохранения ключа. [Подробнее](passkey.md#v-windows-hello).
- **Менеджеры паролей.** После установки и настройки менеджера паролей (например, Касперский, Bitwarden) ключ можно сохранить в любом браузере на базе Chromium (Яндекс, Google Chrome, Opera и др.).[Подробнее](passkey.md#v-menedzhere-parolej).

**Для версий Windows 8 и ниже:**

Настройте менеджер паролей [по инструкции](passkey.md#bitwarden). Если данным способ не удалось сохранить ключ, обратитесь [в техническую поддержку.](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support)

---

[Окно всплывает после ввода почты или логина в окне авторизации](faq-passkey.md#usb_login)

- Проверьте, не пользуется ли одним аккаунтом **несколько сотрудников одновременно.** Общий аккаунт необходимо разделить: создать для каждого сотрудника отдельную учетную запись, после чего настроить ключ доступа для каждой учетной записи.
- Если аккаунтом пользуется только один сотрудник, значит до этого уже был настроен ключ доступа **на другом устройстве.**
- Если вы **владелец проекта**, войдите на проект с помощью уже настроенного ключа на том устройстве, на котором был настроен этот ключ. Перейдите в редактирование своего профиля и отправьте себе новую ссылку на установку ключа [по инструкции](passkey.md#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).
- В ином случае обратитесь к владельцу проекта или к другому сотруднику с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала» для [установки нового ключа доступа](passkey.md#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa). Новый ключ необходимо настроить на текущем устройстве с ошибкой.

Перед настройкой ключа на новом устройстве рекомендуется проверить доступные варианты на тестовом сервисе [**WebAuthn.io**](https://webauthn.io/) Если на тестовом сервисе также возникает ошибка с USB-портом, попробуйте настроить один из вариантов из п.1 решения.

[Как использовать сервис **WebAuthn.io**](faq-passkey.md#usb_login_webauthn)

1. Перейдите по ссылке <https://webauthn.io/>.
2. На сайте введите любой тестовый логин и нажмите «Register»:

   ![faq-passkey-webauth-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-test.png)
3. Сайт предложит все доступные на устройстве варианты для настройки ключа доступа:

   ![faq-passkey-webauth-options.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-options.png)
4. После успешной настройки ключа попробуйте авторизоваться с его помощью:

   ![faq-passkey-webauth-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-auth.png)

Если вы видите экран «You’re logged in!», авторизация прошла успешно.

![faq-passkey-webauth-win.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-win.png)

---

[Окно всплывает при попытке входа через удаленный рабочий стол](faq-passkey.md#usb_remote_desktop)

Удаленный рабочий стол - это другое удаленное устройство, которое может обладать другими техническими характеристиками и настройками. Ключи, настроенные до подключения к удаленному рабочему столу, могут не работать после подключения к нему.

1. Уточните у системных администраторов, возможно ли на удаленном рабочем столе:
   - Авторизоваться в аккаунт Google
   - Настроить менеджер паролей (Bitwarden/Касперский)
   - Настроить Windows Hello
2. Если один из методов поддерживается, запросите [ссылку](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa) для настройки нового ключа и настройте ключ одним из доступных методов.
3. Если ни один из методов не поддерживается и нет возможности работать вне удаленного рабочего стола, обратитесь [в техническую поддержку](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support).

---

[**Ошибка «Время ожидания ввода ключа доступа истекло» или «Ошибка при вводе ключа доступа»**](faq-passkey.md#timeout_error)

Ошибки чаще всего возникают во время сканирования QR-кода с помощью телефона.

![faq-passkey-timeout-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-timeout-error.png)

*Вид ошибки в интерфейсе*

**Особенности сканирования QR-кода**

- На iPhone необходимо использовать обычную камеру телефона.
- На Android используйте приложение-аутентификатор (например, Google Authenticator или Microsoft Authenticator).

Если для сканирования был использован корректный способ:

1. Проверьте, что Bluetooth включен и на компьютере, и на телефоне.
2. Используйте другое интернет подключение (например, мобильный интернет).
3. Перезагрузите устройство.

**Если шаги выше не помогли**

- Протестируйте, работает ли сохранение через QR-код на тестовом сервисе [WebAuthn.io](https://webauthn.io/)

[Как использовать сервис **WebAuthn.io**](faq-passkey.md#timeout_error_webauthn)

1. Перейдите по ссылке <https://webauthn.io/>.
2. На сайте введите любой тестовый логин и нажмите «Register»:  
   ![faq-passkey-webauth-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-test.png)
3. Сайт предложит все доступные на устройстве варианты для настройки ключа доступа:  
   ![faq-passkey-webauth-options.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-options.png)
4. После успешной настройки ключа попробуйте авторизоваться с его помощью:  
   ![faq-passkey-webauth-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-auth.png)

Если вы видите экран «You’re logged in!», авторизация прошла успешно.

![faq-passkey-webauth-win.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-win.png)

- Обратитесь в [техническую поддержку](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support) с результатами теста.

## Google менеджер паролей

[**При настройке ключа в Google Chrome нет варианта «Google менеджер паролей»**](faq-passkey.md#google_setup)

При корректной настройке менеджера паролей Google окно с выбором варианта сохранения будет выглядеть так:

![faq-passkey-used-link.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager.png)

**Для использования менеджера паролей Google:**

1. Выполните вход в аккаунт Google в браузере.
2. Перейдите в настройки браузера «Пароли и автозаполнение» → «Google Менеджер паролей»:

   ![faq-paskey-google-manager-path.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-paskey-google-manager-path.png)
3. Перейдите в раздел «Настройки» и включите настройки:

   - Предлагать сохранение паролей и ключей доступа
   - Автоматически создавать ключи доступа для быстрого входа в аккаунт
   - Использовать пароли и ключи доступа, сохраненные в аккаунте Google, и добавлять в него новые

   ![faq-passkey-google-manager-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-settings.png)
4. С помощью тестового сервиса [**WebAuthn.io**](https://webauthn.io/) проверьте, работает ли настройка ключа с помощью Google Менеджера паролей. Если регистрация и аутентификация проходят успешно, вернитесь в Mindbox и попробуйте настроить ключ еще раз.

[Как использовать сервис **WebAuthn.io**](faq-passkey.md#google_setup_webauthn)

1. Перейдите по ссылке <https://webauthn.io/>.
2. На сайте введите любой тестовый логин и нажмите «Register»:  
   ![faq-passkey-webauth-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-test.png)
3. Сайт предложит все доступные на устройстве варианты для настройки ключа доступа:  
   ![faq-passkey-webauth-options.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-options.png)
4. После успешной настройки ключа попробуйте авторизоваться с его помощью:  
   ![faq-passkey-webauth-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-auth.png)

Если вы видите экран «You’re logged in!», авторизация прошла успешно.

![faq-passkey-webauth-win.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-win.png)

---

[**При авторизации не предлагается ранее настроенный в менеджере паролей Google ключ**](faq-passkey.md#google_no_option)

1. Проверьте, что в браузере выполнен вход в аккаунт Google, в котором был настроен ключ, и в аккаунте включена [синхронизация](https://support.google.com/chrome/answer/165139?sjid=17236812494774544104-EU#:~:text=%D0%9A%D0%B0%D0%BA%20%D1%83%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C%2C%20%D0%BA%D0%B0%D0%BA%D0%B0%D1%8F%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D1%8F%D1%82%D1%8C%D1%81%D1%8F%20%D0%B2%20%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B5%20Google).
2. Перейдите в настройки браузера «Пароли и автозаполнение» → «Google Менеджер паролей»:

   ![faq-paskey-google-manager-path.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-paskey-google-manager-path.png)
3. Перейдите в раздел «Настройки» и включите настройки:

   - Предлагать сохранение паролей и ключей доступа
   - Автоматически создавать ключи доступа для быстрого входа в аккаунт
   - Использовать пароли и ключи доступа, сохраненные в аккаунте Google, и добавлять в него новые

   ![faq-passkey-google-manager-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-settings.png)
4. Проверьте сохранен ли в этом аккаунте Google ключ доступа:

   - **Ключ доступа есть.** Перейдите к следующим шагам решения.
   - **Ключа доступа нет.** Запросите [ссылку для настройки нового ключа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa) доступа у владельца вашего проекта или другого сотрудника с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала».[**Как найти ключ в Google менеджере паролей**](faq-passkey.md#google_no_option_key)

   1. Перейдите в настройки браузера «Пароли и автозаполнение» → «Google Менеджер паролей»:  
      ![faq-paskey-google-manager-path.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-paskey-google-manager-path.png)
   2. Во вкладке «Пароли» с помощью поиска найдите ключи доступа Mindbox:  
      ![faq-passkey-google-manager-search.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-search.png)
   3. Запись ключа будет выглядеть так:

      ![faq-passkey-google-key-card.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-key-card.png)

[**5. При работе через удаленный рабочий стол**:](faq-passkey.md#google_no_option_remote)

Удаленный рабочий стол - это другое удаленное устройство, которое может обладать другими техническими характеристиками и настройками. Ключи, настроенные до подключения к удаленному рабочему столу, могут не работать после подключения к нему.

- Проверьте, авторизованы ли вы в аккаунте Google в браузере на удаленном рабочем столе.
- Если нет, попробуйте авторизоваться в аккаунте Google, если есть такая возможность.
- Если политикой безопасности запрещено использовать аккаунт Google, уточните, поддерживается ли один из других методов настройки ключа доступа:
  - Настроить [менеджер паролей](https://help.mindbox.ru/docs/passkey#v-menedzhere-parolej) (Bitwarden/Касперский);
  - Настроить [Windows Hello](https://help.mindbox.ru/docs/passkey#v-windows-hello).

Для настройки ключа другим методом запросите [ссылку для настройки ключа доступа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).

- Если ни один из методов не поддерживается и нет возможности работать вне удаленного рабочего стола, обратитесь [в техническую поддержку](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-mindbox-support).

6. Обновите браузер до последней версии.
7. С помощью тестового сервиса [**WebAuthn.io**](https://webauthn.io/) проверьте, работает ли настройка ключа с помощью Google Менеджера паролей.

   - **Ключ сохранился** → повторите попытку входа в Mindbox
   - **Ключ не сохранился** → протестируйте другие варианты настройки ключа доступа на сайте [**WebAuthn.io**](http://WebAuthn.io). Если регистрация и аутентификация с другим методом проходят успешно, запросите [ссылку на настройку нового ключа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).[Как использовать сервис **WebAuthn.io**](faq-passkey.md#google_no_webauthn)

   1. Перейдите по ссылке <https://webauthn.io/>.
   2. На сайте введите любой тестовый логин и нажмите «Register»:

      ![faq-passkey-webauth-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-test.png)
   3. Сайт предложит все доступные на устройстве варианты для настройки ключа доступа:

      ![faq-passkey-webauth-options.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-options.png)
   4. После успешной настройки ключа попробуйте авторизоваться с его помощью:

      ![faq-passkey-webauth-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-auth.png)

   Если вы видите экран «You’re logged in!», авторизация прошла успешно.

   ![faq-passkey-webauth-win.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-win.png)

---

[**Нет связи с Google менеджером паролей**](faq-passkey.md#google_no_connection)

![faq-passkey-google-manager-no-connection.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-no-connection.png)

1. Проверьте, что в браузере выполнен вход в аккаунт Google и в аккаунте включена [синхронизация](https://support.google.com/chrome/answer/165139?sjid=17236812494774544104-EU#:~:text=%D0%9A%D0%B0%D0%BA%20%D1%83%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C%2C%20%D0%BA%D0%B0%D0%BA%D0%B0%D1%8F%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D1%8F%D1%82%D1%8C%D1%81%D1%8F%20%D0%B2%20%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B5%20Google).
2. Используйте другое интернет подключение (например, мобильный интернет).
3. Если при работе вы используете VPN, проверьте работает ли вход при его включении или выключении.
4. Перейдите в настройки браузера «Пароли и автозаполнение» → «Google Менеджер паролей»:

   ![faq-paskey-google-manager-path.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-paskey-google-manager-path.png)
5. Перейдите в раздел «Настройки» и включите настройки:

   - Предлагать сохранение паролей и ключей доступа
   - Автоматически создавать ключи доступа для быстрого входа в аккаунт
   - Использовать пароли и ключи доступа, сохраненные в аккаунте Google, и добавлять в него новые

   ![faq-passkey-google-manager-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-settings.png)
6. Временно отключите расширения и блокировщики рекламы (uBlock/AdGuard) в браузере.
7. Очистите кеш и cookie браузера [по инструкции](https://help.mindbox.ru/docs/how-to-clear-cache#google-chrome).
8. Обновите Chrome до последней версии
9. Перезагрузите устройство.
10. **Если ключ доступа уже был настроен в Google менеджере паролей и это не первая попытка входа**, проверьте сохранен ли в этом аккаунте ключ доступа:

    - **Ключ доступа есть.** Перейдите к следующему шагу.
    - **Ключа доступа нет.** Запросите [ссылку для настройки нового ключа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa) доступа у владельца вашего проекта или другого сотрудника с правами «Редактирование персонала» и «Просмотр и экспорт списка персонала».[**Как найти ключ в Google менеджере паролей**](faq-passkey.md#google_no_connection_key)

    1. Перейдите в настройки браузера «Пароли и автозаполнение» → «Google Менеджер паролей»:

       ![faq-paskey-google-manager-path.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-paskey-google-manager-path.png)
    2. Во вкладке «Пароли» с помощью поиска найдите ключи доступа Mindbox:

       ![faq-passkey-google-manager-search.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-manager-search.png)
    3. Запись ключа будет выглядеть так:

       ![faq-passkey-google-key-card.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-key-card.png)
11. С помощью тестового сервиса [**WebAuthn.io**](https://webauthn.io/) проверьте, работает ли настройка ключа с помощью Google Менеджера паролей.

    - **Ключ сохранился** → повторите попытку входа в Mindbox
    - **Ключ не сохранился** → протестируйте другие варианты настройки ключа доступа на сайте [**WebAuthn.io**](http://WebAuthn.io). Если регистрация и аутентификация с другим методом проходят успешно, [запросите ссылку на настройку нового ключа](https://help.mindbox.ru/docs/passkey#kak-otpravit-ssylku-dlya-ustanovki-klyucha-dostupa).[Как использовать сервис **WebAuthn.io**](faq-passkey.md#google_no_connection_webauthn)

    1. Перейдите по ссылке <https://webauthn.io/>.
    2. На сайте введите любой тестовый логин и нажмите «Register»:

       ![faq-passkey-webauth-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-test.png)
    3. Сайт предложит все доступные на устройстве варианты для настройки ключа доступа:

       ![faq-passkey-webauth-options.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-options.png)
    4. После успешной настройки ключа попробуйте авторизоваться с его помощью:

       ![faq-passkey-webauth-auth.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-auth.png)

    Если вы видите экран «You’re logged in!», авторизация прошла успешно.

    ![faq-passkey-webauth-win.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-webauth-win.png)

---

[**Google менеджером паролей запрашивает ПИН-код, откуда его взять?**](faq-passkey.md#google_pin)

После выбора Google менеджера паролей в качестве варианта сохранения ключа, Google может запросить:

1. **ПИН-код из Windows Hello**

   ![faq-passkey-winhello-pin.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-winhello-pin.png)

   Если в настройках менеджера включена настройка «Использовать Windows Hello при заполнении паролей», то при сохранении и использовании ключа Google может попросить ввести ПИН-код, сохраненный в Windows Hello.

   ![faq-passkey-winhello-pin-set.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-winhello-pin-set.png)

---

1. **PIN-код Google Менеджер паролей**

   ![faq-passkey-google-pin](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-pin.png)

   PIN-код настраивается в настройках Google Менеджер паролей. Если вы не помните PIN-код, его можно изменить по [инструкции Google](https://support.google.com/chrome/answer/16608973?sjid=11474160412400149534-EU#zippy=%2C%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-pin-%D0%BA%D0%BE%D0%B4%2C%D0%BA%D0%B0%D0%BA-%D1%83%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D0%BA%D0%BB%D1%8E%D1%87%D0%B8-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%2C%D0%BA%D0%B0%D0%BA-%D1%81%D0%B1%D1%80%D0%BE%D1%81%D0%B8%D1%82%D1%8C-pin-%D0%BA%D0%BE%D0%B4-%D0%B5%D1%81%D0%BB%D0%B8-%D0%B2%D1%8B-%D0%B5%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B1%D1%8B%D0%BB%D0%B8).

   ![faq-passkey-google-pin-set.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/faq-passkey-google-pin-set.png)

   Если такой настройки в Google Менеджер паролей нет, вы можете сбросить PIN-код через сброс **всех ключей доступа** в вашем аккаунте Google по [инструкции Google](https://support.google.com/chrome/answer/16608973?co=GENIE.Platform%3DDesktop&oco=2#zippy=%2C%D0%BA%D0%B0%D0%BA-%D1%83%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D0%BA%D0%BB%D1%8E%D1%87%D0%B8-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0). После этого попробуйте создать новый ключ доступа по инструкции. Менеджер паролей попросит создать новый PIN-код перед сохранением ключа доступа.
