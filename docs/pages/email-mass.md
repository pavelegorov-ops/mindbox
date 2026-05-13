---
title: "Как создать массовую email-рассылку"
slug: "email-mass"
source_url: "https://help.mindbox.ru/docs/email-mass"
vcs_path: "email-mass.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:2349f06d042da8cdd303564106b20224aae404c6af7ba1985e4e88dbfd5fda5b"
---

# Как создать массовую email-рассылку

Массовые рассылки — это разовые кампании, которые отправляются по заранее известному списку получателей.

## Добавление рассылки

Чтобы создать массовую email-рассылку:

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» → «Массовая рассылка»:

![mass-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-create1.png)

3. Выберите канал «Email», [папку](folders.md) и нажмите «Создать»:

![mass-email-create2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-create2.png)

## Настройки рассылки

### Имя рассылки

![mass-email-name.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-name.png)

Применение:

- название нужно для поиска рассылки среди кампаний и в фильтрах на проекте;
- при использовании [utm-метки](email-mass.md#utm-metki) с параметром `${Message.MailingUtmName}` в метки попадет транслитерированное название рассылки.

### Письмо

![mass-email-letter.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-letter.png)

- **Тема письма**. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) и эмоджи.
- **Прехедер**.

  - «Взять из письма» — почтовый сервис подтянет начало письма или прехедер из верстки и отобразит его в качестве прехедера;
  - «Задать вручную» — самостоятельно задать текст прехедера. Можно использовать параметры шаблонизатора и эмоджи;
  - «Сделать пустым» — в почтовом сервисе после темы ничего не отобразится.

Полученные письма в зависимости от настроенного прехедера:

![mass-email-preheaders.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-preheaders.png)

- **Отправитель** — имя [отправителя](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8F-%D0%B2-email-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md), которое отобразится в почтовом сервисе получателей.
- **Шаблон письма** — способ создания письма:

  - Редактор — полностью через HTML-верстку с самостоятельным вводом [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md);
  - [Новый конструктор](email-editor.md) — визуальный конструктор из блоков без необходимости использования HTML и большинства параметров;
  - [Конструктор](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B2-%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC-%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D0%B5.md) — прошлая версия визуального конструктора;
  - URL — загрузка по ссылке;
  - ZIP — загрузка ZIP-архивом.

После заполнения шаблона появляются опции:

- **Добавить [AMP-версию](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-amp-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE-%D0%B8-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B-%D0%B8%D0%B7-%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%B0.md)** — для создания интерактивных элементов (игры, карусели, опросники) без переадресации на сторонние ресурсы;
- **Ссылки в письме** — посмотреть все ссылки из шаблона и при необходимости поменять их тип (например, при использовании пользовательских ссылок [подтверждения подписки](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BF%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BD%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83.md) или [отписки](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BE%D1%82-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%B0-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8.md)).

![mass-email-links.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-links.png)

#### Тестовая отправка

После заполнения раздела «Письмо» можно посмотреть пример сформированной рассылки для пользователя.

При тестовой отправке выбранный клиент **получает письмо на почту**.

Поэтому отправлять тесты можно **только на контакты, имеющиеся на проекте**. Для создания карточки клиента воспользуйтесь [инструкцией](client-add.md).

Кликните по кнопке «Тестовая отправка», отметьте пользователей из списка или добавьте новых и нажмите «Отправить выбранным»:

![mass-email-test2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-test2.png)

Тестовые отправки никак не фиксируются в карточке клиента. Их статусы можно посмотреть списком по ссылке:

![mass-email-test3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-test3.png)

Сформированное письмо можно посмотреть **без отправки клиенту на почту** — для этого кликните по «Предпросмотру».

![mass-email-test4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-test4.png)

### Общие настройки

![mass-email-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-general.png)

- **Бренд** — актуально для [мультибрендовых](multibrand.md) проектов;
- **Тематика** — разделение на [тематики](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md) позволяет пользователям настроить гибкую подписку, чтобы получать коммуникации только по интересующим темам;
- **Теги** — с помощью [тегов действий](tag.md) можно объединять рассылки по дополнительному признаку, если не хватает разделения по каналам, тематикам и папкам. Это позволит группировать рассылки в фильтрах и отчетах;
- **Профиль** — тип рассылки и ограничения по получателям, которые должны применяться или игнорироваться в зависимости от него:
  - Стандартная — для маркетинговых кампаний. Применяются базовые проверки по получателям:
    - есть валидный email;
    - есть подписка на email (или тематику в email, если она указана в рассылке);
    - не входит в [глобальную контрольную группу](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0.md) (если включена функция) — не путать [с контрольной группой рассылки](email-mass-new.md#ab-test-i-kontrolnaya-gruppa-rassylki);
    - не превышен лимит по [коммуникациям за день](frequency-policy.md) (если включена функция).  
        
      Эти проверки можно отключить в рамках рассылки, используя соответствующие переключатели в профиле. Игнорирование подписки возможно только в [транзакционных рассылках](email-trigger.md) и допускается только для сервисных рассылок, которые клиент обязательно должен получить.
  - Opt-in — для [подтверждения подписки](doi-turn-on.md). Применяются проверки:
    - есть валидный email;
    - подписка на email (или тематику в email, если она указана в рассылке) в статусе «Ожидает подтверждения»;
    - не превышен лимит по коммуникациям за день (если включена функция).  
        
      Можно отключить проверку по частоте коммуникаций.

### Получатели

Способ отбора получателей:

- по [сегменту](segments-clients.md)
- по фильтру
- [по файлу](how-to-use-manual-import-in-campaigns.md).

![mass-email-users.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-users.png)

### UTM-метки

![mass-email-utm.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-utm.png)

Метки позволяют определить [источник перехода](%D0%BA%D0%B0%D0%BA-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0-%D1%81%D0%B0%D0%B8%D1%82.md) на сайт и тем самым атрибутировать трафик к конкретной кампании и каналу.

Можно создать стандартные метки и переиспользовать их в email-рассылках или ввести пользовательские метки для конкретной рассылки.

## После заполнения настроек

### Готовность к отправке

В разделе автоматически проверяется наличие всех обязательных полей. Кликом по пункту можно перейти к нужному разделу.

Если всё заполнено, рассылка переходит из статуса «Черновик» в «Готова к отправке»:

![mass-email-ready.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-ready.png)

### Выбрать время отправки

![mass-email-send.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-send.png)

**Часы и скорость отправки:**

![mass-email-time.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-time.png)

- **Часы отправки** — можно ограничить по [часовому поясу клиента](client-timezone.md) или [проекта](project-settings.md);
- **Скорость отправки сообщений в час** — можно ограничить поток. Например, чтобы регулировать нагрузку на сайт или колл-центр. Допустимы значения от 500 до 2 000 000. При ограничении скорости дается приблизительная оценка длительности отправки.
- **Повторять попытки отправки** (актуальность рассылки) — время, в течение которого имеет смысл отправлять рассылку. Считается от времени запуска.  
  Например, рассылку запустили в 10:00 с актуальностью 3 часа. → После 13:00 письма не отправляются.

**Время запуска:**

![](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-send-now.png) ![](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-send-later.png)

- **Отправить сейчас** — рассылка сразу запустится и перейдет в статус «Отправляется»;
- **Запланировать** — задается время в будущем, когда отправка запустится **автоматически**. До этого она будет находиться в статусе «Отправится в будущем». Во время ожидания рассылку можно будет редактировать, в том числе менять время запуска.

## АБ-тест и контрольная группа рассылки

**[АБ-тесты](what-is-ab-test.md)** позволяют сравнивать разные варианты рассылок по влиянию на открытия, клики, выручку.

![mass-email-ab-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-ab-test.png)

![mass-email-variant2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-variant2.png)

**Контрольная группа (КГ)** определяет эффективность кампании, сравнивая поведение пользователей, получивших письмо, и клиентов без рассылки.

![mass-email-control.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-control.png)

Можно одновременно запустить АБ-тест и использовать контрольную группу.

В email доступны показатели:

- **Конверсия в открытие** — процент клиентов, открывших рассылку за время тестирования (только без сравнения с контрольной группой);
- **Конверсия в клик** — процент клиентов, сделавших хотя бы один клик в рассылке за время тестирования (только при включенном отслеживании кликов и без сравнения с контрольной группой);
- **Конверсия в заказ** — процент клиентов, совершивших хотя бы один заказ за время тестирования. Возвраты и отмены не включаются;
- **Средний чек** — выручка, деленная на количество заказов за время тестирования. Возвраты и отмены не включаются;
- **Средняя выручка на клиента (ARPU)** — выручка за время тестирования, деленная на количество участников в варианте. Возвраты и отмены не включаются.

![mass-email-ab-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-ab-settings.png)

При добавлении теста и КГ параллельно создается АБ-тест в соответствующем разделе. В нем можно будет посмотреть отчет по проведенному тесту:

![mass-email-ab-page.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-ab-page.png)

Подробнее об АБ-тестах в массовых рассылках — [в инструкции](ab-tests-mailings.md).

Общие рекомендации по запуску АБ-тестов — [в статье](what-is-ab-test.md#rekomendacii-po-zapusku-ab-testov).

## После завершения рассылки

### Фильтры

Для каждой рассылки создаются [статусы](customer-message-statuses.md), которые выдаются клиентам, чтобы обозначить взаимодействия с рассылкой:

![mass-email-client-page.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-client-page.png)

С их помощью можно фильтрами отобрать:

- [клиентов, которые взаимодействовали с рассылкой](filter-clients-mailing.md):

![mass-email-filter-clients.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-filter-clients.png)

- [статусы по рассылке](filter-clients-mailing.md#poisk-izmenenij-statusov-rassylki):

![mass-email-filter-statuses.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-filter-statuses.png)

### Отчеты

- После завершения рассылки доступен [отчет по ее показателям](%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md):

![mass-email-report.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-report.png)

- Можно посмотреть [карту кликов](click-maps.md):

![click-maps.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/click-maps.png)

- Также рассылка попадает в общий [отчет по рассылкам](mailings-dashboard.md):

![mass-email-dashboard.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-dashboard.png)

- [Лучшее время для отправки email- и SMS-рассылок](https://mindbox.ru/academy/education/luchshee-vremya-dlya-rassylok/). Данные об эффективности рассылок 60 клиентов Mindbox
- Как написать [письмо для продающей рассылки](https://mindbox.ru/journal/education/prodayushee-pismo-dlya-rassylki/), которое клиент захочет открыть
