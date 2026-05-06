---
title: Настройка интеграции Tilda c Mindbox через Zapier
slug: "настройка-интеграции-tilda-c-mindbox-через-zapier"
source_url: "https://help.mindbox.ru/docs/настройка-интеграции-tilda-c-mindbox-через-zapier"
vcs_path: "настройка-интеграции-tilda-c-mindbox-через-zapier.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:6c356fa5da26cf660d0ca5a8f9be502919a87509b567ab3d9fe772c9ff8718e9"
---

# Настройка интеграции Tilda c Mindbox через Zapier

Сервис Zapier ограничил работу сервиса в РФ.

В Tilda вы сможете легко создать лендинг страницу, чтобы получить заявку от клиента, провести опрос, собрать адреса электронной почты и телефоны потенциальных клиентов с помощью форм, пригласить на вебинар или провести реактивацию.  
Одна страница, одно предложение, одно действие.

Получая эти данные в Mindbox, можно сегментировать базу клиентов, учитывая их ответы на лендинге; настраивать welcome-цепочки email и sms, цепочки напоминаний о мероприятиях.

**Почему через Zapier?**

Zapier — универсальный онлайн-конструктор автоматизаций. Он может заставить два веб-приложения работать вместе. Соединение осуществляется по схеме «ЕСЛИ случилось событие X, TO совершить действие Y».  
Прямой интеграции между Tilda и Mindbox нет, поэтому используем этот ресурс.

Интеграция сводится к следующим шагам:

1. Настройка Tilda.
2. Настройка Mindbox.
3. Настройка Zapier:  
   3.1. Интеграция Tilda и Zapier.  
   3.2. Интеграция Zapier и Mindbox.

## 1.Настройка Tilda

На этом шаге у вас должен быть создан сайт или лендинг в Tilda. Как это сделать можно узнать по ссылке <http://help-ru.tilda.ws/customdomain> или [https://tilda.cc/ru/lp/kak-i-gde-sozdat-landing/](https://tilda.cc/ru/lp/kak-i-gde-sozdat-landing)

Когда страница создана кликаем на нее:

![108537852315faa79c05e2bb80b5da2d0Screenshot8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108537852315faa79c05e2bb80b5da2d0Screenshot8.png)

Выбираем блок с данными и даем имена переменным. Это необходимо для передачи данных через Zapier:

![108538629e1b674fbaee7d67a76e155bfScreenshot1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108538629e1b674fbaee7d67a76e155bfScreenshot1.png)

![108539380042882c2a8d72b9a18b69e93Screenshot4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108539380042882c2a8d72b9a18b69e93Screenshot4.png)

Даем имена переменным для всех нужных полей и нажимаем Сохранить и закрыть.

## 2. Настройка Mindbox.

Создаем точку [интеграции](как-создать-и-настроить-точку-интеграции)  в Mindbox: Администрирование — Интеграции — Добавить точку интеграции.

Пример созданной точки:

![Снимок экрана 2021-11-24 в 16.18.43.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-24%20%D0%B2%2016.18.43.png)

Тип приложения — сайт.

Секретный ключ генерируется автоматически.

Следующим шагом создаем [операцию](операции-v-основные-сведения)  для точки интеграции. Заходим в нужную Компанию, жмем Добавить — Операцию.

Пример операции:

![Снимок экрана 2021-11-24 в 16.24.16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-24%20%D0%B2%2016.24.16.png)

*Для точек интеграции* — выбираем нашу созданную точку.  
*Операция требует передачи секретного сервисного ключа* — ставим галочку.  
*Шаги* — указываем шаги действий при совершении операции. В примере регистрируем потребителей в базе.

Настройки для Mindbox готовы!

## 3. Настройка Zapier.

### 3.1. Интеграция Tilda и Zapier.

Подробно процесс интеграции описан по ссылке <https://help-ru.tilda.ws/formszapier>.

Обратите внимание, что интеграция в статусе Бета и обязательно надо перейти в Zapier по ссылке из инструкции.

### 3.2.Интеграция Zapier и Mindbox.

После интеграции Tilda и Zapier настроим передачу данных в Mindbox.  
Во 2ом блоке Action делаем следующее:

- Choose App — выбираем Webhooks

![1085649696e51c49f6696c9aa816274dcScreenshot7.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/1085649696e51c49f6696c9aa816274dcScreenshot7.png)

- Кликаем на метод Custom Request и жмем Save+Continue

![108589890e3b6426f4f75e58ee678dd28Screenshot12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108589890e3b6426f4f75e58ee678dd28Screenshot12.png)

- Настраиваем Webhook.

**Method** - Post.  
**URL** - вида [https://api.mindbox.ru/v3/operations/async?operation=Param1&endpointId=Param2,](https://help.mindbox.ru/ru/) где Param1 — системное название операции из Mindbox; Param2 — системное имя точки интеграции.

![108588689ce5d99172714864af3d8e3bdScreenshot11.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108588689ce5d99172714864af3d8e3bdScreenshot11.png)

**Data** - запрос на передачу, можно взять шаблон универсальной операции отсюда <https://developers.mindbox.ru/docs/userregxml> , ненужные поля удалить.

В шаблоне надо расставить переменные из Tilda, чтобы система понимала, куда подставлять данные. Кликните на иконку, как показано на скрине, откроется поиск переменных:

![108583377740ffefeeb77e8978f4e1696joxiscreenshot1552485379608.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108583377740ffefeeb77e8978f4e1696joxiscreenshot1552485379608.png)

**Headers** - прописать следующие параметры:  
Content-Type application/xml  
Accept application/xml  
Authorization Mindbox secretKey="ключ берем из точки интеграции"  
Жмем Save+Continue

- Test this step

На этом шаге необходимо протестировать наш триггер. Для этого нажимаем на кнопку Re-test This Step, следуем подсказкам и получаем ответ системы. Устраняем ошибки, если есть. Проверяем в Mindbox, попал ли в базу потребитель, и корректное ли выдалось действие.  
Жмем кнопку «Finish» и переводим триггер в режим включен «ON»:

![108600870b27065aafc86cc394323a875joxiscreenshot1552488681865.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/108600870b27065aafc86cc394323a875joxiscreenshot1552488681865.png)

[Работа с API без навыков программирования](https://mindbox.ru/academy/education/kak-rabotat-s-api/) - интегрируем друг с другом разные сервисы типа банкинга, телефонии и CRM-систем.
