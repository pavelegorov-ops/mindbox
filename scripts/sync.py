"""
Sync all MindBox knowledge mirrors.

Runs scrapers sequentially and forwards flags to each:

    scrape_docs.py         help.mindbox.ru                  → docs/
    scrape_developers.py   developers.mindbox.ru            → developers/
    scrape_journal.py      mindbox.ru/journal/education/    → journal/education/
    scrape_journal.py      mindbox.ru/journal/cases/        → journal/cases/

First run downloads everything; subsequent runs are incremental
(re-fetches all pages, rewrites only files whose content changed).

Usually invoked via the OS launcher, which sets up a local .venv and
calls this file with the venv's Python:

    mindbox                   (Windows: mindbox.bat)
    ./sync.sh                 (macOS / Linux — not yet rebranded)

Flags pass through to every scraper:

    mindbox --full            force-rewrite every page
    mindbox --dry-run         report changes, write nothing

Direct usage (assumes deps already installed in the active interpreter):

    python sync.py [--full] [--dry-run]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent          # scripts/
REPO_ROOT = SCRIPTS_DIR.parent                         # repo root — cwd для скрейперов

SCRAPERS: list[tuple[str, Path, list[str]]] = [
    ("help.mindbox.ru",                 SCRIPTS_DIR / "scrape_docs.py",       []),
    ("developers.mindbox.ru",           SCRIPTS_DIR / "scrape_developers.py", []),
    ("mindbox.ru/journal/education",    SCRIPTS_DIR / "scrape_journal.py",    ["--section", "education"]),
    ("mindbox.ru/journal/cases",        SCRIPTS_DIR / "scrape_journal.py",    ["--section", "cases"]),
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync all MindBox knowledge mirrors (help + developers + journal).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="force-rewrite every page (slower; use after schema changes)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change without writing files",
    )
    args = parser.parse_args()

    forwarded: list[str] = []
    if args.full:
        forwarded.append("--full")
    if args.dry_run:
        forwarded.append("--dry-run")

    failed: list[str] = []
    started = time.monotonic()

    for label, script, extra_args in SCRAPERS:
        if not script.exists():
            print(f"[mindbox] missing scraper: {script.name}", file=sys.stderr)
            failed.append(label)
            continue

        print(f"\n=== {label}  ({script.name}) ===", flush=True)
        result = subprocess.run(
            [sys.executable, str(script), *extra_args, *forwarded], cwd=REPO_ROOT
        )
        if result.returncode != 0:
            failed.append(label)

    elapsed = time.monotonic() - started
    print(f"\n[mindbox] finished in {elapsed:.1f}s")

    if failed:
        print(f"[mindbox] FAILED: {', '.join(failed)}", file=sys.stderr)
        return 1
    print(f"[mindbox] all {len(SCRAPERS)} mirrors synced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
