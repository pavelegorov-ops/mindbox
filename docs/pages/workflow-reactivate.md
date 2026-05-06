---
title: Сценарий для реактивации по заказам
slug: "workflow-reactivate"
source_url: "https://help.mindbox.ru/docs/workflow-reactivate"
vcs_path: "workflow-reactivate.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - После заказа
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:082cf0950c647a30723de597dac9677db580c9f558647733986890edd32297b8"
---

# Сценарий для реактивации по заказам

**Задача**: вернуть клиентов, которые давно не совершали заказы.

**Решение**: отправить рассылку для напоминания о бренде с помощью [сценария](what-is-workflow.md); при отсутствии заказов дополнительно мотивировать на покупку бонусом.

Перед созданием сценария:

- Добавьте автоматические рассылки в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md)

Создаем сценарий:

1. Запуск — [по расписанию](workflow-schedule.md), раз в сутки.  
   Проверяем валидность контакта и подписку [в канале рассылки](workflow-check-subscription.md); попадание в базу — от полугода назад; заказы есть, но не за последние полгода:

![Снимок экрана 2024-05-28 в 14.25.35.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2014.25.35.png)

Выборка клиентов зависит от модели бизнеса, индустрии и продолжительности цикла покупки.

Можно сегментировать отток по сумме прошлых покупок, их частоте и т. д., в том числе с помощью [RFM-сегментации](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-rfm-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.md), и строить с ними разные цепочки коммуникаций.

2. Отправляем первую рассылку:

![Снимок экрана 2024-05-28 в 13.07.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.07.30.png)

Что отправить в рассылке

- опрос — поможет выявить возможный негативный опыт и неудобства для клиентов;
- [популярные продукты](recommendations-bestsellers.md) или [персональные рекомендации](recommendations-personal.md) (параметр [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) или через [новый конструктор](new-email-builder-recommendations.md));
- популярные продукты из [любимой категории](parameters-category-from-computed-field.md);
- собранный вручную набор, например, с новинками — с помощью [пересчитываемого](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статического](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегмента (параметр [Products.GetBySegment()](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md));
  - дополнительно можно ограничить выборку [по любимому признаку](parameters-products-by-computed-field.md) клиента (цвет, стиль и т.д.);
- напоминание о широком ассортименте в виде карточек категорий.

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

3. Ждем 7 дней:

![Снимок экрана 2024-05-28 в 13.08.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.08.22.png)

4. Проверяем, были ли заказы:

![Снимок экрана 2024-05-28 в 13.11.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.11.42.png)

5. Отправляем рассылку с бонусом:

![Снимок экрана 2024-05-28 в 13.12.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.12.59.png)

Какие бонусы отправить

Для мотивации можно выдать [промокод](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md) или начислить [баллы](balances-create.md).

- параметр для вывода промокода — [Recipient.LastReceivedPromoCode.WithType{название пула}.Value](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md);
- для вывода даты сгорания баллов добавьте к отправке рассылки (Message.SendingDateTime) нужное количество дней с помощью [функции AddDays](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85?highlight=AddDays.md).

Дальше условия в трех блоках дублируются, поэтому их можно [скопировать](what-is-workflow.md#massovoe-kopirovanie-i-udalenie-blokov) с внесением незначительных изменений:

![Снимок экрана 2024-05-28 в 13.13.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.13.30.png)

6. Ждем ещё 12 дней:

![Снимок экрана 2024-05-28 в 13.14.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.14.48.png)

7. Проверяем, не воспользовался ли клиент бонусом:

![Снимок экрана 2024-05-28 в 13.15.09.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.15.09.png)

8. Отправляем напоминание о бонусе со сроком сгорания:

![Снимок экрана 2024-05-28 в 13.16.01.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2013.16.01.png)

9. В стартовом блоке ограничиваем [частоту срабатываний](workflow-limit-per-customer.md) по клиенту:

![Снимок экрана 2024-05-28 в 14.14.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2014.14.23%281%29.png)

В фильтре первого блока условия заданы таким образом, что клиенты могут повторно попадать в сценарий только при совершении нового заказа и только через 180 дней. Поэтому задавать частоту применений в нем необязательно.

Но при других настройках механики это ограничение может быть необходимым.

  

Сценарий готов, можно запускать:

![Снимок экрана 2024-05-28 в 14.14.36.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-28%20%D0%B2%2014.14.36%281%29.png)

## Дополнительные материалы

- [Реактивация базы](https://mindbox.ru/journal/education/reaktivaciya-bazy/?utm_source=help&utm_campaign=workflow-reactivate): как вернуть клиентов
- [Отток клиентов](https://mindbox.ru/journal/education/ottok-klientov/?utm_source=help&utm_campaign=workflow-reactivate): как контролировать уход пользователей
- Как бизнесу адаптироваться к [сезонному спаду](https://mindbox.ru/journal/experts/sezonniy-spad/?utm_source=help&utm_campaign=workflow-reactivate): 7 способов
- Автоматические сценарии реактивации и мобильные пуши помогли [Secret Kitchen](https://mindbox.ru/journal/cases/reaktivacii-mobilnye-pushi-secret-kitchen/?utm_source=help&utm_campaign=workflow-reactivate) увеличить количество повторных покупок в 1,7 раза
- [Подборка механик](https://mindbox.ru/journal/cases/podborka-mekhanik-triggernye-rassylki/?utm_source=help&utm_campaign=workflow-reactivate). Триггерные рассылки для роста конверсии в индустриях красоты и одежды
- [Геймификация в бизнесе](https://mindbox.ru/journal/education/gejmifikaciya-v-biznese/?utm_source=help&utm_campaign=workflow-reactivate): как маркетинговые игры увеличивают продажи
- 7,92% — инкрементальный прирост из CRM-канала. Как в [«Много лосося»](https://mindbox.ru/journal/cases/mnogolososya/?utm_source=help&utm_campaign=workflow-reactivate) сегментируют базу, выбирают офферы и автоматизируют рассылки
- Как [«Снежная Королева»](https://mindbox.ru/journal/cases/snezhnaya-koroleva/?utm_source=help&utm_campaign=workflow-reactivate) удвоила конверсию в покупку из email-канала
- ×4,4 выручка от CRM-канала. Как [Колесо.ру](https://mindbox.ru/journal/cases/koleso-ru/?utm_source=help&utm_campaign=workflow-reactivate) удерживает клиентов и увеличивает выручку в бизнесе с яркой сезонностью
- 9% → 14% доля email в выручке интернет-магазина. Как «[Галерея косметики](https://mindbox.ru/journal/cases/galereya-kosmetiki/?utm_source=help&utm_campaign=workflow-reactivate)» восстановила показатели CRM
- «[Магнит Доставка](https://mindbox.ru/journal/cases/magnit-dostavka/?utm_source=help&utm_campaign=workflow-reactivate)» получает 20% выручки из CRM-канала: мобильные пуши, каскадные сценарии, AB-тесты и NPS-опросы
- [Foodband](https://mindbox.ru/journal/cases/foodband/?utm_source=help&utm_campaign=workflow-reactivate) возвращает до 34% новых клиентов с помощью автоматического сценария

[Курс «Сегментация клиентов: удержание и возврат»](https://mindbox.ru/journal/course/segmentation-okko/)

В видеоуроках рассказываем, как сегментировать базу клиентов, чтобы получить максимум выгоды.

**Программа курса**

- Что такое сегментация
- Когда пора сегментировать базу
- Какие методы использовать для сегментации
- Как построить процесс сегментации
- С чего начать работу с сегментами
- Как понять, что выбранный подход работает
- Как использовать сегментацию для развития бизнеса
- Подводим итоги: как собрать структуру бизнес-процесса

**Урок 1. Что такое сегментация**

  

Урок также доступен [на youtube.](https://www.youtube.com/embed/ustBKnd8aQI?rel=0)

**[Ссылка для регистрации на курс](https://mindbox.ru/journal/course/segmentation-okko/)**

[Механики персонализации](https://mindbox.ru/academy/mechanics/unikalnye-mehaniki-personalizaczii-sajta/) — используйте идеи механик персонализации сайта наших клиентов из разных индустрий.
