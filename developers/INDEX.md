# MindBox Developers — Index

Source: <https://developers.mindbox.ru/docs/>

Hierarchy is reconstructed from each page's left-sidebar breadcrumb
(Zudoku reveals only the open chain, so the tree is the union of all
fetched pages). Each leaf links to the local Markdown copy under `pages/`.

Per-section indexes (lighter than this file) live in `index/`. Use
`summaries.json` for fast, grep-based topic triage.

## Стандартные интеграции

- [PHP SDK](pages/php-sdk.md)
- [Интеграция Bitrix](pages/bitrix-integration.md)
- [Интеграция Frontol](pages/frontol-integration.md)
- [Интеграция iiko](pages/iiko-integration.md)
- [Интеграция OSMI Cards](pages/osmi-cards-integration.md)
- [Интеграция Passteam](pages/passteam-integration.md)
- [Интеграция rkeeper](pages/rkeeper-integration.md)
- [Интеграция Set Retail](pages/set-retail-integration.md)
- [Интеграция модуля для 1С:Розница](pages/1c-retail-module-integration.md)
- [Интеграция с Segmel](pages/segmel-integration.md)
- [Интеграция с приложением «Кошелёк»](pages/koshelek-app-integration.md)
- [Интеграция через Albato](pages/albato-integration.md)

### Интеграция с приложением «Кошелёк»

- [Механики для интеграции приложения «Кошелёк» для отправки пушей](pages/cardsmobile-integration-mechanics-for-loyalty-module.md)
- [Механики для интеграции приложения «Кошелёк» с модулем лояльность на Mindbox](pages/create-integration-for-cdp-and-loyalty-module.md)

### Интеграция iiko

- [Инструкция по работе с кассой IIKO](pages/iiko-pos-instructions.md)
- [Настройка плагина iiko версии V8.1.0.62 и выше](pages/iiko-plugin-setup-version-n-plus.md)

### Интеграция модуля для 1С:Розница

- [Версия розницы 2.3](pages/retail-version-23.md)

## Данные для аналитики

- [Как периодически обновлять данные](pages/periodic-data-updates.md)
- [Как прочитать данные](pages/how-to-read-data.md)
- [Описание схемы данных](pages/analytics-data-schema.md)

### Описание схемы данных

- [Заказы клиентов](pages/customer-orders.md)
- [История изменений внешних идентификаторов клиентов](pages/external-ids-change-history.md)
- [История сегментов клиентов](pages/customer-segments-history.md)
- [Объединения клиентов](pages/customer-merges.md)
- [Связь между списаниями и начислениями баллов](pages/link-between-bonus-redemptions-and-accruals.md)
- [События изменений балансов баллов клиентов](pages/customer-bonus-balance-change-events.md)
- [Состав заказов клиентов](pages/customer-order-lines.md)
- [Справочник АБ-тестов](pages/ab-tests-reference.md)
- [Справочник балльных промоакций](pages/bonus-promotions-reference.md)
- [Справочник балльных счетов](pages/bonus-accounts-reference.md)
- [Справочник вариантов АБ-тестов](pages/ab-test-variants-reference.md)
- [Справочник дополнительных полей](pages/customfields-reference.md)
- [Справочник папок](pages/folders-reference.md)
- [Справочник рассылок](pages/mailings-reference.md)
- [Справочник сегментаций](pages/segmentations-reference.md)
- [Справочник сегментов](pages/segments-reference.md)
- [Справочник статусов позиций заказов](pages/order-line-statuses-reference.md)
- [Справочник тегов](pages/tags-reference.md)
- [Справочник тематик рассылок](pages/mailing-topics-reference.md)
- [Справочник точек контакта](pages/touchpoints-reference.md)
- [Статусы рассылок](pages/mailing-statuses.md)
- [Теги в рассылках](pages/tags-in-mailings.md)
- [Участники АБ-тестов](pages/ab-test-participants.md)

### Как периодически обновлять данные

- [Как работать с объединением клиентов](pages/how-to-work-with-customer-merges.md)
- [Как рассчитать балльный баланс](pages/calculate-loyalty-points-balance.md)
- [Как сверить данные по заказам с отчетом](pages/reconcile-orders-with-report.md)

## Клиент

- [Аутентификация](pages/authentication.md)
- [Массовое редактирование клиентов](pages/customers-edit-v3.md)
- [Массовый импорт действий клиентов](pages/bulk-import-customer-actions.md)
- [Массовый импорт карт и клиентов](pages/bulk-import-cards-clients.md)
- [Массовый импорт клиентов](pages/customers-import-v3.md)
- [Объединение клиентов по запросу](pages/on-demand-customer-merging.md)
- [Отправка кода подтверждения](pages/send-confirmation-code.md)
- [Передача часового пояса](pages/time-zone-edit.md)
- [Подтверждение мобильного телефона и подписки на СМС](pages/mobile-phone-verification.md)
- [Подтверждение мобильного телефона на стороне заказчика](pages/phone-verification-client-side.md)
- [Получение данных клиента](pages/get-customer-data.md)
- [Проверка наличия клиента в БД](pages/customer-existence-database-check.md)
- [Регистрация, формы подписки, трекинг входа на сайт](pages/registration-authorization-subscription.md)
- [Редактирование данных клиента](pages/account-data-editing.md)
- [Реферальная программа](pages/referral-code-registration.md)
- [Черный список контактов](pages/blacklist.md)

### Получение данных клиента

- [javascript](pages/javascript-1.md)
- [json](pages/get-customer-data-json.md)
- [xml](pages/get-customer-data-xml.md)

### Регистрация, формы подписки, трекинг входа на сайт

- [javascript](pages/userregjson.md)
- [json](pages/json.md)
- [xml](pages/userregxml.md)

### Аутентификация

- [Аутентификация по паролю](pages/password-based-authentication.md)
- [Аутентификация по секретному коду](pages/secret-code-authentication.md)
- [Аутентификация по ссылке из рассылки](pages/ticket-authentication.md)

### Редактирование данных клиента

- [javascript](pages/userredjson.md)
- [json](pages/userredjson-1.md)
- [xml](pages/userredxml.md)

## Мобильные приложения

- [Android SDK](pages/android-sdk.md)
- [Expo SDK](pages/expo-sdk.md)
- [Flutter SDK](pages/flutter-sdk.md)
- [In-App](pages/in-app.md)
- [iOS SDK](pages/ios-sdk.md)
- [Mindbox SDK](pages/mindbox-sdk.md)
- [React Native SDK](pages/react-native-sdk.md)
- [Справочное](pages/mobile-sdk-reference.md)
- [Универсальные ссылки](pages/universal-links.md)
- [Центр уведомлений](pages/notification-center.md)
- [Чек-лист проверки интеграции SDK](pages/sdk-integration-checklist.md)

### Android SDK

- [1. Добавление SDK в приложение](pages/add-android-sdk.md)
- [2. Инициализация SDK](pages/android-sdk-initialization.md)
- [3.1. Отправка push-notifications через Firebase](pages/firebase-send-push-notifications.md)
- [3.2. Отправка push-notifications через Huawei](pages/huawei-send-push-notifications.md)
- [3.3. Отправка push-notifications через RuStore](pages/rustore-send-push-notifications.md)
- [4. Получение кликов на мобильные push-уведомления](pages/android-get-click.md)
- [5. Получение источника установки мобильного приложения](pages/android-app-start-tracking.md)
- [6. Интеграция действий в приложении](pages/android-integration-of-actions.md)
- [Cинхронизация deviceUUID между Android mobile SDK и JS SDK в приложении с WebView](pages/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview.md)
- [Как получать пуши из нескольких источников отправки](pages/how-to-receive-push-notifications-from-multiple-sources.md)
- [Методы Android SDK](pages/android-sdk-methods.md)
- [Настройка точек интеграции](pages/add-android-integration.md)
- [Переход с V1 на V2 Android SDK](pages/v1-v2-android-sdk.md)
- [Получение ключей провайдеров пушей](pages/android-push-provider-keys.md)
- [Поля конфигурации Android SDK](pages/android-sdk-configuration.md)
- [Структура конструктора запроса Android SDK](pages/android-sdk-request-body.md)
- [Структура конструктора ответа Android SDK](pages/android-sdk-response-body.md)
- [Формат пуш уведомления Android](pages/android-push-notification-format.md)

- **Получение ключей провайдеров пушей**
  - [Получение Firebase ключей](pages/firebase-key-setup.md)
  - [Получение Huawei ключей](pages/huawei-get-keys.md)
  - [Получение RuStore ключей](pages/rustore-get-keys.md)
### React Native SDK

- [Android | Настройка пуш-уведомлений](pages/rn-android-push-notifications-setup.md)
- [Android | Передача кликов по push-уведомлениям](pages/android-get-click-react-native.md)
- [Cинхронизация deviceUUID между React Native mobile SDK и JS SDK в приложении с WebView](pages/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-react-native.md)
- [iOS | Настройка Rich-push уведомлений](pages/rn-ios-rich-push-notifications.md)
- [iOS | Настройка гарантированной доставки](pages/ios-setup-background-tasks-react-native.md)
- [iOS | Настройка пуш-уведомлений](pages/ios-send-push-notifications-react-native.md)
- [iOS | Передача кликов по push-уведомлениям](pages/ios-get-click-react-native.md)
- [Добавление SDK в приложение](pages/add-sdk-react-native.md)
- [Инициализация SDK](pages/sdk-initialization-react-native.md)
- [Интеграция действий в приложении](pages/integration-actions-react-native.md)
- [Методы React Native SDK](pages/react-native-sdk-methods.md)
- [Навигация по клику на push-уведомление](pages/flutter-push-navigation-react-native.md)
- [Настройка точек интеграции](pages/add-integration-rn.md)
- [Получение источника установки мобильного приложения](pages/ios-app-start-tracking-react-native.md)
- [Получение ключей для пуш-уведомлений](pages/rn-get-push-keys.md)

- **Android | Настройка пуш-уведомлений**
  - [Firebase](pages/firebase-send-push-notifications-react-native.md)
  - [Huawei](pages/huawei-send-push-notifications-react-native.md)
  - [RuStore](pages/rustore-send-push-notifications-react-native.md)
- **iOS | Настройка Rich-push уведомлений**
  - [Отображение картинки и кнопки](pages/ios-rich-push-image-and-button-react-native.md)
  - [Отображение превью картинки](pages/ios-rich-push-image-preview-react-native.md)
### iOS SDK

- [Cинхронизация deviceUUID между iOS mobile SDK и JS SDK в приложении с WebView](pages/ios-webview-sync-with-sdk.md)
- [Добавление SDK в приложение](pages/add-sdk-to-app.md)
- [Инициализация SDK](pages/ios-sdk-initialization.md)
- [Интеграция действий в приложении](pages/ios-integration-actions.md)
- [Методы iOS SDK](pages/ios-sdk-methods.md)
- [Настройка push-уведомлений](pages/ios-quick-setup-push-notifications.md)
- [Настройка Rich-push уведомлений](pages/ios-rich-push-notifications.md)
- [Настройка Sandbox окружения](pages/sandbox-integration-setup.md)
- [Настройка гарантированной доставки](pages/ios-guarantee-delivery-setup.md)
- [Настройка точки интеграции](pages/add-ios-integration.md)
- [Передача кликов по push-уведомлениям](pages/ios-push-click-forwarding.md)
- [Передача событий через iOS SDK](pages/ios-sdk-events.md)
- [Переход по ссылке из push-уведомления](pages/ios-push-notification-deep-linking.md)
- [Получение источника установки мобильного приложения](pages/ios-get-app-install-source.md)
- [Получение ключей и настройка подключения к APNS](pages/apns-keys-setup.md)
- [Поля конфигурации iOS SDK](pages/ios-sdk-configuration-fields.md)
- [Структура конструктора запроса iOS SDK](pages/ios-sdk-request-constructor.md)
- [Формат пуш уведомления iOS](pages/ios-push-notification-format.md)

- **Настройка Rich-push уведомлений**
  - [Отображение картинки и кнопки](pages/rich-push-notifications-buttons.md)
  - [Отображение превью картинки](pages/rich-push-notifications-preview.md)
### Flutter SDK

- [Android | Настройка пуш-уведомлений](pages/flutter-android-push-notifications-setup.md)
- [Cинхронизация deviceUUID между Flutter mobile SDK и JS SDK в приложении с WebView](pages/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-flutter.md)
- [iOS | Настройка Rich-push уведомлений](pages/flutter-ios-rich-push-notifications.md)
- [iOS | Настройка гарантированной доставки](pages/ios-setup-background-tasks-flutter.md)
- [iOS | Настройка пуш-уведомлений](pages/ios-send-push-notifications-flutter.md)
- [Добавление SDK в приложение](pages/add-sdk-flutter.md)
- [Инициализация SDK](pages/flutter-sdk-initialization.md)
- [Интеграция действий в приложении](pages/integration-actions-flutter.md)
- [Методы Flutter SDK](pages/flutter-sdk-methods.md)
- [Навигация по клику на push-уведомление](pages/flutter-push-navigation.md)
- [Настройка точек интеграции](pages/flutter-new-integration-setup.md)
- [Передача кликов по push-уведомлениям](pages/ios-get-click-flutter.md)
- [Получение источника установки мобильного приложения](pages/ios-app-start-tracking-flutter.md)
- [Получение ключей для пуш-уведомлений](pages/flutter-get-push-keys.md)

- **Android | Настройка пуш-уведомлений**
  - [Firebase](pages/firebase-send-push-notifications-flutter.md)
  - [Huawei](pages/huawei-send-push-notifications-flutter.md)
  - [RuStore](pages/rustore-send-push-notifications-flutter.md)
- **iOS | Настройка Rich-push уведомлений**
  - [Отображение картинки и кнопки](pages/ios-rich-push-image-and-button.md)
  - [Отображение превью картинки](pages/ios-rich-push-image-preview.md)
### Expo SDK

- [Базовая установка Expo SDK](pages/expo-sdk-setup.md)

- **Дополнительные настройки**
  - [Expo Notifications](pages/expo-notification.md)
  - [Навигация по клику на push-уведомление в Expo](pages/push-navigation-expo.md)
### In-App

- [Настройка операций в приложении для таргетинга in-app на операцию](pages/in-app-targeting-by-custom-operation.md)
- [Настройка операций в приложении для таргетинга на экран категории и экран продукта](pages/in-app-operation-category-and-product-targeting.md)

### Справочное

- [Проверка корректной работы мобильных push-уведомлений](pages/mobile-push-check.md)
- [Создание клиента в Mindbox](pages/sdk-subscribe-customer.md)

### Чек-лист проверки интеграции SDK

- [Android](pages/sdk-checklist-android.md)
- [IOS](pages/sdk-checklist-ios.md)
- [Общее](pages/sdk-checklist-general.md)

- **Android**
  - [Push-уведомление отображается не так, как ожидается](pages/sdk-checklist-push-not-as-expected.md)
  - [В push-уведомлении не отображается картинка](pages/sdk-checklist-push-no-image.md)
  - [В push-уведомлении не отображаются кнопки по нажатию](pages/sdk-checklist-push-buttons-not-working.md)
  - [Иконка push-уведомления отображается другим цветом](pages/sdk-checklist-push-icon-wrong-color.md)
  - [Клик на push-уведомление был, но нужный раздел приложения не открылся](pages/sdk-checklist-push-click-did-not-open-section.md)
  - [После отправки уведомлений приложение падает](pages/sdk-checklist-app-crashes-after-notifications.md)
  - [При клике на push-уведомление информация об этом не отображается в Mindbox](pages/sdk-checklist-push-click-not-tracked-in-mindbox-android.md)
  - [При отправке push-уведомления в системе статус «отправлено», но уведомление не отображается](pages/sdk-checklist-sent-but-not-displayed.md)
  - [При отправке push-уведомления статус «ContractMismatch»](pages/sdk-checklist-contractmismatch.md)
  - [При отправке уведомления ошибка с текстом «wrong token» или «все токены доступа некорректны»](pages/sdk-checklist-wrong-token-or-invalid-tokens.md)
  - [У установки статус «приложение не зарегистрировано в системе отправки пушей»](pages/sdk-checklist-installation-status-not-registered-android.md)
  - [Уведомления приходят, но в них не отображаются текст, иконка или вообще ничего](pages/sdk-checklist-push-missing-text-icon.md)
- **Общее**
  - [Пользователь есть в системе, но ему не доходит push-уведомление](pages/sdk-checklist-user-not-receiving-push.md)
  - [При отправке запроса через SDK в консоли ошибка](pages/sdk-checklist-console-error-when-sending-request.md)
  - [Приложение запустилось, но в консоли ошибка](pages/sdk-checklist-app-started-console-error.md)
- **IOS**
  - [В push-уведомлении не отображается большая картинка по нажатию](pages/sdk-checklist-push-no-large-image.md)
  - [В push-уведомлении не отображается маленькая картинка](pages/sdk-checklist-push-no-small-image.md)
  - [В push-уведомлении не отображаются кнопки по нажатию](pages/sdk-checklist-push-no-large-image-on-click.md)
  - [Клик вызывается, но данные не сохраняются в админке](pages/sdk-checklist-click-called-but-not-saved.md)
  - [Ошибка с текстом «неправильное окружение / Все токены доступа невалидны»](pages/sdk-checklist-wrong-environment-all-tokens-invalid.md)
  - [При клике на push-уведомление информация об этом не отображается в Mindbox](pages/sdk-checklist-push-click-not-tracked-in-mindbox.md)
  - [При отправке push-уведомления ошибка с текстом «wrong token»](pages/sdk-checklist-wrong-token.md)
  - [При отправке push-уведомления статус «ContractMismatch»](pages/sdk-checklist-contractmismatch-ios.md)
  - [Приложение не собирается — ошибка сборки](pages/sdk-checklist-build-error.md)
  - [У пользователя нет разрешения на push-уведомления](pages/sdk-checklist-no-push-permission.md)
  - [У установки статус «приложение не зарегистрировано в системе отправки пушей»](pages/sdk-checklist-installation-status-not-registered.md)
## Сегментации

- [Включение в сегмент](pages/add-customer-to-segment.md)
- [Исключение из сегментации](pages/remove-customer-from-segmentation.md)
- [Массовый импорт статических сегментаций клиентов](pages/static-customer-segments-v3.md)
- [Получение сегментов клиента](pages/get-customer-segments.md)
- [Получение списка сегментаций](pages/get-project-segments-list.md)

## Рассылки

- [Загрузка вложений для использования в письмах](pages/upload-attachments-for-emails.md)
- [Отправка рассылок по API](pages/api-mailings-send.md)

### Вебпуши

- [Настройка отправки пушей на сайт через Firebase](pages/get-firebase-keys-for-web-push.md)

### Отправка рассылок по API

- [javascript](pages/json-1.md)
- [json](pages/mailings-send-json.md)
- [xml](pages/tranletterxml.md)

## Общее

- [Javascript SDK](pages/javascript-sdk.md)
- [V3 API](pages/v3.md)
- [Ограничения при импорте данных](pages/data-import-limitations.md)
- [Тикет для авторизации на сайте](pages/website-authorization-ticket.md)
- [Требования и рекомендации по использованию API](pages/api-usage-recommendations.md)

### V3 API

- [Обработка ошибок](pages/error_processing.md)
- [Ограничения при работе с API](pages/api-restrictions.md)

### Javascript SDK

- [Интеграция JavaScript SDK через Анонимизатор](pages/javascript-sdk-anonymization.md)

## Промокоды и промоакции

- [Архивация внешних акций](pages/archive-external-promotions.md)
- [Выдача промокода](pages/bind-promocode.md)
- [Импорт внешних промоакций](pages/import-external-promotions.md)
- [Массовый импорт промокодов](pages/bulk-import-promocodes-v3.md)
- [Массовый импорт пулов промокодов](pages/bulk-import-promocode-pools-v3.md)
- [Отменить гашение промокода](pages/cancel-promocode-redemption.md)
- [Погасить промокод](pages/redeem-promocode.md)
- [Получение персональных предложений](pages/get-personal-offers-list.md)
- [Получение списка доступных для клиента промоакций](pages/get-promotions-for-customer.md)
- [Получение списка промокодов](pages/get-promocodes-list.md)
- [Создание и редактирование внешней промоакции](pages/save-external-promotion.md)
- [Установка персональных предложений](pages/set-personal-offers-list.md)

## Карты

- [Выдача дисконтной карты клиенту](pages/customer-card-activation.md)
- [Выдача дисконтной карты клиенту с смс-подтверждением](pages/bind-discount-card-with-sms-confirmation.md)
- [Замена дисконтной карты](pages/replace-card.md)
- [Массовый импорт пула дисконтных карт](pages/bulk-import-discount-card-pool-v3.md)
- [Массовый импорт пула подарочных карт](pages/bulk-import-gift-card-pool-v3.md)
- [Массовый импорт статусов дисконтных карт](pages/bulk-import-discount-card-statuses-v3.md)
- [Открепление дисконтной карты](pages/unbind-discount-card.md)
- [Получение данных дисконтной карты](pages/get-discount-card-details.md)
- [Получение списка дисконтных карт клиента](pages/get-customer-discount-cards-list.md)
- [Работа с подарочными картами в операциях сохранения заказов](pages/gift-cards-in-order-save-operations.md)
- [Смена статуса дисконтной карты в личном кабинете](pages/change-card-status-in-account.md)
- [Смена статуса дисконтной карты на кассе](pages/change-card-status-at-pos.md)

## Номенклатура

- [Действия с категориями](pages/product-category-actions.md)
- [Действия с продуктами](pages/product-actions.md)
- [Действия со списками продуктов](pages/product-list-actions.md)
- [Импорт категорий продуктов](pages/product-category-import.md)
- [Импорт персональных предложений](pages/import-personal-offers.md)
- [Импорт продуктов](pages/product-import.md)
- [Импорт региональных данных продуктов](pages/regional-products-import.md)
- [Массовое добавление продуктов в список](pages/bulk-add-products-to-list-v3.md)
- [Массовое обновление списка продуктов](pages/import-personalproductlist-v3.md)
- [Обновление информации о категории](pages/update-product-category.md)
- [Обновление информации о продукте](pages/update-product.md)
- [Обновление региональных данных продукта](pages/save-product-regional-info.md)
- [Получение списка продуктов клиента](pages/get-customer-product-list.md)
- [Удаление категорий](pages/delete-categories.md)

### Действия с категориями

- [javascript](pages/catactionjson.md)
- [xml](pages/catactionxml.md)

### Импорт категорий продуктов

- [csv](pages/catimportcsv.md)

### Действия с продуктами

- [javascript](pages/prodactionjson.md)
- [xml](pages/prodactionxml.md)

### Импорт продуктов

- [csv](pages/prodimportcsv.md)
- [xml](pages/prodimportxml.md)

### Действия со списками продуктов

- [javascript](pages/prodlistactionjson.md)
- [xml](pages/prodlistactionxml.md)

## Точки контакта, магазины, зоны

- [Массовое удаление зон](pages/bulk-delete-zones-v3.md)
- [Массовый импорт зон](pages/bulk-import-zones-v3.md)
- [Массовый импорт каналов](pages/bulk-import-channels-v3.md)
- [Массовый импорт точек контакта](pages/bulk-import-touchpoints-v3.md)

## Бонусный счет

- [Изменение бонусного счета клиента](pages/update-customer-bonus-account.md)
- [Массовый импорт изменений баланса](pages/bulk-import-balance-changes-v3.md)
- [Получение баланса клиента](pages/get-customer-bonus-balance.md)
- [Получение истории изменений баланса клиента](pages/get-customer-bonus-balance-history.md)

## Персонализация сайта

- [Базовая интеграция](pages/website-personalization-basic-integration.md)
- [Общая информация](pages/website-personalization.md)
- [Особенности установки виджетов рекомендаций на сайте](pages/website-recommendation-widgets-installation.md)
- [Расширенная интеграция](pages/website-personalization-advanced-integration.md)

### Чеклист проверки интеграции персонализации

- [Виджет рекомендаций не работает по тестовой ссылке](pages/widget-not-working-test-link.md)
- [Механика не работает по тестовой ссылке](pages/mechanics-not-working-test-link.md)
- [Механика персонализации включена, но не показывается клиенту](pages/mechanics-enabled-not-shown.md)
- [Механика персонализации прогружается медленно](pages/mechanics-loads-slowly.md)

- **Механика персонализации отображается, игнорируя условия таргетинга**
  - [Корзина клиента изменилась и не соответствует условиям таргетинга](pages/cart-changed-does-not-match-targeting.md)
  - [Обновление сегмента в таргетинге механики произошло без перезагрузки страницы](pages/segment-updated-without-page-reload.md)
  - [Сайт работает как SPA (сменяет страницы без перезагрузки)](pages/spa-navigation-without-reload.md)
- **Механика персонализации включена, но не показывается клиенту**
  - [В таргетинге указаны противоречивые условия](pages/targeting-conditions-conflict.md)
  - [Завершился АВ-тест через Google Optimize](pages/google-optimize-ab-test-ended.md)
  - [Не передаются данные по странице продукта, категории или продуктам в корзине](pages/targeting-uses-product-conditions-but-data-not-sent.md)
  - [Превышен лимит по показам](pages/impression-limit-exceeded.md)
  - [Устройство не привязано к клиенту, который входит в сегмент таргетинга механики](pages/device-not-linked-to-target-customer.md)
- **Механика не работает по тестовой ссылке**
  - [В механике не указаны необходимые настройки](pages/mechanics-missing-required-settings.md)
  - [В механике указана не та точка интеграции](pages/mechanics-wrong-endpoint.md)
  - [На сайте настроена переадресация](pages/website-has-redirects.md)
  - [Не установлен трекер Mindbox](pages/tracker-not-installed.md)
  - [Некорректно выбрано место отображения](pages/incorrect-display-location.md)
  - [Скрипты персонализации не установлены](pages/scripts-not-installed.md)
  - [Трекер Mindbox установлен некорректно](pages/tracker-installed-incorrectly.md)
- **Виджет рекомендаций не работает по тестовой ссылке**
  - [Не отображается виджет с рекомендациями к категории](pages/widget-not-displayed-for-category.md)
  - [Не отображается виджет с рекомендациями к продукту](pages/widget-not-displayed-for-product.md)
  - [Нет продуктов для рекомендации](pages/no-products-for-recommendation.md)
### Расширенная интеграция

- [Передача данных с бэкенда](pages/website-personalization-backend.md)
- [Передача данных с фронтенда](pages/website-personalization-frontend.md)
- [Проверка расширенной интеграции](pages/verify-advanced-integration.md)

- **Бэкенд**
  - [1. Создание операций для работы с бэкенда](pages/step-1-create-operations-for-backend.md)
  - [2. Вызов операций из бэкенда сайта или из сторонней системы](pages/step-2-call-operations-from-backend-or-external-system.md)
  - [3. Вызов операций для работы персонализации](pages/step-3-call-operations-for-personalization.md)
  - [4. Настройки персонализации сайта в точке интеграции при интеграции с бэкенда](pages/step-4-website-personalization-settings-for-backend-integration.md)
- **Фронтенд**
  - [1. Создание операций для работы с фронтенда](pages/step-1-create-operations-for-frontend.md)
  - [2. Вызов операций с помощью JavaScript SDK Mindbox](pages/step-2-call-operations-with-javascript-sdk.md)
  - [3. Настройки персонализации сайта в точке интеграции](pages/step-3-website-personalization-settings-at-integration-point.md)
### Базовая интеграция

- [1. Установка трекера](pages/tracker-installation.md)
- [2. Создание механики](pages/step-2-run-mechanics.md)
- [3. Подключение модуля](pages/step-3-connect-module.md)
- [4. Проверка базовой интеграции](pages/step-4-verify-basic-integration.md)

### Особенности установки виджетов рекомендаций на сайте

- [Размещения виджета с реко по продукту или категории без расширенной интеграции](pages/widget-placement-without-advanced-integration.md)
- [Размещения виджета с реко по продукту или категории с расширенной интеграцией](pages/widget-placement-with-advanced-integration.md)

## Чат-боты

- [Аутентификация клиента по QR-коду на кассе](pages/chat-bots-qr-authentication.md)
- [Методы для интеграции чат-ботов с Fasttrack](pages/chat-bots-methods.md)
- [Чат-боты. Авторизация клиента по ссылке](pages/chatbot-authorization.md)

## Заказы

- [Изменение заказа](pages/update-order.md)
- [Изменение статуса позиции заказа](pages/update-order-line-status.md)
- [Массовый импорт заказов](pages/retailorder-import-v3.md)
- [Отложенное сохранение заказа (процессинг)](pages/processing-offline-order.md)
- [Оформление заказа](pages/order-checkout.md)
- [Получение информации о заказе](pages/get-order-info.md)
- [Получение общей суммы оплаченных заказов](pages/get-total-paid-orders-amount.md)
- [Получение списка заказов клиента](pages/get-orders-list.md)
- [Получение списка заказов клиента v2.1](pages/get-customer-orders-list.md)
- [Предварительный расчет заказа с процессингом](pages/preorder.md)
- [Расчет цен в каталоге и на карточке товара](pages/processing-calculate-product-list.md)
- [Создание и обновление заказа (Процессинг)](pages/create-order-with-processing.md)

## Экспорты

- [Общий принцип экспортов](pages/exports-overview.md)
- [Экспорт действий клиентов](pages/export-customer-actions.md)
- [Экспорт журнала событий](pages/export-event-log.md)
- [Экспорт заказов и позиций заказов](pages/export-orders-and-lines.md)
- [Экспорт изменения сегментации клиентов](pages/export-customer-segmentation-changes.md)
- [Экспорт изменения сегментации продуктов](pages/export-product-segmentation-changes.md)
- [Экспорт клиентов](pages/export-customers.md)
- [Экспорт клиентов из блоков сценариев](pages/export-customers-from-scenario-blocks.md)
- [Экспорт логов вебхуков](pages/export-webhook-logs.md)
- [Экспорт логов операций](pages/export-operation-logs.md)
- [Экспорт на FTP/SFTP](pages/export-ftps-sftp.md)
- [Экспорт объединений клиентов](pages/export-customer-merges.md)
- [Экспорт отчетов по API](pages/export-api-reports.md)
- [Экспорт промоакций](pages/export-promotions.md)
- [Экспорт рассылок](pages/export-mailings.md)
- [Экспорт статусов рассылок](pages/export-mailing-statuses.md)
- [Экспорт сценариев](pages/export-scenarios.md)

## Рекомендации

- [Получение списка рекомендаций](pages/get-popular-products.md)

## Разное

- [Импорт возможных значений дополнительных полей](pages/import-field-values.md)
- [Интеграция с сервисом SLA](pages/sla-integration.md)

## (Без раздела)

- [[Flutter] [iOS] Быстрая настройка пуш-уведомлений](pages/ios-mindboxflutterappdelegate.md)
- [[Flutter] [iOS] Самостоятельная настройка пуш-уведомлений](pages/flutter-ios-advanced-push-setup.md)
- [[iOS] Быстрая настройка пушей](pages/ios-push-notifications-setup.md)
- [[iOS] Самостоятельная настройка пушей](pages/ios-push-notifications-setup-advanced.md)
- [custom-push-notification-rendering](pages/custom-push-notification-rendering.md)
- [Huawei Push Service](pages/huawei-push-service.md)
- [RuStore Push Service](pages/rustore-push-service.md)
- [test](pages/test.md)
- [Личный кабинет](pages/usercab.md)
- [Лояльность на кассе (v2.1)](pages/loyaloffline.md)
- [Мобильные пуши - SDK](pages/мобильные-пуши-sdk.md)
- [Мультирегиональные проекты](pages/мультирегиональные-проекты.md)
- [Призовые механики](pages/призовые-механики.md)
- [Реализация сервиса для подключения Firebase](pages/firebase-integration-service-implementation.md)
- [Рекомендации](pages/recommendation.md)
- [Стандартные интеграции](pages/стандартные-интеграции-1.md)
