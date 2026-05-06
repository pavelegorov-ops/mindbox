---
title: Интеграция с Yandex.Forms
slug: "yandex-forms-integration"
source_url: "https://help.mindbox.ru/docs/yandex-forms-integration"
vcs_path: "yandex-forms-integration.md"
toc_path:
  - Операции и интеграция
  - Дополнительные возможности
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:d04b585efc3f68583204055436808c3ca4384dfeb11c0ba46d0fbc83958e7083"
---

# Интеграция с Yandex.Forms

Яндекс.Формы можно использовать для разных задач: сбора заявок на сайте, проведения опросов и тестирований, регистраций на мероприятия и т.д.

В данной инструкции рассмотрим, как настроить передачу данных из Яндекс.Формы в Mindbox.

## Настройки в Mindbox

1. Создайте новую [интеграцию](%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D1%87%D0%BA%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8.md) для Yandex Forms с типом «Другое»:

![yandexforms-intergation-endpoint1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-intergation-endpoint1.png)

2. При необходимости создайте [дополнительные поля](additional-data.md) для записи ответов из формы.

Тип поля может быть любым.

Сущность поля также выбирайте исходя из задачи:

- **По клиенту** — если нужно зафиксировать информацию в профиле и использовать ее в дальнейшем для сегментирования. Например, тип кожи, размер одежды, любимый производитель и т.д:

![yandexforms-integration-customfield-skintype.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-customfield-skintype.png)

- **По действию** — если нужно зафиксировать событие, например, прохождение NPS-опроса:

![yandexforms-integration-customfield-npsopros.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-customfield-npsopros.png)

2.1. При передаче данных в дополнительное поле к действию клиента можно [создать новый шаблон](template-action.md) или переиспользовать существующий:

![yandexforms-integration-actiontemplate-nps.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-actiontemplate-nps.png)

3. Создайте [операцию](%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-v-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F.md) для передачи данных.

- Проставьте флаг «Операция требует передачи секретного сервисного ключа».
- Выберите нужный шаг для [создания](steps-create-client.md) или [редактирования/дополнения](steps-edit-client.md) клиента в зависимости от того, как и какие поля должны быть записаны.
- Чтобы передать данные в дополнительное поле к действию, вторым шагом выберите «Действие — Выдать» с ранее созданным шаблоном.

Пример операции:

![yandexforms-integration-operation-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-operation-example.png)

## Настройки в Yandex.Forms

1. Создайте [форму опроса](https://forms.yandex.ru/admin/). Выберите блоки, которые будут присутствовать в форме:

![yandexforms-intagration-yandex-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-intagration-yandex-example.png)

2. Перейдите в раздел «Интеграции». В конце страницы выберите «API» → «Запрос заданным методом»:

![yandexforms-integration-zapros-api.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-zapros-api.png)

3. Настройте данные для запроса. Используйте спецификацию ранее созданной операции:

![yandexforms-integration-request-body-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-request-body-example.png)

- **URL** — укажите, как будет вызываться операция: синхронно или асинхронно; в endpointId пропишите системное имя созданной интеграции.
- **Метод запроса** — POST.
- **Тело запроса** — пропишите согласно спецификации в зависимости от того, какие поля будут передаваться в Mindbox.

С помощью переменных задайте, какие данные из формы должны подставиться в определенный узел запроса. Для этого выделите нужное значение → нажмите на значок плюса в правом верхнем углу → выберите «Ответ на вопрос»:  
![yandexforms-integrations-answer1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integrations-answer1.png)

В выпадающем списке выберите нужный вопрос и сохраните изменения:

![yandexforms-integration-answer2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-answer2.png)

- **Заголовки** — секретный ключ берется из созданной интеграции.

4. Сохраните изменения в блоке «Интеграция» и опубликуйте форму.
5. Заполните форму, чтобы протестировать передачу данных на проект. Результаты можно отследить в [логах интеграций](operation-logs.md), а также проверить создание или редактирование клиента в его карточке.

Пример клиента, добавленного из формы:

![yandexforms-integration-clientcard.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/yandexforms-integration-clientcard.png)
