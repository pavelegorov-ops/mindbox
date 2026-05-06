---
description: Refresh local MindBox docs mirrors (help + developers)
argument-hint: [--full | --dry-run]
allowed-tools: Bash, Read, Grep
---

The user wants to refresh the local MindBox documentation corpora —
`docs/` (mirrored from help.mindbox.ru) and `developers/` (mirrored from
developers.mindbox.ru).

## What to run

From the project root:

```
./scripts/mindbox.bat $ARGUMENTS
```

`$ARGUMENTS` is whatever the user appended after the command — typically
empty (default = incremental update), `--full` (force-rewrite every page),
or `--dry-run` (preview without writing).

The launcher is self-contained:

- Locates Python 3 on PATH (`py -3` first, then `python`).
- Creates `.venv/` in the **repo root** (not in `scripts/`) on first run.
- Installs `requirements.txt` into the venv. Skipped on subsequent runs
  unless `requirements.txt` was modified after the last install.
- Runs `scripts/sync.py` with `cwd = repo root`, which calls both
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

- `[mindbox] Python 3 not found on PATH` — surface the launcher's install
  hints verbatim. Don't try to install Python yourself.
- Non-zero exit code from `scripts/mindbox.bat` — show the last ~20
  lines of output and diagnose briefly.
- Network/TLS errors mid-fetch — usually transient; suggest a retry.
