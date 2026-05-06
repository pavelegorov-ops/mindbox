---
title: Как настроить импорт с FTP
slug: "как-настроить-импорт-с-ftp"
source_url: "https://help.mindbox.ru/docs/как-настроить-импорт-с-ftp"
vcs_path: "как-настроить-импорт-с-ftp.md"
toc_path:
  - Операции и интеграция
  - Начало работы
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:3af04423796dc8bb1eb967fcaa0f11564aeeb2543aed6c28beb747e263c59e08"
---

# Как настроить импорт с FTP

Для того чтобы импортировать файлы с FTP, необходимо выполнить следующие шаги:

1. Заходим в **Интеграции** и выбираем «FTP/SFTP импорт и экспорт данных»:

![Снимок экрана 2022-07-08 в 20.59.40.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-08%20%D0%B2%2020.59.40.png)

2. Нажимаем «Добавить»:

![Снимок экрана 2021-11-18 в 19.03.23.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-18%20%D0%B2%2019.03.23.png)

Выбираем:

![Снимок экрана 2021-11-18 в 19.04.54.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-18%20%D0%B2%2019.04.54.png)

3. В открывшейся форме заполняем все поля:

![Снимок экрана 2021-11-18 в 19.07.48.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-11-18%20%D0%B2%2019.07.48.png)

Операция импорта может быть выполнена для клиентов, продуктов и заказов. В зависимости от этого ссылка в Параметрах операции импорта будет отличаться:  
При импорте товаров ссылка будет иметь вид:

```
https://project-services.directcrm.ru/v2/import?operation=DirectCrm.Retail.ImportProducts&csvCodePage=65001&externalSystem={Идентификатор внешней системы}
```

- csvCodePage — идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter — символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier — символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.

При импорте клиентов ссылка будет иметь вид:

```
https://project-services.directcrm.ru/v2/import?operation=DirectCrm.Customers.Import&brand={Бренд}&csvCodePage=65001&csvColumnDelimiter=%3B&csvTextQualifier=%22&SourceActionTemplate={Действие регистрации клиента}
```

- csvCodePage — идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter — символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier — символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.
- brand — бренд, к которому относятся клиенты. Значение настраивается в системе
- SourceActionTemplate — действие регистрации клиента. Например, «Регистрация на сайте» или «Заполнение бумажной анкеты в магазине». Значение настраивается в системе.

При импорте заказов ссылка будет иметь вид:

```
https://project-services.directcrm.ru/v2/import?operation=DirectCrm.Orders.ImportInCurrentStatus&csvCodePage=65001&brand={Бренд}&identityProviderSystemName={Идентификатор клиента}&externalSystem={Идентификатор внешней системы}
```

- csvCodePage — идентификатор кодовой страницы Windows для CSV-файла. Предпочтительно использовать 65001 (UTF-8).
- csvColumnDelimiter — символ, использующийся для разделения колонок в CSV-файле.
- csvTextQualifier — символ, опционально добавляющийся в начале и в конце значения колонки, позволяя использовать в нём символы, обычно не разрешённые.

4. Нажимаем кнопку «Сохранить».

[Как использовать метрику LTV](https://mindbox.ru/journal/experts/kak-ispolzovat-ltv/): 6 стратегий управления жизненным циклом клиента
