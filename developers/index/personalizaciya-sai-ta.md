# Персонализация сайта

Section index — part of <https://developers.mindbox.ru/docs/>.
Pages live under `../pages/`. Full TOC: [INDEX.md](../INDEX.md).

- [Базовая интеграция](../pages/website-personalization-basic-integration.md)
- [Общая информация](../pages/website-personalization.md)
- [Особенности установки виджетов рекомендаций на сайте](../pages/website-recommendation-widgets-installation.md)
- [Расширенная интеграция](../pages/website-personalization-advanced-integration.md)

### Чеклист проверки интеграции персонализации

- [Виджет рекомендаций не работает по тестовой ссылке](../pages/widget-not-working-test-link.md)
- [Механика не работает по тестовой ссылке](../pages/mechanics-not-working-test-link.md)
- [Механика персонализации включена, но не показывается клиенту](../pages/mechanics-enabled-not-shown.md)
- [Механика персонализации прогружается медленно](../pages/mechanics-loads-slowly.md)

- **Механика персонализации отображается, игнорируя условия таргетинга**
  - [Корзина клиента изменилась и не соответствует условиям таргетинга](../pages/cart-changed-does-not-match-targeting.md)
  - [Обновление сегмента в таргетинге механики произошло без перезагрузки страницы](../pages/segment-updated-without-page-reload.md)
  - [Сайт работает как SPA (сменяет страницы без перезагрузки)](../pages/spa-navigation-without-reload.md)
- **Механика персонализации включена, но не показывается клиенту**
  - [В таргетинге указаны противоречивые условия](../pages/targeting-conditions-conflict.md)
  - [Завершился АВ-тест через Google Optimize](../pages/google-optimize-ab-test-ended.md)
  - [Не передаются данные по странице продукта, категории или продуктам в корзине](../pages/targeting-uses-product-conditions-but-data-not-sent.md)
  - [Превышен лимит по показам](../pages/impression-limit-exceeded.md)
  - [Устройство не привязано к клиенту, который входит в сегмент таргетинга механики](../pages/device-not-linked-to-target-customer.md)
- **Механика не работает по тестовой ссылке**
  - [В механике не указаны необходимые настройки](../pages/mechanics-missing-required-settings.md)
  - [В механике указана не та точка интеграции](../pages/mechanics-wrong-endpoint.md)
  - [На сайте настроена переадресация](../pages/website-has-redirects.md)
  - [Не установлен трекер Mindbox](../pages/tracker-not-installed.md)
  - [Некорректно выбрано место отображения](../pages/incorrect-display-location.md)
  - [Скрипты персонализации не установлены](../pages/scripts-not-installed.md)
  - [Трекер Mindbox установлен некорректно](../pages/tracker-installed-incorrectly.md)
- **Виджет рекомендаций не работает по тестовой ссылке**
  - [Не отображается виджет с рекомендациями к категории](../pages/widget-not-displayed-for-category.md)
  - [Не отображается виджет с рекомендациями к продукту](../pages/widget-not-displayed-for-product.md)
  - [Нет продуктов для рекомендации](../pages/no-products-for-recommendation.md)
### Расширенная интеграция

- [Передача данных с бэкенда](../pages/website-personalization-backend.md)
- [Передача данных с фронтенда](../pages/website-personalization-frontend.md)
- [Проверка расширенной интеграции](../pages/verify-advanced-integration.md)

- **Бэкенд**
  - [1. Создание операций для работы с бэкенда](../pages/step-1-create-operations-for-backend.md)
  - [2. Вызов операций из бэкенда сайта или из сторонней системы](../pages/step-2-call-operations-from-backend-or-external-system.md)
  - [3. Вызов операций для работы персонализации](../pages/step-3-call-operations-for-personalization.md)
  - [4. Настройки персонализации сайта в точке интеграции при интеграции с бэкенда](../pages/step-4-website-personalization-settings-for-backend-integration.md)
- **Фронтенд**
  - [1. Создание операций для работы с фронтенда](../pages/step-1-create-operations-for-frontend.md)
  - [2. Вызов операций с помощью JavaScript SDK Mindbox](../pages/step-2-call-operations-with-javascript-sdk.md)
  - [3. Настройки персонализации сайта в точке интеграции](../pages/step-3-website-personalization-settings-at-integration-point.md)
### Базовая интеграция

- [1. Установка трекера](../pages/tracker-installation.md)
- [2. Создание механики](../pages/step-2-run-mechanics.md)
- [3. Подключение модуля](../pages/step-3-connect-module.md)
- [4. Проверка базовой интеграции](../pages/step-4-verify-basic-integration.md)

### Особенности установки виджетов рекомендаций на сайте

- [Размещения виджета с реко по продукту или категории без расширенной интеграции](../pages/widget-placement-without-advanced-integration.md)
- [Размещения виджета с реко по продукту или категории с расширенной интеграцией](../pages/widget-placement-with-advanced-integration.md)
