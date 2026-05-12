"""Shared Anthropic client helpers for journal enrichment scripts.

Two responsibilities:

- Lazy SDK init with a clear "skip enrichment" signal when the SDK isn't
  installed or `ANTHROPIC_API_KEY` isn't set, so scripts can degrade
  gracefully instead of crashing the whole pipeline.
- A single `call_structured` helper that invokes Claude with a forced
  tool_use schema and returns the parsed JSON. This is how we get
  reliable structured output at temperature 0 without parsing free-form
  Markdown.

If you find yourself wrapping retries / parsing JSON-from-text in a
caller, push that here instead.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Any


# Default model — Haiku 4.5 is the cheapest model that handles the
# enrichment task well (Russian summaries, structured fact extraction).
# Switch to claude-sonnet-4-6 if quality is insufficient on a sample.
DEFAULT_MODEL = "claude-haiku-4-5-20251001"

# Conservative retry policy for transient errors (529 Overloaded, 5xx,
# rate limits). Anthropic SDK already retries 5xx internally, so this is
# the outer envelope — keeps a long enrichment run from dying on a single
# transient hiccup.
MAX_RETRIES = 4
RETRY_BASE_DELAY = 2.0  # seconds; doubled each attempt


class LLMUnavailable(RuntimeError):
    """Raised at startup if the SDK can't be loaded or the key is missing.

    Callers catch this and skip enrichment with a warning. Other errors
    (429, 500, malformed JSON) should NOT be wrapped in this — those are
    real failures that deserve a non-zero exit code.
    """


@dataclass
class LLMClient:
    """Thin wrapper around the Anthropic SDK with our defaults baked in."""

    client: Any                     # anthropic.Anthropic
    model: str = DEFAULT_MODEL

    def call_structured(
        self,
        *,
        system: str,
        user: str,
        tool_name: str,
        tool_description: str,
        tool_schema: dict,
        max_tokens: int = 1024,
    ) -> dict:
        """Invoke Claude and return the parsed `tool_use` input as a dict.

        Forces the model to call the named tool by setting `tool_choice`
        — this is the supported way to get strict-schema JSON output.
        Temperature is fixed at 0 to keep enrichment runs reproducible
        across re-invocations on the same content_hash.
        """
        last_err: Exception | None = None
        for attempt in range(MAX_RETRIES):
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    temperature=0,
                    system=system,
                    tools=[
                        {
                            "name": tool_name,
                            "description": tool_description,
                            "input_schema": tool_schema,
                        }
                    ],
                    tool_choice={"type": "tool", "name": tool_name},
                    messages=[{"role": "user", "content": user}],
                )
            except Exception as exc:  # noqa: BLE001 — SDK raises various subclasses
                last_err = exc
                if not _is_retriable(exc) or attempt == MAX_RETRIES - 1:
                    raise
                delay = RETRY_BASE_DELAY * (2**attempt)
                time.sleep(delay)
                continue

            for block in resp.content:
                # SDK objects: ToolUseBlock has .type == "tool_use" and .input
                if getattr(block, "type", None) == "tool_use" and getattr(block, "name", None) == tool_name:
                    inp = getattr(block, "input", None)
                    if isinstance(inp, dict):
                        return inp
            raise RuntimeError(
                f"Model did not return a tool_use block for {tool_name!r}; "
                f"stop_reason={getattr(resp, 'stop_reason', None)!r}"
            )
        # Unreachable — the loop either returns or raises.
        raise RuntimeError(f"unreachable; last error: {last_err!r}")


def _is_retriable(exc: BaseException) -> bool:
    """Return True for transient errors worth retrying."""
    name = type(exc).__name__
    # Anthropic SDK exception names: APIStatusError, RateLimitError,
    # APIConnectionError, APITimeoutError, InternalServerError, ...
    if name in {"RateLimitError", "APIConnectionError", "APITimeoutError", "InternalServerError"}:
        return True
    # APIStatusError carries a status_code; retry 5xx and 529.
    code = getattr(exc, "status_code", None)
    if isinstance(code, int) and (code >= 500 or code == 529):
        return True
    return False


def get_client(*, model: str = DEFAULT_MODEL) -> LLMClient:
    """Build an `LLMClient` or raise `LLMUnavailable` with a clear reason.

    The two failure modes a user can fix are checked first (no SDK,
    no key), so the warning printed by callers is actionable.
    """
    try:
        import anthropic  # type: ignore[import-not-found]
    except ImportError as exc:
        raise LLMUnavailable(
            "anthropic SDK is not installed. Run `pip install -r requirements.txt` "
            "from the repo root inside your .venv."
        ) from exc

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise LLMUnavailable(
            "ANTHROPIC_API_KEY is not set. Export it in your shell before running "
            "enrichment, or skip enrichment by running scrape_journal.py directly."
        )

    return LLMClient(client=anthropic.Anthropic(api_key=api_key), model=model)
