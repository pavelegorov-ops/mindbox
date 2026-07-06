"""Shared LLM client helpers for journal enrichment scripts.

Supports two interchangeable backends, selected by the
`MINDBOX_LLM_PROVIDER` env var (default `anthropic`):

- `anthropic` — Claude via forced `tool_use` (the original path).
- `openai`    — GPT via forced function calling (`OPENAI_API_KEY`).

Both expose the same `call_structured` contract and are keyed on the
same retry envelope, so callers don't care which one is active.

Two responsibilities:

- Lazy SDK init with a clear "skip enrichment" signal when the SDK isn't
  installed or the provider's API key isn't set, so scripts can degrade
  gracefully instead of crashing the whole pipeline.
- A single `call_structured` helper that forces a strict-schema tool call
  and returns the parsed JSON. This is how we get reliable structured
  output at temperature 0 without parsing free-form Markdown.

If you find yourself wrapping retries / parsing JSON-from-text in a
caller, push that here instead.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any


# Default model — Haiku 4.5 is the cheapest model that handles the
# enrichment task well (Russian summaries, structured fact extraction).
# Switch to claude-sonnet-4-6 if quality is insufficient on a sample.
DEFAULT_MODEL = "claude-haiku-4-5-20251001"

# Default model for the OpenAI backend — gpt-4o-mini is the cheap tier;
# bump to gpt-4o if summary/fact quality is insufficient on a sample.
OPENAI_DEFAULT_MODEL = "gpt-4o-mini"

# Which env var holds the API key for each provider. Single source of
# truth so sync.py's pre-flight check and get_client() stay in sync.
PROVIDER_KEY_ENV = {
    "anthropic": "ANTHROPIC_API_KEY",
    "openai": "OPENAI_API_KEY",
}


def resolve_provider() -> str:
    """Active backend from `MINDBOX_LLM_PROVIDER` (default `anthropic`)."""
    return (os.environ.get("MINDBOX_LLM_PROVIDER") or "anthropic").strip().lower()

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
    """Thin wrapper around a provider SDK with our defaults baked in."""

    client: Any                     # anthropic.Anthropic | openai.OpenAI
    model: str = DEFAULT_MODEL
    provider: str = "anthropic"

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
        """Force a strict-schema tool call and return its input as a dict.

        Wraps the single-attempt provider call in a retry envelope for
        transient errors. Temperature is fixed at 0 to keep enrichment
        runs reproducible across re-invocations on the same content_hash.
        A non-retriable error (bad JSON, missing tool call) propagates.
        """
        kwargs = dict(
            system=system,
            user=user,
            tool_name=tool_name,
            tool_description=tool_description,
            tool_schema=tool_schema,
            max_tokens=max_tokens,
        )
        last_err: Exception | None = None
        for attempt in range(MAX_RETRIES):
            try:
                if self.provider == "openai":
                    return self._call_openai(**kwargs)
                return self._call_anthropic(**kwargs)
            except Exception as exc:  # noqa: BLE001 — SDK raises various subclasses
                last_err = exc
                if not _is_retriable(exc) or attempt == MAX_RETRIES - 1:
                    raise
                time.sleep(RETRY_BASE_DELAY * (2**attempt))
        # Unreachable — the loop either returns or raises.
        raise RuntimeError(f"unreachable; last error: {last_err!r}")

    def _call_anthropic(
        self, *, system, user, tool_name, tool_description, tool_schema, max_tokens
    ) -> dict:
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

    def _call_openai(
        self, *, system, user, tool_name, tool_description, tool_schema, max_tokens
    ) -> dict:
        resp = self.client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=0,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "description": tool_description,
                        "parameters": tool_schema,
                    },
                }
            ],
            tool_choice={"type": "function", "function": {"name": tool_name}},
        )
        choice = resp.choices[0]
        for call in choice.message.tool_calls or []:
            if call.function.name == tool_name:
                # Arguments come back as a JSON string — a decode error here
                # is a real failure (not retriable) and should propagate.
                return json.loads(call.function.arguments)
        raise RuntimeError(
            f"Model did not return a function call for {tool_name!r}; "
            f"finish_reason={choice.finish_reason!r}"
        )


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


def get_client(*, provider: str | None = None, model: str | None = None) -> LLMClient:
    """Build an `LLMClient` or raise `LLMUnavailable` with a clear reason.

    Provider is chosen by `MINDBOX_LLM_PROVIDER` (default `anthropic`).
    The two failure modes a user can fix are checked first (no SDK,
    no key), so the warning printed by callers is actionable.
    """
    provider = (provider or resolve_provider())
    if provider == "openai":
        return _build_openai(model)
    if provider == "anthropic":
        return _build_anthropic(model)
    raise LLMUnavailable(
        f"Unknown MINDBOX_LLM_PROVIDER={provider!r}; expected 'anthropic' or 'openai'."
    )


def _build_anthropic(model: str | None) -> LLMClient:
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

    return LLMClient(
        client=anthropic.Anthropic(api_key=api_key),
        model=model or DEFAULT_MODEL,
        provider="anthropic",
    )


def _build_openai(model: str | None) -> LLMClient:
    try:
        import openai  # type: ignore[import-not-found]
    except ImportError as exc:
        raise LLMUnavailable(
            "openai SDK is not installed. Run `pip install -r requirements.txt` "
            "from the repo root inside your .venv."
        ) from exc

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LLMUnavailable(
            "OPENAI_API_KEY is not set. Export it in your shell before running "
            "enrichment, or skip enrichment by running scrape_journal.py directly."
        )

    return LLMClient(
        client=openai.OpenAI(api_key=api_key),
        model=model or OPENAI_DEFAULT_MODEL,
        provider="openai",
    )
