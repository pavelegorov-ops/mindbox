"""Query the BM25 index built by `build_bm25.py`.

Used by the agent (and humans) when `summaries.json` triage doesn't
surface the answer — typically when the user asks about a fact buried
in a long article ("у кого open rate выросла на 30%?") or hits the
RU↔EN vocabulary gap ("удержание" vs. "retention").

CLI (run from repo root):

    python scripts/journal_search.py "удержание клиентов"
    python scripts/journal_search.py "retention" --section education --top 10
    python scripts/journal_search.py "open rate" --format text

The default JSON output is designed for agent consumption — one array
of result objects, each with enough metadata (slug, source_url,
section_title, snippet, score) to decide whether to read the full page
via the Read tool.
"""

from __future__ import annotations

import argparse
import json
import pickle
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _journal_tokens import tokenize  # noqa: E402


SNIPPET_MAX_CHARS = 280


def load_index(section_dir: Path) -> tuple[object, list]:
    """Return (BM25 instance, list[Chunk]) for a section."""
    path = section_dir / "search_index.pkl"
    if not path.exists():
        raise FileNotFoundError(
            f"BM25 index missing at {path}. Build it with "
            f"`python scripts/build_bm25.py --section {section_dir.name}`."
        )
    with open(path, "rb") as f:
        payload = pickle.load(f)  # noqa: S301 — local trusted file
    return payload["bm25"], payload["chunks"]


def make_snippet(text: str, query_tokens: set[str]) -> str:
    """Highlight the densest window of query-token hits, ≤ SNIPPET_MAX_CHARS.

    Heuristic, not perfect — but for an agent-facing snippet the goal is
    "show enough context that the model can decide whether to read the
    full page", and a lemma-aware window beats raw truncation.
    """
    if len(text) <= SNIPPET_MAX_CHARS:
        return text
    words = re.findall(r"\S+", text)
    if not words:
        return text[:SNIPPET_MAX_CHARS]
    word_norms = [tokenize(w) for w in words]
    hits = [bool(set(ns) & query_tokens) for ns in word_norms]
    # Find the window of ~50 words with the most hits.
    window = 50
    best_start = 0
    best_score = -1
    for i in range(len(words)):
        score = sum(hits[i : i + window])
        if score > best_score:
            best_score = score
            best_start = i
    chosen = " ".join(words[best_start : best_start + window])
    if len(chosen) > SNIPPET_MAX_CHARS:
        chosen = chosen[: SNIPPET_MAX_CHARS - 1].rstrip(" ,.;:—-") + "…"
    prefix = "…" if best_start > 0 else ""
    suffix = "…" if best_start + window < len(words) else ""
    return f"{prefix}{chosen}{suffix}".strip()


def search_section(section_dir: Path, query: str, top_k: int) -> list[dict]:
    bm25, chunks = load_index(section_dir)
    query_tokens = tokenize(query)
    if not query_tokens:
        return []
    scores = bm25.get_scores(query_tokens)  # type: ignore[attr-defined]
    # Top-k by score, but keep only positive scores — zero means no match.
    ranked = sorted(
        ((s, i) for i, s in enumerate(scores) if s > 0),
        key=lambda x: x[0],
        reverse=True,
    )[:top_k]
    qtok_set = set(query_tokens)
    results: list[dict] = []
    section_name = section_dir.name
    for score, idx in ranked:
        chunk = chunks[idx]
        results.append(
            {
                "section": section_name,
                "slug": chunk.slug,
                "source_url": f"https://mindbox.ru/journal/{section_name}/{chunk.slug}/",
                "section_title": chunk.section_title,
                "score": round(float(score), 3),
                "snippet": make_snippet(chunk.text, qtok_set),
                "page_path": str(section_dir / "pages" / f"{chunk.slug}.md"),
            }
        )
    return results


def render_text(results: list[dict]) -> str:
    if not results:
        return "No matches.\n"
    out: list[str] = []
    for i, r in enumerate(results, 1):
        title_bit = f"{r['section']}/{r['slug']}"
        if r["section_title"]:
            title_bit += f"  ({r['section_title']})"
        out.append(f"[{i}] score={r['score']}  {title_bit}")
        out.append(f"    {r['source_url']}")
        out.append(f"    {r['snippet']}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    # Windows consoles default to cp1251/cp866 and choke on Cyrillic +
    # exotic spaces (U+202F) the corpus contains. Forcing UTF-8 here keeps
    # both `--format json` and `--format text` legible regardless of shell.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="search query (Russian or English)")
    parser.add_argument(
        "--section",
        choices=["education", "cases"],
        default=None,
        help="restrict search to one section (default: search both, merge results)",
    )
    parser.add_argument("--top", type=int, default=8, help="number of results (default: 8)")
    parser.add_argument(
        "--out",
        default="journal",
        help="parent journal directory (default: journal)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="output format (default: json — for agent consumption)",
    )
    args = parser.parse_args()

    sections = [args.section] if args.section else ["cases", "education"]
    all_results: list[dict] = []
    for section in sections:
        section_dir = Path(args.out) / section
        try:
            res = search_section(section_dir, args.query, args.top)
        except FileNotFoundError as exc:
            print(f"[search] {section}: {exc}", file=sys.stderr)
            continue
        all_results.extend(res)

    all_results.sort(key=lambda r: r["score"], reverse=True)
    all_results = all_results[: args.top]

    if args.format == "json":
        json.dump(all_results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(all_results))

    return 0


if __name__ == "__main__":
    sys.exit(main())
