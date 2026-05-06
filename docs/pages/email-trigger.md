---
title: "Как создать автоматическую email-рассылку"
slug: "email-trigger"
source_url: "https://help.mindbox.ru/docs/email-trigger"
vcs_path: "email-trigger.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:0f4e98c1ac5e3628c49442272b56915f954681367136bc6af13937066487c561"
---

# Как создать автоматическую email-рассылку

Автоматические рассылки — это кампании, которые отправляется клиенту из сценария или операции с наступлением определенного события.

В механиках можно использовать только автоматические рассылки в статусе «Готова к использованию», которые находятся в той же папке, что и создаваемая кампания, или в её дочерней папке.

## Добавление рассылки

Чтобы создать автоматическую email-рассылку:

1. Перейдите в раздел **Кампании**:

![список.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%281%29.png)

2. Нажмите «Создать кампанию» → «Автоматизация» → «Автоматическая рассылка»:

![trigger-email-create1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create1.png)

3. Выберите канал «Email», [папку](folders.md) и нажмите «Создать»:

![trigger-email-create2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-create2.png)

## Настройки рассылки

### Имя рассылки

![trigger-email-name.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-name.png)

Применение:

- название нужно для поиска рассылки среди кампаний и в фильтрах на проекте;
- при использовании [utm-метки](email-mass.md#utm-metki) с параметром `${Message.MailingUtmName}` в метки попадет транслитерированное название рассылки.

### Письмо

![trigger-email-letter.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-letter.png)

- **Тема письма**. Можно использовать [параметры шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md) и эмоджи.
- **Прехедер**.

  - «Взять из письма» — почтовый сервис подтянет начало письма или прехедер из верстки и отобразит его в качестве прехедера;
  - «Задать вручную» — самостоятельно задать текст прехедера. Можно использовать параметры шаблонизатора и эмоджи;
  - «Сделать пустым» — в почтовом сервисе после темы ничего не отобразится.

Полученные письма в зависимости от настроенного прехедера:

![trigger-email-preheaders.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-preheaders.png)

- **Отправитель** — имя [отправителя](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8F-%D0%B2-email-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md), которое отобразится в почтовом сервисе получателей.
- **Шаблон письма** — способ создания письма:

  - Редактор — полностью через HTML-верстку с самостоятельным вводом [параметров шаблонизатора](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80.md);
  - [Новый конструктор](email-editor.md) — визуальный конструктор из блоков без необходимости использования HTML и большинства параметров;
  - [Конструктор](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B2-%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC-%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D0%B5.md) — прошлая версия визуального конструктора;
  - URL — загрузка по ссылке;
  - ZIP — загрузка ZIP-архивом.

После заполнения шаблона появляются опции:

- **Добавить [AMP-версию](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-amp-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE-%D0%B8-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B-%D0%B8%D0%B7-%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%B0.md)** — для создания интерактивных элементов (игры, карусели, опросники) без переадресации на сторонние ресурсы;
- **Ссылки в письме** — посмотреть все ссылки из шаблона и при необходимости поменять их тип (например, при использовании пользовательских ссылок [подтверждения подписки](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BF%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BD%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83.md) или [отписки](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%BE%D1%82%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%BE%D1%82-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D0%B0-%D0%B8%D0%BB%D0%B8-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8.md)):

![trigger-email-links.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-links.png)

#### Тестовая отправка

После заполнения раздела «Письмо» можно посмотреть пример сформированной рассылки для пользователя.

**Исключение:** рассылки [с событийными параметрами](%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D0%B1%D1%8B%D0%B2%D0%B0%D1%8E%D1%82-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%BE-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D0%B8.md#sobytijnye-parametry). Проверить их можно с помощью [тестового режима рассылки](mailings-test-mode.md).

При тестовой отправке выбранный клиент **получает письмо на почту**.

Кликните по кнопке «Тестовая отправка»:

![trigger-email-test1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-test1.png)

Отметьте пользователей из списка или добавьте новых и нажмите «Отправить выбранным»:

![trigger-email-test2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-test2.png)

Отправлять тесты можно **только на контакты, имеющиеся на проекте**. Для создания карточки клиента воспользуйтесь [инструкцией](client-add.md).

Тестовые отправки никак не фиксируются в карточке клиента. Их статусы можно посмотреть списком по ссылке.

Сформированное письмо можно посмотреть **без отправки клиенту на почту** — для этого кликните по «Предпросмотру».

### Общие настройки

![trigger-email-general.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-general.png)

- **Бренд** — актуально для [мультибрендовых](multibrand.md) проектов;
- **Тематика** — разделение на [тематики](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D1%83-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md) позволяет пользователям настроить гибкую подписку, чтобы получать коммуникации только по интересующим темам;
- **Теги** — с помощью [тегов действий](tag.md) можно объединять рассылки по дополнительному признаку, если не хватает разделения по каналам, тематикам и папкам. Это позволит группировать рассылки в фильтрах и отчетах;
- **Профиль** — тип рассылки и ограничения по получателям, которые должны применяться или игнорироваться в зависимости от него:
  - Стандартная — для маркетинговых кампаний. Применяются базовые проверки по получателям:
    - есть валидный email;
    - есть подписка на email (или тематику в email, если она указана в рассылке);
    - не входит в [глобальную контрольную группу](%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0.md) (если включена функция) — не путать [с контрольной группой рассылки](email-mass-new.md#ab-test-i-kontrolnaya-gruppa-rassylki);
    - не превышен лимит по [коммуникациям за день](frequency-policy.md) (если включена функция).  
        
      Эти проверки можно отключить в рамках рассылки, используя соответствующие переключатели в профиле.
  - Opt-in — для [подтверждения подписки](doi-turn-on.md). Применяются проверки:
    - есть валидный email;
    - подписка на email (или тематику в email, если она указана в рассылке) в статусе «Ожидает подтверждения»;
    - не превышен лимит по коммуникациям за день (если включена функция).  
        
      Можно отключить проверку по частоте коммуникаций.
  - Транзакционная — рассылка, которую клиент сам запрашивает и ожидает получить как можно быстрее. Проверки не применяются.

### Ограничения отправки

![trigger-email-time.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-time.png)

- **Часы отправки** — можно ограничить по [часовому поясу клиента](client-timezone.md) или [проекта](project-settings.md);
- **Актуальность** — время, в течение которого имеет смысл отправлять рассылку. Можно ограничить по времени отправки сообщения или задать дату вручную.

### UTM-метки

![mass-email-utm.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/mass-email-utm.png)

Метки позволяют определить [источник перехода](%D0%BA%D0%B0%D0%BA-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0-%D1%81%D0%B0%D0%B8%D1%82.md) на сайт и тем самым атрибутировать трафик к конкретной кампании и каналу.

Можно создать стандартные метки и переиспользовать их в email-рассылках или ввести пользовательские метки для конкретной рассылки.

## После заполнения настроек

### Готовность к отправке

В разделе автоматически проверяется наличие всех обязательных полей. Кликом по пункту можно перейти к нужному разделу.

Если всё заполнено, рассылка переходит из статуса «Черновик» в «Готова к отправке»:

![trigger-email-ready.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-ready.png)

Чтобы рассылку можно было выбирать в сценариях и операциях, нужно перевести ее в статус «Готова к использованию». Для этого кликните по кнопке «Закончить редактирование»:

![trigger-email-is-ready.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-is-ready.png)

После завершения редактирования нельзя будет менять бренд, профиль (кроме приоритета) и настройки АБ-тестирования рассылки.

## АБ-тест и контрольная группа рассылки

- **АБ-тесты** позволяют сравнивать разные варианты рассылок по влиянию на открытия, клики, выручку.
- **Контрольная группа (КГ)** определяет эффективность кампании, сравнивая поведение пользователей, получивших письмо, и клиентов без рассылки.  
  ![trigger-email-ab-test.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-ab-test.png)

В email доступны критерии оценки:

- **Показатель открытий** — процент клиентов, открывших рассылку за время тестирования (только без сравнения с контрольной группой);
- **Показатель кликов** — процент клиентов, сделавших хотя бы один клик в рассылке за время тестирования (только без сравнения с контрольной группой);
- **Целевое действие** — личное действие, совершенное клиентом за время тестирования.

![ab-test-trigger-email-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/ab-test-trigger-email-settings.png)

Подробнее об АБ-тестах автоматических рассылках — [в инструкции](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

## Результаты рассылки

### Фильтры

Для каждой рассылки создаются [статусы](customer-message-statuses.md), которые выдаются клиентам, чтобы обозначить взаимодействия с рассылкой:

![trigger-email-client-page.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-client-page.png)

С их помощью можно фильтрами отобрать:

- [клиентов, которые взаимодействовали с рассылкой](filter-clients-mailing.md):

![trigger-email-filter-clients.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-filter-clients.png)

- [статусы по рассылке](filter-clients-mailing.md#poisk-izmenenij-statusov-rassylki):

![trigger-email-filter-statuses.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-filter-statuses.png)

### Отчеты

- В рассылке доступен [отчет по ее показателям](%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8.md) сводным и динамическим:

![trigger-email-report.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-report.png)

- Можно посмотреть [карту кликов](click-maps.md):

![click-maps.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/click-maps.png)

- Также рассылка попадает в общий [отчет по рассылкам](mailings-dashboard.md):  
  ![trigger-email-dashboard.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/trigger-email-dashboard.png)

- [Подборка механик](https://mindbox.ru/academy/mechanics/kompanii-povyshayut-ehffektivnost-rassylok/) — как компании повышают эффективность рассылок
- [Автоматизация рассылок](https://mindbox.ru/journal/education/avtomatizaciya-rassylki/): когда и зачем она нужна
