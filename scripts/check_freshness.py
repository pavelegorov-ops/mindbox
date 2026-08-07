"""Report how stale each MindBox corpus mirror is.

Informational only: reads `generated_at` from every corpus manifest, prints
an OK / WARN / MISSING line per corpus, and ALWAYS exits 0. The corpora are
per-user, git-ignored, and refreshed only by `/sync-docs`, so the agent has
no built-in freshness signal — this gives it one before answering.

Pure stdlib, cwd-independent (paths resolve relative to this file), and
fail-open: a corrupt or unreadable manifest is reported, not raised.

    python scripts/check_freshness.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent          # scripts/
REPO_ROOT = SCRIPTS_DIR.parent                         # repo root

# Corpus label → manifest path (relative to repo root), команда обновления,
# on_demand: журнал качается только по запросу, поэтому его отсутствие — норма.
CORPORA: list[tuple[str, Path, str, bool]] = [
    ("docs (Help)",             REPO_ROOT / "docs" / "manifest.json",                    "/sync-docs", False),
    ("developers (Developers)", REPO_ROOT / "developers" / "manifest.json",              "/sync-docs", False),
    ("journal/cases",           REPO_ROOT / "journal" / "cases" / "manifest.json",       "/sync-docs --journal cases", True),
    ("journal/education",       REPO_ROOT / "journal" / "education" / "manifest.json",   "/sync-docs --journal education", True),
]

WARN_DAYS = 14


def age_days(generated_at: str) -> float | None:
    """Days since `generated_at` (ISO 8601, e.g. 2026-05-14T10:07:58Z)."""
    try:
        ts = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None
    return (datetime.now(timezone.utc) - ts).total_seconds() / 86400.0


def report(label: str, manifest: Path, hint: str, on_demand: bool) -> None:
    if not manifest.exists():
        if on_demand:
            print(f"SKIP     {label}: не выгружен — качаем по запросу ({hint})")
        else:
            print(f"MISSING  {label}: не синхронизировано, запусти {hint}")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"MISSING  {label}: манифест нечитаем ({type(exc).__name__}), запусти {hint}")
        return

    age = age_days(data.get("generated_at", ""))
    if age is None:
        print(f"MISSING  {label}: нет поля generated_at, запусти {hint}")
    elif age > WARN_DAYS:
        print(f"WARN     {label}: {age:.0f} дн. назад (>{WARN_DAYS}) — возможно устарело, {hint}")
    else:
        print(f"OK       {label}: {age:.0f} дн. назад")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for label, manifest, hint, on_demand in CORPORA:
        report(label, manifest, hint, on_demand)
    return 0  # informational — never blocks


if __name__ == "__main__":
    sys.exit(main())
