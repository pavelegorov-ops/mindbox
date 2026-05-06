---
title: "Найти клиентов, которые взаимодействовали со списками"
slug: "filter-clients-list-changes"
source_url: "https://help.mindbox.ru/docs/filter-clients-list-changes"
vcs_path: "filter-clients-list-changes.md"
toc_path:
  - Фильтры
  - Регистрация и действия клиента
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:794715c10b83d78dc9e28f336b38e31bfc4905fa02b627bc999cbcbabd645780"
---

# Найти клиентов, которые взаимодействовали со списками

Клиенты могут добавлять товары в [списки](personal-list.md), например, «Корзину» или «Избранное».

При этом в карточке у клиента появляется действие добавления, связанное с продуктом.  
Отобрать эти действия можно с помощью специального условия «Изменения списков продуктов».

### По каким критериям можно отбирать изменения

Изменением списка считается:

- добавление продукта;
- удаление продукта;
- изменение стоимости линии или количества продуктов в ней;
- установка списка;
- очистка списка.

При добавлении или удалении линии клиенту выдается действие, связанное с [продуктом](product.md):

![Снимок экрана 2024-02-19 в 18.05.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-19%20%D0%B2%2018.05.54.png)

При изменении стоимости линии выводится, насколько поменялась цена за штуку:

![Снимок экрана 2024-02-28 в 11.51.06.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-28%20%D0%B2%2011.51.06.png)

При изменении количества продуктов в линии выводится, насколько изменилось значение:

![Снимок экрана 2024-02-28 в 11.44.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-28%20%D0%B2%2011.44.54.png)

При установке списка с одним действием может быть связано несколько линий:

![Снимок экрана 2024-02-28 в 11.50.11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-02-28%20%D0%B2%2011.50.11.png)

При очистке в действии фиксируется только список:

![Снимок экрана 2023-12-01 в 10.26.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-01%20%D0%B2%2010.26.33.png)

Можно отобрать клиентов с определенным типом изменения:

![Снимок экрана 2023-12-21 в 13.02.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2013.02.33.png)

А также уточнить связанный продукт и список, сузить выборку по месту и времени события:

![Снимок экрана 2023-12-21 в 13.09.51.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-21%20%D0%B2%2013.09.51.png)

При добавлении в список можно проверить, что продукт всё ещё в списке с помощью одноименного условия.

### Пример поиска клиентов с действиями по списку

Задача: отобрать клиентов, которые за последний час добавляли в корзину очки.

На вкладке **Данные** → **Клиенты** внесите условие «Изменения списков продуктов»:

![Снимок экрана 2023-12-01 в 10.57.14.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-01%20%D0%B2%2010.57.14.png)

Такой фильтр находит клиентов с любым действием по любому списку за всё время.

Уточните [условия по изменению](%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B2-%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%85.md):

- тип изменения:

![тип](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%B8%D0%BF.png)

![тип-д](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%82%D0%B8%D0%BF-%D0%B4.png)

- список продуктов:

![Снимок%20экрана%202023-12-01%20в%2011.03.27](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-01%20%D0%B2%2011.03.27.png)

![список-д](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B4.png)

- критерии по продукту:

![прод](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D1%80%D0%BE%D0%B4.png)

![прод-д](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%BF%D1%80%D0%BE%D0%B4-%D0%B4.png)

- время события:

![время](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D1%80%D0%B5%D0%BC%D1%8F.png)

![время-д](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%B4.png)

### Найти действия со списком

На вкладке **Данные** → **Действия** можно отобрать действия добавления, удаления, коррекции и очистки и посмотреть их подробности.

«Изменения списков продуктов» на вкладке включает те же свойства, что и одноименный фильтр на странице клиентов.

Чтобы найти действия из примера выше, воспользуйтесь фильтром:

![Снимок экрана 2023-12-01 в 11.30.17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-01%20%D0%B2%2011.30.17.png)

Узнать больше о работе фильтров можно в курсе [«Фильтры Mindbox»](https://stepik.org/course/130156/info).

В видеоуроках собрана вся основная информация о фильтрах, которая может понадобиться в работе, а после каждого урока идет закрепление материала в практических заданиях.

[Как использовать метрику LTV](https://mindbox.ru/journal/experts/kak-ispolzovat-ltv/): 6 стратегий управления жизненным циклом клиента
