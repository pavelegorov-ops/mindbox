"""Render Markdown documentation for MindBox trigger scenarios.

Source: ``scenarios/src/*.yaml`` (one file per scenario, hand-edited).
Output: ``scenarios/rendered/`` containing per-scenario cards, an INDEX,
a reverse-dependency index, and an ``issues.md`` validator report.

Usage:

    python render_scenarios.py             # incremental: rewrite only changed files
    python render_scenarios.py --full      # force rewrite everything
    python render_scenarios.py --dry-run   # report without writing files

Exit code is 0 when all scenarios validate, 1 when at least one scenario
emitted hard errors (warnings never fail the build).

Design decisions live in ``scenarios/schema.md``. Block-type reference is
[docs/index/scenarii.md](docs/index/scenarii.md).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent  # scripts/.. = repo root
PRIVATE_DIR = ROOT / "private"
DOCS_SUMMARIES = ROOT / "docs" / "summaries.json"
HELP_BASE = "https://help.mindbox.ru/docs"


def _detect_tenant(explicit: str | None) -> str | None:
    """Find the active tenant under ``private/``.

    Returns ``None`` when no tenant is present (the engine then runs in
    "no business data" mode and exits cleanly). Raises ``SystemExit`` with
    a human message when several tenants exist and ``--tenant`` is required.
    """
    if explicit:
        path = PRIVATE_DIR / explicit
        if not path.is_dir():
            sys.stderr.write(
                f"[render] tenant '{explicit}' not found at {path}\n"
            )
            raise SystemExit(2)
        return explicit
    if not PRIVATE_DIR.is_dir():
        return None
    candidates = [
        p.name for p in PRIVATE_DIR.iterdir()
        if p.is_dir() and p.name != "_template" and not p.name.startswith(".")
    ]
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    sys.stderr.write(
        f"[render] multiple tenants under private/: {sorted(candidates)}. "
        f"Pass --tenant <name> to choose one explicitly.\n"
    )
    raise SystemExit(2)


def tenant_paths(tenant: str | None) -> tuple[Path, Path]:
    """Return ``(src_dir, out_dir)`` for the active tenant.

    When ``tenant`` is ``None`` we still return paths under ``private/``
    so the rest of the code can call ``discover_yaml_files`` and get an
    empty list cleanly.
    """
    if tenant is None:
        return PRIVATE_DIR / "_no_tenant" / "scenarios" / "src", PRIVATE_DIR / "_no_tenant" / "scenarios" / "rendered"
    base = PRIVATE_DIR / tenant / "scenarios"
    return base / "src", base / "rendered"


# Enum vocabularies. Source of truth is docs/index/scenarii.md and the
# schema.md doc — keep these lists in sync.
STATUS_VALUES = {"enabled", "draft", "stopped"}
TRIGGER_TYPES = {"event", "schedule"}
FREQUENCY_VALUES = {"once", "every", "per_period"}
SCHEDULE_MODES = {"daily", "weekly", "monthly"}
WEEKDAY_VALUES = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
BLOCK_TYPES = {"condition", "steps", "delay", "splitter", "ab_test", "limit"}
CONDITION_MODES = {"regular", "multibranch"}
DELAY_MODES = {"fixed", "interval", "dynamic"}
CONDITION_CONTEXTS = {
    "customer", "action", "order", "session", "product", "promotion",
    "segment", "subscription", "loyalty", "campaign",
}

# Block-type → docs slug mapping (from docs/index/scenarii.md "Блоки сценария").
BLOCK_TYPE_TO_SLUG: dict[str, str] = {
    "condition":  "workflow-conditions",
    "steps":      "workflow-steps",
    "delay":      "workflow-delay",
    "splitter":   "workflow-flow-splitter",
    "ab_test":    "workflow-ab-tests",
    "limit":      "workflow-limit",
}

# Recognised step.kind values. Anything else triggers a "Unknown step kind"
# warning but is otherwise allowed through.
STEP_KIND_TO_DEPS: dict[str, str] = {
    "email":          "email_templates",
    "sms":            "sms_templates",
    "viber":          "viber_templates",
    "push":           "push_templates",
    "wallet":         "wallet_templates",
    "webhook":        "webhooks",
    "edit_customer": "custom_fields",
    "change_balance": "",
}

# Mermaid colours per block type. Hex chosen so light themes stay legible.
BLOCK_CSS = {
    "condition": "fill:#cfe9ff,stroke:#3a7bd5,color:#053",
    "steps":     "fill:#cdebcd,stroke:#3aa345,color:#053",
    "delay":     "fill:#e0e0e0,stroke:#777,color:#222",
    "splitter":  "fill:#ffe0b8,stroke:#cc7a00,color:#222",
    "ab_test":   "fill:#e2cdf7,stroke:#7a3fb0,color:#222",
    "limit":     "fill:#fff2b3,stroke:#b3a000,color:#222",
}
END_CSS_DONE = "fill:#bcd9ff,stroke:#1f4faa,color:#053"
END_CSS_STOP = "fill:#ffc4c4,stroke:#aa1f1f,color:#330"

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class Block:
    id: str
    type: str
    raw: dict[str, Any]

    @property
    def edges(self) -> dict[str, str]:
        """Normalised mapping label → target id (block or end)."""
        out: dict[str, str] = {}
        edges = self.raw.get("edges") or {}
        if isinstance(edges, dict):
            for k, v in edges.items():
                if isinstance(v, str):
                    out[str(k)] = v
        if self.type == "splitter":
            for i, br in enumerate(self.raw.get("branches") or []):
                if isinstance(br, dict) and isinstance(br.get("next"), str):
                    label = f"{br.get('weight', '?')}%"
                    out[f"{label}#{i}"] = br["next"]
        if self.type == "ab_test":
            for i, var in enumerate(self.raw.get("variants") or []):
                if isinstance(var, dict) and isinstance(var.get("next"), str):
                    label = var.get("name") or f"V{i+1}"
                    label = f"{label} ({var.get('share', '?')}%)"
                    out[f"{label}#{i}"] = var["next"]
        return out


@dataclass
class Scenario:
    id: str
    source_path: Path
    raw: dict[str, Any]
    blocks: list[Block] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def title(self) -> str:
        return str(self.raw.get("title") or self.id)

    @property
    def status(self) -> str:
        return str(self.raw.get("status") or "")

    @property
    def folder(self) -> str:
        return str(self.raw.get("folder") or "")

    @property
    def trigger(self) -> dict[str, Any]:
        t = self.raw.get("trigger")
        return t if isinstance(t, dict) else {}

    @property
    def ends(self) -> dict[str, str]:
        e = self.raw.get("ends")
        if isinstance(e, dict):
            return {str(k): str(v) for k, v in e.items()}
        return {}

    @property
    def dependencies(self) -> dict[str, list[str]]:
        d = self.raw.get("dependencies")
        if not isinstance(d, dict):
            return {}
        out: dict[str, list[str]] = {}
        for k, v in d.items():
            if isinstance(v, list):
                out[str(k)] = [str(item) for item in v]
        return out

    def trigger_label(self) -> str:
        t = self.trigger
        kind = str(t.get("type") or "?")
        if kind == "event":
            return f"event · {t.get('event', '?')}"
        if kind == "schedule":
            sch = t.get("schedule") if isinstance(t.get("schedule"), dict) else {}
            mode = sch.get("mode") or "?"
            time_s = sch.get("time") or "?"
            tz = sch.get("timezone") or "?"
            spec = ""
            if mode == "weekly" and isinstance(sch.get("weekdays"), list):
                spec = " " + ",".join(str(x) for x in sch["weekdays"])
            elif mode == "monthly":
                if isinstance(sch.get("days"), list):
                    spec = " " + ",".join(str(x) for x in sch["days"])
                elif sch.get("day_of_month"):
                    spec = f" {sch['day_of_month']}"
            return f"schedule · {mode}{spec} {time_s} {tz}"
        return kind


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def discover_yaml_files(src_dir: Path) -> list[Path]:
    if not src_dir.is_dir():
        return []
    return sorted(
        p for p in src_dir.glob("*.yaml")
        if not p.name.startswith("_")
    )


def _normalise_yaml(node: Any) -> Any:
    """YAML 1.1 maps unquoted ``yes``/``no`` to booleans, ``on``/``off`` too.

    We rely on those tokens as edge labels for ``condition`` blocks, so walk
    every mapping and convert boolean keys back to ``"yes"``/``"no"`` strings.
    Values are left intact.
    """
    if isinstance(node, dict):
        out: dict[Any, Any] = {}
        for k, v in node.items():
            if isinstance(k, bool):
                k = "yes" if k else "no"
            out[k] = _normalise_yaml(v)
        return out
    if isinstance(node, list):
        return [_normalise_yaml(x) for x in node]
    return node


def load_scenario(path: Path) -> Scenario:
    with path.open("r", encoding="utf-8") as fh:
        try:
            raw = yaml.safe_load(fh)
        except yaml.YAMLError as exc:
            sc = Scenario(id=path.stem, source_path=path, raw={})
            sc.errors.append(f"YAML parse error: {exc}")
            return sc
    if not isinstance(raw, dict):
        sc = Scenario(id=path.stem, source_path=path, raw={})
        sc.errors.append("YAML root is not a mapping")
        return sc
    raw = _normalise_yaml(raw)

    sid = str(raw.get("id") or path.stem)
    sc = Scenario(id=sid, source_path=path, raw=raw)
    blocks_raw = raw.get("blocks") or []
    if isinstance(blocks_raw, list):
        for i, b in enumerate(blocks_raw):
            if not isinstance(b, dict):
                sc.errors.append(f"blocks[{i}] is not a mapping")
                continue
            bid = b.get("id")
            btype = b.get("type")
            if not isinstance(bid, str) or not bid:
                sc.errors.append(f"blocks[{i}].id missing or non-string")
                continue
            if not isinstance(btype, str) or not btype:
                sc.errors.append(f"blocks[{i}].type missing or non-string (id={bid})")
                continue
            sc.blocks.append(Block(id=bid, type=btype, raw=b))
    else:
        sc.errors.append("blocks must be a list")
    return sc


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_scenario(sc: Scenario) -> None:
    """Populate ``sc.errors`` / ``sc.warnings`` in-place."""
    if sc.errors:
        # Skip deeper checks on YAML-broken files; they will be reported anyway.
        pass

    if not sc.raw.get("title"):
        sc.errors.append("title is required")
    if not sc.raw.get("folder"):
        sc.errors.append("folder is required")
    if sc.status and sc.status not in STATUS_VALUES:
        sc.errors.append(f"status='{sc.status}' not in {sorted(STATUS_VALUES)}")
    if not sc.status:
        sc.errors.append("status is required")

    _validate_trigger(sc)
    _validate_blocks(sc)
    _validate_dependencies(sc)
    _check_patterns(sc)


def _validate_trigger(sc: Scenario) -> None:
    t = sc.trigger
    if not t:
        sc.errors.append("trigger is required")
        return
    kind = t.get("type")
    if kind not in TRIGGER_TYPES:
        sc.errors.append(f"trigger.type='{kind}' not in {sorted(TRIGGER_TYPES)}")
    if kind == "event" and not t.get("event"):
        sc.errors.append("trigger.event is required when type=event")
    if kind == "schedule":
        _validate_schedule(sc, t.get("schedule"))
    _validate_pre_filters(sc, t.get("pre_filters"))
    fpc = t.get("frequency_per_customer")
    if fpc is not None and fpc not in FREQUENCY_VALUES:
        sc.errors.append(
            f"trigger.frequency_per_customer='{fpc}' not in {sorted(FREQUENCY_VALUES)}"
        )
    if fpc == "per_period":
        pp = t.get("per_period")
        if not isinstance(pp, dict) or not pp.get("every"):
            sc.errors.append(
                "trigger.frequency_per_customer=per_period requires "
                "trigger.per_period.every"
            )
    fpo = t.get("frequency_per_order")
    if fpo is not None and fpo not in FREQUENCY_VALUES:
        sc.errors.append(
            f"trigger.frequency_per_order='{fpo}' not in {sorted(FREQUENCY_VALUES)}"
        )


def _validate_schedule(sc: Scenario, sch: Any) -> None:
    if not isinstance(sch, dict):
        sc.errors.append("trigger.schedule is required when type=schedule (mapping)")
        return
    mode = sch.get("mode")
    if mode not in SCHEDULE_MODES:
        sc.errors.append(
            f"trigger.schedule.mode='{mode}' not in {sorted(SCHEDULE_MODES)}"
        )
    time_s = sch.get("time")
    if not isinstance(time_s, str) or not re.fullmatch(r"\d{1,2}:\d{2}", time_s or ""):
        sc.errors.append(
            "trigger.schedule.time is required (string HH:MM, e.g. '14:10')"
        )
    if not sch.get("timezone"):
        sc.errors.append("trigger.schedule.timezone is required (e.g. 'Europe/Moscow')")
    if mode == "weekly":
        wd = sch.get("weekdays")
        if not isinstance(wd, list) or not wd:
            sc.errors.append(
                "trigger.schedule.weekdays is required for mode=weekly (non-empty list)"
            )
        else:
            bad = [x for x in wd if x not in WEEKDAY_VALUES]
            if bad:
                sc.errors.append(
                    f"trigger.schedule.weekdays contains unknown values {bad}; "
                    f"allowed: {sorted(WEEKDAY_VALUES)}"
                )
    if mode == "monthly":
        days = sch.get("days")
        dom = sch.get("day_of_month")
        if days is None and dom is None:
            sc.errors.append(
                "trigger.schedule for mode=monthly requires either 'days' "
                "(list of int) or 'day_of_month'"
            )
        if days is not None and (
            not isinstance(days, list) or not all(isinstance(x, int) for x in days)
        ):
            sc.errors.append("trigger.schedule.days must be a list of integers")


def _validate_pre_filters(sc: Scenario, pf: Any) -> None:
    if pf is None:
        return
    if not isinstance(pf, dict):
        sc.errors.append(
            "trigger.pre_filters must be a mapping with 'summary' (and optional 'detail')"
        )
        return
    summary = pf.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        sc.errors.append("trigger.pre_filters.summary is required (non-empty string)")
    detail = pf.get("detail")
    if detail is not None and not isinstance(detail, list):
        sc.errors.append("trigger.pre_filters.detail must be a list (when present)")


def _validate_blocks(sc: Scenario) -> None:
    if not sc.blocks:
        sc.errors.append("blocks: at least one block required")
        return

    # Duplicate IDs
    seen: set[str] = set()
    for b in sc.blocks:
        if b.id in seen:
            sc.errors.append(f"duplicate block id '{b.id}'")
        seen.add(b.id)

    block_ids = {b.id for b in sc.blocks}
    end_ids = set(sc.ends.keys())

    # Per-type required-fields and edges shape
    for b in sc.blocks:
        _validate_block_shape(sc, b)

    # Edge resolution
    referenced_ends: set[str] = set()
    referenced_blocks: set[str] = set()
    for b in sc.blocks:
        for label, target in b.edges.items():
            if target in block_ids:
                referenced_blocks.add(target)
            elif target in end_ids:
                referenced_ends.add(target)
            else:
                sc.errors.append(
                    f"{b.id}.edges.{label.split('#')[0]} references unknown block "
                    f"or end '{target}'"
                )

    # Unused ends / undeclared ends
    for end in end_ids - referenced_ends:
        sc.errors.append(f"end '{end}' declared in 'ends' but not referenced in any edges")
    # Note: unknown end refs are already caught above as "unknown block or end".

    # Dead blocks (no incoming reference). Entry block = first block — always alive.
    if sc.blocks:
        entry = sc.blocks[0].id
        for b in sc.blocks[1:]:
            if b.id not in referenced_blocks:
                sc.errors.append(f"block '{b.id}' is unreachable (no incoming edges)")
        # The entry block needs no validation — trigger reaches it implicitly.
        _ = entry


def _validate_block_shape(sc: Scenario, b: Block) -> None:
    if b.type not in BLOCK_TYPES:
        sc.errors.append(f"{b.id}.type='{b.type}' not in {sorted(BLOCK_TYPES)}")
        return

    raw = b.raw
    edges = raw.get("edges") or {}
    if not isinstance(edges, dict):
        edges = {}

    if b.type == "condition":
        mode = raw.get("mode")
        if mode not in CONDITION_MODES:
            sc.errors.append(
                f"{b.id}.mode='{mode}' not in {sorted(CONDITION_MODES)}"
            )
        if not raw.get("context"):
            sc.errors.append(f"{b.id}.context is required for condition")
        elif raw.get("context") not in CONDITION_CONTEXTS:
            sc.warnings.append(
                f"{b.id}.context='{raw.get('context')}' is not a known condition context"
            )
        if not raw.get("summary"):
            sc.errors.append(f"{b.id}.summary is required for condition")
        # filters_detail shape (optional). Accepts either:
        #   - list[str]   — verbatim filter lines as in MindBox UI
        #   - list[dict]  — structured; if {field, op, value} present, rendered
        #                   as a triple, otherwise as YAML-flat key=value pairs
        fd = raw.get("filters_detail")
        if fd is not None:
            if not isinstance(fd, list):
                sc.errors.append(f"{b.id}.filters_detail must be a list")
            else:
                for i, f in enumerate(fd):
                    if not isinstance(f, (str, dict)):
                        sc.errors.append(
                            f"{b.id}.filters_detail[{i}] must be a string or mapping"
                        )
        # edges
        if mode == "regular":
            if set(edges.keys()) - {"yes", "no"}:
                sc.warnings.append(
                    f"{b.id}.edges has unexpected keys for regular condition: "
                    f"{sorted(edges.keys())}"
                )
            for k in ("yes", "no"):
                if k not in edges:
                    sc.errors.append(f"{b.id}.edges.{k} is required for regular condition")
        elif mode == "multibranch":
            if not edges:
                sc.errors.append(f"{b.id}.edges must have at least one branch for multibranch")
        if "on_fail" in edges:
            sc.errors.append(f"{b.id}.edges.on_fail not allowed on condition")

    elif b.type == "steps":
        if not raw.get("actuality"):
            sc.errors.append(f"{b.id}.actuality is required for steps")
        steps = raw.get("steps")
        if not isinstance(steps, list) or not steps:
            sc.errors.append(f"{b.id}.steps must be a non-empty list")
        else:
            for i, s in enumerate(steps):
                _validate_step(sc, b, i, s)
        if "next" not in edges:
            sc.errors.append(f"{b.id}.edges.next is required for steps")

    elif b.type == "delay":
        mode = raw.get("mode")
        if mode not in DELAY_MODES:
            sc.errors.append(f"{b.id}.mode='{mode}' not in {sorted(DELAY_MODES)}")
        if mode == "fixed" and not raw.get("duration"):
            sc.errors.append(f"{b.id}.duration is required for delay mode=fixed")
        if mode == "dynamic":
            for k in ("source", "field_name", "offset"):
                if k not in raw:
                    sc.errors.append(f"{b.id}.{k} is required for delay mode=dynamic")
        if "next" not in edges:
            sc.errors.append(f"{b.id}.edges.next is required for delay")
        if "on_fail" in edges:
            sc.errors.append(f"{b.id}.edges.on_fail not allowed on delay")

    elif b.type == "splitter":
        branches = raw.get("branches")
        if not isinstance(branches, list) or len(branches) < 2:
            sc.errors.append(f"{b.id}.branches must have at least 2 entries")
        else:
            for i, br in enumerate(branches):
                if not isinstance(br, dict):
                    sc.errors.append(f"{b.id}.branches[{i}] must be a mapping")
                    continue
                if "weight" not in br:
                    sc.errors.append(f"{b.id}.branches[{i}].weight is required")
                if "next" not in br:
                    sc.errors.append(f"{b.id}.branches[{i}].next is required")
        if "on_fail" in edges:
            sc.errors.append(f"{b.id}.edges.on_fail not allowed on splitter")

    elif b.type == "ab_test":
        if not raw.get("hypothesis"):
            sc.errors.append(f"{b.id}.hypothesis is required for ab_test")
        if not raw.get("primary_metric"):
            sc.errors.append(f"{b.id}.primary_metric is required for ab_test")
        variants = raw.get("variants")
        if not isinstance(variants, list) or len(variants) < 2:
            sc.errors.append(f"{b.id}.variants must have at least 2 entries")
        else:
            for i, var in enumerate(variants):
                if not isinstance(var, dict):
                    sc.errors.append(f"{b.id}.variants[{i}] must be a mapping")
                    continue
                if "share" not in var:
                    sc.errors.append(f"{b.id}.variants[{i}].share is required")
                if "next" not in var:
                    sc.errors.append(f"{b.id}.variants[{i}].next is required")
        if "on_fail" in edges:
            sc.errors.append(f"{b.id}.edges.on_fail not allowed on ab_test")

    elif b.type == "limit":
        for k in ("quantity", "period"):
            if k not in raw:
                sc.errors.append(f"{b.id}.{k} is required for limit")
        for k in ("до_лимита", "после_лимита"):
            if k not in edges:
                sc.errors.append(f"{b.id}.edges.{k} is required for limit")
        if "on_fail" in edges:
            sc.errors.append(f"{b.id}.edges.on_fail not allowed on limit")


def _validate_step(sc: Scenario, b: Block, i: int, s: Any) -> None:
    if not isinstance(s, dict):
        sc.errors.append(f"{b.id}.steps[{i}] must be a mapping")
        return
    kind = s.get("kind")
    if not kind:
        sc.errors.append(f"{b.id}.steps[{i}].kind is required")
        return
    if kind not in STEP_KIND_TO_DEPS:
        sc.warnings.append(f"Unknown step kind: '{kind}' (in {b.id}.steps[{i}])")
        return
    if kind == "email" and not s.get("template"):
        sc.errors.append(f"{b.id}.steps[{i}] (email) requires 'template'")
    if kind == "sms":
        if not s.get("template"):
            sc.errors.append(f"{b.id}.steps[{i}] (sms) requires 'template'")
        if not s.get("pool"):
            sc.errors.append(f"{b.id}.steps[{i}] (sms) requires 'pool'")
    if kind in ("viber", "push", "wallet") and not s.get("template"):
        sc.errors.append(f"{b.id}.steps[{i}] ({kind}) requires 'template'")
    if kind == "webhook" and not s.get("url"):
        sc.errors.append(f"{b.id}.steps[{i}] (webhook) requires 'url'")
    if kind == "edit_customer":
        st = s.get("set")
        if not isinstance(st, dict) or not st:
            sc.errors.append(
                f"{b.id}.steps[{i}] (edit_customer) requires non-empty 'set' map"
            )
    if kind == "change_balance" and "amount" not in s:
        sc.errors.append(f"{b.id}.steps[{i}] (change_balance) requires 'amount'")


_REQUIRED_DEP_KEYS = (
    "email_templates",
    "sms_templates",
    "push_templates",
    "viber_templates",
    "wallet_templates",
    "action_templates",
    "segments",
    "promo_pools",
    "webhooks",
    "custom_fields",
    "excludes_scenarios",
    "product_categories",
    "brands",
)


def _validate_dependencies(sc: Scenario) -> None:
    deps = sc.raw.get("dependencies")
    if not isinstance(deps, dict):
        sc.errors.append("dependencies is required (must be a mapping)")
        return
    for k in _REQUIRED_DEP_KEYS:
        if k not in deps:
            sc.errors.append(f"dependencies.{k} is required (use [] when empty)")
        elif not isinstance(deps[k], list):
            sc.errors.append(f"dependencies.{k} must be a list")


def _check_patterns(sc: Scenario) -> None:
    """Lightweight heuristics → warnings only."""
    by_id = {b.id: b for b in sc.blocks}

    # ab_test branches with differing delay durations
    for b in sc.blocks:
        if b.type != "ab_test":
            continue
        durations: list[tuple[str, Any]] = []
        for var in b.raw.get("variants") or []:
            if not isinstance(var, dict):
                continue
            nxt = var.get("next")
            if not isinstance(nxt, str):
                continue
            target = by_id.get(nxt)
            if target is not None and target.type == "delay":
                durations.append((nxt, target.raw.get("duration")))
        if durations:
            unique = {d[1] for d in durations}
            if len(unique) > 1:
                pretty = ", ".join(f"{n}:{d}" for n, d in durations)
                sc.warnings.append(
                    f"[PATTERN] ab_test '{b.id}' variants point to delays with "
                    f"different durations ({pretty}) — biases the experiment"
                )

        # condition between ab_test and its first steps block
        for var in b.raw.get("variants") or []:
            if not isinstance(var, dict):
                continue
            nxt = var.get("next")
            target = by_id.get(nxt) if isinstance(nxt, str) else None
            if target and target.type == "condition":
                sc.warnings.append(
                    f"[PATTERN] ab_test '{b.id}' branch goes through condition "
                    f"'{nxt}' before steps — distorts measurement purity"
                )

    # delay > 30d without exit_window
    for b in sc.blocks:
        if b.type != "delay":
            continue
        dur = b.raw.get("duration")
        if isinstance(dur, str):
            days = _parse_duration_days(dur)
            if days is not None and days > 30 and "exit_window" not in b.raw:
                sc.warnings.append(
                    f"[PATTERN] delay '{b.id}' duration={dur} (>30d) without "
                    f"exit_window — risk of clients stuck in the queue"
                )


_DURATION_RE = re.compile(r"^\s*(\d+)\s*([smhdw])\s*$", re.IGNORECASE)


def _parse_duration_days(s: str) -> float | None:
    m = _DURATION_RE.match(s)
    if not m:
        return None
    n = int(m.group(1))
    unit = m.group(2).lower()
    return {
        "s": n / 86400,
        "m": n / 1440,
        "h": n / 24,
        "d": float(n),
        "w": n * 7.0,
    }[unit]


# ---------------------------------------------------------------------------
# Cross-check against docs/summaries.json
# ---------------------------------------------------------------------------


def cross_check(scenarios: list[Scenario]) -> tuple[bool, str | None]:
    """Walk all valid scenarios and append [CROSS] warnings in-place.

    Returns (ran, skip_reason).  When summaries.json is missing we silently
    skip and report a single line in issues.md.
    """
    if not DOCS_SUMMARIES.exists():
        return False, f"docs/summaries.json missing — run sync.py to populate"

    try:
        payload = json.loads(DOCS_SUMMARIES.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return False, f"docs/summaries.json unreadable ({exc!r})"

    pages: dict[str, dict] = payload.get("pages") or {}
    if not isinstance(pages, dict):
        return False, "docs/summaries.json has no 'pages' mapping"

    # Pre-build search structures
    slug_set = set(pages.keys())
    title_lower_to_slug = {
        (p.get("title") or "").lower(): slug
        for slug, p in pages.items()
        if isinstance(p, dict)
    }

    for sc in scenarios:
        if sc.errors:
            # Skip cross-check for scenarios that already failed validation;
            # noisy and the [CROSS] codes are addressed separately.
            continue
        _cross_check_event(sc, pages, slug_set, title_lower_to_slug)
        _cross_check_block_types(sc, pages)
    return True, None


def _cross_check_event(
    sc: Scenario,
    pages: dict[str, dict],
    slug_set: set[str],
    title_lower_to_slug: dict[str, str],
) -> None:
    t = sc.trigger
    if t.get("type") != "event":
        return
    event = t.get("event")
    if not isinstance(event, str) or not event:
        return

    # Heuristic: look for events on workflow-events page or any page whose slug
    # contains the event name. Mindbox event ids are not always pages but the
    # workflow-events page lists most of them as headings.
    workflow_events = pages.get("workflow-events")
    if isinstance(workflow_events, dict):
        # The event name itself is likely not in headings (those are human
        # phrases), but we still grep slugs as a fallback.
        pass

    # Direct slug hit (rare but possible)
    if event in slug_set:
        page = pages[event]
        if isinstance(page, dict) and page.get("deprecation_hint"):
            sc.warnings.append(
                f"[CROSS] Uses deprecated function: '{page.get('title') or event}' "
                f"({HELP_BASE}/{event})"
            )
        return

    # Fuzzy: any slug starting with the event name
    for slug in slug_set:
        if slug == event or slug.startswith(event + "-") or slug.endswith("-" + event):
            page = pages[slug]
            if isinstance(page, dict) and page.get("deprecation_hint"):
                sc.warnings.append(
                    f"[CROSS] Trigger event '{event}' resolved to deprecated page "
                    f"'{page.get('title') or slug}' ({HELP_BASE}/{slug})"
                )
            return

    # Not found anywhere
    sc.warnings.append(
        f"[CROSS] Event '{event}' not found in MindBox docs corpus."
    )


def _cross_check_block_types(sc: Scenario, pages: dict[str, dict]) -> None:
    seen_slugs: set[str] = set()
    for b in sc.blocks:
        slug = BLOCK_TYPE_TO_SLUG.get(b.type)
        if not slug or slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        page = pages.get(slug)
        if not isinstance(page, dict):
            sc.warnings.append(
                f"[CROSS] Block type '{b.type}' has no docs page '{slug}' "
                f"in local corpus."
            )
            continue
        if page.get("deprecation_hint"):
            sc.warnings.append(
                f"[CROSS] Block type '{b.type}' page is flagged deprecated: "
                f"'{page.get('title') or slug}' ({HELP_BASE}/{slug})"
            )


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------


_MERMAID_SAFE_RE = re.compile(r'["`]')


def _mermaid_label(text: str) -> str:
    """Sanitize text for use inside a Mermaid node label.

    Mermaid supports ``<br/>`` for explicit line breaks inside quoted labels.
    Callers may pass embedded ``<br/>`` to split a label into two visual rows.
    """
    text = _MERMAID_SAFE_RE.sub("", text)
    text = text.replace("|", "/").replace("\n", " ")
    # Collapse runs of whitespace but preserve the explicit <br/> tokens.
    parts = text.split("<br/>")
    parts = [re.sub(r"\s+", " ", p).strip() for p in parts]
    text = "<br/>".join(parts)
    # Truncate the visible portion (count without the markup).
    visible = text.replace("<br/>", " ")
    if len(visible) > 90:
        # Cheap truncation: take first 80 chars of the joined form.
        text = text[:80].rstrip() + "..."
    return text


def _node_id(s: str) -> str:
    """Mermaid node ids must be ASCII-friendly; ends keys may be Russian."""
    return re.sub(r"[^A-Za-z0-9_]+", "_", s) or "node"


def render_mermaid(sc: Scenario) -> str:
    lines: list[str] = ["```mermaid", "flowchart TD"]
    # Class definitions
    for typ, css in BLOCK_CSS.items():
        lines.append(f"    classDef {typ} {css};")
    lines.append(f"    classDef end_done {END_CSS_DONE};")
    lines.append(f"    classDef end_stop {END_CSS_STOP};")

    # Trigger node
    trig_label = _mermaid_label(f"trigger<br/>{sc.trigger_label()}")
    lines.append(f'    TRIG(["{trig_label}"])')

    # Block nodes
    for b in sc.blocks:
        nid = _node_id(b.id)
        sub = _block_label(b)
        label = _mermaid_label(f"{b.id}: {b.type}<br/>{sub}")
        lines.append(f'    {nid}["{label}"]:::{b.type}')

    # End nodes
    for end_id, descr in sc.ends.items():
        nid = _node_id(end_id)
        cls = "end_done" if end_id.startswith("done") else "end_stop"
        label = _mermaid_label(f"{end_id}<br/>{descr}")
        lines.append(f'    {nid}(("{label}")):::{cls}')

    # Trigger -> first block
    if sc.blocks:
        first = _node_id(sc.blocks[0].id)
        lines.append(f"    TRIG --> {first}")

    # Edges
    for b in sc.blocks:
        src = _node_id(b.id)
        for label, target in b.edges.items():
            tgt = _node_id(target)
            clean_label = label.split("#")[0]
            arrow = "-..->" if clean_label == "on_fail" else "-->"
            if clean_label and clean_label not in ("next",):
                lines.append(f'    {src} {arrow}|{clean_label}| {tgt}')
            else:
                lines.append(f"    {src} {arrow} {tgt}")

    lines.append("```")
    return "\n".join(lines)


def _block_label(b: Block) -> str:
    """Short subline shown in the Mermaid node body."""
    if b.type == "condition":
        return str(b.raw.get("summary") or "")
    if b.type == "steps":
        kinds = []
        for s in b.raw.get("steps") or []:
            if isinstance(s, dict) and s.get("kind"):
                kinds.append(str(s.get("kind")))
        return ",".join(kinds)
    if b.type == "delay":
        if b.raw.get("mode") == "fixed":
            return f"fixed {b.raw.get('duration', '?')}"
        if b.raw.get("mode") == "dynamic":
            return f"dynamic ({b.raw.get('field_name', '?')})"
        return str(b.raw.get("mode") or "")
    if b.type == "splitter":
        weights = []
        for br in b.raw.get("branches") or []:
            if isinstance(br, dict):
                weights.append(str(br.get("weight", "?")))
        return "/".join(weights) + "%"
    if b.type == "ab_test":
        return str(b.raw.get("primary_metric") or "ab_test")
    if b.type == "limit":
        return f"{b.raw.get('quantity', '?')}/{b.raw.get('period', '?')}"
    return ""


def render_card(sc: Scenario) -> str:
    """Render a single scenario card. ``generated_at`` is intentionally
    omitted — we want byte-stable output across runs."""
    fm = {
        "id": sc.id,
        "title": sc.title,
        "status": sc.status,
        "folder": sc.folder,
        "trigger": sc.trigger_label(),
        "source_file": f"src/{sc.source_path.name}",
    }
    out: list[str] = ["---"]
    for k, v in fm.items():
        out.append(f"{k}: {_yaml_inline(v)}")
    out.append("---")
    out.append("")
    out.append(f"# {sc.title}")
    out.append("")
    notes = sc.raw.get("notes")
    if isinstance(notes, str) and notes.strip():
        out.append(notes.strip())
        out.append("")

    out.extend(_render_trigger_section(sc))

    out.append("## Диаграмма")
    out.append("")
    out.append(render_mermaid(sc))
    out.append("")

    out.append("## Блоки")
    out.append("")
    out.append("| id | type | mode | summary | edges |")
    out.append("|---|---|---|---|---|")
    for b in sc.blocks:
        mode = str(b.raw.get("mode") or "")
        summary = _block_label(b)
        edges_pretty = ", ".join(
            f"{k.split('#')[0]}→{v}" for k, v in b.edges.items()
        )
        out.append(
            f"| `{b.id}` | {b.type} | {mode} | {_md_cell(summary)} | "
            f"{_md_cell(edges_pretty)} |"
        )
    out.append("")

    out.append("## Карточки блоков")
    out.append("")
    for b in sc.blocks:
        out.extend(_render_block_card(b))
        out.append("")

    if sc.ends:
        out.append("## Концевые узлы")
        out.append("")
        out.append("| id | описание |")
        out.append("|---|---|")
        for k, v in sc.ends.items():
            out.append(f"| `{k}` | {_md_cell(v)} |")
        out.append("")

    out.append("## Зависимости")
    out.append("")
    deps = sc.dependencies
    any_dep = False
    for k in _REQUIRED_DEP_KEYS:
        items = deps.get(k) or []
        if not items:
            continue
        any_dep = True
        out.append(f"- **{k}**: " + ", ".join(f"`{x}`" for x in items))
    if not any_dep:
        out.append("_Нет объявленных зависимостей._")
    out.append("")

    return "\n".join(out).rstrip() + "\n"


def _render_trigger_section(sc: Scenario) -> list[str]:
    t = sc.trigger
    if not t:
        return []
    out: list[str] = ["## Триггер", ""]
    out.append(f"- **type:** {t.get('type', '?')}")
    if t.get("type") == "event":
        out.append(f"- **event:** `{t.get('event', '?')}`")
    if t.get("type") == "schedule" and isinstance(t.get("schedule"), dict):
        sch = t["schedule"]
        out.append(f"- **schedule:** {sch.get('mode', '?')} в {sch.get('time', '?')} "
                   f"({sch.get('timezone', '?')})")
        if sch.get("mode") == "weekly" and sch.get("weekdays"):
            out.append(f"  - **weekdays:** {', '.join(str(x) for x in sch['weekdays'])}")
        if sch.get("mode") == "monthly":
            if sch.get("days"):
                out.append(f"  - **days:** {', '.join(str(x) for x in sch['days'])}")
            if sch.get("day_of_month"):
                out.append(f"  - **day_of_month:** {sch['day_of_month']}")
    for k in ("frequency_per_customer", "frequency_per_order"):
        if t.get(k):
            out.append(f"- **{k}:** {t[k]}")
    pp = t.get("per_period")
    if isinstance(pp, dict) and pp.get("every"):
        out.append(f"- **per_period.every:** {pp['every']}")
    pf = t.get("pre_filters")
    if isinstance(pf, dict) and pf.get("summary"):
        out.append("")
        out.append("**Pre-filters (клиенты на запуске):**")
        out.append("")
        for line in str(pf["summary"]).splitlines():
            line = line.rstrip()
            if line:
                out.append(f"- {line}")
        detail = pf.get("detail")
        if isinstance(detail, list) and detail:
            out.append("")
            out.append("Pre-filters detail (структурно):")
            for d in detail:
                out.append(f"- `{d}`")
    out.append("")
    return out


def _render_block_card(b: Block) -> list[str]:
    out: list[str] = [f"### {b.id}: {b.type}"]
    raw = b.raw
    if raw.get("name"):
        out.append(f"- **name:** `{raw['name']}`")
    if b.type == "condition":
        out.append(f"- **mode:** {raw.get('mode', '')}")
        out.append(f"- **context:** {raw.get('context', '')}")
        if raw.get("summary"):
            out.append(f"- **summary:** {raw.get('summary')}")
        if isinstance(raw.get("filters_detail"), list) and raw["filters_detail"]:
            out.append("- **filters_detail:**")
            for f in raw["filters_detail"]:
                if isinstance(f, str):
                    out.append(f"    - {f}")
                elif isinstance(f, dict):
                    if {"field", "op", "value"} <= set(f.keys()):
                        out.append(
                            f"    - `{f.get('field')}` `{f.get('op')}` "
                            f"`{f.get('value')}`"
                        )
                    else:
                        kv = ", ".join(f"{k}={v!r}" for k, v in f.items())
                        out.append(f"    - {kv}")
    elif b.type == "steps":
        out.append(f"- **actuality:** {raw.get('actuality', '')}")
        for i, s in enumerate(raw.get("steps") or []):
            if not isinstance(s, dict):
                continue
            kind = s.get("kind", "?")
            extras = ", ".join(f"{k}={v!r}" for k, v in s.items() if k != "kind")
            out.append(f"- **steps[{i}]** `{kind}` — {extras}")
    elif b.type == "delay":
        out.append(f"- **mode:** {raw.get('mode', '')}")
        if raw.get("duration"):
            out.append(f"- **duration:** {raw.get('duration')}")
        for k in ("source", "field_name", "offset", "exit_window"):
            if k in raw:
                out.append(f"- **{k}:** {raw[k]}")
    elif b.type == "splitter":
        for i, br in enumerate(raw.get("branches") or []):
            if isinstance(br, dict):
                out.append(
                    f"- **branch {i}** weight={br.get('weight', '?')} → "
                    f"`{br.get('next', '?')}`"
                )
    elif b.type == "ab_test":
        out.append(f"- **hypothesis:** {raw.get('hypothesis', '')}")
        out.append(f"- **primary_metric:** {raw.get('primary_metric', '')}")
        for i, var in enumerate(raw.get("variants") or []):
            if isinstance(var, dict):
                out.append(
                    f"- **variant {i}** share={var.get('share', '?')} → "
                    f"`{var.get('next', '?')}`"
                )
    elif b.type == "limit":
        out.append(f"- **quantity:** {raw.get('quantity', '?')}")
        out.append(f"- **period:** {raw.get('period', '?')}")
        if "notify_threshold" in raw:
            out.append(f"- **notify_threshold:** {raw['notify_threshold']}")
    edges_pretty = ", ".join(
        f"`{k.split('#')[0]}` → `{v}`" for k, v in b.edges.items()
    )
    out.append(f"- **Edges:** {edges_pretty}")
    return out


def _yaml_inline(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return json.dumps(v)
    s = "" if v is None else str(v)
    if s == "" or re.search(r'[:#\-?&*!|>\'"%@`,\[\]\{\}\n]', s) or s.strip() != s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def _md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_index(scenarios: list[Scenario], generated_at: str) -> str:
    valid = [s for s in scenarios if not s.errors]
    counts = {k: 0 for k in STATUS_VALUES}
    for s in valid:
        if s.status in counts:
            counts[s.status] += 1
    out: list[str] = [
        "# Trigger scenarios — INDEX",
        "",
        f"Generated at {generated_at}.",
        "",
        f"Total: {len(valid)} valid scenarios "
        f"(enabled={counts['enabled']}, draft={counts['draft']}, "
        f"stopped={counts['stopped']}). See `issues.md` for warnings.",
        "",
        "| id | title | status | trigger | folder |",
        "|---|---|---|---|---|",
    ]
    sorted_valid = sorted(valid, key=lambda s: (s.folder, s.title.lower(), s.id))
    for s in sorted_valid:
        out.append(
            f"| [{s.id}]({s.id}.md) | {_md_cell(s.title)} | {s.status} | "
            f"{_md_cell(s.trigger_label())} | {_md_cell(s.folder)} |"
        )
    if not sorted_valid:
        out.append("| _no valid scenarios_ |  |  |  |  |")
    out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_dependencies(scenarios: list[Scenario]) -> str:
    """Reverse dependency index: category → value → list of scenarios."""
    valid = [s for s in scenarios if not s.errors]
    out: list[str] = [
        "# Reverse dependency index",
        "",
        "Each entry lists the scenarios that reference a given asset.",
        "Use this to answer 'what breaks if I delete X?'.",
        "",
    ]
    # Always include all known categories; show "_none_" for empty ones.
    for cat in _REQUIRED_DEP_KEYS:
        out.append(f"## {cat}")
        out.append("")
        bucket: dict[str, list[Scenario]] = {}
        for s in valid:
            for v in (s.dependencies.get(cat) or []):
                bucket.setdefault(v, []).append(s)
        if not bucket:
            out.append("_none_")
            out.append("")
            continue
        for v in sorted(bucket.keys()):
            refs = bucket[v]
            ref_links = ", ".join(
                f"[{r.id}]({r.id}.md)" for r in sorted(refs, key=lambda r: r.id)
            )
            out.append(f"- **`{v}`** — {ref_links}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_issues(
    scenarios: list[Scenario],
    cross_check_skipped: str | None,
    generated_at: str,
) -> str:
    out: list[str] = [
        "# Validator issues",
        "",
        f"Generated at {generated_at}.",
        "",
    ]
    if cross_check_skipped:
        out.append(f"_Cross-check skipped: {cross_check_skipped}_")
        out.append("")

    total_warn = sum(len(s.warnings) for s in scenarios)
    total_err = sum(len(s.errors) for s in scenarios)
    affected = sum(1 for s in scenarios if s.warnings or s.errors)
    out.append(
        f"Total: {total_err} errors, {total_warn} warnings across "
        f"{affected} scenarios."
    )
    out.append("")

    if total_err == 0 and total_warn == 0:
        out.append("No issues found.")
        out.append("")
        return "\n".join(out).rstrip() + "\n"

    for sc in sorted(scenarios, key=lambda s: s.id):
        if not sc.errors and not sc.warnings:
            continue
        out.append(f"## {sc.id}")
        out.append("")
        for e in sc.errors:
            out.append(f"- **[ERROR]** {e}")
        for w in sc.warnings:
            out.append(f"- {w}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------------------
# File I/O — idempotent writes
# ---------------------------------------------------------------------------


_TIMESTAMP_LINE_RE = re.compile(
    r"^Generated at \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\.?$",
    re.MULTILINE,
)


def _stable(content: str) -> str:
    """Strip variable lines (e.g. ``Generated at <timestamp>``) for hashing."""
    return _TIMESTAMP_LINE_RE.sub("Generated at <timestamp>.", content)


def write_if_changed(path: Path, content: str, *, dry_run: bool) -> str:
    """Returns 'created' | 'updated' | 'unchanged' | 'would-create' | 'would-update' | 'would-unchange'.

    Idempotency: ``Generated at <timestamp>`` lines are normalised before
    comparing so a re-run with no real changes leaves the file untouched.
    """
    exists = path.exists()
    same = False
    if exists:
        existing = path.read_text(encoding="utf-8")
        same = _stable(existing) == _stable(content)
    if dry_run:
        if not exists:
            return "would-create"
        if not same:
            return "would-update"
        return "would-unchange"
    if same:
        return "unchanged"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "created" if not exists else "updated"


def remove_stale(out_dir: Path, expected: set[str], *, dry_run: bool) -> list[str]:
    """Delete .md files in ``out_dir`` whose name is not in ``expected``."""
    removed: list[str] = []
    if not out_dir.is_dir():
        return removed
    for p in out_dir.glob("*.md"):
        if p.name in expected:
            continue
        removed.append(p.name)
        if not dry_run:
            p.unlink()
    return removed


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


@dataclass
class RenderStats:
    created: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    would_create: list[str] = field(default_factory=list)
    would_update: list[str] = field(default_factory=list)
    would_unchange: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)


def run(args: argparse.Namespace) -> int:
    if args.src or args.out:
        # Explicit overrides skip tenant detection — preserved for tests / CI.
        default_src, default_out = tenant_paths(_detect_tenant(args.tenant))
        src_dir = Path(args.src) if args.src else default_src
        out_dir = Path(args.out) if args.out else default_out
        tenant = args.tenant
    else:
        tenant = _detect_tenant(args.tenant)
        if tenant is None:
            print(
                "[render] no active tenant under private/ — engine has no "
                "business data to render. Clone a tenant repo into "
                "private/<name>/ to populate."
            )
            return 0
        src_dir, out_dir = tenant_paths(tenant)
        print(f"[render] active tenant: {tenant}")

    files = discover_yaml_files(src_dir)
    if not files:
        print(f"[render] no YAML files in {src_dir} — nothing to do.")
        if not args.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            write_if_changed(
                out_dir / "INDEX.md",
                render_index([], ts),
                dry_run=False,
            )
            write_if_changed(
                out_dir / "dependencies.md",
                render_dependencies([]),
                dry_run=False,
            )
            write_if_changed(
                out_dir / "issues.md",
                render_issues([], None, ts),
                dry_run=False,
            )
        return 0

    print(f"[render] discovered {len(files)} YAML files in {src_dir}")
    scenarios: list[Scenario] = [load_scenario(p) for p in files]

    # Duplicate scenario IDs across files → error reported on each duplicate.
    seen_ids: dict[str, Path] = {}
    for sc in scenarios:
        prev = seen_ids.get(sc.id)
        if prev is not None and prev != sc.source_path:
            sc.errors.append(
                f"duplicate scenario id '{sc.id}' (also defined in {prev.name})"
            )
        else:
            seen_ids[sc.id] = sc.source_path

    for sc in scenarios:
        validate_scenario(sc)

    cross_ran, cross_skip = cross_check(scenarios)
    if cross_ran:
        print("[render] cross-check against docs/summaries.json: ok")
    else:
        print(f"[render] cross-check skipped: {cross_skip}")

    valid_scenarios = [s for s in scenarios if not s.errors]
    invalid_scenarios = [s for s in scenarios if s.errors]
    print(
        f"[render] {len(valid_scenarios)} valid, "
        f"{len(invalid_scenarios)} with errors"
    )

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stats = RenderStats()
    expected_files = {"INDEX.md", "dependencies.md", "issues.md"}

    # Per-scenario cards
    for sc in valid_scenarios:
        target = out_dir / f"{sc.id}.md"
        expected_files.add(target.name)
        content = render_card(sc)
        result = write_if_changed(target, content, dry_run=args.dry_run or args.full and False)
        # `--full` forces rewrite even when content is unchanged so that file
        # mtimes match the run; we approximate by writing again only when changed
        # (idempotent semantics dominate). Implementation: --full just disables
        # the "unchanged" short-circuit by touching the file.
        if args.full and not args.dry_run and result == "unchanged":
            target.write_text(content, encoding="utf-8")
            result = "updated"
        _record(stats, result, target.name)

    # INDEX / dependencies / issues
    for name, content in (
        ("INDEX.md", render_index(scenarios, generated_at)),
        ("dependencies.md", render_dependencies(scenarios)),
        ("issues.md", render_issues(scenarios, cross_skip, generated_at)),
    ):
        target = out_dir / name
        result = write_if_changed(target, content, dry_run=args.dry_run)
        if args.full and not args.dry_run and result == "unchanged":
            target.write_text(content, encoding="utf-8")
            result = "updated"
        _record(stats, result, name)

    # Cleanup stale files
    if not args.dry_run:
        stats.removed = remove_stale(out_dir, expected_files, dry_run=False)
    else:
        stats.removed = remove_stale(out_dir, expected_files, dry_run=True)

    _print_summary(stats, args.dry_run, invalid_scenarios)
    return 1 if invalid_scenarios else 0


def _record(stats: RenderStats, result: str, name: str) -> None:
    target = {
        "created":         stats.created,
        "updated":         stats.updated,
        "unchanged":       stats.unchanged,
        "would-create":    stats.would_create,
        "would-update":    stats.would_update,
        "would-unchange":  stats.would_unchange,
    }.get(result)
    if target is not None:
        target.append(name)


def _print_summary(stats: RenderStats, dry_run: bool, invalid: list[Scenario]) -> None:
    if dry_run:
        print(
            f"[render] dry-run: {len(stats.would_create)} would create, "
            f"{len(stats.would_update)} would update, "
            f"{len(stats.would_unchange)} unchanged, "
            f"{len(stats.removed)} would remove"
        )
        for n in stats.would_create:
            print(f"    + would create scenarios/rendered/{n}")
        for n in stats.would_update:
            print(f"    ~ would update scenarios/rendered/{n}")
        for n in stats.removed:
            print(f"    - would remove scenarios/rendered/{n}")
    else:
        changed = len(stats.created) + len(stats.updated)
        print(
            f"[render] {changed} changed "
            f"({len(stats.created)} created, {len(stats.updated)} updated), "
            f"{len(stats.unchanged)} unchanged, "
            f"{len(stats.removed)} removed"
        )
        for n in stats.created:
            print(f"    + {n}")
        for n in stats.updated:
            print(f"    ~ {n}")
        for n in stats.removed:
            print(f"    - {n}")
    if invalid:
        print("[render] scenarios with errors (no Markdown emitted):")
        for sc in invalid:
            print(f"    ! {sc.id} ({sc.source_path.name}): {len(sc.errors)} errors")
            for e in sc.errors[:5]:
                print(f"        - {e}")
            if len(sc.errors) > 5:
                print(f"        ... and {len(sc.errors) - 5} more")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--tenant",
        help="tenant name under private/ (default: auto-detect when only one exists)",
    )
    parser.add_argument(
        "--src",
        help="source directory (default: private/<tenant>/scenarios/src)",
    )
    parser.add_argument(
        "--out",
        help="output directory (default: private/<tenant>/scenarios/rendered)",
    )
    parser.add_argument("--full", action="store_true", help="rewrite every file even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing files")
    args = parser.parse_args()
    try:
        return run(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
