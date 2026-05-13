---
title: Добавление SDK в приложение
slug: "add-sdk-react-native"
source_url: "https://developers.mindbox.ru/docs/add-sdk-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:751f1abdbdb9ad6760f74260911f1aa5761099d31fe45d66f4684b7b8710eeb0"
---

# Добавление SDK в приложение

### Результат шага «Добавление SDK в приложение»:

в файле `package.json` в блоке `dependencies` появилась строка `mindbox-sdk`.

```
"dependencies": {
    "@react-navigation/native": "^6.0.4",
    "mindbox-sdk": "{последняя актуальная версия}",
    "react": "18.2.0",
    "react-native": "0.72.7"
  }
```

---

## Добавление плагина в приложение.

В файл `package.json` добавить зависимость на плагин.

Можете указать фиксированную версию, чтобы контролировать обновления. Актуальную версию вы можете посмотреть [тут](https://www.npmjs.com/package/mindbox-sdk).

```
npm i --save mindbox-sdk
```
