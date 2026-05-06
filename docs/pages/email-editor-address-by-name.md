---
title: Обращение по имени (новый конструктор)
slug: "email-editor-address-by-name"
source_url: "https://help.mindbox.ru/docs/email-editor-address-by-name"
vcs_path: "email-editor-address-by-name.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:af612758cf6fb6b53203fa9c8232feb37d57922e1e6ef69dfd7cf0905fe96fb2"
---

# Обращение по имени (новый конструктор)

[Новый конструктор](email-editor.md) email-рассылок позволяет обратиться к пользователю по имени, если оно заполнено, без использования кода и [параметров](%D0%BA%D0%B0%D0%BA-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C%D1%81%D1%8F-%D0%BF%D0%BE-%D0%BF%D0%BE%D0%BB%D1%83-%D1%81-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8-%D0%B5%D1%81%D0%BB%D0%B8-%D0%BE%D0%BD%D0%BE-%D0%B5%D1%81%D1%82%D1%8C.md).

---

1. В нужном поле нажмите [Добавить переменную](new-builder-personalize.md) → «Обращение по имени»:

   ![email-editor-address-by-name1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-address-by-name1.png)
2. Заполните текст для вывода при наличии и отсутствии имени; выберите регистр:

   - как записано в профиле клиента;
   - заглавные буквы (аналог [функции](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.md) `ToUpper`)
   - первая буква заглавная (аналог [функции](%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.md) `Capitalize`)

   Проверяется не только заполнение, но и наличие в списке стандартных имен (аналог параметра `Recipient.OnlyStandardFirstName`)

   ![email-editor-address-by-name2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-address-by-name2.png)
3. Нажмите «Добавить».

---

Готово:

![email-editor-address-by-name3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-address-by-name3.png)
