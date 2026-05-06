---
title: Сценарий для поздравления с днем рождения
slug: "workflow-birthday"
source_url: "https://help.mindbox.ru/docs/workflow-birthday"
vcs_path: "workflow-birthday.md"
toc_path:
  - Сценарии
  - Примеры механик со сценариями
  - Работа с данными анкеты
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:8bff28772ac96587ab7feabdb1b98737cb2d5ec75bf5e1cf094de2ca7adddd36"
---

# Сценарий для поздравления с днем рождения

**Задача:** поздравить клиента с днем рождения.

Для решения задачи настроим [сценарий](what-is-workflow.md).

Перед созданием сценария:

- Добавьте автоматические рассылки в нужном канале: [email](email-trigger.md), [SMS](sms-campaign-automated.md), [Viber](viber-campaign-automated.md), [мобильный пуш](mobilepush-campaign-automated.md) или [вебпуш](webpush-campaign-automated.md)

Создаем сценарий:

1. Запуск — [по расписанию](workflow-schedule.md), раз в сутки.  
   Проверяем день рождения, валидность контакта и подписку [в канале рассылки](workflow-check-subscription.md):

![Снимок экрана 2021-12-17 в 12.37.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-17%20%D0%B2%2012.37.23.png)

Не путайте фильтры «День рождения» и «Дата рождения».

> 1 июня 1990 года — **дата** рождения, 1 июня — **день** рождения.

Если хотите отправить первое письмо заранее, используйте режим фильтра «до него»:

![Снимок экрана 2024-09-05 в 11.09.12](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.09.12.png)

2. Ограничиваем [частоту применения](workflow-limit-per-customer.md) сценария одним разом за календарный год:

![Снимок экрана 2024-09-05 в 11.08.35](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.08.35.png)

3. Выдаем бонус и отправляем рассылку:

![Снимок экрана 2024-09-05 в 11.03.38](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.03.38.png)

Что отправить в рассылке

- Можно выдать [промокод](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md) или начислить [баллы](balances-create.md):
  - параметр для вывода промокода — [Recipient.LastReceivedPromoCode.WithType{название пула}.Value](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md);
  - для вывода даты сгорания баллов добавьте к отправке рассылки (Message.SendingDateTime) нужное количество дней с помощью [функции AddDays](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85?highlight=AddDays.md).
- Рекомендации:
  - [популярные продукты](recommendations-bestsellers.md) или [персональные рекомендации](recommendations-personal.md) (параметр [Recipient.Recommendations.{название алгоритма}](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE.md) или через [новый конструктор](new-email-builder-recommendations.md));
  - популярные продукты из [любимой категории](parameters-category-from-computed-field.md);
  - собранный вручную набор, например, с новинками — с помощью [пересчитываемого](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B8-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) или [статического](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%BF%D0%BE-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%D0%BC.md) сегмента (параметр [Products.GetBySegment()](%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0-%D0%B8%D0%B7-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0.md));
    - дополнительно можно ограничить выборку [по любимому признаку](parameters-products-by-computed-field.md) клиента (цвет, стиль и т.д.).

Оценить эффективность и подобрать лучший вариант можно с помощью [АБ-тестирования](%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%83-%D0%B8-%D0%B0%D0%B1-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B5.md).

4. Ставим ожидание:

![Снимок экрана 2024-09-05 в 11.04.15](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.04.15.png)

5. Если промокод всё ещё не использован:

![Снимок экрана 2024-09-05 в 11.06.27](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.06.27.png)

6. Напоминаем о сроке его сгорания:

![Снимок экрана 2024-09-05 в 11.07.44](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.07.44.png)

Сценарий готов. Можно запускать:

![Снимок экрана 2024-09-05 в 11.08.50](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-05%20%D0%B2%2011.08.50.png)

## Дополнительные материалы

- [Триггерная рассылка в день рождения: как поздравить клиента с пользой для бизнеса](https://mindbox.ru/journal/education/rassylka-s-dnem-rozhdeniya/?utm_source=help&utm_campaign=workflow-birthday)

[Как собирать базу email-подписчиков в онлайне](https://mindbox.ru/academy/education/kak-sobirat-bazu-podpischikov/) — 10 реальных механик
