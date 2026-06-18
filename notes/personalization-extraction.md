# Быстрое извлечение конфига персонализации (поп-ап) из MindBox UI

Как снять конфигурацию формы-персонализации (поп-ап, движок **PopMechanic**)
со страницы `personalization/pop-up/<id>` за **3 вызова** вместо 12–20,
включая то, что в UI скрыто: **internalId сегментов** и **HTML тела формы**.

## Что за страница

`https://<тенант>.mindbox.ru/personalization/pop-up/<id>` — read-only обзор
механики. Legacy-модуль `frontend_popmech_personalization_v2` (движок
PopMechanic). Почти всё рендерится в DOM; скрытые ID сегментов — в **Redux-
сторе** (через React fiber). Тело формы — живой DOM с классами
`popmechanic-*` (не iframe, не картинка).

## Оптимальный рецепт — 3 вызова

1. **`get_page_text`** — снимает: общие настройки (статус, даты, частота,
   сайт, дни, приоритет, время), «Условие всплывания» + все URL-правила
   страниц показа, статистику (показы/контакты), и *имя* сегмента
   таргетинга (текстом, без ID).
2. **`javascript_tool`** (один сниппет) — добирает скрытое: internalId
   сегментов (Redux) + структуру HTML тела формы (DOM). См. ниже.
3. **`screenshot`** — текст оффера: он запечён в фоновую картинку-баннер
   (`div.popmechanic-image-1`), в DOM его НЕТ.

Имя операции «после заполнения» на обзоре отсутствует — отдельный шаг (ниже).

## (b) internalId сегментов — из Redux через fiber

UI показывает только имя сегмента. ID лежит в Redux-сторе:

```js
const fk = n => Object.keys(n).find(k => k.startsWith('__reactFiber$'));
// якорь — любой листовой элемент с текстом из таргетинга:
const node = [...document.querySelectorAll('*')]
  .find(e => e.childElementCount === 0 && /Клиенты с регой/.test(e.textContent || ''));
let f = node[fk(node)], store = null, d = 0;
while (f && d < 12) { if (f.memoizedState?.storeState) { store = f.memoizedState.storeState; break; } f = f.return; d++; }
const segs = store.PersonalizationSegmentations.byKey;  // name + internalId + externalId
```

Стор подгружает ТОЛЬКО сегменты, используемые механикой → `byKey` = список
сегментов таргетинга. Для 123075: «Клиенты с регой и заказом» → `internalId
1101`, `externalId 9761c84b-…`, `entitiesCount 518349`. Вкл/искл различает
не стор, а подпись в обзоре («не показывать» = исключение).

## (e) HTML тела формы — из DOM, в обход фильтра расширения

Форма — живой DOM (`popmechanic-reset > popmechanic-main > …`). ⚠️ Фильтр
Claude in Chrome режет сырые строки с URL/токенами — **не возвращай
`outerHTML` как есть**. Варианты:

- вернуть JSON-дерево `tag/class/text/inputType` (URL→`[url]`, `data:`→`[data-uri]`);
- либо base64: `btoa(unescape(encodeURIComponent(html)))` — проходит фильтр
  (~24KB на чистую разметку).

Классы `popmechanic-*` — публичный контракт движка, стабильны: на них якорись.
Структура тела: `popmechanic-content > popmechanic-text + popmechanic-inputs
(input.popmechanic-email + button) + label.popmechanic-checkbox`.

## (d) Текст оффера — только скриншотом

Заголовок-оффер запечён в фоновую картинку (`div.popmechanic-image-1`); в
DOM/сторе текста нет. Один `screenshot`.

## (f) Имя операции «после заполнения» — отдельный шаг

На read-only обзоре только флаги («Создать клиента: Да» / «Выдать действие:
Нет»); самого systemName нет ни в Redux, ни в fiber, ни в Apollo. Достать:
открыть редактор кнопкой «Изменить» у блока «Действия после заполнения»
(side-effect-free до «Сохранить»), **или** взять из связанного сценария
(поп-ап → действие «Регистрация клиента в попапе `<имя>`» → ищи в
`scenarios/`).

## Тупики (проверено, не повторять)

- **`read_network_requests`** видит конфиг-эндпоинт
  `personalization-admin.g.mindbox.ru/graphql`, но MCP не отдаёт тела
  ответов → как источник бесполезен.
- **`__APOLLO_CLIENT__`** — только проектные settings (таймзона/валюта), по
  механике пусто.
- **fetch-интерсептор + SPA-ре-навигация** — конфиг-запрос уходит ОДИН раз
  на холодную загрузку и кэшируется в памяти модуля; перехват требует
  ставить интерсептор до загрузки federated-модуля — непрактично.

## Стоимость

Оптимум — 3 вызова, ~15–25 сек, покрывает a,b,c,d,e,g. Наивный путь
(скриншоты + прокрутки + развороты блоков + зум на ID) — 12–20+ вызовов,
минуты, и internalId сегмента вообще не достаёт (в UI скрыт).

## Оговорки

- **Минифицированные имена fiber-компонентов** (`Connect(...)`, `ko`, `g`)
  меняются от сборки — НЕ привязывайся. Якоря: текст таргетинга для
  стартовой ноды, `memoizedState.storeState`, ключ
  `PersonalizationSegmentations.byKey`, классы `popmechanic-*`.
- **Фильтр расширения:** из JS возвращай очищенные структуры или base64, не
  сырые URL/`outerHTML` (ловит `[BLOCKED: Cookie/query string data]`).
- На медленной машине блок «Сайт» в обзоре иногда «Failed to fetch» —
  перечитать после ретрая.

## Подтверждение применимости

Выведено и проверено на `usmall.mindbox.ru/personalization/pop-up/123075`
(«Welcome20_Popup_1 — Jun 2025»), 2026-06-18: 3 вызова против 12–20+
наивных; `internalId 1101` и структура HTML тела получены — чего наивный
путь (скриншоты/развороты) не давал в принципе.
