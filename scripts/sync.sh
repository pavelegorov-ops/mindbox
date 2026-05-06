#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  sync.sh — macOS / Linux launcher for MindBox docs sync.
#
#  Usage (from repo root):
#      scripts/sync.sh             incremental update
#      scripts/sync.sh --full      rewrite every page
#      scripts/sync.sh --dry-run   preview without writing
#
#  1. Locates Python 3 (python3 first, then python).
#  2. Creates a local .venv in the repo root if missing.
#  3. Installs / updates requirements.txt into the venv (idempotent).
#  4. Runs sync.py inside the venv with cwd=repo root, forwarding all flags.
# ---------------------------------------------------------------------------

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VENV="$ROOT/.venv"
VENV_PY="$VENV/bin/python"
REQ="$ROOT/requirements.txt"
STAMP="$VENV/.requirements.stamp"

# --- 1. Find a system Python -------------------------------------------------
if command -v python3 >/dev/null 2>&1; then
    PY=python3
elif command -v python >/dev/null 2>&1; then
    PY=python
else
    cat >&2 <<'EOF'
[sync] Python 3 not found on PATH.

Install one of:
    macOS:  brew install python3
    Debian/Ubuntu:  sudo apt install python3 python3-venv
    Fedora:         sudo dnf install python3
    Arch:           sudo pacman -S python

EOF
    exit 1
fi

# --- 2. Create venv if missing ----------------------------------------------
if [ ! -x "$VENV_PY" ]; then
    echo "[sync] Creating virtualenv at $VENV"
    "$PY" -m venv "$VENV"
fi

# --- 3. Install/update deps if requirements.txt changed ----------------------
need_install=1
if [ -f "$STAMP" ] && [ "$STAMP" -nt "$REQ" ]; then
    need_install=0
fi

if [ "$need_install" = "1" ]; then
    echo "[sync] Installing dependencies from requirements.txt"
    "$VENV_PY" -m pip install --quiet --upgrade pip
    "$VENV_PY" -m pip install --quiet -r "$REQ"
    : > "$STAMP"
fi

# --- 4. Run the orchestrator -------------------------------------------------
cd "$ROOT"
exec "$VENV_PY" "$HERE/sync.py" "$@"
