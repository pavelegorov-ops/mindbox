# Как поставить mindBox

Этот проект — локальная база знаний по MindBox для Claude Code:
два корпуса документации (Help и Developers) + генератор сценариев +
slash-команды для маркетолога. Этот файл — «как начать» в одном экране.

Поддерживаются **Windows**, **macOS** и **Linux**. Команды ниже даны
параллельно — выбирай свою колонку.

## Что нужно поставить заранее

1. **Python 3.10+** — для скрейперов и генератора. Проверка:

   - **Windows** (`cmd` / PowerShell):
     ```
     py -3 --version
     ```
     Если нет — `winget install Python.Python.3.12` или
     <https://www.python.org/downloads/windows/>.
   - **macOS** (Terminal):
     ```bash
     python3 --version
     ```
     Если нет — `brew install python3` (нужен
     [Homebrew](https://brew.sh)) или скачай инсталлятор:
     <https://www.python.org/downloads/macos/>.
   - **Linux**:
     ```bash
     python3 --version
     ```
     Если нет — `sudo apt install python3 python3-venv` (Debian/Ubuntu),
     `sudo dnf install python3` (Fedora), `sudo pacman -S python` (Arch).

2. **Git** — для клонирования и `/обнови-данные` / `/отправь-данные`.

   - Windows: <https://git-scm.com/download/win>
   - macOS: уже стоит вместе с Xcode Command Line Tools
     (`xcode-select --install`), либо `brew install git`.
   - Linux: `sudo apt install git` / `sudo dnf install git` /
     `sudo pacman -S git`.

3. **Claude Code** — собственно, среда, в которой ты сейчас читаешь это.
   <https://claude.com/claude-code>.

4. **Chrome + расширение Claude in Chrome** — нужны, если ты планируешь
   обновлять `mailing-parameters/` или вытаскивать сценарии напрямую из
   админки `<тенант>.mindbox.ru`. Без него вся остальная работа всё
   равно работает.

## Шаг 1. Склонировать репо

Публичный репозиторий движка:

- **Windows**:
  ```
  git clone <URL движка> mindBox
  cd mindBox
  ```
- **macOS / Linux**:
  ```bash
  git clone <URL движка> mindBox
  cd mindBox
  ```

Если ты — коллега из Usmall, дополнительно склонируй приватный репо
с бизнес-данными в подкаталог `private/usmall/`:

```bash
git clone <URL приватного репо Usmall> private/usmall
```

(Точные URL — у того, кто давал тебе доступ.)

### Только для macOS / Linux: дать запускалке право на исполнение

Скрипт `scripts/sync.sh` помечен в git как исполняемый, но если по
каким-то причинам (например, файл создан на Windows) бит сбился —
поправь:

```bash
chmod +x scripts/sync.sh
```

## Шаг 2. Открыть в Claude Code и запустить `/bootstrap`

```
claude
```

В появившемся чате введи:

```
/bootstrap
```

`/bootstrap` сделает за тебя:

- определит твою ОС и выберет правильный лаунчер
  (`scripts/mindbox.bat` для Windows, `scripts/sync.sh` для macOS/Linux);
- проверит Python;
- создаст `.venv/` и поставит зависимости;
- проверит, что корпуса доков (`docs/`, `developers/`) на месте;
- найдёт активного тенанта в `private/` и сравнит `engine.txt`;
- прогонит smoke-test чтения корпуса.

Это безопасно: никаких сетевых запросов по корпусам,
ничего публичного.

## Шаг 3. (Если нужно) выгрузить корпуса доков

Если `/bootstrap` сообщил, что `docs/` или `developers/` не выгружены,
скачай их:

```
/sync-docs
```

Это потянет ~1000 страниц с help.mindbox.ru и developers.mindbox.ru
(~1–2 минуты при первом запуске, дальше инкрементально).

## Что дальше

- Спроси Claude любой вопрос про MindBox: «как настроить сегмент по
  оплаченным заказам?», «какой формат payload у webhook integration?» —
  ответ придёт со ссылкой на канонический источник.
- Если есть `private/<тенант>/scenarios/` — спроси про конкретный
  сценарий по id или по описанию.
- Чтобы увидеть, что лежит в репо, читай `CLAUDE.md` в корне.
- Чтобы добавить ещё одного тенанта — `private/_template/README.md`.

## Повседневные команды (для маркетолога)

Когда ты в Claude Code и хочешь синхронизироваться с коллегами:

- `/обнови-данные` — `git pull` сразу в публичном и приватном репо.
- `/отправь-данные` — закоммитить и запушить твои правки в приватный
  репо тенанта (с предварительным `scripts/render_scenarios.py`).

Без этих команд ту же работу можно сделать руками: `git pull`,
`git add`, `git commit`, `git push` отдельно в корне и в
`private/<тенант>/`.

## Если что-то пошло не так

- **Windows** `scripts\mindbox.bat` падает с «Python 3 not found on PATH»
  → поставь Python и **перезапусти терминал**.
- **macOS / Linux** `scripts/sync.sh: Permission denied` →
  `chmod +x scripts/sync.sh`. Если `python3` не найден —
  `brew install python3` (mac) или `sudo apt install python3 python3-venv`
  (Linux).
- **macOS** скрейпер `developers.mindbox.ru` падает по TLS на
  системном Python — проверь, что используется venv-питон из репо
  (`.venv/bin/python`). Скрейпер по умолчанию идёт с `verify=False`,
  потому что у dev-сайта неполная TLS-цепочка; если ты сам передал
  `--verify` — убери.
- `/bootstrap` ругается, что тенант требует более новый движок →
  `git pull` в корне репо.

## Где какие файлы лежат

- Скрипты движка — `scripts/`. Все вызывай **из корня репо**:
  - **Windows**: `scripts\mindbox.bat`, `python scripts\render_scenarios.py`.
  - **macOS / Linux**: `scripts/sync.sh`, `python3 scripts/render_scenarios.py`.
- Корпуса доков — `docs/` и `developers/`.
- Бизнес-данные тенанта — `private/<имя>/`.
- Заметки и приёмы — `notes/`.
- Slash-команды Claude Code — `.claude/commands/`.
