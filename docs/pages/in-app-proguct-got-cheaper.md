---
title: "Как добавить In-App «Товар в вашей корзине стал дешевле»"
slug: "in-app-proguct-got-cheaper"
source_url: "https://help.mindbox.ru/docs/in-app-proguct-got-cheaper"
vcs_path: "in-app-proguct-got-cheaper.md"
toc_path:
  - Персонализация
  - Персонализация мобильных приложений
  - "Интересные механики In-App"
  - Механики для увеличения конверсии и среднего чека
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:376abc57b2d70edb23825397b3c2f26f3e8fcd9c5032cc338a5a320f87e542b5"
---

# Как добавить In-App «Товар в вашей корзине стал дешевле»

**Цель механики** — повысить конверсию в покупку среди пользователей, которые добавили товар в корзину, вышли из приложения, а позже цена на товар снизилась.

Особенно важно показать такой In-App тем, с кем нельзя связаться через другие каналы, например, если у клиента запрещены уведомления MobilePush.

## Как это работает

1. На продукт снижается цена. По этому событию запускается сценарий и добавляет клиента в сегмент для показа In-App.
2. Пользователь заходит в приложение.
3. Видит In-App о том, что цена на продукт в корзине упала.
4. По клику на In-App переходит в корзину и завершает заказ.

## Шаги настройки

Некоторые настройки на этой странице требуют обновления SDK приложения до версии 2.14.0. Для обновления SDK версии обратитесь к вашим разработчикам.

### 1. Создайте сегмент

Создайте [статический сегмент](segment-client-static.md), который будет использоваться в сценарии и таргетинге In-App.

![in-app-product-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-segment.png)

### 2. Создайте сценарий по снижению цены продукта

В стартовом блоке укажите запуск по событию [Продукт в списке продуктов изменился — Цена на продукт снизилась](workflow-events.md#cena-na-produkt-snizilas):

![Снимок экрана 2024-02-12 в 18.55.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-12%20%D0%B2%2018.55.35.png)

В блоке «Ожидание» ограничиваем выход с 08:00 до 20:00, чтобы In-App показался только в активное время клиента:

![Снимок экрана 2023-11-09 в 13.07.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-09%20%D0%B2%2013.07.19.png)

Проверяем, что продукт в наличии:

![Снимок экрана 2021-09-29 в 18.52.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-29%20%D0%B2%2018.52.11.png)

Добавляем клиента в ранее созданный статический сегмент, чтобы клиент попал в таргетинг In-App:

![in-app-product-workflow-add-to-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-workflow-add-to-segment.png)

Добавляем ожидание в один день, чтобы дать время клиенту зайти в приложение:

![in-app-product-workflow-check-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-workflow-check-segment.png)

После ожидания удаляем клиента из сегмента, чтобы In-App больше не показывался по этому понижению цены:

![in-app-product-workflow-del-segment.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-workflow-del-segment.png)

В стартовом блоке ограничиваем [количество срабатываний](workflow-limit-per-customer.md), чтобы не показывать In-App слишком часто:

![in-app-product-workflow-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-workflow-frequency.png)

Сценарий готов, можно запускать:

![in-app-product-workflow-done.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-workflow-done.png)

### 3. Создайте In-App

Создайте In-App по [инструкции](in-apps.md) с уведомлением, что цена снизилась.

#### Внешний вид формы

- Выберите и отредактируйте один из предлагаемых [шаблонов Figma](https://www.figma.com/file/QoJ0yKREcTsP3CPNUUZ8LG/%D0%93%D0%B0%D0%BB%D0%B5%D1%80%D0%B5%D1%8F-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-In-App?type=design&node-id=0%3A1&mode=design&t=COtICWsqaoJBMAJO-1) либо используйте свой дизайн.

С техническими рекомендациями к размеру и формату картинки для In-app можно ознакомиться [здесь](in-apps.md#shablon-modalnoe-okno).

- Добавьте ссылку перехода по клику на In-App. Так как In-App сообщает о сниженной цене на товар в корзине, стоит направить клиента на страницу корзины, где можно увидеть товар и новую цену на него. Рекомендуемый формат диплинка: `https://link`.

![in-app-product-form.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-form.png)

#### Общие настройки

- Выберите приложения, в которых будет отображаться форма, и даты показа.
- Укажите частоту всплывания **«Не чаще одного раза в указанный период»** раз в 7 дней, чтобы форма не показывалась еще раз по этому снижению цены.

![in-app-product-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-general.png)

#### Условия всплывания

Так как по умолчанию In-App отображается сразу после входа в приложение, укажите в настройке всплывания **«Спустя время после попадания в таргетинг»**, например, через 10 или 20 секунд. Так форма не будет всплывать в ту же секунду после входа в приложения.

![in-app-product-frequency.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-frequency.png)

#### Таргетинг

- Выберите сегмент, созданный [в первом пункте](in-app-proguct-got-cheaper.md#1-sozdajte-segment).
- При первом входе в приложение клиент получает несколько системных окон для настройки приложения и онбординга. Чтобы не перегружать пользователя уведомлениям, добавьте условие **«Количество входов в приложение больше или равно 2»**. Так In-App покажется только после второго входа в приложение.

![in-app-product-targeting.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-targeting.png)

### 4. Протестируйте In-App

Чтобы понять, правильно ли отображается In-App, добавьте сегмент с тестовым клиентом в таргетинг In-App. Подробнее в [статье](in-apps.md#kak-protestirovat-in-app).

### 5. Запустите In-App

Когда форма готова и протестирована, запустите ее:

![in-app-product-start.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/in-app-product-start.png)

## Отслеживайте данные по механике

Отслеживайте метрики по запущенному In-App с помощью [отчета по In-App](report-in-apps.md).

![reports-in-app.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/reports-in-app.png)

## Рекомендации для АБ-тестов с механикой

Чтобы увеличить конверсию в покупку, необходимо тестировать различные подходы и инструменты, которые подходят именно вашей аудитории.

Ниже несколько идей для проведения АБ-тестов, которые помогут вам в этом.

Базовые шаги по созданию и настройке АБ-теста по In-App описаны [здесь](ab-test-app.md).

1. Сравните In-App о сниженной цене против контрольной группы по метрике «Конверсия в заказ», чтобы понять, помогает ли сообщение о сниженной цене внутри приложения конвертировать пользователя в покупку.
2. Сравните разное время всплывания In-App по метрике «Конверсия в заказ», чтобы понять, когда лучше показывать уведомление о сниженной цене: через 10 секунд после входа в приложение или через 30 секунд.
3. Сравните разные триггеры всплывания In-App по метрике «Конверсия в заказ», чтобы понять, когда пользователь больше настроен на покупку. Например, через N секунд после входа в приложение или через N секунд после просмотра любой карточки товара.

Чтобы запустить In-App с триггером по просмотру товаров, необходимо настроить операцию просмотра и сделать новый релиз приложения. Подробнее [в инструкции](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3-in-app-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%83-%D0%B8%D0%BB%D0%B8-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%BE%D0%B2.md)
