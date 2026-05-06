---
title: Интеграция через Albato
slug: "подключение-mindbox-к-albato"
source_url: "https://help.mindbox.ru/docs/подключение-mindbox-к-albato"
vcs_path: "подключение-mindbox-к-albato.md"
toc_path:
  - Операции и интеграция
  - Стандартные интеграции
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:d655cc4d08f755e00a76287bf01c4f8e4f769a3e7eb98d880fa00ec9ca85d92e"
---

# Интеграция через Albato

Порядок настройки, ограничения и возможности указаны по ссылке ([Интеграция через Albato](https://developers.mindbox.ru/docs/%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-albato))

## Как настроить подключение Albato к Mindbox

В Albato перейдите в раздел «Подключения» и нажмите на «Добавить подключение».

![1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/1-RSKD636R.png)

В открывшемся окне выберите из списка — «Mindbox».

![2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/2%285%29.png)

В подключении укажите данные из вашего проекта в Mindbox.

![3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/3%285%29.png)

Эти данные можно найти в разделе «Интеграции» в вашем проекте Mindbox:

1. «ID конечной точки» — это системное имя точки интеграции. В списке «Интеграции» перейдите в выбранную точку и скопируйте системное имя

![4.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/4%285%29.png)

![5.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/5%284%29.png)

2. «Секретный ключ» — это секретный ключ выбранной точки интеграции. Нужно перейти в выбранную точку и скопировать ее секретный ключ.

Если необходимо, отдельную точку интеграции можно завести [по инструкции](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md).

После заполнения в подключении Albato «ID конечной точки» и «Секретного ключа» cохраните подключение.

![6.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/6%283%29.png)  
Подключение готово, теперь можно приступать к настройке связок для передачи данных.

## Как настроить передачу данных в Mindbox

Рассмотрим на примере интеграции с AmoCRM.

### Настройка в аккаунте Mindbox

[Заведите необходимые операции](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md#sozdanie-operacii-v3), по которым будут приходить данные из AmoCRM.

### Настройка в аккаунте Albato

Далее создайте связку в Albato под созданные операции: на каждую связку нужна отдельная операция.

![7.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/7%284%29.png)

В связке укажите в первом блоке — «AmoCRM» и событие, по которому должна сработать связка, во втором блоке — «Mindbox» и событие, которое должно сохраниться в кабинете Mindbox.

*Подключения с аккаунтами AmoCRM и Mindbox должны быть заведены заранее.*

![8.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/8%282%29.png)

![10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/10%282%29.png)

![Снимок экрана 2023-08-03 в 09.37.13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2009.37.13.png)

Далее настройте соответствие полей.

1. Часть полей заполните данными, которые вам нужны из AmoCRM.

![Снимок экрана 2023-08-03 в 09.45.17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2009.45.17%281%29.png)  
2. Часть полей, нужно заполнить статическими значениями:  
a. «Название операции» — системное имя операции, по которой будут приходить данные в Mindbox;

![Снимок экрана 2023-08-03 в 09.50.10.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2009.50.10.png)

![Снимок экрана 2023-08-03 в 09.54.49.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-03%20%D0%B2%2009.54.49.png)  
b. «Системное имя идентификатора клиента» — системное имя поля в кабинете Mindbox;  
![12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/12%282%29.png)

![13.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/13%281%29.png)

После завершения настройки полей нажмите «Запустить».

![15.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/15%281%29.png)  
Если все настроено корректно, то на проекте в Mindbox на странице «Действия» по названию операции можно найти переданные данные.

![16.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/16.png)

## Передача дополнительных полей через Albato

В Albato перейдите в раздел «Подключения» и выберите подключенный аккаунт Mindbox.

![Снимок экрана 2023-08-04 в 09.50.26.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2009.50.26.png)

В разделе «Доступ», в конце списка, найдите «Дополнительные поля к клиенту», «Дополнительные поля к отправке Email», «Дополнительные поля к действию», «Дополнительные поля к заказу».

Выберите нужное поле, в нашем примере это — «Дополнительные поля к клиенту» и «Дополнительные поля к заказу».

![Снимок экрана 2023-08-04 в 09.55.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2009.55.28.png)

![17.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/17%281%29.png)

Укажите системное имя дополнительного поля из кабинета Mindbox:

- По клиенту

![18.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/18.png)

![Снимок экрана 2023-08-04 в 10.29.02.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2010.29.02.png)

- По заказу

![Снимок экрана 2023-08-04 в 10.35.28.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2010.35.28.png)

![Снимок экрана 2023-08-04 в 10.37.57.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2010.37.57.png)

Нажмите «Сохранить».

После этого в связках Albato появится возможность указать значение дополнительного поля.

![Снимок экрана 2023-08-04 в 11.08.12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2011.08.12.png)

![Снимок экрана 2023-08-04 в 11.05.12.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2011.05.12.png)

![Снимок экрана 2023-08-04 в 10.59.41.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-08-04%20%D0%B2%2010.59.41.png)
