---
title: Как массово импортировать дисконтные карты и клиентов по файлу
slug: "discount-cards-and-clients-import"
source_url: "https://help.mindbox.ru/docs/discount-cards-and-clients-import"
vcs_path: "discount-cards-and-clients-import.md"
toc_path:
  - Лояльность и акции
  - Дисконтные карты
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:9e3d429a195231425d2a76bd6d66a367ee5597a5eec332b08b9449d30c785cc8"
---

# Как массово импортировать дисконтные карты и клиентов по файлу

1. На вкладке **Клиенты** кликаем на «Импорт» → «Импорт клиентов»:

   ![Снимок экрана 2022-06-08 в 19.26.45.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-08%20%D0%B2%2019.26.45.png)
2. В поле «Операция» выберите **Импорт карт и клиентов.** После этого, в правой части экрана будет доступен для скачивания файл с примерами заполнения полей:

   ![Снимок экрана 2021-04-30 в 10.51.16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-30%20%D0%B2%2010.51.16.png)
3. Подготовьте файл для импорта

   - Для идентификации клиентов можно использовать поля **Email** или **MobilePhone**.
   - Обязательными к заполнению являются поля **Status** (Статус) и **StatusChangeDateTimeUtc** (Время изменения статуса).

     - Статус карты может принимать значения:
     - Inactive — Не активирована
     - Activated — Активирована
     - Blocked — Заблокирована
   - Номера карт записываются в поле **CardNumber**.

   *Пример заполнения файла:*

   ![Снимок экрана 2021-04-30 в 11.01.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-30%20%D0%B2%2011.01.41.png)
4. Заполните настройки импорта и добавьте задачу:

   - Операция: *«Импорт карт и клиентов;»*
   - Комментарий к задаче: *необязательно, но так будет проще найти в списке задач;*
   - Кодировка файла: *по умолчанию — utf-8;*
   - Файл для импорта:*подготовленный файл для импорта;*
   - [Точка интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md);
   - Точка контакта: *Административный сайт DirectCRM;*
   - Разрешить создание новых карт: *поставить метку.*

   ![Снимок экрана 2021-04-30 в 11.06.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-30%20%D0%B2%2011.06.58.png)

Появится ссылка на задачу:

![Снимок экрана 2021-04-30 в 11.07.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-04-30%20%D0%B2%2011.07.14.png)

После выполнения задачи клиенты с картами загружены:

![Снимок экрана 2022-06-19 в 19.18.50.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-19%20%D0%B2%2019.18.50.png)

[Арбитраж промоакций](https://mindbox.ru/academy/education/arbitrazh-promoakczij/) — важная функция программы лояльности
