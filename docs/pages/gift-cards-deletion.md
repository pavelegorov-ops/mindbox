---
title: Как удалить подарочные карты
slug: "gift-cards-deletion"
source_url: "https://help.mindbox.ru/docs/gift-cards-deletion"
vcs_path: "gift-cards-deletion.md"
toc_path:
  - Лояльность и акции
  - Подарочные карты
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:c1025e5a7b1a82e43d3e9ce84a1055a2491a2bd64f1c6050db9162d6f559fe1d"
---

# Как удалить подарочные карты

Когда необходимо удаление подарочных карт:

- карты импортированы **с неверным номиналом**
- карты импортированы **в неверный пул**
- в проект добавлены тестовые карты
- требуется очистить пул перед повторным импортом корректных данных (с новыми номерами)

Удаление карт происходит безвозвратно.

## Ограничения

Удаление возможно только для карт, по которым **нет действий**:

- Продажи подарочной карты
- Заказов с оплатой подарочной картой

Прежде чем удалить карты, удалите все связанные с ними заказы.

### Как найти действия с картами

Перейдите в раздел Данные → Действия.

Воспользуйтесь одним из фильтров для поиска действий:

1. Все действия продажи карты из пула:  
   ![gift-cards-deletion-filter1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-filter1.png)
2. Все действия покупок с помощью подарочных карт из пула:  
   ![gift-cards-deletion-filter2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-filter2.png)
3. Все действия покупок с помощью подарочной карты определенного номера:  
   ![gift-cards-deletion-filter3.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-filter3.png)

## Удаление подарочных карт

1. Перейдите в раздел **Кампании → Лояльность → Пул подарочных карт**. Нажмите «Перейти ко всем подарочным картам», чтобы перейти к списку карт:

   ![Снимок экрана 2024-01-16 в 18.21.37.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-01-16%20%D0%B2%2018.21.37.png)
2. Нажмите на **«Импорт»**:

   ![Снимок экрана 2024-01-16 в 18.20.59.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-01-16%20%D0%B2%2018.20.59.png)
3. Выберите операцию «Удаление подарочных карт» и подготовьте файл. На странице доступен шаблон с примером:

   ![gift-cards-deletion-operation.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-operation.png)
4. Загрузите подготовленный файл и запустите задачу:

   ![gift-cards-deletion-upload.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-upload.png)

### Поля для заполнения

| Поле | Описание | Обязательно |
| --- | --- | --- |
| PoolSystemName | Системное имя пула | Да |
| Number | Номер подарочной карты | Да |

[**Как найти системное имя пула**](gift-cards-deletion.md#pool-system-name)

1. Через список **Кампании → Лояльность → Пул подарочных карт**:  
   ![gift-cards-pool-system-name1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-pool-system-name1.png)
2. Через данные подарочной карты:  
   ![gift-cards-pool-system-name2.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-pool-system-name2.png)

### Пример заполненного файла

| PoolSystemName | Number |
| --- | --- |
| Gift1000CVV3y | GC1000001 |
| Gift1000CVV3y | GC1000002 |
| GiftOpenAmount3y | GC2000001 |

[Пример в виде строки с разделителем](gift-cards-deletion.md#file-example)

```
PoolSystemName;Number;
Gift1000CVV3y;GC1000001;
Gift1000CVV3y;GC1000002;
GiftOpenAmount3y;GC2000001;
```

## Результат выполнения

Проверьте результат выполнения по ссылке на задачу:

![gift-cards-deletion-task.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-task.png)

Пример успешной задачи:

![gift-cards-deletion-complete.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-complete.png)

### Частые ошибки

Если задача завершилась ошибкой, скачайте файл результата для просмотра ошибки.

![gift-cards-deletion-error.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/gift-cards-deletion-error.png)

|  |  |
| --- | --- |
| **Ошибка** | **Решение** |
| Подарочная карта не найдена | Проверьте корректность номера карты |
| Пул не найден | Проверьте корректность [системного имени пула](gift-cards-deletion.md#pool-system-name) |
| Нельзя удалить карту, есть заказ в котором она продана | Проверьте наличие действий продажи карты или заказов с оплатой по карте по [инструкции](gift-cards-deletion.md#kak-najti-dejstviya-s-kartami) |
