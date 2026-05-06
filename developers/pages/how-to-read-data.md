---
title: Как прочитать данные
slug: "how-to-read-data"
source_url: "https://developers.mindbox.ru/docs/how-to-read-data"
breadcrumb:
  - Данные для аналитики
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:e0a6f8110673cf57e4ef66587c419bd12f22776bd9d1636533caaa0f25106a38"
---

# Как прочитать данные

## Общий принцип

История данных (за исключением удаленных) проекта доступна для чтения с помощью интеграции [Данные для аналитики](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%8D%D0%BA%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B8).

Данные хранятся в delta-формате в parquet-файлах. Обновление данных происходит к 00:00 UTC ежедневно. Получение доступа к данным происходит по протоколу delta-sharing — это open-source протокол для обмена большим объемом данных, с его документацией можно ознакомиться [здесь](https://github.com/delta-io/delta-sharing/blob/main/README.md). Можно воспользоваться REST API или готовыми библиотеками для python.

Для доступа к данным нужны секретный ключ и URL сервиса созданной интеграции «Данные для аналитики».

Ниже подробнее описаны методы получения данных по REST API и методы python из библиотеки delta-sharing.

### Особенности и ограничения интеграции

- Можно создать не более одной интеграции;
- Данные для аналитики обновляются раз в сутки к 00:00 UTC;
- Можно запросить не более 10 версий данных за один запрос. Передача параметров **startingVersion** и **endingVersion** обязательна;
- Данные из автоудаления попадают в аналитику, удаленные вручную данные будут помечены флагом _*isDeleted = TRUE*;
- Точность данных для аналитики составляет 99%. Это означает, что не менее 99% данных, которые есть на проекте, доступны для экспорта.

### Зашифрованные данные

В некоторых таблицах данные шифруются. Для расшифровки потребуется Ключ шифрования

**Ключ шифрования:** можно посмотреть в административной панели Mindbox в [настройках интеграции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%8D%D0%BA%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B8)

Пример скрипта на Python для расшифровки нужных колонок

```
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM # Имплементация AESGCM на питоне, библиотека cryptography

def decrypt(encrypted_data_b64: str, master_key_b64: str) -> str:

    # Декодируем входные параметры из Base64
    encrypted_data = base64.b64decode(encrypted_data_b64)
    master_key = base64.b64decode(master_key_b64)

    NONCE_SIZE = 12  # Размер nonce для AES-GCM

    key_nonce = encrypted_data[0:NONCE_SIZE]       # nonce для расшифровки data_key
    value_nonce = encrypted_data[NONCE_SIZE:NONCE_SIZE*2]  # nonce для расшифровки значения
    encrypted_data_key = encrypted_data[24:72]     # зашифрованный data_key
    encrypted_value = encrypted_data[72:]          # зашифрованное значение

    # Расшифровка data_key, используя master_key (Ключ шифрования со страницы интеграции)
    aesgcm_master = AESGCM(master_key)
    data_key = aesgcm_master.decrypt(key_nonce, encrypted_data_key, associated_data=None)

    # Расшифровка значения, используя data_key
    aesgcm_data_key = AESGCM(data_key)
    decrypted_value = aesgcm_data_key.decrypt(value_nonce, encrypted_value, associated_data=None)

    return decrypted_value.decode("utf-8")
```

## REST API

### Общая информация

- share — логическая группировка схем, по сути — БД. На данный момент существует одна - “exports”;
- schema — логическая группа таблиц. На данный момент существуют следующие группы: CDP, ProcessingOrders, Mailings, AbTests
- table — [Delta Lake](https://delta.io/) таблица или представление.

### Метод для получения доступных БД

**Метод**

*GET {URL сервиса}/shares*

**Заголовки**

- Authorization: Bearer {token}

**QueryString параметры**

- **maxResults** (type: Int32, optional): Максимальное количество БД, которые будут возвращены в ответе. Если существует больше БД, чем указано в maxResults, то в ответе будет получен параметр nextPageToken - токен следующей страницы
- **pageToken** (type: String, optional): Передайте в параметре токен страницы

#### **Пример ответа**

**Заголовки**

- Content-Type: application/json; charset=utf-8

**Тело**

```
{
  "items": [
    {
      "name": "string",
      "id": "string"
    }
  ],
  "nextPageToken": "string"
}
```

`items` - массив доступных БД. Может быть пустым

`nextPageToken` - токен следующей страницы

### Метод для получения доступных схем

**Метод**

*GET {URL сервиса}/shares/{share}/schemas*

**Заголовки**

- Authorization: Bearer {token}

**Параметры запроса**

- {share} - название БД

**QueryString параметры**

- **maxResults** (type: Int32, optional): Максимальное количество схем, которые будут возвращены в ответе. Если существует больше схем, чем указано в maxResults, то в ответе будет получен параметр nextPageToken - токен следующей страницы
- **pageToken** (type: String, optional): Передайте в параметре токен страницы

#### **Пример ответа**

**Заголовки**

- Content-Type: application/json; charset=utf-8

**Тело**

```
{
  "items": [
    {
      "name": "string",
      "share": "string"
    }
  ],
  "nextPageToken": "string"
}
```

`items` - массив доступных схем. Может быть пустым

`name` - имя схемы

`share` - имя БД, которой принадлежит схема

`nextPageToken` - токен следующей страницы

### Метод для получения таблиц в схеме

**Метод**

*GET {URL сервиса}/shares/{share}/schemas/{schema}/tables*

**Заголовки**

- Authorization: Bearer {token}

**Параметры запроса**

- {share} - название БД
- {schema} - название схемы

**QueryString параметры**

- **maxResults** (type: Int32, optional): Максимальное количество схем, которые будут возвращены в ответе. Если существует больше схем, чем указано в maxResults, то в ответе будет получен параметр nextPageToken - ссылка на следующую страницу
- **pageToken** (type: String, optional): Передайте в параметре токен страницы

#### **Пример ответа**

**Заголовки**

- Content-Type: application/json; charset=utf-8

**Тело**

```
{
  "items": [
    {
      "name": "string",
      "schema": "string",
      "share": "string",
      "shareId": "string",
      "id": "string"
    }
  ],
  "nextPageToken": "string"
}
```

`items` - массив доступных схем. Может быть пустым

`name` - имя таблицы

`schema` - имя схемы, которой принадлежит таблица

`share` - имя БД, которой принадлежит схема

`id` - идентификатор таблицы

`nextPageToken` - токен следующей страницы

### Метод для получения таблиц в БД

**Метод**

*GET {URL сервиса}/shares/{share}/all-tables*

**Заголовки**

- Authorization: Bearer {token}

**Параметры запроса**

- {share} - название БД

**QueryString параметры**

- **maxResults** (type: Int32, optional): Максимальное количество схем, которые будут возвращены в ответе. Если существует больше схем, чем указано в maxResults, то в ответе будет получен параметр nextPageToken - ссылка на следующую страницу
- **pageToken** (type: String, optional): Передайте в параметре токен страницы

#### **Пример ответа**

**Заголовки**

- Content-Type: application/json; charset=utf-8

**Тело**

```
{
  "items": [
    {
      "name": "string",
      "schema": "string",
      "share": "string",
      "shareId": "string",
      "id": "string"
    }
  ],
  "nextPageToken": "string"
}
```

`items` - массив доступных схем. Может быть пустым

`name` - имя таблицы

`schema` - имя схемы, которой принадлежит таблица

`share` - имя БД, которой принадлежит схема

`id` - идентификатор таблицы

`nextPageToken` - токен следующей страницы

### Метод для получения файлов в таблице

**Метод**

*GET {URL сервиса}/shares/{share}/schemas/{schema}/tables/{table}/changes*

**Заголовки**

- Authorization: Bearer {token}

**Параметры запроса**

- {share} - название БД
- {schema} - название схемы
- {table} - название таблицы

**QueryString параметры**

- **startingVersion** (type: Long): стартовая версия, с которой нужно получить данные. Обязательный параметр
- **endingVersion** (type: Long): финальная версия, по которую нужно получить данные. Обязательный параметр

#### **Пример ответа**

**Заголовки**

- Content-Type: application/json; charset=utf-8

**Тело**

```
{
    "protocol": {
        "minReaderVersion": 1
    }
}
{
    "metaData": {
        "id": "ec1809ba-0be9-4f3a-b004-8bd20712c3e8",
        "format": {
            "provider": "parquet"
        },
        "schemaString": "{\"type\":\"struct\",\"fields\":[{\"name\":\"internalId\",\"type\":\"string\",\"nullable\":false,\"metadata\":{}},{\"name\":\"id\",\"type\":\"integer\",\"nullable\":true,\"metadata\":{}},{\"name\":\"name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"systemName\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"description\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"_tenant\",\"type\":\"string\",\"nullable\":false,\"metadata\":{}},{\"name\":\"_isDeleted\",\"type\":\"boolean\",\"nullable\":true,\"metadata\":{}},{\"name\":\"_rowversion_ts\",\"type\":\"timestamp\",\"nullable\":false,\"metadata\":{}}]}",
        "configuration": {
            "enableChangeDataFeed": "true"
        },
        "partitionColumns": [
            "_tenant"
        ],
        "version": 4
    }
}
{
    "add": {
        "url": "https://data-mesh-exports-production.storage.yandexcloud.net/stable/exports/Balances/_tenant%3DTenant/part-00067-191b93f1-c8d7-4300-aef8-03a8d4608a3a.c000.snappy.parquet?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240819T074744Z&X-Amz-SignedHeaders=host&X-Amz-Expires=36000&X-Amz-Credential=YCAJEtjPkLj9KXZ69Fc2yqrz0%2F20240819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b52b400427e276ba2f07d0d3f08ccac967fc1cea852d1ba532f6f22f03a692b6",
        "id": "9ae10c0ff8387ea00f7387b70a5d85ee",
        "partitionValues": {
            "_tenant": "Mindbox"
        },
        "size": 2281,
        "expirationTimestamp": 1724089664079,
        "version": 4,
        "timestamp": 1723720346485,
        "stats": "{\"numRecords\":3,\"minValues\":{\"internalId\":\"1\",\"id\":1,\"name\":\"Основной счет\",\"systemName\":\"MainAccount\",\"_rowversion_ts\":\"2024-08-15T07:55:36.790Z\"},\"maxValues\":{\"internalId\":\"2\",\"id\":2,\"name\":\"Дополнительный счет\",\"systemName\":\"AdditionalAccount\",\"_rowversion_ts\":\"2024-08-15T07:55:36.790Z\"},\"nullCount\":{\"internalId\":0,\"id\":0,\"name\":0,\"systemName\":0,\"description\":3,\"_isDeleted\":3,\"_rowversion_ts\":0}}"
    }
}
```

Первый JSON объект в ответе содержит информацию о протоколе.

Второй JSON объект в ответе содержит информацию о метаданных таблицы:

- `schemaString` - схема таблицы
- `version` - максимальная версия данных в таблице. При этом таблица обновляется каждый день, то есть версия таблицы увеличивается на один. Если за какой-то день не было событий, то данных в версии не будет.

Третий JSON объект в ответе содержит:

- `url` - подписанная ссылка на файл формата parquet с данными (подпись живет 10 минут)
- `size` - размер файла (в байтах)
- `version` - версию данных в файле
- `timestamp` - время подписи файла
- `expirationTimestamp` - время истечения подписи

## Python коннектор

Подробнее со спецификацией методов можно ознакомиться [здесь](https://github.com/delta-io/delta-sharing/blob/main/README.md).

### Не поддерживается чтение всей таблицы сразу

Так как таблицы могут быть большого размера, то не поддерживаются методы для чтения всей таблицы: load_as_pandas и load_as_spark

Коннектор получает доступ к данным с помощью файла профиля Profile.json с учетными данными для подключению к сервису.

### Как выглядит файл Profile.json

С помощью этого файла аутентифицируемся в delta-sharing сервисе. Формат файла:

```
{
    "shareCredentialsVersion": 1,
    "endpoint": "URL сервиса",
    "bearerToken": "секретный ключ"
}
```

**URL сервиса:** можно посмотреть URL в административной панели Mindbox в [настройках интеграции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%8D%D0%BA%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B8)

**Секретный ключ:** можно посмотреть или сбросить секретный ключ в административной панели Mindbox в [настройках интеграции](https://help.mindbox.ru/docs/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%8D%D0%BA%D1%81%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B8)

**shareCredentialsVersion:** сейчас используется 1 версия. Если будет изменен формат файла с учетными данными, то будет возвращена соответствующая ошибка.

### Чтение данных

Чтобы получить список доступных таблиц с данными можно использовать следующий код:

```
import delta_sharing
from delta_sharing.protocol import DeltaSharingProfile, CdfOptions
from delta_sharing.rest_client import DataSharingRestClient

share_file_path = {путь к файлу} + "/Profile.json" # задаем путь к файлу с учетными данными для подуключения

client = delta_sharing.SharingClient(share_file_path) # создаем клиент для чтения данных

print(client.list_all_tables()) # отображаем все, что в хранилище есть: все БД / схемы / таблицы
```

Получение доступа к данным осуществляется с помощью создания REST клиента, который получает доступ к изменениям таблицы:

```
import delta_sharing
from delta_sharing.protocol import DeltaSharingProfile, CdfOptions
from delta_sharing.rest_client import DataSharingRestClient

share_file_path = {путь к файлу} + "/Profile.json" # задаем путь к файлу с учетными данными для подуключения

profile = DeltaSharingProfile.read_from_file(share_file_path) # создаем профиль, с которым будем создавать rest клиент

rest_client = DataSharingRestClient(profile) # создаем rest клиент

table = delta_sharing.Table(share="название БД", schema="название схемы", name="название таблицы") # создаем таблицу, из которой будем читать

# Обратите внимание, что указание версий при чтении обязательно
res = rest_client.list_table_changes( 
	table,
	cdfOptions=CdfOptions(starting_version=0, ending_version=10)
) # читаем изменения таблицы от 0-ой до 10-ой версий
```

Переменная res содержит массив actions, который содержит ссылки на parquet файлы с изменениями таблицы. Далее можно работать с этими файлами, прочитав их в датафрейм.

### Чтение данных с помощью spark

Также прочесть данные можно с помощью spark

### Не поддерживается чтение всей таблицы сразу

Обратите внимание, что для чтения используется опция readChangeFeed - чтение изменений в таблице

```
import delta_sharing
from pyspark.sql import SparkSession
import pathlib

# Создание SparkSession
spark = (
    SparkSession.builder.config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-azure:3.3.1,io.delta:delta-core_2.12:2.2.0,io.delta:delta-sharing-spark_2.12:3.2.0",
    )
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

share_file_path = str(pathlib.Path().resolve()) + "/Profile.json" # аутентифицируемся

table_url = share_file_path + "#exports.ProcessingOrders.BonusPointChanges" # указываем путь к интересующей нас таблице

# Записываем данные версий 1 и 2 в spark датафрейм shared_df
shared_df = (
    spark.read.format("deltaSharing")
    .option("readChangeFeed", "true")
    .option("startingVersion", 1)
    .option("endingVersion", 2)
    .load(table_url)
)
```

Полный пример кода для чтения данных и сохранения их в dwh смотрите [здесь](periodic-data-updates.md).
