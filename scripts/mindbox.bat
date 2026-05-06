@echo off
setlocal EnableDelayedExpansion

REM ---------------------------------------------------------------------------
REM  mindbox.bat — single console command for the MindBox docs corpus.
REM
REM  Usage (from repo root):
REM     scripts\mindbox             first-run setup + sync, or incremental update
REM     scripts\mindbox --full      rewrite every page (slower)
REM     scripts\mindbox --dry-run   report changes without writing files
REM
REM  What it does:
REM    1. Locates Python 3 (py launcher first, then `python` on PATH).
REM    2. Creates a local .venv in the repo root if missing.
REM    3. Installs / updates requirements.txt into the venv (idempotent).
REM    4. Runs sync.py in the venv to refresh both doc mirrors.
REM ---------------------------------------------------------------------------

set "HERE=%~dp0"
set "ROOT=%HERE%.."
set "VENV=%ROOT%\.venv"
set "VENV_PY=%VENV%\Scripts\python.exe"
set "REQ=%ROOT%\requirements.txt"
set "STAMP=%VENV%\.requirements.stamp"

REM --- 1. Find a system Python --------------------------------------------------
REM  Use && chains so we don't have to worry about %ERRORLEVEL% expansion
REM  inside nested if/else blocks (it would expand at parse time, not at run).
set "PY="
where py >nul 2>&1 && set "PY=py -3"
if "%PY%"=="" where python >nul 2>&1 && set "PY=python"

if "%PY%"=="" (
    echo [mindbox] Python 3 not found on PATH.
    echo.
    echo Install one of:
    echo     winget install Python.Python.3.12
    echo     https://www.python.org/downloads/windows/
    echo.
    echo Then re-open this terminal and run `mindbox` again.
    exit /b 1
)

REM --- 2. First-run banner + venv creation -------------------------------------
if not exist "%VENV_PY%" (
    echo.
    echo =========================================================
    echo   MindBox docs - first-time setup
    echo =========================================================
    echo This will:
    echo   * create a local Python venv in .venv\
    echo   * install httpx, markdownify, beautifulsoup4
    echo   * download both doc mirrors - help + developers, ~1000 pages
    echo.
    echo Takes ~1-2 minutes. Subsequent runs are incremental and fast.
    echo =========================================================
    echo.
    echo [mindbox] Creating virtualenv at "%VENV%"
    %PY% -m venv "%VENV%"
    if errorlevel 1 (
        echo [mindbox] failed to create venv.
        exit /b 1
    )
)

REM --- 3. Install/update deps if requirements.txt changed ----------------------
set "NEED_INSTALL=1"
if exist "%STAMP%" (
    for /f %%A in ('powershell -NoProfile -Command "(Get-Item '%REQ%').LastWriteTime.Ticks"') do set "REQ_T=%%A"
    for /f %%A in ('powershell -NoProfile -Command "(Get-Item '%STAMP%').LastWriteTime.Ticks"') do set "STAMP_T=%%A"
    if !REQ_T! LEQ !STAMP_T! set "NEED_INSTALL=0"
)

if "%NEED_INSTALL%"=="1" (
    echo [mindbox] Installing dependencies from requirements.txt
    "%VENV_PY%" -m pip install --quiet --upgrade pip
    "%VENV_PY%" -m pip install --quiet -r "%REQ%"
    if errorlevel 1 (
        echo [mindbox] dependency install failed.
        exit /b 1
    )
    echo. > "%STAMP%"
)

REM --- 4. Run the orchestrator -------------------------------------------------
REM  cd to repo root so scrape_*.py default --out (docs / developers) lands in
REM  the correct directory.
pushd "%ROOT%"
"%VENV_PY%" "%HERE%sync.py" %*
set "RC=%ERRORLEVEL%"
popd
exit /b %RC%
