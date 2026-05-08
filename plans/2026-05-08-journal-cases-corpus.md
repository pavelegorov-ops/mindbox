# Добавить корпус кейсов журнала MindBox

## Контекст

В проекте mindBox уже зеркалится один раздел журнала — учебные материалы
из `https://mindbox.ru/journal/education/`. Скрейпер `scripts/scrape_journal.py`
живёт в репо, выходит в плоскую папку `journal/`, регистрируется в
`scripts/sync.py` и упоминается в `CLAUDE.md`, `WELCOME.md`,
`journal/CLAUDE.md` и команде `/sync-docs`.

Пользователь хочет добавить второй раздел — **кейсы** из
`https://mindbox.ru/journal/cases/<slug>/` — и работать с ними так же,
как с учебными материалами (но с чуть более подробной формулировкой
ответа человеку: можно перечислить ключевые механики из кейса с
обязательным `source_url`, тело статьи всё равно не пересказывать).

Подтверждённые факты (после двух Explore-проходов и проверки sitemap):

- Скрейпер уже принимает `--section <name>` и фильтрует
  `https://mindbox.ru/sitemap.xml` по регексу `/journal/<section>/<slug>/`.
  Для cases этот регекс работает без правок (URL шаблон совпадает с
  education).
- Внутренние ссылки в Markdown переписываются только для статей
  *той же* секции; кросс-секционные остаются абсолютными — это нас
  устраивает.
- На текущий момент скрейпер пишет всё (pages, manifest.json,
  summaries.json, INDEX.md, index/by-tag/) в `<out>/`, без вложенности
  по секциям. Если запустить второй раз с `--section cases` в тот же
  `--out`, манифесты затрут друг друга. Это нужно поправить.
- В `scripts/sync.py:40-44` есть статический список SCRAPERS; журнальный
  скрейпер вызывается один раз с дефолтным `--section education`.

Решения, согласованные с пользователем:

- **Layout**: вложенный `journal/<section>/`. Существующее содержимое
  `journal/` мигрируется в `journal/education/`. Кейсы лежат в
  `journal/cases/`. Будущие секции добавляются однотипно.
- **Scope**: только cases в этой итерации. Прочие секции (events,
  course, news, podcast) — отдельно, если понадобится.
- **Правило ответа агента для cases**: «чуть подробнее, чем education» —
  можно перечислить ключевые механики и результат, но обязательно с
  `source_url` и без полного пересказа.

## Критичные файлы

- `scripts/scrape_journal.py` — переключить выход на `<out>/<section>/`.
  Целевая правка: `out_dir = Path(args.out) / args.section` (≈ строка
  581 по результатам Explore). Все пути ниже (pages dir, manifest,
  summaries, INDEX, index/by-tag/) собираются от `out_dir` — нужно
  убедиться этому грепом перед правкой: **пройти по файлу `args.out`**
  и подтвердить, что после правки нет ни одного употребления, которое
  бы пропустило подкаталог секции (например, в логах или метаданных
  манифеста). URL-фильтр, парсинг HTML и схема frontmatter
  не меняются.
- `scripts/sync.py` — расширить запись в SCRAPERS, чтобы передавать
  per-entry дополнительные аргументы и зарегистрировать обе секции
  как отдельные шаги:

  ```python
  SCRAPERS: list[tuple[str, Path, list[str]]] = [
      ("help.mindbox.ru",                SCRIPTS_DIR / "scrape_docs.py",       []),
      ("developers.mindbox.ru",          SCRIPTS_DIR / "scrape_developers.py", []),
      ("mindbox.ru/journal/education",   SCRIPTS_DIR / "scrape_journal.py",    ["--section", "education"]),
      ("mindbox.ru/journal/cases",       SCRIPTS_DIR / "scrape_journal.py",    ["--section", "cases"]),
  ]
  ```

  В цикле запуска: `subprocess.run([sys.executable, str(script), *extra, *forwarded], cwd=REPO_ROOT)`.
  Лейблы шагов в логе остаются осмысленными.
  **Проверка whitelist'а forwarded**: убедиться, что `sync.py`
  пробрасывает в скрейперы только `--full`/`--dry-run` (а не любые
  argv). Если пробрасывает всё — добавить явный whitelist до этого
  шага, иначе будущий запуск `python scripts/sync.py --section foo`
  передаст `--section` дважды и сломает journal-скрейпер.
- `journal/` — миграция содержимого:
  - `git mv journal/pages journal/education/pages`
  - `git mv journal/manifest.json journal/education/manifest.json`
  - `git mv journal/summaries.json journal/education/summaries.json`
  - `git mv journal/INDEX.md journal/education/INDEX.md`
  - `git mv journal/index journal/education/index`
  - `journal/CLAUDE.md` остаётся в корне `journal/` (общие правила
    для всех секций).
- `journal/CLAUDE.md` — переписать раздел «как использовать»:
  - Перечислить два подкорпуса: `journal/education/` и `journal/cases/`.
  - У каждого свой `summaries.json` для триажа.
  - Правило для education без изменений (1–2 предложения сути +
    `source_url`, не пересказывать).
  - Правило для cases: можно дать суть + 2–3 ключевые механики +
    результат (если он указан в статье), всегда с `source_url`,
    тело статьи не пересказывать. Подчеркнуть: кейс — это
    демонстрация, что подобное уже делали, не продуктовая истина.
- `CLAUDE.md` (корень) — обновить:
  - Раздел «Корпуса документации MindBox»: упомянуть cases как второй
    подкорпус journal.
  - Таблица «Где искать ответ»: добавить строку про кейсы — «когда
    нужны примеры/референсы реализации механики».
  - Описание `journal/` в «Структура проекта»: указать вложенность по
    секциям и правило для cases.
- `WELCOME.md` — расширить упоминание journal: «учебные материалы и
  кейсы».
- `notes/claude-behavior.md` — добавить запись «как отвечать на основе
  кейсов» (зеркало правила из journal/CLAUDE.md). В auto-memory
  отдельный feedback-файл **не заводим**: правило выводится из
  CLAUDE.md и notes/, обе сущности уже автоматически попадают в
  контекст будущих сессий — дубликат в memory нарушил бы собственное
  правило «не сохранять то, что выводится из текущего состояния».
- `.claude/commands/sync-docs.md` — проверить и при необходимости
  обновить перечень того, что синкается; команда сама по себе вызывает
  `scripts/sync.py`, кода менять не нужно.
- `plans/2026-05-08-кейсы-журнала.md` — копия этого плана после
  approve, плюс строка в `plans/INDEX.md`.

## Шаги выполнения

Шаги 1–4 идут в **одном коммите** («код + миграция»). Шаги 5–6 идут во
**втором коммите** («контент cases + документация»). Так refactor и
миграция атомарны, а большой контент cases (сотни файлов) лежит в
отдельном diff'е, который удобно ревьюить отдельно.

1. **Refactor + миграция education в одном изменении.**
   - Грепнуть `scripts/scrape_journal.py` по `args.out`, убедиться, что
     все употребления идут через `out_dir`. Если есть голое
     `args.out` где-то ещё (логи манифеста, в начале функции), точечно
     поправить.
   - Сделать правку: `out_dir = Path(args.out) / args.section`.
   - Серия `git mv`:
     - `journal/pages → journal/education/pages`
     - `journal/manifest.json → journal/education/manifest.json`
     - `journal/summaries.json → journal/education/summaries.json`
     - `journal/INDEX.md → journal/education/INDEX.md`
     - `journal/index → journal/education/index`
   - `journal/CLAUDE.md` НЕ перемещаем — общие правила остаются
     в корне `journal/`.
   - **Verification (главный сигнал корректности refactor)**:
     `python scripts/scrape_journal.py --section education --dry-run` →
     **строго 0 изменений**. Если хоть один файл — стоп, разобраться
     до коммита. Это подтверждает: путь записи стал
     `journal/education/...`, контент идентичен старому, manifest
     совместим.

2. **Расширить sync.py**: добавить третий элемент `extra_args` в
   tuple SCRAPERS, зарегистрировать education и cases как два шага.
   Проверить whitelist forwarded args (см. выше). Прогнать
   `python scripts/sync.py --dry-run` — должны отработать все 4
   шага без изменений (cases ещё пуст → скрейпер скажет «N новых
   страниц» — это ожидаемо для первого прогона; учитываем при
   verification: только education должен быть в нуле).

3. **Коммит 1**: refactor + миграция + sync.py. Пуш.

4. **Первичный сбор cases.**
   - `python scripts/scrape_journal.py --section cases --dry-run` для
     оценки объёма (сколько статей в sitemap).
   - Без `--dry-run` — пишет в `journal/cases/`. Может занять минуты
     при первом проходе.
   - Глазами проверить:
     - `journal/cases/manifest.json` → `source =
       https://mindbox.ru/journal/cases/`
     - `journal/cases/summaries.json` существует, содержит статьи
     - 2–3 страницы в `journal/cases/pages/` имеют корректный
       frontmatter (особенно `source_url` начинается с
       `https://mindbox.ru/journal/cases/`)
   - Если cases вернул 0 страниц — **стоп**, разобраться (возможно
     URL-pattern другой; sitemap проверен, но мало ли).

5. **Документация**:
   - `journal/CLAUDE.md`: переписать раздел «как использовать», ввести
     правило для education (1–2 предложения + `source_url`) и более
     развёрнутое правило для cases (суть + 2–3 механики + результат +
     `source_url`, без пересказа тела статьи).
   - `CLAUDE.md` (корень): обновить раздел «Корпуса документации
     MindBox» и таблицу «Где искать ответ» (новая строка про
     референсы из кейсов).
   - `WELCOME.md`: точечно поменять упоминание journal с «учебные
     материалы» на «учебные материалы и кейсы».
   - `notes/claude-behavior.md`: добавить пункт про правило ответа
     по кейсам (зеркало правила из journal/CLAUDE.md).
   - `.claude/commands/sync-docs.md`: проверить и обновить, если
     перечисляет конкретные пути или секции.

6. **Plan registry**: скопировать этот план в
   `plans/2026-05-08-кейсы-журнала.md`, добавить строку в
   `plans/INDEX.md`.

7. **Коммит 2**: контент `journal/cases/*` + документация + plans/.
   Пуш в репо движка. Тенантский репо в этой задаче не трогаем.

## Verification

**Блокирующие проверки (если любая не прошла — стоп до коммита):**

- После refactor + миграции (до коммита 1):
  `python scripts/scrape_journal.py --section education --dry-run` →
  **строго 0 изменений**. Это главный сигнал, что refactor корректен.
- После сбора cases:
  - `journal/cases/manifest.json` содержит
    `source = https://mindbox.ru/journal/cases/`.
  - `journal/cases/summaries.json` существует и не пустой.
  - 2–3 случайные страницы в `journal/cases/pages/` имеют валидный
    frontmatter с `source_url` под `/journal/cases/`.
  - `journal/education/` нетронуто (`git diff` пустой).
- После всех правок:
  `python scripts/sync.py --dry-run` — итог «0 changes» по всем 4
  шагам.
- `git status` чистый после обоих коммитов; `git log --oneline -5`
  показывает ровно 2 целевых коммита.

**Опциональный smoke-тест** (полезно, но не блокирующий):
в новом чате задать вопрос про конкретную механику (например,
«есть ли у MindBox кейсы по retention в FMCG?»). Ответ должен
опираться на `journal/cases/summaries.json`, давать суть + 2–3
механики + результат + `source_url`, не пересказывать тело статьи.
Если правило не соблюдается — поправить формулировку в
`journal/CLAUDE.md`.

## Что НЕ делаем сейчас (известные ограничения)

- Не добавляем секции events / course / news / podcast / romi-community.
  Если понадобятся — отдельный план, но изменения скрейпера и sync.py
  уже сделают это тривиальным (одна строка в SCRAPERS + один прогон).
- **Cross-section ссылки остаются абсолютными.** Текущий регекс
  переписывает `/journal/<section>/<slug>/` → `<slug>.md` только в
  пределах своей секции. Поэтому education-страница, в которой
  встречается ссылка на `/journal/cases/foo/`, после добавления cases
  продолжит держать абсолютный URL — это не баг, а сознательное
  решение текущей архитектуры. Если когда-нибудь захотим относительные
  кросс-секционные ссылки (`../cases/foo.md`), это отдельная задача.
- Не меняем frontmatter, схему manifest.json или summaries.json —
  существующая схема уже несёт `source_url`, и этого достаточно для
  определения секции по URL.
- Не заводим feedback-память для правила про cases — оно полностью
  выводится из `journal/CLAUDE.md` и `notes/claude-behavior.md`,
  которые загружаются автоматически.
- Не трогаем приватный репо тенанта — изменение только в движке.
