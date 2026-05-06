---
title: "Завершился АВ-тест через Google Optimize"
slug: "google-optimize-ab-test-ended"
source_url: "https://developers.mindbox.ru/docs/google-optimize-ab-test-ended"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
  - "Механика персонализации включена, но не показывается клиенту"
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e8963c60d53f84dda9d65058f2fd8d5389b6176d8fdb1021fe1650c5a9aaec52"
---

# Завершился АВ-тест через Google Optimize

**Как проверить**

1. Зайдите в настройки таргетинга формы
2. Проверьте, есть ли условие Google Optimize в таргетинге

![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/664de6c-image.png)

3. Зайдите в отчет о работе механики прямо из формы и проверьте, было ли резкое падение попадания в таргетинг

   ![](https://storage.yandexcloud.net/assets-developers-mindbox-ru/images/1c2c7cc-image.png)

Если видите резкое падение попадания в таргетинг и показа формы и при этом в таргетинге есть условие с [Google Optimize](https://help.mindbox.ru/docs/ab-test-google-optimize) - форма не отображается из-за теста Google Optimize

**Как исправить**

Подведите итоги АВ-теста, выберите выигравшую форму и запустите её без условия с Google Optimize
