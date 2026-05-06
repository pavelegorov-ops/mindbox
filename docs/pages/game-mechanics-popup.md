---
title: Как добавить игровую механику со случайным подарком
slug: "game-mechanics-popup"
source_url: "https://help.mindbox.ru/docs/game-mechanics-popup"
vcs_path: "game-mechanics-popup.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - Интересные механики персонализации
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:3ba8b6b75863e047c8172dc689c52f464f0515d10debac13446d604058f4b197"
---

# Как добавить игровую механику со случайным подарком

Задача: создать игровую форму, в которой можно получить один из подарков за подписку и отправить пользователю полученный подарок.

![game-mechanics-examples.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-examples.png)  
*Можно использовать любой набор подарков.*

Чтобы запустить механику, нужно:

1. Создать и запустить форму из шаблона для игровой механики
2. Создать дополнительное поле, в которое будет записываться выигрыш
3. Настроить сценарий, выдающий и отправляющий подарок
4. Добавить рассылку с выводом выигрыша

Рассмотрим шаги подробнее.

## Создание попапа

[Создайте](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md) новый попап. Для механики нужна определенная форма (можно воспользоваться фильтром «С игровой механикой»):

![game-mechanics-templates.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-templates.png)

## Настройки попапа

Перейдите в [редактирование шаблона](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md#redaktirovanie-shablona) и скорректируйте дизайн попапа под ваш сайт.

### Подарки

Перейдите в настройки игрового элемента и найдите настройки секторов и вероятности выпадения.

![game-mechanics-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-settings.png)

1. Отредактируйте набор подарков: удалите или добавьте.
2. Кликните на подарок, чтобы перейти в его настройки, и укажите:

   - Название или картинка подарка.
   - **Идентификатор выигрыша**. Укажите названия подарков. Идентификатор будет передаваться в действие или в поле клиента и использоваться для определения подарка в сценарии. Подробнее [тут](spin-the-wheel-popup.md#nastrojka-peredachi-dannyh-na-proekt).
   - Текст, который будет выводиться в случае, если подарок выпадет.

   ![game-mechanics-prize.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-prize.png)
3. Укажите вероятность выпадения подарков:

   - **Простое** — позволяет быстро распределить вероятность выпадения подарка с помощью степени шанса. При выборе проценты **автоматически** перераспределяются между вариантами.
   - **Ввод в процентах** — позволяет вручную указать точный процент выпадения.

   ![game-mechanics-chance.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-chance.png)

   Данная настройка работает на фронтенде и не является защищенной от «взлома» посетителями через код сайта. Не рекомендуем использовать её для розыгрышей дорогих и особо ценных подарков.

### Поля сбора контактов

Перейдите к настройкам элементов формы и выберите поля, в которых будут запрашиваться данные клиента для отправки подарка.

![game-mechanics-data-fields.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-data-fields.png)

Мы не рекомендуем полностью удалять поля для ввода контактов, чтобы избежать злоупотребления формой. При этом отчет попапа всегда будет формироваться как для формы сбора контактов даже при отсутствии этих полей.

### Таргетинг

Ограничьте таргетинг формы, чтобы она не показывалась при каждом заходе на сайт.  
Базовые настройки попапов можно посмотреть в [общей инструкции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF-%D0%B0%D0%BF.md).

## Настройка передачи данных на проект

Передача данных работает по принципам, описанным в [инструкции](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B8%D0%B7-%D1%84%D0%BE%D1%80%D0%BC%D1%8B-%D0%BD%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md).

Для начала нужно добавить [дополнительное поле](additional-data.md) для хранения выигрыша.

> Можно создать как поле по действию, так и по клиенту. У первого варианта есть следующие плюсы: новое значение не переписывает предыдущий выигрыш, сохраняется история участий; дополнительные поля по клиенту используются в работе чаще, поэтому их излишнее количество может делать интерфейс более перегруженным.

Через поле действия

1. Создайте дополнительное поле по сущности действия с типом «строка»:

   ![Снимок экрана 2023-01-17 в 02.24.57.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-01-17%20%D0%B2%2002.24.57.png)
2. В настройках попапа «Действия после заполнения формы клиентом» задайте создание клиента с контактом, а также выдачу действия, в дополнительное поле которого будет записан выигрыш:

   - Поле в Mindbox — ранее созданное дополнительное поле по действию;
   - Поле формы — «Результат».

   ![Снимок экрана 2023-01-17 в 02.37.49.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-01-17%20%D0%B2%2002.37.49.png)

После участия в розыгрыше клиенту будет выдано действие регистрации и действие с подарком:

![Снимок экрана 2023-02-28 в 22.05.30.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-02-28%20%D0%B2%2022.05.30.png)

Через поле клиента

1. Создайте дополнительное поле по сущности «Клиент» с типом «строка»:

   ![game-mechanics-customer-customfield.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-customer-customfield.png)
2. В настройках попапа «Действия после заполнения формы клиентом» задайте создание клиента с контактом и созданным в п.1 поле и добавьте выдачу действия:

   - Поле в Mindbox — ранее созданное дополнительное поле по клиенту;
   - Поле формы — «Результат».

   ![Снимок экрана 2023-03-02 в 00.16.31.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-02%20%D0%B2%2000.16.31.png)

После участия в розыгрыше клиенту будет выдано действие регистрации, а подарок будет в его дополнительном поле:

![game-mechanics-customer-customfield-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-customer-customfield-example.png)

## Выдача и отправка подарка в сценарии

Форма — игровая составляющая механики. Выдачу и отправку подарков нужно настраивать отдельно с помощью сценария.

Сценарий запускается по действию выдачи подарка. Далее в блоке «Условие» проверяется сам подарок (он записан в дополнительное поле действия или клиента), выдается соответствующий подарок и отправляется рассылка.

Заранее создайте:

- [Автоматическую рассылку](email-trigger.md) для отправки подарка. Как вывести выигрыш в рассылке, рассмотрим ниже.
- [Пулы с промокодами](%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4%D1%8B-%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.md). Подарки будут выдаваться в виде промокодов, которые можно использовать в качестве бенефита к следующей покупке. Для каждого типа подарка нужен отдельный пул.

*При использовании других подарков настройка сценариев может различаться.*

Как настроить сценарий:

1. Запускающее событие — выдача подарка. Выберите шаблон из попапа:

   ![game-mechanics-workflow-event.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-workflow-event.png)
2. Проверьте значение выигрыша через [режим «Мультиветки»](multibranches.md). Необходимо добавить все варианты подарков, как они указаны **в идентификаторе выигрыша**.

   - Если приз передается в поле действия:

   ![Снимок экрана 2023-03-01 в 22.02.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-01%20%D0%B2%2022.02.28.png)

   - Если приз передается в поле клиента:

   ![Снимок экрана 2023-03-01 в 23.40.37.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-01%20%D0%B2%2023.40.37.png)
3. Выдайте соответствующий подарок и отправьте рассылку:

   ![Снимок экрана 2023-03-01 в 22.13.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-03-01%20%D0%B2%2022.13.26.png)
4. Добавьте отправку подарка для каждого варианта подарка и запустите сценарий:

   ![game-mechanics-workflow-done.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/game-mechanics-workflow-done.png)

## Вывод подарка в рассылке

Для вывода подарка в верстке проверяется значение выигрыша с помощью [блока if](%D0%BA%D0%B0%D0%BA-%D0%B2%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5-%D0%B1%D0%BB%D0%BE%D0%BA%D0%BE%D0%BC-if-else-if-end-if.md): в зависимости от его значения [выводится персональный промокод](%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%BA%D0%BE%D0%B4-%D0%B2-%D1%80%D0%B0%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83.md) из соответствующего пула и текст.

Например, нужно вывести сообщение:

```
Используйте промокод PROMO для получения PRIZE на следующую покупку.
```

Где вместо PROMO будет код клиента, а вместо PRIZE — тип выигрыша.

Задачу можно решить следующим кодом:

Реализация через действие

```
Используйте промокод

@{if CustomerAction.CustomField.Wheel.Name = "Скидка 5"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov1.Value} для получения скидки 5%

@{else if CustomerAction.CustomField.Wheel.Name = "Доставка"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov2.Value} для получения бесплатной доставки

@{else if CustomerAction.CustomField.Wheel.Name = "Бонус 400"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov3.Value} для получения 400 бонусов

@{else if CustomerAction.CustomField.Wheel.Name = "Бонус 500"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov4.Value} для получения 500 бонусов

@{end if}

на следующую покупку.
```

Реализация через поле клиента

```
Используйте промокод

@{if Recipient.CustomField.Podarok.Name = "Скидка 5"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov1.Value} для получения скидки 5%

@{else if CustomerAction.CustomField.Podarok.Name = "Доставка"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov2.Value} для получения бесплатной доставки

@{else if Recipient.CustomField.Podarok.Name = "Бонус 400"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov3.Value} для получения 400 бонусов

@{else if Recipient.CustomField.Podarok.Name = "Бонус 500"}
    ${Recipient.LastReceivedPromoCode.WithTypeNovyjPulPromokodov4.Value} для получения 500 бонусов

@{end if}

на следующую покупку.
```

*Параметры промокодов вида Recipient.LastReceivedPromoCode.WithType**NovyjPulPromokodov1**.Value составляются на основе системного имени пула; значение можно посмотреть на странице конкретного пула.*

Пример полученного сообщения:

> Используйте промокод 1234ABCD для получения 400 бонусов на следующую покупку.

[Механики персонализации](https://mindbox.ru/academy/mechanics/unikalnye-mehaniki-personalizaczii-sajta/) — используйте идеи механик персонализации сайта наших клиентов из разных индустрий.
