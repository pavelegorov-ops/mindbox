---
title: "Как отправлять события в Google Analytics, установленный через GTM"
slug: "как-отправлять-события-в-google-analytics-установленныи-через-gtm"
source_url: "https://help.mindbox.ru/docs/как-отправлять-события-в-google-analytics-установленныи-через-gtm"
vcs_path: "как-отправлять-события-в-google-analytics-установленныи-через-gtm.md"
toc_path:
  - Персонализация
  - Персонализация сайта
  - "Google Analytics, Google Optimize и Google Tag Manager"
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:c67a43fa4e3f1afd1710fc4a86ced6e9114729ef29b3a2471acd00c4137eea60"
---

# Как отправлять события в Google Analytics, установленный через GTM

Важно

При сборе данных через Google Analytics происходит трансграничная передача персональных данных.  
В таких случаях перед использованием иностранных сервисов нужно предпринять обязательные шаги, в том числе уведомить Роскомнадзор о соответствующем намерении. При необходимости проконсультируйтесь с юристами или специалистами по защите данных.

Если Google Analytics(GA) установлен через Google Tag Manager(GTM), то нужно подготовить GTM, чтобы он мог отправлять данные в GA.  
Простое правило:  
**1 событие = 1 триггер GTM + 1 тег GTM**

## 1. Настраиваем Google Analytics в GTM

1.1. Убедитесь, что в GTM заведена переменная, ссылающаяся на нужный трекер в GA. Если её нет, заведите её:

![Снимок экрана 2021-03-25в 13.38.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2013.38.53.png)

1.2. В открывшемся окне создания переменной нажимаем на иконку редактирования:

![Снимок экрана 2021-03-25в 13.39.33.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2013.39.33.png)

1.3. Надо создать последнюю переменную, которая указывает, к какому трекеру GA относить события. Для этого нужно создать переменную типа **Настройки Google Analytics**:

![Снимок экрана 2021-03-25в 13.40.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2013.40.28.png)

1.4. Тут также нужно задать два значения:

- Идентификатор отслеживания;
- Название переменной, например «Код трекера GA».

Остальные настройки игнорируем.

![Снимок экрана 2021-03-25в 13.56.47.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2013.56.47.png)

1.5. Идентификатор отслеживания можно найти в GA, в разделе Ресурсы и приложения:

![Снимок экрана 2021-03-25в 13.48.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2013.48.42.png)  
1.6 Сохраняем переменную.

## 2. Заводим триггер

2.1. Заходим в **Рабочую область** —> вкладка **Триггеры** —> нажимаем **Создать**:

![Снимок экрана 2021-03-25в 14.03.05.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.03.05.png)

2.2. В открывшемся окне создания триггера нажимаем на иконку редактирования:

![Снимок экрана 2021-03-25в 14.03.22.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.03.22.png)

2.3. Во всплывшем справа меню выбираем «Cпециальное событие»:

![Снимок экрана 2021-03-25в 14.03.53.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.03.53.png)

2.4. Например, нам нужно отследить показы формы. Создаем:

- Имя события — mindbox1111show
- Имя триггера — mindbox1111show

Остальные настройки игнорируем.

![Снимок экрана 2021-03-25 в 15.17.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2015.17.23.png)

Вместо цифр для удобства подставляйте id формы, который вы можете найти в настройках формы:

![Снимок экрана 2021-03-25в 14.13.08.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.13.08.png)

2.4 Сохраняем триггер.

## 3. Заводим тег

3.1. Заходим в **Рабочую область** —> вкладка **Теги** —> нажимаем **Создать**:

![Снимок экрана 2021-03-25в 14.28.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.28.13.png)

3.2. В открывшемся окне создания переменной нажимаем на иконку редактирования в карточке конфигурации тега:

![Снимок экрана 2021-03-25в 14.28.42.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.28.42.png)

3.3. Выбираем тип тега **Google Аналитика: Universal Analytics**:

![Снимок экрана 2021-03-25в 14.29.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.29.19.png)

3.4. Действия для настройки конфигурации тега при показе форм:

- Название тега —> mindbox1111show
- Тип отслеживания —> Событие
- Категория —> mindbox
- Действие —> show
- Ярлык —> 1111
- Настройки Google Analytics —> выбираем созданную переменную «Код трекера GA»

![Снимок экрана 2021-03-25 в 15.19.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2015.19.10.png)

3.5. Далее переходим в карточку настройки триггера:

![Снимок экрана 2021-03-25 в 15.20.15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2015.20.15.png)

3.6. Выбираем созданный ранее mindbox1111show и сохраняем тег:

![Снимок экрана 2021-03-25 в 15.21.58.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2015.21.58.png)

3.7. Публикуем изменения.  
На вкладке **Обзор** нажмите на кнопку **Отправить**:

![Снимок экрана 2021-03-25в 14.52.34.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.52.34.png)

В открывшейся вкладке введите название версии, например, «Mindbox для аналитики», и опубликуйте версию:

![Снимок экрана 2021-03-25в 14.56.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2014.56.28.png)

Клик на версию открывает все изменения, которые будут опубликованы. Возможно, помимо тех, что вы внесли, есть что-то еще, способное повлиять на работу вашего сайта

## 4. Настраиваем Mindbox

4.1. Чтобы настроить отправку событий из Mindbox, нужно открыть раздел **Действия после заполнения формы клиентом** -> **Показ формы** и вводим

```
dataLayer.push({ event: 'mindbox1111show' });
```

![Снимок экрана 2021-03-25в 15.07.19.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-03-25%20%D0%B2%2015.07.19.png)

4.2. Аналогично заводятся любые другие события в Mindbox на любой из стадий срабатывания формы.

[Как проводить эксперименты на сайте](https://mindbox.ru/academy/education/ehksperimenty-google-optimize/) с помощью инструмента Google Optimize
