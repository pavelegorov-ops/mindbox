"""Shared helpers for the MindBox docs/developers scrapers.

These utilities used to be copy-pasted into each scraper. Centralizing them
here keeps bug fixes (e.g. the manifest atomicity guarantee) in one place.

Pure functions and module-level constants only — no I/O state, no classes.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


# ---------- deprecation markers ----------

# Phrases that signal "this page describes a deprecated/legacy/unused feature".
# Substring match on the lowercased Markdown body (incl. title). Detected labels
# end up in the page's `deprecation_hint` frontmatter field so Claude can
# qualify answers sourced from these pages.
DEPRECATION_MARKERS: list[str] = [
    "устарел",
    "устаревш",
    "больше не работа",
    "больше не поддержив",
    "не используется",
    "старый интерфейс",
    "старая версия",
    "deprecated",
    "прекращ",
    "снят с поддержки",
    "архивн",
]


def detect_deprecation(text: str) -> list[str]:
    """Return matched deprecation markers (preserves DEPRECATION_MARKERS order)."""
    low = text.lower()
    return [m for m in DEPRECATION_MARKERS if m in low]


# ---------- transliteration ----------

# Cyrillic → Latin transliteration for converting section names into safe
# filenames for `<corpus>/index/<section-slug>.md`. Lossy but stable.
RU_TO_LAT: dict[str, str] = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
    "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


# ---------- inline-markdown stripping for lead extraction ----------

_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_MD_ITALIC_RE = re.compile(r"(?<!\w)[*_]([^*_\n]+)[*_](?!\w)")
_MD_CODE_RE = re.compile(r"`([^`]+)`")
_WS_RE = re.compile(r"\s+")


def strip_markdown_inlines(s: str) -> str:
    s = _MD_IMAGE_RE.sub("", s)
    s = _MD_LINK_RE.sub(r"\1", s)
    s = _MD_BOLD_RE.sub(r"\1", s)
    s = _MD_ITALIC_RE.sub(r"\1", s)
    s = _MD_CODE_RE.sub(r"\1", s)
    return _WS_RE.sub(" ", s).strip()


def extract_lead(body_md: str, max_chars: int = 240) -> str:
    """Pull the first informative paragraph from rendered Markdown.

    Skips headings, blockquotes, list markers, code fences and short
    fragments; truncates at a word boundary near max_chars when needed.
    """
    paragraphs: list[str] = []
    buf: list[str] = []
    for line in body_md.splitlines():
        if line.strip():
            buf.append(line)
        elif buf:
            paragraphs.append(" ".join(buf).strip())
            buf = []
    if buf:
        paragraphs.append(" ".join(buf).strip())

    for raw in paragraphs:
        if raw.startswith(("#", ">", "```", "- ", "* ", "+ ", "|")):
            continue
        clean = strip_markdown_inlines(raw)
        if len(clean) < 20:
            continue
        if len(clean) <= max_chars:
            return clean
        cut = clean[:max_chars]
        sp = cut.rfind(" ")
        if sp > max_chars * 0.6:
            cut = cut[:sp]
        return cut.rstrip(" ,.;:—-") + "…"
    return ""


# ---------- YAML frontmatter rendering ----------

def to_yaml_scalar(value: Any) -> str:
    """Minimal YAML scalar serializer (strings, lists of strings, ISO dates)."""
    if isinstance(value, str):
        if value == "" or re.search(r'[:#\-?&*!|>\'"%@`,\[\]\{\}\n]', value) or value.strip() != value:
            return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
        return value
    if isinstance(value, (int, float, bool)):
        return json.dumps(value)
    raise TypeError(f"unsupported scalar: {type(value)!r}")


def render_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {to_yaml_scalar(item)}")
        else:
            lines.append(f"{k}: {to_yaml_scalar(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# ---------- page filename ----------

def page_filename(slug: str) -> str:
    """Slug → on-disk filename. Defensive: strip path separators."""
    return slug.replace("/", "_").replace("\\", "_") + ".md"


# ---------- secret redaction ----------

# Patterns of example secrets that appear in upstream MindBox docs (not real
# credentials — illustrative formats). GitHub's secret scanning rejects
# pushes that contain them, so we replace with placeholders before hashing
# and saving. Keep this list minimal; extend when push fails on a new pattern.
_SECRET_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"shpat_[A-Za-z0-9]{20,}"), "shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"shpss_[A-Fa-f0-9]{20,}"), "shpss_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"shppa_[A-Fa-f0-9]{20,}"), "shppa_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"),    "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
]


def redact_secrets(text: str) -> str:
    for pat, repl in _SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text


# ---------- manifest I/O ----------

def load_manifest_strict(path: Path) -> dict:
    """Load JSON manifest. Empty dict if file is missing.

    Raises RuntimeError on a corrupted file — the previous "silently return
    empty dict" behaviour would mask a partial-write bug and trigger a full
    re-scrape without warning.
    """
    if not path.exists():
        return {"version": 1, "pages": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Manifest at {path} is corrupted ({exc.msg} at line {exc.lineno}). "
            f"Back it up and delete the file to force a full re-scrape, "
            f"then re-run this script."
        ) from exc


def compute_removed_slugs(
    *,
    old_slugs: set[str],
    new_slugs: set[str],
    failed_slugs: set[str],
) -> tuple[list[str], list[str]]:
    """Decide which previously-known slugs are gone for good vs. just failed.

    Returns (to_delete, to_preserve_from_old):

    - `to_delete` — slugs we successfully re-walked and confirmed missing
      from upstream (sorted, safe to unlink on disk).
    - `to_preserve_from_old` — slugs that failed this run but were known
      before; their old manifest entry should be kept so they aren't
      reported as removed and aren't re-added next run as "added".

    A slug that's missing from new_slugs but present in failed_slugs is
    NOT deleted — that's the bug fix: a transient HTTP failure must not
    churn files on disk.
    """
    to_delete = sorted(old_slugs - new_slugs - failed_slugs)
    to_preserve_from_old = sorted(failed_slugs & old_slugs)
    return to_delete, to_preserve_from_old


def atomic_write_text(path: Path, content: str, *, encoding: str = "utf-8") -> None:
    """Write to <path>.tmp, then os.replace onto <path>.

    A kill mid-write must leave the original file intact; otherwise readers
    see a truncated payload (which load_manifest_strict will now refuse).
    """
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding=encoding)
    os.replace(tmp, path)


# ---------- error formatting ----------

def format_fetch_error(exc: BaseException, *, url: str | None = None) -> str:
    """One-liner that captures HTTP status, error class, message, and URL.

    The previous `repr(exc)` lost everything useful — readers had no idea if
    a slug failed because of a 404, a timeout, or a malformed payload.
    """
    # Lazy import: httpx is the only consumer-relevant exception family,
    # but _common shouldn't unconditionally depend on it being importable
    # at import time.
    try:
        import httpx  # type: ignore[import-not-found]
    except ImportError:
        httpx = None  # type: ignore[assignment]

    if httpx is not None and isinstance(exc, httpx.HTTPStatusError):
        return (
            f"HTTP {exc.response.status_code} {exc.response.reason_phrase} "
            f"for {exc.request.url}"
        )
    msg = f"{type(exc).__name__}: {exc}".strip()
    if url:
        msg = f"{msg} (url={url})"
    return msg
