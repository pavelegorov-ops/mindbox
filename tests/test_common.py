"""Regression tests for scripts/_common.py.

These cover the two correctness bugs fixed in this branch:

1. compute_removed_slugs: a transient fetch failure must NOT cause the
   file to be deleted (was: any slug in old_manifest but not in new_manifest
   was unlinked, even if its fetch failed this run).
2. atomic_write_text + load_manifest_strict: a kill mid-write must leave
   the original file intact, and a corrupted manifest must surface loudly
   instead of silently triggering a full re-scrape.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from _common import (  # type: ignore[import-not-found]
    atomic_write_text,
    compute_removed_slugs,
    format_fetch_error,
    load_manifest_strict,
)


# ---------- compute_removed_slugs ----------

def test_removed_slugs_preserves_failed_fetches() -> None:
    """A slug that fails to fetch must NOT be deleted, even if missing
    from the new run's success set."""
    old = {"page-a", "page-b", "page-c"}
    new = {"page-a"}            # only A succeeded this run
    failed = {"page-b"}         # B's fetch raised; C is genuinely gone

    to_delete, to_preserve = compute_removed_slugs(
        old_slugs=old, new_slugs=new, failed_slugs=failed
    )

    assert to_delete == ["page-c"]   # only the genuinely-removed slug
    assert to_preserve == ["page-b"]  # B is kept across the failure


def test_removed_slugs_no_failures_classic_behavior() -> None:
    """With no failures, behavior matches the original `old - new`."""
    old = {"a", "b", "c"}
    new = {"a", "b"}
    to_delete, to_preserve = compute_removed_slugs(
        old_slugs=old, new_slugs=new, failed_slugs=set()
    )
    assert to_delete == ["c"]
    assert to_preserve == []


def test_removed_slugs_failure_for_brand_new_slug() -> None:
    """A failed fetch for a slug we've never seen before is NOT preserved
    — there's nothing to preserve. It's just reported as a failure."""
    old = {"a"}
    new = {"a"}
    failed = {"unknown-new-slug"}
    to_delete, to_preserve = compute_removed_slugs(
        old_slugs=old, new_slugs=new, failed_slugs=failed
    )
    assert to_delete == []
    assert to_preserve == []  # not in old_slugs → nothing to preserve


# ---------- atomic_write_text + load_manifest_strict ----------

def test_atomic_write_basic(tmp_path: Path) -> None:
    target = tmp_path / "manifest.json"
    atomic_write_text(target, '{"version": 1, "pages": {}}\n')
    assert target.read_text(encoding="utf-8") == '{"version": 1, "pages": {}}\n'
    # tmp file should be cleaned up by os.replace
    assert not (tmp_path / "manifest.json.tmp").exists()


def test_atomic_write_preserves_original_when_replace_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """If os.replace explodes after the .tmp is written, the original
    target must be untouched."""
    target = tmp_path / "manifest.json"
    target.write_text('{"original": true}\n', encoding="utf-8")

    import _common  # type: ignore[import-not-found]

    def boom(_src: object, _dst: object) -> None:
        raise OSError("simulated mid-replace failure")

    monkeypatch.setattr(_common.os, "replace", boom)

    with pytest.raises(OSError, match="simulated mid-replace failure"):
        atomic_write_text(target, '{"new": true}\n')

    # Original is intact; tmp file may linger but original wasn't truncated.
    assert json.loads(target.read_text(encoding="utf-8")) == {"original": True}


def test_load_manifest_missing_returns_empty(tmp_path: Path) -> None:
    target = tmp_path / "no-such.json"
    assert load_manifest_strict(target) == {"version": 1, "pages": {}}


def test_load_manifest_corrupt_raises(tmp_path: Path) -> None:
    """A truncated/corrupted manifest must surface a clear error, not
    silently trigger a re-scrape (the previous behavior)."""
    target = tmp_path / "manifest.json"
    target.write_text('{"version": 1, "pages": {"a"', encoding="utf-8")  # truncated

    with pytest.raises(RuntimeError) as excinfo:
        load_manifest_strict(target)

    msg = str(excinfo.value)
    assert "corrupted" in msg.lower()
    assert str(target) in msg
    # Should hint at the recovery path (delete + re-run)
    assert "delete" in msg.lower() or "re-scrape" in msg.lower()


def test_load_manifest_valid_returns_payload(tmp_path: Path) -> None:
    target = tmp_path / "manifest.json"
    target.write_text(
        json.dumps({"version": 1, "pages": {"foo": {"hash": "abc"}}}),
        encoding="utf-8",
    )
    payload = load_manifest_strict(target)
    assert payload["pages"]["foo"]["hash"] == "abc"


# ---------- format_fetch_error ----------

def test_format_fetch_error_generic_exception_carries_url() -> None:
    msg = format_fetch_error(ValueError("bad payload"), url="https://x/y")
    assert "ValueError" in msg
    assert "bad payload" in msg
    assert "https://x/y" in msg


def test_format_fetch_error_http_status() -> None:
    """When httpx is available and we get an HTTPStatusError, the
    formatter must surface status + URL."""
    httpx = pytest.importorskip("httpx")
    request = httpx.Request("GET", "https://example.com/missing")
    response = httpx.Response(404, request=request, text="not found")
    exc = httpx.HTTPStatusError("404", request=request, response=response)
    msg = format_fetch_error(exc)
    assert "404" in msg
    assert "https://example.com/missing" in msg
