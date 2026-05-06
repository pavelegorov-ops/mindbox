---
title: Размещения виджета с реко по продукту или категории без расширенной интеграции
slug: "widget-placement-without-advanced-integration"
source_url: "https://developers.mindbox.ru/docs/widget-placement-without-advanced-integration"
breadcrumb:
  - Персонализация сайта
  - Особенности установки виджетов рекомендаций на сайте
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:1e3586ae1f4b3ede42a00d36cec6b6adc1f98ef57312d3cd795ee10e1e036265"
---

# Размещения виджета с реко по продукту или категории без расширенной интеграции

Если расширенная интеграция не реализована, для корректной работы виджетов, где рекомендации формируются к товарам или категориям, понадобится дополнительно передавать `data-popmechanic-argument`

```
<div data-popmechanic-embed="{Ваш id}" data-popmechanic-argument="{ID продукта}">div>
```

```
<div data-popmechanic-embed="{Ваш id}" data-popmechanic-argument="{ID категории}">div>
```
