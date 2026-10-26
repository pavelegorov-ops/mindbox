"""Render a complete MCP flow snapshot without interpreting Mindbox predicates.

Input directory must contain the exact JSON envelopes saved by a read-only MCP
collector: flows_get.json and flows_lookup_full.json. The collector (agent or
Hermes registry adapter) is intentionally outside this deterministic renderer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_if_changed(path: Path, data: bytes) -> bool:
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def as_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def active_version(flow_get: dict[str, Any]) -> int | None:
    for key in ("activeVersion", "activeVersionNumber"):
        version = as_int(flow_get.get(key))
        if version is not None:
            return version
    # Adapter-friendly fallback: exact statuses, never max(version).
    for item in flow_get.get("versions", []):
        if isinstance(item, dict) and item.get("status") == "Execution":
            return as_int(item.get("number", item.get("versionNumber")))
    # Native MCP's flows_get is a human-readable envelope; preserve it raw,
    # but deterministically pin its explicitly reported active version.
    summary = flow_get.get("result")
    if isinstance(summary, str):
        match = re.search(r"^active version:\s*(\d+)\b", summary, flags=re.MULTILINE)
        if match:
            return int(match.group(1))
    return None


def campaign_summary(campaigns: dict[str, Any], guid: str, channel: str) -> str:
    envelope = campaigns.get(guid)
    if envelope is None:
        return "not-read" if channel == "Email" else "unknown"
    return "read (campaign_get envelope)"


def campaign_text(envelope: Any) -> str:
    if not isinstance(envelope, dict):
        return ""
    value = envelope.get("result")
    return value if isinstance(value, str) else ""


def field_after(text: str, label: str) -> str | None:
    """Return a complete one-line MCP field, including nested quoted expressions."""
    match = re.search(rf"^\s*{re.escape(label)}:\s*(.*?)\s*$", text, re.MULTILINE)
    if not match:
        return None
    value = match.group(1)
    return value[1:-1] if len(value) >= 2 and value.startswith('"') and value.endswith('"') else value


def email_sources(text: str) -> list[dict[str, str]]:
    """Extract MCP-reported email format sources without converting editor JSX to HTML."""
    found: list[dict[str, str]] = []
    variant_matches = list(re.finditer(r"^\[(?:\d+)] variant ([^\s]+)", text, re.MULTILINE))
    for index, variant_match in enumerate(variant_matches):
        section = text[variant_match.end() : variant_matches[index + 1].start() if index + 1 < len(variant_matches) else len(text)]
        variant = variant_match.group(1)
        formats = list(re.finditer(r"^\s*format: (.*?)  formatInternalId: ([^\s]+).*?(?:\n|$)", section, re.MULTILINE))
        for format_index, format_match in enumerate(formats):
            format_section = section[format_match.end() : formats[format_index + 1].start() if format_index + 1 < len(formats) else len(section)]
            format_description, format_id = format_match.groups()
            state_match = re.search(r"·\s*(active|draft)\b", format_description, re.I)
            state = state_match.group(1).lower() if state_match else "unknown"
            body_marker = re.search(r"^\s*── .*? body · (raw HTML|visual editor source) \(([^)]+)\) ──\s*$", format_section, re.MULTILINE)
            metadata = {"variant": variant, "format_id": format_id, "state": state, "description": format_description, "subject": field_after(section, "subject") or "unavailable", "sender": field_after(section, "sender") or "unavailable", "preheader": field_after(section, "preheader") or "unavailable"}
            if not body_marker:
                found.append(metadata | {"source_type": "unavailable", "body": ""})
                continue
            body_start = body_marker.end()
            if format_section[body_start : body_start + 2] == "\r\n":
                body_start += 2
            elif format_section[body_start : body_start + 1] == "\n":
                body_start += 1
            terminator = re.search(r"^[ \t]*── end body ──[ \t]*\r?$", format_section[body_start:], re.MULTILINE)
            if terminator:
                body = format_section[body_start : body_start + terminator.start()]
                if body.endswith("\r\n"):
                    body = body[:-2]
                elif body.endswith("\n"):
                    body = body[:-1]
            else:
                # Older MCP responses have no terminator; retain the established fallback.
                body = format_section[body_start:].strip("\n")
            found.append(metadata | {"source_type": "html" if body_marker.group(1) == "raw HTML" else "visual-editor-source", "body": body})
    return found


def write_communication_docs(out: Path, raw_campaigns_rel: str, blocks: list[dict[str, Any]], campaigns: dict[str, Any]) -> bool:
    """Write campaign cards and only MCP-returned email sources from one snapshot."""
    changed = False
    by_guid: dict[str, list[dict[str, str]]] = {}
    for binding in bindings(blocks, campaigns):
        by_guid.setdefault(binding["guid"], []).append(binding)
    for guid, references in sorted(by_guid.items()):
        text = campaign_text(campaigns.get(guid))
        channel = references[0]["channel"]
        card_lines = [f"# Campaign `{guid}`", "", "## Bound scenario steps", ""]
        for reference in references:
            card_lines.append(f"- `{reference['block']}` — {reference['block_name']} (mode: `{reference['mode']}`)")
        card_lines += ["", "## MCP metadata", "", f"- name: {field_after(text, 'Campaign') or references[0]['name']}", f"- channel: {channel}", f"- state: {field_after(text, 'state') or 'unavailable'}", f"- rowVersion: {field_after(text, 'rowVersion') or 'unavailable'}", f"- raw source: [`campaigns/{guid}.json`]({raw_campaigns_rel}/campaigns/{guid}.json)", ""]
        if channel == "Email":
            card_lines += ["## Email metadata", ""]
            card_lines += ["", "## Formats", ""]
            sources = email_sources(text)
            if not sources:
                card_lines.append("- содержимое не получено: `campaign_get(includeBodyForVariants='*')` returned no format body.")
            for source in sources:
                base = f"email/{source['variant']}/{source['format_id']}-{source['state']}"
                card_lines += [f"- variant `{source['variant']}`; {source['description']}", f"  - subject: {source['subject']}", f"  - sender: {source['sender']}", f"  - preheader: {source['preheader']}"]
                if source["source_type"] == "html":
                    target = out / "communications" / guid / f"{base}.html"
                    changed |= write_if_changed(target, source["body"].encode() + b"\n")
                    card_lines.append(f"  - source: raw HTML — [`{base}.html`]({base}.html)")
                elif source["source_type"] == "visual-editor-source":
                    target = out / "communications" / guid / f"{base}.txt"
                    changed |= write_if_changed(target, source["body"].encode() + b"\n")
                    card_lines.append(f"  - source: visual-editor source (not HTML) — [`{base}.txt`]({base}.txt)")
                else:
                    card_lines.append("  - содержимое не получено.")
        elif channel == "MobilePush":
            card_lines += ["## Push content", "", "**содержимое не получено** — campaign_get response did not return push title/body/image/deeplink fields. This does not mean the push does not exist.", ""]
        else:
            card_lines += ["## Content", "", "содержимое не получено: unsupported channel in this MCP-first renderer.", ""]
        changed |= write_if_changed(out / "communications" / guid / "card.md", "\n".join(card_lines).encode() + b"\n")
    return changed


def bindings(blocks: list[dict[str, Any]], campaigns: dict[str, Any] | None = None) -> list[dict[str, str]]:
    campaigns = campaigns or {}
    found: list[dict[str, str]] = []
    for block in blocks:
        props = block.get("properties") if isinstance(block.get("properties"), dict) else {}
        group = props.get("stepGroup") if isinstance(props.get("stepGroup"), dict) else {}
        for step in group.get("steps", []):
            if not isinstance(step, dict) or not isinstance(step.get("mailing"), dict):
                continue
            mailing = step["mailing"]
            channel = mailing.get("channelViewModel") if isinstance(mailing.get("channelViewModel"), dict) else {}
            found.append({
                "block": str(block.get("id", "")), "block_name": str(block.get("name", "")),
                "guid": str(mailing.get("internalId", "")), "name": str(mailing.get("name", "")),
                "channel": str(channel.get("systemName", "unknown")), "mode": str(step.get("mode", "unknown")),
                "content": campaign_summary(campaigns, str(mailing.get("internalId", "")), str(channel.get("systemName", "unknown"))),
            })
    return sorted(found, key=lambda item: (item["block"], item["guid"]))


def validate(flow_get: Any, full: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(flow_get, dict) or not isinstance(full, dict):
        return ["invalid JSON envelope"]
    flow_id, scenario_id = as_int(flow_get.get("flowId")), as_int(full.get("scenarioId"))
    active, version = active_version(flow_get), as_int(full.get("versionNumber"))
    if flow_id is None: errors.append("flowId absent")
    if scenario_id is None: errors.append("scenarioId absent")
    if flow_id is not None and scenario_id is not None and flow_id != scenario_id: errors.append("flowId differs from scenarioId")
    if active is None: errors.append("active version absent")
    if version is None: errors.append("Full version absent")
    if active is not None and version is not None and active != version: errors.append("Full version differs from active version")
    if not full.get("rowVersion"): errors.append("rowVersion absent")
    if not isinstance(full.get("settings"), dict): errors.append("settings absent")
    blocks = full.get("blocks")
    if not isinstance(blocks, list): return errors + ["blocks absent"]
    ids = {b.get("id") for b in blocks if isinstance(b, dict) and b.get("id")}
    for block in blocks:
        if not isinstance(block, dict):
            errors.append("non-object block")
            continue
        for edge in block.get("next", []):
            if isinstance(edge, dict) and edge.get("blockId") and edge["blockId"] not in ids:
                errors.append(f"missing edge target {edge['blockId']}")
    starts = [b["id"] for b in blocks if isinstance(b, dict) and b.get("type") == "inboundEventBlock"]
    if starts:
        seen, queue = set(starts), list(starts)
        by_id = {b.get("id"): b for b in blocks if isinstance(b, dict)}
        while queue:
            for edge in by_id[queue.pop(0)].get("next", []):
                target = edge.get("blockId") if isinstance(edge, dict) else None
                if target in by_id and target not in seen: seen.add(target); queue.append(target)
        if len(seen) != len(ids): errors.append(f"unreachable blocks: {len(ids - seen)}")
    if full.get("orphanBranchStartBlockIds"): errors.append("orphan branch starts reported")
    return errors


def render(full: dict[str, Any], campaigns: dict[str, Any] | None = None) -> str:
    blocks = full["blocks"]
    lines = ["# MCP snapshot", "", f"- version: `{full['versionNumber']}`", f"- rowVersion: `{full['rowVersion']}`", "", "## Settings", "", "```json", json.dumps(full["settings"], ensure_ascii=False, sort_keys=True, indent=2), "```", "", "## Bindings", "", "| Block | Campaign GUID | Name | Channel | Mode | Content | Card |", "|---|---|---|---|---|---|---|"]
    for item in bindings(blocks, campaigns): lines.append(f"| `{item['block']}` | `{item['guid']}` | {item['name']} | {item['channel']} | {item['mode']} | {item['content']} | [card](communications/{item['guid']}/card.md) |")
    lines += ["", "## Graph", "", "```mermaid", "flowchart TD"]
    for block in blocks:
        label = str(block.get("name") or block.get("type") or block.get("id")).replace('"', "'")
        lines.append(f'  {block["id"]}["{label}"]')
        for edge in block.get("next", []):
            if isinstance(edge, dict) and edge.get("blockId"): lines.append(f'  {block["id"]} -->|{edge.get("output", "")}| {edge["blockId"]}')
    lines += ["```", "", "## Original predicates and block properties", ""]
    for block in sorted(blocks, key=lambda item: str(item.get("id", ""))):
        lines += [f"### `{block.get('id')}` — {block.get('name', '')}", "```json", json.dumps(block.get("properties", {}), ensure_ascii=False, sort_keys=True, indent=2), "```", ""]
    return "\n".join(lines)


def comparable(flow_get: dict[str, Any], full: dict[str, Any], campaigns: dict[str, Any]) -> dict[str, Any]:
    return {
        "version": {"active": active_version(flow_get), "full": full.get("versionNumber"), "status": flow_get.get("versions", flow_get.get("result"))},
        "settings": full["settings"],
        "blocks": {str(block.get("id")): {"properties": block.get("properties", {}), "next": block.get("next", [])} for block in full.get("blocks", []) if isinstance(block, dict)},
        "bindings": bindings(full.get("blocks", []), campaigns),
    }


def render_diff(previous: dict[str, Any], current: dict[str, Any]) -> str:
    lines = ["# MCP snapshot diff", ""]
    changes = 0
    for field in ("version", "settings", "bindings"):
        if previous.get(field) != current.get(field):
            changes += 1
            lines += [f"## {field}", "```json", json.dumps({"before": previous.get(field), "after": current.get(field)}, ensure_ascii=False, sort_keys=True, indent=2), "```", ""]
    old_blocks, new_blocks = previous.get("blocks", {}), current.get("blocks", {})
    for block_id in sorted(set(old_blocks) | set(new_blocks)):
        if old_blocks.get(block_id) != new_blocks.get(block_id):
            changes += 1
            lines += [f"## block `{block_id}`", "```json", json.dumps({"before": old_blocks.get(block_id), "after": new_blocks.get(block_id)}, ensure_ascii=False, sort_keys=True, indent=2), "```", ""]
    return "\n".join(lines if changes else lines + ["No configuration changes.", ""])


def ingest(staging: Path, out: Path, *, observed_at: str | None = None) -> dict[str, Any]:
    try:
        flow_get, full = read_json(staging / "flows_get.json"), read_json(staging / "flows_lookup_full.json")
    except (OSError, json.JSONDecodeError) as exc:
        return {"complete": False, "error": str(exc)}
    errors = validate(flow_get, full)
    if errors: return {"complete": False, "errors": errors}
    campaigns = {}
    campaigns_dir = staging / "campaigns"
    if campaigns_dir.is_dir():
        for path in sorted(campaigns_dir.glob("*.json")):
            campaigns[path.stem] = read_json(path)
    identity = {"scenarioId": full.get("scenarioId"), "versionNumber": full["versionNumber"], "rowVersion": full["rowVersion"]}
    payload = {"identity": identity, "flows_get": flow_get, "flows_lookup_full": full, "campaigns": campaigns}
    digest = hashlib.sha256(canonical(payload)).hexdigest()
    snapshot = out / "snapshots" / f"v{identity['versionNumber']}-{digest[:12]}"
    changed = False
    changed |= write_if_changed(snapshot / "flows_get.json", canonical(flow_get) + b"\n")
    changed |= write_if_changed(snapshot / "flows_lookup_full.json", canonical(full) + b"\n")
    for guid, envelope in campaigns.items():
        changed |= write_if_changed(snapshot / "campaigns" / f"{guid}.json", canonical(envelope) + b"\n")
    # Observation time is metadata only: an unchanged config keeps generated bytes stable.
    manifest_path = snapshot / "manifest.json"
    if not manifest_path.exists():
        changed |= write_if_changed(manifest_path, canonical({"complete": True, "observed_at": observed_at or datetime.now(timezone.utc).isoformat(), "sha256": digest, **identity}) + b"\n")
    rendered = render(full, campaigns).encode() + b"\n"
    changed |= write_if_changed(snapshot / "rendered.md", rendered)
    changed |= write_communication_docs(snapshot, "../..", full["blocks"], campaigns)
    changed |= write_communication_docs(out, f"../../{snapshot.relative_to(out).as_posix()}", full["blocks"], campaigns)
    previous_latest = read_json(out / "latest.json") if (out / "latest.json").exists() else None
    if previous_latest and previous_latest.get("snapshot") != snapshot.name:
        previous_dir = out / "snapshots" / previous_latest["snapshot"]
        previous_campaigns = {path.stem: read_json(path) for path in (previous_dir / "campaigns").glob("*.json")}
        previous = comparable(read_json(previous_dir / "flows_get.json"), read_json(previous_dir / "flows_lookup_full.json"), previous_campaigns)
        diff = render_diff(previous, comparable(flow_get, full, campaigns)).encode() + b"\n"
        changed |= write_if_changed(snapshot / f"diff-from-{previous_latest['snapshot']}.md", diff)
        changed |= write_if_changed(out / "latest-diff.md", diff)
    # latest is advanced only after all complete artifacts are written.
    changed |= write_if_changed(out / "latest.json", canonical({"complete": True, "snapshot": snapshot.name, "sha256": digest, **identity}) + b"\n")
    changed |= write_if_changed(out / "rendered.md", rendered)
    return {"complete": True, "snapshot": str(snapshot), "sha256": digest, "changed": changed}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging", type=Path, required=True, help="directory with raw MCP JSON envelopes")
    parser.add_argument("--out", type=Path, required=True, help="scenario/version output root")
    parser.add_argument("--observed-at")
    args = parser.parse_args()
    result = ingest(args.staging, args.out, observed_at=args.observed_at)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result.get("complete") else 1

if __name__ == "__main__": raise SystemExit(main())
