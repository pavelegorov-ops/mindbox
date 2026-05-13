---
title: Размещения виджета с реко по продукту или категории без расширенной интеграции
slug: "widget-placement-without-advanced-integration"
source_url: "https://developers.mindbox.ru/docs/widget-placement-without-advanced-integration"
breadcrumb:
  - Персонализация сайта
  - Особенности установки виджетов рекомендаций на сайте
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:011d53649bab09104a5530219d85df9315b6818132dd21f533a04880f0f87e1e"
---

# Размещения виджета с реко по продукту или категории без расширенной интеграции

Если расширенная интеграция не реализована, для корректной работы виджетов, где рекомендации формируются к товарам или категориям, понадобится дополнительно передавать `data-popmechanic-argument`

```
<div data-popmechanic-embed="{Ваш id}" data-popmechanic-argument="{ID продукта}">div>
```

```
<div data-popmechanic-embed="{Ваш id}" data-popmechanic-argument="{ID категории}">div>
```
