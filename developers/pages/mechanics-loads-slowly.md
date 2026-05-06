---
title: Механика персонализации прогружается медленно
slug: "mechanics-loads-slowly"
source_url: "https://developers.mindbox.ru/docs/mechanics-loads-slowly"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:b7ad7fcf46efa6034371e19f3fd31a505da353869d0911a6ac47edda845eeddb"
---

# Механика персонализации прогружается медленно

**Как исправить**

Убедитесь, что:

- подключение скрипта прописано в head корневого html документа сайта

```
DOCTYPE html>
<html>
    <head>
				...
		    <script>
				    mindbox = window.mindbox || function() { mindbox.queue.push(arguments); };
				    mindbox.queue = mindbox.queue || [];
				    mindbox('create', {
				        endpointId: '<Идентификатор точки интеграции>'
				    });
				script>
				<script src="https://api.mindbox.ru/scripts/v1/tracker.js" async>script>
				...
		head>
		...
html>
```

- при наличии на проекте нескольких точек интеграций `endpointId` сайта явно передается в `mindbox('create')`
- перед подключением tracker.js нет скриптов, подключаемых без async
