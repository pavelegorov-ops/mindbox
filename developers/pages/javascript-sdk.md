---
title: Javascript SDK
slug: "javascript-sdk"
source_url: "https://developers.mindbox.ru/docs/javascript-sdk"
breadcrumb:
  - Общее
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:758e2f001c564cdc5a2fea8616f9fa17174478344362f340e13b4c7a76bf9e0e"
---

# Javascript SDK

## Общее описание

JavaScript SDK позволяет асинхронно взаимодействовать сайту с платформой Mindbox. Он интегрируется аналогично Google Analytics или Яндекс.Метрике, при этом не влияя на скорость загрузки сайта и работу трекеров.

Для работы с JavaScript SDK используется один объект "mindbox". Для вызова метода используется следующая конструкция: `mindbox('methodName', methodParameters, ... )`

*methodParameters* - объект с параметрами для метода. Набор параметров зависит от метода. С помощью данной конструкции можно вызывать методы в любом месте страницы после кода отслеживания. Если код JavaScript SDK еще не загружен, операции встанут в очередь и выполнятся, как только произойдет полная инициализация скрипта.

### Domain API Mindbox

Это домен, по которому будет происходить обращение в API Mindbox.

Чтобы получить нужный домен для вашего проекта, сделайте следующее:

1. Откройте админку проекта
2. Перейдите в операции (Кампании - Операции)
3. Откройте любую операцию
4. Нажмите "Посмотреть описание"
5. Возьмите домен из Url в спецификации

![domain-api.png](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/domain-api.png.png)

Не передавайте в этом поле адрес административного раздела

Так как JavaScript SDK может использовать различные поддомены на домене mindbox.ru, настройки сайта должны позволять использование кросс-доменных запросов (подробней можно прочитать [здесь](https://developer.mozilla.org/ru/docs/Web/HTTP/CORS)). Количество поддоменов и ip-адреса доменов не фиксируются, поэтому следует включать все поддомены в Content Security Policy директиву.

## Инициализация

#### Точка интеграции передается в настройках

```
<script>
      mindbox = window.mindbox || function() { mindbox.queue.push(arguments); };
      mindbox.queue = mindbox.queue || [];
      mindbox('create', {
          endpointId: '<Идентификатор точки интеграции>'
      });
  script>
  <script src="https:///scripts/v1/tracker.js" async>script>
```

#### Точка интеграции определяется по домену

#### Из консоли (для тестирования)

#### В режиме обратной совместимости (для старых клиентов)

Код отслеживания должен подключаться в самом верху страницы, до остальных вызовов JavaScript SDK.  
Чтобы точка интеграции определялась по домену, необходимо добавить этот домен в ее настройках.

## Получение deviceUUID

Метод позволяет получить уникальный идентификатор устройства (deviceUUID), который используется Mindbox для идентификации пользователей, и использовать его для вызова. Например, для интеграции с системами аналитики или для передачи на backend вашего сайта.

```
mindbox("helpers.getDeviceUUID", value => {
  // Ваш код для работы с deviceUUID
  })
```

## Вызов операций

#### Асинхронный

```
mindbox('async', {
operation: '<Название операции>',
data: <Данные для операции>,
onSuccess: <Функция, вызываемая при успехе>,
onError: <Функция, вызываемая при ошибке>
});
```

#### Синхронный

Обязательно передавать только имя операции. Для некоторых операций данные не нужны. Нужно ли выполнять функции при успехе или ошибке, зависит от сайта.

## Примеры

#### Асинхронный

```
mindbox('async', {
  operation: 'MySite.Registration',
  data: {
    customer: {
      mobilePhone: '79374134389',
      firstName: 'Иван',
      email: 'pivan@mindbox.ru'
    }
  },
  onSuccess: function() {
    alert("Вы успешно зарегистрированы.");
  },
  onError: function(error) {
    console.log(error);
  }
});
```

#### Синхронный

Если сайт использует SPA (сменяет страницы без перезагрузки).

Для корректной работы форм [персонализации сайта](https://developers.mindbox.ru/page/%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%BD%D0%B0-%D1%81%D0%B0%D0%B9%D1%82#%D0%B5%D1%81%D0%BB%D0%B8-%D1%81%D0%B0%D0%B9%D1%82-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82-%D0%BA%D0%B0%D0%BA-spa-%D1%81%D0%BC%D0%B5%D0%BD%D1%8F%D0%B5%D1%82-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B-%D0%B1%D0%B5%D0%B7-%D0%BF%D0%B5%D1%80%D0%B5%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8) следует:

- Перед трекером Mindbox добавить тег

```
<script> 
    window.PopMechanic = {watchLocation: false}; 
  script>
```

- После смены страницы вызывать в JS

```
window.PopMechanic && window.PopMechanic.update && window.PopMechanic.update()
```

## Возможные ошибки

| Ошибка | Причина | Решение |
| --- | --- | --- |
| 401 Unauthorized | Домен или поддомен не разрешен для использования трекера | Добавить домен или поддомен в список "Сайты с JavascriptSDK" в настройках точки интеграции с типом "Сайт" |
| Cross-Origin Request Blocked | Поддомен, который используется Javascript SDK для работы, был заблокирован настройками сайта. | Необходимо разрешить кросс-доменные запросы, либо добавить <https://*.mindbox.ru> в разрешенные зоны для кросс-доменных запросов |
| Refused to connect to '<https://....mindbox.ru/....>' because it violates the following Content Security Policy directive: ... | Настройки сайта запрещают трекеру обращаться к api на одном из наших поддоменов. | Разрешить все для скриптов с <https://*.mindbox.ru> |
| Refused to load the script '<https://....mindbox.ru/....js>' because it violates the following Content Security Policy directive: ... | Настройки сайта запрещают загружать трекер или его части из-за используемых ими возможностей браузера. | Разрешить все для скриптов с <https://*.mindbox.ru> |
