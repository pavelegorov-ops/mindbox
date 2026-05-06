---
title: "Как создаются каналы и точки контакта по utm-меткам"
slug: "как-создаются-каналы-и-точки-контакта-по-utm-меткам"
source_url: "https://help.mindbox.ru/docs/как-создаются-каналы-и-точки-контакта-по-utm-меткам"
vcs_path: "как-создаются-каналы-и-точки-контакта-по-utm-меткам.md"
toc_path:
  - "Клиенты, заказы и продукты"
  - Действия
  - Каналы и точки контакта
  - Каналы
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:80a97568037456f06e387fe54b804b5a6167ed28972f6b4fa02156837cba4b10"
---

# Как создаются каналы и точки контакта по utm-меткам

[Точка контакта](point-of-contact-add) – это способ связи с клиентом (иногда: место действия), с помощью которого происходит действие. [Канал](channel-add) – это средство объединения точек контакта в группы.

Каналы и точки контакта в системе создаются автоматически после того, как js-трекер Mindbox на целевом сайте зафиксирует переход по ссылке с меткой. Это значит, что клика по ссылке с меткой не достаточно для создания дерева контактов.

#### Может быть три сценария:

1. Ссылки с метками из рассылки ведут на сторонний сайт без трекера. В этом случае каналы и точки контакта не будут созданы.
2. Трекер установлен, но не успел зафиксировать клиента (например, клиент кликнул, но сразу закрыл сайт). Каналы и точки контакта не будут созданы.
3. Трекер установлен и зафиксировал переход по ссылке (то есть, клиент не просто кликнул и побыл на сайте), то создаются каналы и точки контакта для каждой уникальной ссылки.

С первыми двумя все понятно. Разберем, как именно создается дерево каналов и точек контакта.

#### Если трекер установлен и зафиксировал переход

Используемые в ссылке UTM-метки запишутся веткой вида:

![84724756a7bab4fa72b1831c71bab2d308-11-201815-41-53.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/84724756a7bab4fa72b1831c71bab2d308-11-201815-41-53.jpg)

В канал " WEB — источники переходов":

![847249782a94080eb49857139cbef75308-11-201815-42-52.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/847249782a94080eb49857139cbef75308-11-201815-42-52.jpg)

Метка Utm_term относится к опциональным, т.е. ее использование не обязательно. В случае, если она не использовалась в ссылке, то просто не будет создана соответствующая точка контакта.

#### Примеры

Клиент перешел по ссылке [**http://project.ururu/?utm_source=the&utm_medium=must&utm_term=on&utm_content=go&utm_campaign=show**](http://project.ururu/?utm_source=the&utm_medium=must&utm_term=on&utm_content=go&utm_campaign=show)  и был зафиксирован трекером. В канале " WEB — источники переходов" появится ветка:

![84728261c6c7d5dc4b74f3b5be50ea0108-11-201816-01-59.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/84728261c6c7d5dc4b74f3b5be50ea0108-11-201816-01-59.jpg)

Клиент перешел по ссылке без метки utm_term: [**http://project.ururu/?utm_source=the&utm_medium=must&utm_content=go&utm_campaign=show**](http://project.ururu/?utm_source=the&utm_medium=must&utm_content=go&utm_campaign=show)  и был зафиксирован трекером. В канале " WEB — источники переходов" появится ветка:

![84730240097cf359c82245352bf1ed8a08-11-201816-12-16.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/84730240097cf359c82245352bf1ed8a08-11-201816-12-16.jpg)

Клиент перешел по ссылке [**https://www.site-without-tracker.coco/vse-produkty.html?utm_source=announcement-mailing&utm_medium=email&utm_term=vsyakoe&utm_content=button&utm_campaign=2018-10-20**](https://www.site-without-tracker.coco/vse-produkty.html?utm_source=announcement-mailing&utm_medium=email&utm_term=vsyakoe&utm_content=button&utm_campaign=2018-10-20)  на сайт без нашего трекера. Не будет создано никаких каналов/точек контакта.

[Что такое UTM-метки](https://mindbox.ru/academy/education/chto-takoe-utm-metki/) и как их использовать для сегментации клиентов
