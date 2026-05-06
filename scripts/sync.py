"""
Sync both MindBox documentation mirrors.

Runs scrape_docs.py (help.mindbox.ru) and scrape_developers.py
(developers.mindbox.ru) sequentially and forwards flags to both.

First run downloads everything; subsequent runs are incremental
(re-fetches all pages, rewrites only files whose content changed).

Usually invoked via the OS launcher, which sets up a local .venv and
calls this file with the venv's Python:

    mindbox                   (Windows: mindbox.bat)
    ./sync.sh                 (macOS / Linux — not yet rebranded)

Flags pass through to both scrapers:

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

SCRAPERS: list[tuple[str, Path]] = [
    ("help.mindbox.ru",        SCRIPTS_DIR / "scrape_docs.py"),
    ("developers.mindbox.ru",  SCRIPTS_DIR / "scrape_developers.py"),
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync both MindBox doc mirrors (help + developers).",
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

    for label, script in SCRAPERS:
        if not script.exists():
            print(f"[mindbox] missing scraper: {script.name}", file=sys.stderr)
            failed.append(label)
            continue

        print(f"\n=== {label}  ({script.name}) ===", flush=True)
        result = subprocess.run(
            [sys.executable, str(script), *forwarded], cwd=REPO_ROOT
        )
        if result.returncode != 0:
            failed.append(label)

    elapsed = time.monotonic() - started
    print(f"\n[mindbox] finished in {elapsed:.1f}s")

    if failed:
        print(f"[mindbox] FAILED: {', '.join(failed)}", file=sys.stderr)
        return 1
    print("[mindbox] both mirrors synced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
