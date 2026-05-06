---
title: Интеграция Tilda с Mindbox через GTM
slug: "tilda-mindbox-integration-gtm"
source_url: "https://help.mindbox.ru/docs/tilda-mindbox-integration-gtm"
vcs_path: "tilda-mindbox-integration-gtm.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:5b2508858909fdda15240ae258de07d5f94f5a6d4147fac72ce93fe7c23bd102"
---

# Интеграция Tilda с Mindbox через GTM

Важно

При сборе данных через GTM происходит трансграничная передача персональных данных.  
В таких случаях перед использованием иностранных сервисов нужно предпринять обязательные шаги, в том числе уведомить Роскомнадзор о соответствующем намерении. При необходимости проконсультируйтесь с юристами или специалистами по защите данных.

[Google Tag Manager](https://tagmanager.google.com/) (GTM) — бесплатный инструмент для управления маркетинговыми активностями. Используя GTM, можно отслеживать действия клиентов на сайте при помощи тегов.  
Теги — фрагменты кода, которые настраиваются на стороне GTM и обычно помещаются внутрь страницы. Теги помогают сторонним сервисам собирать данные и проводить анализ поведения клиентов на сайте.

## Основные термины GTM

- **Контейнер** — фрагмент кода на языке JavaScript, аналогичный Mindbox JS SDK или счетчику Яндекс.Метрики. Из контейнера выгружаются и исполняются теги.
- **Тег** — настраиваемый фрагмент кода. Операции в Mindbox являются тегами.
- **Триггер** — условие срабатывания тега. Например, отправка формы, клик по кнопке или открытие страницы с определенным URL.
- **Переменная** — сущность, которая хранит информацию для использования в тегах. Переменные бывают разных типов и могут содержать постоянное значение или фрагмент кода для динамического вычисления.

## Подключение Tilda к GTM

Перед интеграцией Tilda с Mindbox необходимо подключить сайт к GTM. Процесс подключения сайта описан в инструкции [Tilda Help Center](https://help-ru.tilda.cc/googletagmanager).

## Настройка сбора контактов с формы на сайте

Раздел описывает настройку передачи персональных данных клиентов из форм на Tilda. Раздел включает следующие инструкции:

- [Создание интеграции и операций](tilda-mindbox-integration-gtm.md#sozdanie-integracii-i-operacij)
- [Настройка переменных в GTM](tilda-mindbox-integration-gtm.md#nastrojka-peremennyh-v-gtm)
- [Настройка триггеров в GTM](tilda-mindbox-integration-gtm.md#nastrojka-triggerov-v-gtm)
- [Настройка тега с трекером Mindbox в GTM](tilda-mindbox-integration-gtm.md#nastrojka-tega-s-trekerom-mindbox-v-gtm)
- [Настройка тега для отправки данных из формы в Mindbox](tilda-mindbox-integration-gtm.md#nastrojka-tega-dlya-otpravki-dannyh-iz-formy-v-mindbox)
- [Проверка интеграции](tilda-mindbox-integration-gtm.md#proverka-integracii)

### Создание интеграции и операций

В Mindbox создайте [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) для сайта и настройте операцию для создания клиентов на основании данных из формы.  
Пример настроек операции:

![Снимок экрана 2023-07-13 в 13.40.56.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-13%20%D0%B2%2013.40.56.png)

### Настройка переменных в GTM

Для точного сбора клиентских данных из формы необходимы идентификаторы полей ввода.

1. В GTM нажмите на поле ввода правой кнопкой мыши → **Исследовать** или **Исследовать элемент**. Откроется инспектор кода.
2. В инспекторе кода скопируйте значение переменной **id=**:

![image12](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image12.png)

3. Создайте переменную с типом **Собственный код JavaScript** и вставьте код, заменив значение **input_id** на ID поля ввода.  
   Переменная считывает указанное значение в поле формы сбора контактов.  
   Для каждого поля ввода в форме необходимо создать отдельную переменную.

```
function() {
  var data = document.getElementById( 'input_id' ).value;
  return data;
}
```

![image15](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image15.png)

---

Если в инспекторе кода отсутствует параметр **id**, то скопируйте значение переменной **name=**:

![ name.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%20name.png)  
В переменную вставьте код, заменив в нём значение **form_name** на имя поля ввода:

```
function getValue() {
  var inputValue = document.getElementsByName("form_name")[0].value;
  return inputValue;
}
```

### Настройка триггеров в GTM

Для настройки триггера на заполнение формы необходим event ID события.

1. Внутри настраиваемого контейнера нажмите **Предварительный просмотр**.
2. В открывшемся окне укажите адрес страницы с формой.
3. На странице сайта заполните и отправьте форму.  
   На странице с предварительным просмотром появится новое действие.
4. Скопируйте название события.

![image73](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image7%283%29.png)

5. В настройках триггеров создайте новый триггер с типом **Специальное событие**.
6. В поле **Название события** вставьте скопированное название.  
   Под каждую форму на сайте необходимо создать отдельный триггер.

![image81](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image8%281%29.png)

### Настройка тега с трекером Mindbox в GTM

1. Создайте тег с типом **Пользовательский HTML**.
2. В конфигурацию скопируйте [код трекера Mindbox](https://developers.mindbox.ru/docs/%D1%82%D1%80%D0%B5%D0%BA%D0%B5%D1%80).
3. Триггером укажите системное событие **Consent Initialization - All Pages**.

![image15](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image1%285%29.png)

### Настройка тега для отправки данных из формы в Mindbox

Необходимо создать теги для каждой из форм на сайте.

1. Создайте тег с типом **Пользовательский HTML**.
2. В конфигурацию скопируйте код JavaScript async из [созданной операции](tilda-mindbox-integration-gtm.md#sozdanie-integracii-i-operacij).
3. В параметры клиента в операции укажите переменные, получаемые из формы, внутри двойных фигурных скобок.
4. Обрамите код тегами `<script>` и `</script>`

![image161](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image16%281%29.png)

### Проверка интеграции

1. Нажмите **Предварительный просмотр**.
2. В открывшемся окне укажите адрес страницы с формой сбора данных.
3. Отправьте форму.
4. Вернитесь на страницу с предварительным просмотром.  
   В событии отправки формы в блоке **Tags Fired** находится настроенный для формы тег.

![image141](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image14%281%29.png)

5. Чтобы увидеть данные, переданные в Mindbox, нажмите блок **Tags Fired**.

![image10](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image10.png)

При успешной настройке в Mindbox создается новый клиент с введенными в форме данными.

![Снимок экрана 2023-07-13 в 13.58.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-13%20%D0%B2%2013.58.19.png)

6. Чтобы запустить передачу данных с публично доступной страницы, опубликуйте контейнер с изменениями.

## Настройка передачи действий клиентов на сайте

Раздел описывает настройку выдачи клиентам действий в зависимости от их активности на сайте. В описанном случае действие выдается при нажатии на кнопки.  
Раздел включает следующие инструкции:

- [Создание интеграции и операций](tilda-mindbox-integration-gtm.md#sozdanie-integracii-i-operacij1)
- [Настройка триггеров в GTM](tilda-mindbox-integration-gtm.md#nastrojka-triggerov-v-gtm1)
- [Настройка тега с трекером Mindbox в GTM](tilda-mindbox-integration-gtm.md#nastrojka-tega-s-trekerom-mindbox-v-gtm1)
- [Настройка тегов для передачи факта нажатий в Mindbox](tilda-mindbox-integration-gtm.md#nastrojka-tegov-dlya-peredachi-fakta-nazhatij-v-mindbox)
- [Проверка интеграции](tilda-mindbox-integration-gtm.md#proverka-integracii1)

### Создание интеграции и операций

Создайте [точку интеграции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) для сайта и настройте операцию для выдачи клиентам действий при нажатии на кнопки.  
Пример настроек операции:

![Снимок экрана 2023-07-13 в 14.03.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-13%20%D0%B2%2014.03.58.png)

Если на проекте нет нужного шаблона действия, [создайте его](template-action.md):

![tilda-integration-action.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/tilda-integration-action.png)

### Настройка триггеров в GTM

Для отслеживания нажатий используется встроенное событие **Клик**. Триггер содержит только это событие:

![image131](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image13%281%29.png)

### Настройка тега с трекером Mindbox в GTM

1. Создайте тег с типом **Пользовательский HTML**.
2. В конфигурацию скопируйте [код трекера Mindbox](https://developers.mindbox.ru/docs/%D1%82%D1%80%D0%B5%D0%BA%D0%B5%D1%80).
3. Триггером укажите системное событие **Consent Initialization - All Pages**.

![image15](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image1%285%29.png)

### Настройка тегов для передачи факта нажатий в Mindbox

Необходимо создать теги для каждой из форм на сайте.

1. Создайте тег с типом **Пользовательский HTML**.
2. В конфигурацию скопируйте код JavaScript async из [созданной операции](tilda-mindbox-integration-gtm.md#sozdanie-integracii-i-operacij1).
3. Обрамите код тегами `<script>` и `</script>`

Для созданной операции передача дополнительных данных внутри вызова по умолчанию не требуется.

![image43](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image4%283%29.png)

### Проверка интеграции

1. Нажмите **Предварительный просмотр**.
2. В открывшемся окне укажите адрес страницы нужной кнопкой.
3. Нажмите кнопку.
4. Вернитесь на страницу с предварительным просмотром.  
   В событии **Click** в блоке **Tags Fired** находится настроенный тег для формы.

![image52](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image5%282%29.png)

5. Чтобы увидеть данные, переданные в Mindbox, нажмите блок **Tags Fired**.

![image111](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/image11%281%29.png)

При успешной настройке и привязке [DeviceUUID](deviceuuid.md) текущего устройства к одной из карточек клиентов у клиента появляется нужное действие.

![Снимок экрана 2023-07-13 в 14.14.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-13%20%D0%B2%2014.14.26.png)

6. Чтобы запустить передачу данных с публично доступной страницы, опубликуйте контейнер с изменениями.
