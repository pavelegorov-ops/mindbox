"""Bilingual tokenizer for BM25 indexing of the MindBox journal.

Russian queries that should match English-named tags ("retention",
"churn", "open rate") and vice versa are the core motivation for going
through a real lemmatizer/stemmer instead of a naive `re.split`. Both
build_bm25.py and journal_search.py import `tokenize` from here so the
index and the query go through identical normalization.

Module name is `_journal_tokens` (not `_tokenize`) because Python 3.12+
ships a builtin `_tokenize` C extension that wins any local import.

Lazy-init pattern: pymorphy3's MorphAnalyzer is heavy (~2s startup,
~150 MB RAM). We build it once on first use, then cache.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache


@dataclass
class Chunk:
    """One BM25-indexed paragraph and its metadata.

    Lives here (not in build_bm25.py) so the pickled search index
    references `_journal_tokens.Chunk` and unpickles cleanly from any
    entry point — `journal_search.py`, the test suite, ad-hoc REPLs.
    Defining it in `__main__` breaks the moment a different script
    tries to load the index.
    """
    slug: str
    section_title: str  # last seen H2/H3 above the paragraph; "" before any heading
    chunk_index: int    # 0-based position within the article
    text: str           # raw paragraph text (kept for snippet rendering)


_TOKEN_RE = re.compile(r"[A-Za-zА-Яа-яЁё][A-Za-zА-Яа-яЁё0-9_-]*|\d+(?:[.,]\d+)?")

# Common Russian stop words. Short, hand-curated — bigger lists drag in
# words like "большой" / "новый" that carry meaning in this corpus.
_RU_STOPWORDS = {
    "и", "в", "не", "на", "что", "с", "по", "из", "к", "у", "но", "или",
    "это", "как", "так", "же", "уже", "ещё", "еще", "тут", "там", "то",
    "был", "была", "были", "быть", "есть", "нет", "его", "её", "их",
    "мы", "вы", "ты", "он", "она", "они", "оно", "при", "от", "до", "за",
    "для", "над", "под", "без", "через", "между", "о", "об", "обо",
    "если", "когда", "потому", "поэтому", "также", "тоже", "лишь",
    "только", "очень", "бы", "ли", "же", "ну", "да", "вот", "ведь",
    "наш", "ваш", "свой", "этот", "тот", "такой",
}

# English stop words (subset of NLTK's; avoid the dependency on a download).
_EN_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "in", "on", "for",
    "with", "to", "from", "by", "at", "as", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "this", "that", "these", "those", "it", "its", "we", "you", "they",
    "he", "she", "i", "not", "no", "yes",
}

STOPWORDS = _RU_STOPWORDS | _EN_STOPWORDS


@lru_cache(maxsize=1)
def _morph_analyzer():
    """Lazy pymorphy3.MorphAnalyzer; None if pymorphy3 isn't installed.

    Falling back to an unstemmed pipeline is fine — recall drops on
    Russian morphology, but the script still produces a usable index.
    """
    try:
        import pymorphy3  # type: ignore[import-not-found]
        return pymorphy3.MorphAnalyzer()
    except Exception:  # noqa: BLE001 — any failure → fallback
        return None


@lru_cache(maxsize=1)
def _en_stemmer():
    """Lazy NLTK Snowball English stemmer; None if nltk isn't installed."""
    try:
        from nltk.stem.snowball import SnowballStemmer  # type: ignore[import-not-found]
        return SnowballStemmer("english")
    except Exception:  # noqa: BLE001
        return None


def _is_cyrillic(token: str) -> bool:
    return any("а" <= ch <= "я" or ch == "ё" or "А" <= ch <= "Я" or ch == "Ё" for ch in token)


@lru_cache(maxsize=200_000)
def _normalize_token(token: str) -> str:
    """Lemmatize Russian, stem English. Returns "" for tokens to drop."""
    low = token.lower()
    if low in STOPWORDS or len(low) < 2:
        return ""
    if _is_cyrillic(low):
        morph = _morph_analyzer()
        if morph is not None:
            parsed = morph.parse(low)
            if parsed:
                return parsed[0].normal_form
        return low
    # English / numeric / mixed
    stemmer = _en_stemmer()
    if stemmer is not None and low.isalpha():
        return stemmer.stem(low)
    return low


def tokenize(text: str) -> list[str]:
    """Text → list of normalized tokens for BM25 (both index and query)."""
    out: list[str] = []
    for raw in _TOKEN_RE.findall(text):
        norm = _normalize_token(raw)
        if norm:
            out.append(norm)
    return out
