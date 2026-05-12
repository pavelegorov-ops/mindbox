"""Build a BM25 paragraph-level search index over a journal section.

Splits each `pages/<slug>.md` into paragraph chunks (one paragraph =
one chunk), tags each with the slug of its nearest preceding H2/H3 so
search results can show the section context, normalizes tokens via
`_tokenize.tokenize` (RU lemmatization + EN stemming), and pickles the
fitted BM25Okapi together with chunk metadata into a single file.

Run from repo root:

    python scripts/build_bm25.py --section education
    python scripts/build_bm25.py --section cases
    python scripts/build_bm25.py            # both sections

Output (per section): `journal/<section>/search_index.pkl`. The file is
fully derived from `pages/` and not committed to git — see `.gitignore`.

Build time: ~5-15s for 875 articles total (most of it is pymorphy3
warmup on first run).
"""

from __future__ import annotations

import argparse
import pickle
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _journal_tokens import Chunk, tokenize  # noqa: E402


# Bumped when the chunk format or metadata schema changes; older indexes
# get treated as missing and rebuilt.
INDEX_FORMAT_VERSION = 1

# Paragraphs shorter than this are merged into the next paragraph — tiny
# fragments (single-line image captions, "Срок." labels) blow up posting
# lists with no retrieval signal.
MIN_CHUNK_CHARS = 80

# Skip indexing chunks that come from these noisy regions of an article.
# Right now we trust our scraper to have stripped them already, but keep
# the hook for future filters.
_NOISE_PREFIXES = ("![", "[", "|", "---")


def parse_page_for_chunks(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Split a page Markdown file into (title, [(section_title, paragraph)]).

    `text` is the on-disk page content with frontmatter and H1 included
    — we strip both. Section_title is the most recent H2/H3 we saw.
    """
    # Strip frontmatter.
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            text = text[end + 5:]

    title = ""
    paragraphs: list[tuple[str, str]] = []
    section_title = ""
    buf: list[str] = []

    def flush():
        nonlocal buf
        if not buf:
            return
        para = " ".join(line.strip() for line in buf if line.strip()).strip()
        buf = []
        if not para:
            return
        if any(para.startswith(p) for p in _NOISE_PREFIXES):
            return
        paragraphs.append((section_title, para))

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("# ") and not title:
            flush()
            title = stripped[2:].strip()
            continue
        if stripped.startswith(("## ", "### ")):
            flush()
            # Drop leading "##" / "###" + spaces.
            section_title = stripped.lstrip("#").strip()
            continue
        if stripped.startswith(("#### ", "##### ", "###### ")):
            # Deeper headings stay inside the current section but become
            # their own paragraph (so search hits land on the heading too).
            flush()
            paragraphs.append((section_title, stripped.lstrip("#").strip()))
            continue
        if stripped == "":
            flush()
            continue
        if line.startswith("```"):
            # Code fences — skip until the closing fence. Don't index code.
            flush()
            continue
        buf.append(line)
    flush()

    # Merge sub-MIN_CHUNK_CHARS paragraphs forward into the next one within
    # the same section, so we don't bloat the index with fragments.
    merged: list[tuple[str, str]] = []
    pending: tuple[str, str] | None = None
    for sec, para in paragraphs:
        if pending and pending[0] == sec:
            para = (pending[1] + " " + para).strip()
            pending = None
        if len(para) < MIN_CHUNK_CHARS:
            pending = (sec, para)
            continue
        merged.append((sec, para))
    if pending:
        # Stash the trailing fragment as its own chunk if nothing to merge into.
        merged.append(pending)

    return title, merged


def build_section_index(section_dir: Path) -> tuple[int, int]:
    """Build and pickle `<section_dir>/search_index.pkl`. Returns (#chunks, #pages)."""
    pages_dir = section_dir / "pages"
    if not pages_dir.is_dir():
        raise FileNotFoundError(f"missing pages dir: {pages_dir}")

    chunks: list[Chunk] = []
    n_pages = 0
    for page_path in sorted(pages_dir.glob("*.md")):
        slug = page_path.stem
        try:
            text = page_path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"  ! could not read {page_path}: {exc}", file=sys.stderr)
            continue
        _title, paragraphs = parse_page_for_chunks(text)
        n_pages += 1
        for i, (sec, para) in enumerate(paragraphs):
            chunks.append(Chunk(slug=slug, section_title=sec, chunk_index=i, text=para))

    if not chunks:
        raise RuntimeError(f"no chunks produced from {pages_dir}")

    print(f"  tokenizing {len(chunks)} chunks from {n_pages} pages...", flush=True)
    tokenized = [tokenize(c.text) for c in chunks]
    # Drop chunks whose token list is empty (image-only paragraphs etc).
    keep = [(c, toks) for c, toks in zip(chunks, tokenized) if toks]
    chunks = [c for c, _ in keep]
    tokenized = [toks for _, toks in keep]

    from rank_bm25 import BM25Okapi  # type: ignore[import-not-found]
    print(f"  fitting BM25 over {len(chunks)} non-empty chunks...", flush=True)
    bm25 = BM25Okapi(tokenized)

    payload = {
        "format_version": INDEX_FORMAT_VERSION,
        "chunks": chunks,
        "bm25": bm25,
    }
    out_path = section_dir / "search_index.pkl"
    # Pickle protocol 4 — stable across modern Python, allows large objects.
    with open(out_path, "wb") as f:
        pickle.dump(payload, f, protocol=4)
    print(f"  wrote {out_path} ({out_path.stat().st_size // 1024} KB)", flush=True)
    return len(chunks), n_pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--section",
        choices=["education", "cases"],
        default=None,
        help="build for one section (default: build both)",
    )
    parser.add_argument(
        "--out",
        default="journal",
        help="parent journal directory (default: journal)",
    )
    args = parser.parse_args()

    sections = [args.section] if args.section else ["education", "cases"]
    started = time.monotonic()
    failed = 0
    for section in sections:
        section_dir = Path(args.out) / section
        if not section_dir.is_dir():
            print(f"[bm25] {section}: no directory at {section_dir}, skipping.", file=sys.stderr)
            continue
        print(f"[bm25] {section}: building index in {section_dir}...", flush=True)
        try:
            n_chunks, n_pages = build_section_index(section_dir)
        except Exception as exc:  # noqa: BLE001
            print(f"[bm25] {section}: FAILED — {type(exc).__name__}: {exc}", file=sys.stderr)
            failed += 1
            continue
        print(f"[bm25] {section}: {n_chunks} chunks, {n_pages} pages.", flush=True)

    elapsed = time.monotonic() - started
    print(f"[bm25] done in {elapsed:.1f}s.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
