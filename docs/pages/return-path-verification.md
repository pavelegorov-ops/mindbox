---
title: Проверка SPF и MX записей выделенного поддомена
slug: "return-path-verification"
source_url: "https://help.mindbox.ru/docs/return-path-verification"
vcs_path: "return-path-verification.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Дополнительные возможности рассылок
  - Цифровые подписи
fetched_at: "2026-05-13T11:52:59Z"
content_hash: "sha256:0d03ba223e5fc9bde503642291321b59e5eeecab4690d662bccbb5c9750a95aa"
---

# Проверка SPF и MX записей выделенного поддомена

[Подробнее о выделенном поддомене и его настройке](return-path.md).

После настройки выделенного поддомена для email-рассылок необходимо проверить корректность DNS-записей. Правильно настроенные MX и SPF записи обеспечивают надежную доставку писем и предотвращают попадание сообщений в спам.

- **MX-запись (Mail Exchange)** — указывает, какой почтовый сервер обрабатывает письма для вашего поддомена.
- **SPF-запись (Sender Policy Framework)** — разрешает Mindbox отправлять письма от имени поддомена.

После добавления настроек, выделенный поддомен будет готов в течение 48 часов.

---

## MX-запись

### Требования к MX-записи

- Значение записи полностью совпадает с записью, сгенерированной в настройках Mindbox;
- MX-запись Mindbox единственная или имеет наивысший приоритет (наименьшее числовое значение).

### Как проверить MX-запись

Для проверки записи MX воспользуйтесь инструментом «MX Lookup» на сайте [MxToolbox](https://mxtoolbox.com).

![return-path-dns-mx-lookup.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-mx-lookup.png)

1. Значение в колонке `Hostname` должно совпадать со значением из настроек Mindbox:

   ![return-path-dns-mx-record.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-mx-record.png)

   *Сгенерированная MX-запись в настройках Mindbox*

   ![return-path-dns-mx-hostname.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-mx-hostname.png)

   *Проверка значения Hostname в MxToolbox*
2. Значение в колонке `Pref` (приоритет) для записи Mindbox должно быть наименьшим среди всех MX-записей:

   ![return-path-dns-mx-pref-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-mx-pref-error.png)

   *Ошибка. У записи Mindbox самый низкий приоритет*

   ![return-path-dns-mx-pref.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-mx-pref.png)

   *Правильно. У записи Mindbox самый высокий приоритет*

---

## SPF-запись

### Требования к SPF-записи

- Значение записи полностью совпадает с записью, сгенерированной в настройках Mindbox;
- У поддомена только одна SPF-запись. Если есть другие SPF-записи, их нужно объединить.

### Как проверить SPF-запись

Для проверки записи SPF воспользуйтесь инструментом «TXT Lookup» на сайте [MxToolbox](https://mxtoolbox.com).

![return-path-dns-txt-lookup.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-txt-lookup.png)

1. Значение в колонке `Record` должно совпадать со значением из настроек Mindbox:

   ![return-path-dns-spf-record1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-spf-record1.png)

   *Сгенерированная SPF-запись в настройках Mindbox*

   ![return-path-dns-spf-record.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-spf-record.png)

   *Проверка значения Record в MxToolbox*
2. SPF-запись должна быть единственной в поддомене. Если уже есть существующая запись, объедините ее с записью Mindbox. Пример объеденного значения: `v=spf1 include:_spf.google.com include:spf.mindbox.ru ~all`

   ![return-path-dns-spf-merge-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-spf-merge-error.png)

   *Ошибка. В поддомене две SPF-записи*

   ![return-path-dns-spf-merge.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/return-path-dns-spf-merge.png)

   *Правильно. Записи объединены в одну*
