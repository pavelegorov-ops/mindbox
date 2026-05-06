---
description: Refresh local MindBox docs mirrors (help + developers)
argument-hint: [--full | --dry-run]
allowed-tools: Bash, Read, Grep
---

The user wants to refresh the local MindBox documentation corpora —
`docs/` (mirrored from help.mindbox.ru) and `developers/` (mirrored from
developers.mindbox.ru).

## Detect OS first

Run once:

```bash
uname -s 2>/dev/null || echo Windows
```

- `Darwin` / `Linux` / `MINGW*` / `MSYS*` / `CYGWIN*` → use the **POSIX
  launcher** `scripts/sync.sh`.
- Anything else (or command not found) → use the **Windows launcher**
  `scripts/mindbox.bat`.

## What to run

From the project root:

- **macOS / Linux**:
  ```bash
  ./scripts/sync.sh $ARGUMENTS
  ```

  If you get `Permission denied`, run `chmod +x scripts/sync.sh` and
  retry once.

- **Windows**:
  ```
  ./scripts/mindbox.bat $ARGUMENTS
  ```

`$ARGUMENTS` is whatever the user appended after the command — typically
empty (default = incremental update), `--full` (force-rewrite every page),
or `--dry-run` (preview without writing).

Both launchers are self-contained and equivalent:

- Locate Python 3 on PATH (`py -3` / `python` on Windows; `python3` /
  `python` on POSIX).
- Create `.venv/` in the **repo root** (not in `scripts/`) on first run.
  On Windows the venv Python is `.venv/Scripts/python.exe`; on
  macOS/Linux it's `.venv/bin/python`.
- Install `requirements.txt` into the venv. Skipped on subsequent runs
  unless `requirements.txt` was modified after the last install.
- Run `scripts/sync.py` with `cwd = repo root`, which calls both
  scrapers (`scripts/scrape_docs.py`, `scripts/scrape_developers.py`)
  in sequence — they write to `docs/` and `developers/` at the repo
  root by default.

Typical run: ~1–2 min for incremental, longer for `--full`. **Use a
10-minute Bash timeout** to give margin.

## What to report back

Each scraper ends with a `Summary:` block:

```
Summary:
  added:     N
  updated:   N
  unchanged: N
  removed:   N
  failed:    N
  flagged (deprecation_hint): N
```

Extract these per-corpus and report concisely to the user. Highlight any
non-zero `failed` count (and surface the failing slugs if the scraper
listed them).

After a successful (non-`--dry-run`) sync, also report the fresh
`generated_at` timestamp from `docs/manifest.json` and
`developers/manifest.json` (top of each file, line ~5).

If the user passed `--dry-run`, state explicitly that nothing was written.

## Failure modes

- `Python 3 not found on PATH` (either launcher) — surface the launcher's
  install hints verbatim. Don't try to install Python yourself.
- `Permission denied` on `scripts/sync.sh` — run `chmod +x` once and
  retry.
- Non-zero exit code from the launcher — show the last ~20 lines of
  output and diagnose briefly.
- Network/TLS errors mid-fetch — usually transient; suggest a retry.
  On macOS, if the error mentions `SSL: CERTIFICATE_VERIFY_FAILED` for
  `developers.mindbox.ru`, confirm the user is running the venv Python
  (the scraper defaults to `verify=False` for that host because of an
  incomplete TLS chain).
