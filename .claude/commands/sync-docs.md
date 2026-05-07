---
description: Обновить локальные зеркала документации MindBox (help + developers)
argument-hint: [--full | --dry-run]
allowed-tools: Bash, Read, Grep
---

Пользователь хочет обновить локальные корпуса документации MindBox —
`docs/` (зеркало с `help.mindbox.ru`) и `developers/` (зеркало с
`developers.mindbox.ru`).

## Шаг 1. Определить ОС

Запусти один раз:

```bash
uname -s 2>/dev/null || echo Windows
```

- `Darwin` / `Linux` / `MINGW*` / `MSYS*` / `CYGWIN*` → **POSIX-лаунчер**
  `scripts/sync.sh`.
- Что-то ещё (или команда не найдена) → **Windows-лаунчер**
  `scripts/mindbox.bat`.

## Шаг 2. Что запускать

Из корня репо:

- **macOS / Linux**:
  ```bash
  ./scripts/sync.sh $ARGUMENTS
  ```

  Если получишь `Permission denied` — выполни `chmod +x scripts/sync.sh`
  и попробуй ещё раз.

- **Windows**:
  ```
  ./scripts/mindbox.bat $ARGUMENTS
  ```

`$ARGUMENTS` — это то, что пользователь дописал после команды:
- пусто (по умолчанию) — **инкрементальное обновление** (качаются только
  изменившиеся страницы);
- `--full` — принудительно перезаписать каждую страницу;
- `--dry-run` — показать, что изменится, без записи на диск.

Оба лаунчера самодостаточны и эквивалентны:

- Находят Python 3 в PATH (`py -3` / `python` на Windows; `python3` /
  `python` на POSIX).
- При первом запуске создают `.venv/` в **корне репо** (не в `scripts/`).
  На Windows venv-Python — `.venv/Scripts/python.exe`; на macOS/Linux —
  `.venv/bin/python`.
- Ставят зависимости из `requirements.txt` в venv. На последующих
  запусках пропускают, если `requirements.txt` не менялся после
  последней установки.
- Запускают `scripts/sync.py` с `cwd = корень репо`, который вызывает
  оба скрейпера (`scripts/scrape_docs.py`, `scripts/scrape_developers.py`)
  по очереди — они пишут в `docs/` и `developers/` в корне репо.

Типичный прогон: ~1–2 минуты для инкрементального, дольше для `--full`.
**Используй Bash-таймаут 10 минут** для запаса.

## Шаг 3. Что отчитать пользователю

Каждый скрейпер заканчивается блоком `Summary:`:

```
Summary:
  added:     N
  updated:   N
  unchanged: N
  removed:   N
  failed:    N
  flagged (deprecation_hint): N
```

Извлеки эти цифры по каждому корпусу и кратко отчитайся. Любое ненулевое
`failed` — выдели отдельно (и покажи слаги, которые скрейпер перечислил).
Если в выводе появилась строка `preserved N previously-known page(s)` —
скажи об этом: означает, что N страниц не удалось скачать в этот раз, но
их старые версии сохранились на диске и не удалены (это нормально для
временных сетевых сбоев).

После успешного (не `--dry-run`) прогона дополнительно отчитай свежий
`generated_at` из `docs/manifest.json` и `developers/manifest.json` (в
шапке каждого, ~5-я строка).

Если пользователь передал `--dry-run` — явно скажи, что ничего не было
записано.

## Когда что-то идёт не так

- `Python 3 not found on PATH` (один из лаунчеров) — покажи подсказки
  лаунчера по установке как есть. Сам Python не ставь.
- `Permission denied` на `scripts/sync.sh` — один раз `chmod +x` и
  перезапусти.
- Ненулевой код выхода у лаунчера — покажи последние ~20 строк вывода
  и кратко диагностируй.
- Сетевые / TLS-ошибки в середине прогона — обычно временные, предложи
  повторить. На macOS, если ошибка про `SSL: CERTIFICATE_VERIFY_FAILED`
  для `developers.mindbox.ru` — убедись, что используется venv-Python
  (скрейпер по умолчанию идёт с `verify=False` для этого хоста, потому
  что у dev-сайта неполная TLS-цепочка).
- `Manifest at <path> is corrupted` — это новое строгое поведение
  скрейпера (раньше тихо пере-скачивал всё). Скажи пользователю
  забэкапить и удалить указанный `manifest.json`, потом перезапустить
  `/sync-docs`.
