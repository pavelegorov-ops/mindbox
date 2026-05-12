"""
Sync all MindBox knowledge mirrors.

Runs scrapers and post-processing steps sequentially:

    scrape_docs.py         help.mindbox.ru                  → docs/
    scrape_developers.py   developers.mindbox.ru            → developers/
    scrape_journal.py      mindbox.ru/journal/education/    → journal/education/
    scrape_journal.py      mindbox.ru/journal/cases/        → journal/cases/

Then journal-only enrichment, gated by ANTHROPIC_API_KEY:

    enrich_journal.py      LLM-rewritten summary_ru + key_points;
                           cases get fact_index.json + by-{mechanic,industry,kpi}/.

Then BM25 paragraph index for both journal sections (offline, always):

    build_bm25.py          journal/<section>/search_index.pkl

First run downloads everything; subsequent runs are incremental
(re-fetches all pages, rewrites only files whose content changed; skips
LLM calls for pages whose content_hash is unchanged).

Usually invoked via the OS launcher, which sets up a local .venv and
calls this file with the venv's Python:

    mindbox                   (Windows: mindbox.bat)
    ./sync.sh                 (macOS / Linux — not yet rebranded)

Flags pass through to scrapers and enrichment:

    mindbox --full            force-rewrite every page (and re-enrich)
    mindbox --dry-run         report changes, write nothing

If `ANTHROPIC_API_KEY` is unset, journal enrichment is skipped with a
warning — scraping and BM25 still complete.

Direct usage (assumes deps already installed in the active interpreter):

    python sync.py [--full] [--dry-run]
"""

from __future__ import annotations

import argparse
import os
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


def run_step(label: str, cmd: list[str], *, fatal: bool) -> bool:
    """Run one subprocess step; return True on success.

    `fatal=True` means a non-zero exit triggers an overall non-zero exit
    code from sync.py. Enrichment is non-fatal — a transient LLM error
    shouldn't fail the whole sync.
    """
    print(f"\n=== {label} ===", flush=True)
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    if result.returncode == 0:
        return True
    print(f"[mindbox] {label} returned exit code {result.returncode}", file=sys.stderr)
    return not fatal  # non-fatal failures don't taint the overall result


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
    parser.add_argument(
        "--skip-enrichment",
        action="store_true",
        help="skip LLM enrichment even if ANTHROPIC_API_KEY is set",
    )
    parser.add_argument(
        "--skip-bm25",
        action="store_true",
        help="skip rebuilding the BM25 search index",
    )
    args = parser.parse_args()

    forwarded: list[str] = []
    if args.full:
        forwarded.append("--full")
    if args.dry_run:
        forwarded.append("--dry-run")

    failed: list[str] = []
    started = time.monotonic()

    # 1. Scrapers.
    for label, script, extra_args in SCRAPERS:
        if not script.exists():
            print(f"[mindbox] missing scraper: {script.name}", file=sys.stderr)
            failed.append(label)
            continue
        ok = run_step(
            f"{label}  ({script.name})",
            [sys.executable, str(script), *extra_args, *forwarded],
            fatal=True,
        )
        if not ok:
            failed.append(label)

    # 2. Journal enrichment (LLM). Non-fatal, gated on key + flag + dry_run.
    if args.dry_run:
        print("\n[mindbox] dry-run: skipping enrichment + BM25.", flush=True)
    else:
        if args.skip_enrichment:
            print("\n[mindbox] enrichment skipped via --skip-enrichment.", flush=True)
        elif not os.environ.get("ANTHROPIC_API_KEY"):
            print(
                "\n[mindbox] ANTHROPIC_API_KEY not set — skipping LLM enrichment "
                "(summary_ru, key_points, cases/fact_index.json).\n"
                "         Set the env var to enable, or pass --skip-enrichment "
                "to silence this notice.",
                flush=True,
            )
        else:
            enrich_script = SCRIPTS_DIR / "enrich_journal.py"
            for section in ("education", "cases"):
                run_step(
                    f"enrich {section}  ({enrich_script.name})",
                    [sys.executable, str(enrich_script), "--section", section, *forwarded],
                    fatal=False,
                )

        # 3. BM25 index. Offline, always runs unless explicitly skipped.
        if args.skip_bm25:
            print("\n[mindbox] BM25 build skipped via --skip-bm25.", flush=True)
        else:
            bm25_script = SCRIPTS_DIR / "build_bm25.py"
            run_step(
                f"build BM25 index  ({bm25_script.name})",
                [sys.executable, str(bm25_script)],
                fatal=False,
            )

    elapsed = time.monotonic() - started
    print(f"\n[mindbox] finished in {elapsed:.1f}s")

    if failed:
        print(f"[mindbox] FAILED: {', '.join(failed)}", file=sys.stderr)
        return 1
    print("[mindbox] all mirrors synced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
