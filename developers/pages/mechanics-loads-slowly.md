---
title: Механика персонализации прогружается медленно
slug: "mechanics-loads-slowly"
source_url: "https://developers.mindbox.ru/docs/mechanics-loads-slowly"
breadcrumb:
  - Персонализация сайта
  - Чеклист проверки интеграции персонализации
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:8aed23c3bf9045826e5ddfcc3a00db0f48617ba20791d39415823062bdd82751"
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
