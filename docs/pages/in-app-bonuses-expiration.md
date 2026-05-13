---
title: "Как добавить In-App «Ваши бонусы скоро сгорят»"
slug: "in-app-bonuses-expiration"
source_url: "https://help.mindbox.ru/docs/in-app-bonuses-expiration"
vcs_path: "in-app-bonuses-expiration.md"
toc_path:
  - Персонализация
  - Персонализация мобильных приложений
  - "Интересные механики In-App"
  - Механики для увеличения конверсии и среднего чека
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:01dd8154a3167fb797a8b29c5c03e018e3e8699efa18b83d29db1dd9d851ab66"
---

# Как добавить In-App «Ваши бонусы скоро сгорят»

**Цель механики** — повысить конверсию в первую или повторную покупку среди пользователей, которые получили бонусы, но не потратили их.

Особенно важно показать такой In-App тем, с кем нельзя связаться через другие каналы, например, если у клиента запрещены уведомления MobilePush.

## Как это работает

1. Клиент получает бонусы за регистрацию, установку приложения или другие акции. В [статье](in-app-complete-your-profile.md) рассказываем, как начислить клиенту бонусы за заполнение профиля в приложении.
2. Пользователь заходит в приложение.
3. Видит In-App о том, что его баллы скоро сгорят.
4. По клику на In-App переходит на страницу с товарами для выбора товаров или в корзину для завершения заказа.

## Шаги настройки

Некоторые настройки на этой странице требуют обновления SDK приложения до версии 2.14.0. Для обновления SDK версии обратитесь к вашим разработчикам.

### 1. Создайте сегменты

Создайте [статический сегмент](segment-client-static.md), который будет использоваться в сценарии для добавления в него клиентов и в сегменте для таргетинга In-App.

![in-app-bonuses-expiration-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-segment.png)

Создайте [пересчитываемый сегмент](segment-client-filter-recalculate.md) для таргетинга, который будет проверять, что клиент все еще в статическом сегменте и у него есть баллы, которые скоро сгорят.

![in-app-bonuses-expiration-segment2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-segment2.png)

### 2. Создайте сценарий

Создаем сценарий с запуском по событию [Изменение заданного баланса](workflow-events.md#izmeneniya-zadannogo-balansa) и указываем частоту запуска раз в 7 суток:

![in-app-bonuses-workflow-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-workflow-start.png)

Ожидание — [за 7 суток](workflow-delay.md#dinamicheskoe) до сгорания баллов:

![Снимок экрана 2022-05-27 в 19.18.08](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-05-27%20%D0%B2%2019.18.08.png)

Проверяем, что баллы доступны и не потрачены:

![Снимок экрана 2022-05-27 в 19.19.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-05-27%20%D0%B2%2019.19.09.png)

Добавляем клиента в ранее созданный статический сегмент, чтобы клиент попал в таргетинг In-App:

![in-app-bonuses-expiration-add-to-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-add-to-segment.png)

Добавляем ожидание до сгорания бонусов в 7 дней :

![in-app-bonuses-expiration-wait.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-wait.png)

Удаляем клиента из сегмента, чтобы In-App больше не показывался после сгорания баллов:

![in-app-bonuses-expiration-del-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-del-segment.png)

[Протестируйте](workflow-test-mode.md) и запустите сценарий:

![in-app-bonuses-expiration-workflow-done.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-workflow-done.png)

### 3. Создайте In-App

Создайте In-App по [инструкции](in-apps.md) с уведомлением, что бонусы скоро сгорят.

#### Внешний вид формы

- Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

С техническими рекомендациями к размеру и формату картинки для In-app можно ознакомиться [здесь](in-apps.md#shablon-modalnoe-okno).

- Добавьте ссылку перехода по клику на In-App. Так как In-App сообщает о сгорании баллов, стоит направить клиента на страницу с его балансом либо на страницу товарами. Рекомендуемый формат диплинка: `https://link`.

![in-app-bonuses-expiration-form.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-form.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Укажите частоту всплывания **«Не чаще одного раза в указанный период»** и выставите значение **«Один раз в 1 день»** (или реже), чтобы напоминать пользователю о баллах только один раз и не беспокоить повтором формы.

![in-app-bonuses-expiration-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-general.png)

#### Условия всплывания

Так как по умолчанию In-App отображается сразу после входа в приложение, укажите в настройке всплывания **«Спустя время после попадания пользователя в таргетинг»**, например, через 10 или 20 секунд. Так форма не будет всплывать в ту же секунду после входа в приложения.

![in-app-bonuses-expiration-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-frequency.png)

#### Таргетинг

- Выберите **пересчитываемый сегмент**, созданный [в первом пункте](in-app-bonuses-expiration.md#1-sozdajte-segment).
- При первом входе в приложение клиент получает несколько системных окон для настройки приложения и онбординга. Чтобы не перегружать пользователя уведомлениям, добавьте условие **«Количество входов в приложение больше или равно 2»**. Так In-App покажется только после второго входа в приложение.

![in-app-bonuses-expiration-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-targeting.png)

### 4. Протестируйте In-App

Чтобы понять, правильно ли отображается In-App, добавьте сегмент с тестовым клиентом в таргетинг In-App. Подробнее в [статье](in-apps.md#kak-protestirovat-in-app).

### 5. Запустите In-App

Когда форма готова и протестирована, запустите ее:

![in-app-bonuses-expiration-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-bonuses-expiration-start.png)

## Отслеживайте данные по механике

Отслеживайте метрики по запущенному In-App с помощью [отчета по In-App](report-in-apps.md).

![reports-in-app.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/reports-in-app.png)

## Рекомендации для АБ-тестов с механикой

Чтобы увеличить конверсию в покупку, необходимо тестировать различные подходы и инструменты, которые подходят именно вашей аудитории.

Ниже несколько идей для проведения АБ-тестов, которые помогут вам в этом.

Базовые шаги по созданию и настройке АБ-теста по In-App описаны [здесь](ab-test-app.md).

1. Сравните In-App о сгорании бонусов против контрольной группы по метрике «Конверсия в заказ», чтобы понять, помогает ли сообщение про бонусы внутри приложения конвертировать пользователя в покупку
2. Сравните разное время всплывания In-App по метрике «Конверсия в заказ», чтобы понять, когда лучше показывать уведомление о сгорании бонусов: через 10 секунд после входа в приложение, через 30 секунд или через 60.
3. Сравните разные триггеры всплывания In-App по метрике «Конверсия в заказ», чтобы понять, когда пользователь больше настроен на покупку. Например, через N секунд после входа в приложение или через N секунд после просмотра любой карточки товара.

Чтобы запустить In-App с триггером по просмотру товаров, необходимо настроить операцию просмотра и сделать новый релиз приложения. Подробнее [в инструкции](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3-in-app-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%83-%D0%B8%D0%BB%D0%B8-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%BE%D0%B2.md)
