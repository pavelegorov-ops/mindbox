import importlib.util
import json
import re
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_mcp_scenarios.py"


def load_module():
    spec = importlib.util.spec_from_file_location("render_mcp_scenarios", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def flow(blocks, *, row_version="rv-1", orphan=None):
    return {
        "scenarioId": 1,
        "versionNumber": 3,
        "rowVersion": row_version,
        "settings": {"repeatSettings": {"customer": {"$type": "defaultRepeatStrategy"}}},
        "orphanBranchStartBlockIds": orphan or [],
        "blocks": blocks,
    }


def test_complete_snapshot_renders_raw_predicate_binding_and_stable_repeat(tmp_path):
    module = load_module()
    blocks = [
        {"id": "B_start", "type": "inboundEventBlock", "name": "Start", "next": [{"output": "B_start:default", "index": 1, "blockId": "B_mail"}], "properties": {"condition": {"filter": {"raw": "kept"}}}},
        {"id": "B_mail", "type": "operationStepsBlockSettings", "name": "Send", "next": [], "properties": {"stepGroup": {"steps": [{"mailing": {"internalId": "campaign-guid", "name": "Campaign", "channelViewModel": {"systemName": "Email"}}, "mode": "Default"}]}}},
    ]
    staging = tmp_path / "staging"
    staging.mkdir()
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3, "versions": [{"number": 3, "status": "Execution"}]}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow(blocks)), encoding="utf-8")
    out = tmp_path / "out"

    result = module.ingest(staging, out, observed_at="2026-10-20T10:00:00Z")
    assert result["complete"] is True
    assert (out / "latest.json").exists()
    card = (out / "rendered.md").read_text(encoding="utf-8")
    assert "campaign-guid" in card
    assert "not-read" in card  # email content needs a separate campaign_get envelope
    assert '"raw": "kept"' in card
    first = (out / "rendered.md").read_bytes()
    second = module.ingest(staging, out, observed_at="2026-10-20T11:00:00Z")
    assert second["changed"] is False
    assert (out / "rendered.md").read_bytes() == first


def test_incomplete_or_rowversion_mismatch_does_not_promote_latest(tmp_path):
    module = load_module()
    out = tmp_path / "out"
    good = tmp_path / "good"
    good.mkdir()
    (good / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3}), encoding="utf-8")
    (good / "flows_lookup_full.json").write_text(json.dumps(flow([])), encoding="utf-8")
    module.ingest(good, out, observed_at="2026-10-20T10:00:00Z")
    latest = (out / "latest.json").read_bytes()

    bad = tmp_path / "bad"
    bad.mkdir()
    (bad / "flows_get.json").write_text("{}", encoding="utf-8")
    (bad / "flows_lookup_full.json").write_text(json.dumps(flow([], row_version="")), encoding="utf-8")
    result = module.ingest(bad, out, observed_at="2026-10-20T11:00:00Z")
    assert result["complete"] is False
    assert (out / "latest.json").read_bytes() == latest


def test_changed_input_writes_meaningful_deterministic_diff(tmp_path):
    module = load_module()
    staging = tmp_path / "staging"
    staging.mkdir()
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3, "versions": [{"number": 3, "status": "Execution"}]}), encoding="utf-8")
    original = [{"id": "B_start", "type": "inboundEventBlock", "next": [], "properties": {"flag": "before"}}]
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow(original)), encoding="utf-8")
    out = tmp_path / "out"
    module.ingest(staging, out, observed_at="2026-10-20T10:00:00Z")

    changed = [{"id": "B_start", "type": "inboundEventBlock", "next": [], "properties": {"flag": "after"}}]
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow(changed, row_version="rv-2")), encoding="utf-8")
    result = module.ingest(staging, out, observed_at="2026-10-20T10:01:00Z")
    diff = (out / "latest-diff.md").read_text(encoding="utf-8")

    assert result["complete"] is True
    assert "## block `B_start`" in diff
    assert '"flag": "before"' in diff
    assert '"flag": "after"' in diff
    assert "No configuration changes." not in diff


def test_equal_comparable_snapshots_have_no_changes_diff():
    module = load_module()
    snapshot = {"version": {"active": 3}, "settings": {}, "blocks": {}, "bindings": []}
    assert module.render_diff(snapshot, snapshot) == "# MCP snapshot diff\n\nNo configuration changes.\n"


def test_campaign_cards_preserve_raw_html_and_mark_missing_push_content(tmp_path):
    module = load_module()
    campaigns = {
        "email-guid": {
            "result": """Campaign: Test email  [Email]
internalId: email-guid  |  systemName: TestEmail
state: working  |  kind: automatic  |  readyForSending: no
rowVersion: 12

## Email variants (1)
[1] variant variant-guid
     subject: \"Subject\"
     sender: Example Store <help@example.test>
     preheader: \"Preheader\"
     format: Html · active (Rawhtml)  formatInternalId: format-guid  html: yes  ready: yes

     ── Html · active body · raw HTML (Rawhtml) ──
<!doctype html><html><body>exact body</body></html>
     format: Html · draft (Rawhtml)  formatInternalId: draft-format-guid  html: yes  ready: yes

     ── Html · draft body · raw HTML (Rawhtml) ──
<!doctype html><html><body>draft body</body></html>
"""
        },
        "push-guid": {"result": "Campaign: Test push  [MobilePush]\ninternalId: push-guid\nstate: working"},
    }
    blocks = [
        {"id": "B_mail", "name": "Email step", "properties": {"stepGroup": {"steps": [{"mailing": {"internalId": "email-guid", "name": "Test email", "channelViewModel": {"systemName": "Email"}}, "mode": "Default"}]}}},
        {"id": "B_push", "name": "Push step", "properties": {"stepGroup": {"steps": [{"mailing": {"internalId": "push-guid", "name": "Test push", "channelViewModel": {"systemName": "MobilePush"}}, "mode": "Default"}]}}},
        {"id": "B_push_again", "name": "Shared push step", "properties": {"stepGroup": {"steps": [{"mailing": {"internalId": "push-guid", "name": "Test push", "channelViewModel": {"systemName": "MobilePush"}}, "mode": "Test"}]}}},
    ]
    module.write_communication_docs(tmp_path, "snapshots/v3-example", blocks, campaigns)

    card = (tmp_path / "communications" / "email-guid" / "card.md").read_text(encoding="utf-8")
    source = tmp_path / "communications" / "email-guid" / "email" / "variant-guid" / "format-guid-active.html"
    draft = tmp_path / "communications" / "email-guid" / "email" / "variant-guid" / "draft-format-guid-draft.html"
    push_card = (tmp_path / "communications" / "push-guid" / "card.md").read_text(encoding="utf-8")
    assert source.read_text(encoding="utf-8") == "<!doctype html><html><body>exact body</body></html>\n"
    assert draft.read_text(encoding="utf-8") == "<!doctype html><html><body>draft body</body></html>\n"
    assert "active (Rawhtml)" in card and "draft (Rawhtml)" in card
    assert "subject: Subject" in card
    assert "Rawhtml" in card
    assert "snapshots/v3-example/campaigns/email-guid.json" in card
    assert "содержимое не получено" in push_card
    assert "B_push_again" in push_card
    assert "mode: `Test`" in push_card
    assert "campaign_get response did not return push title/body/image/deeplink fields" in push_card


def test_versioned_snapshot_cards_resolve_to_its_own_raw_campaign_and_html(tmp_path):
    module = load_module()
    blocks = [
        {"id": "B_start", "type": "inboundEventBlock", "next": [{"blockId": "B_mail"}], "properties": {}},
        {"id": "B_mail", "name": "Email step", "next": [], "properties": {"stepGroup": {"steps": [{"mailing": {"internalId": "email-guid", "name": "Campaign", "channelViewModel": {"systemName": "Email"}}, "mode": "Default"}]}}},
    ]
    staging = tmp_path / "staging"
    campaigns = staging / "campaigns"
    campaigns.mkdir(parents=True)
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow(blocks)), encoding="utf-8")

    def envelope(body):
        return {"result": f'''Campaign: Test email  [Email]
state: working

## Email variants (1)
[1] variant variant-guid
     subject: "Subject"
     sender: sender@example.test
     preheader: "Preheader"
     format: Html · active (Rawhtml)  formatInternalId: format-guid  html: yes

     ── Html · active body · raw HTML (Rawhtml) ──
{body}
'''}

    campaign_path = campaigns / "email-guid.json"
    campaign_path.write_text(json.dumps(envelope("<html>old</html>")), encoding="utf-8")
    out = tmp_path / "out"
    first = module.ingest(staging, out, observed_at="2026-10-20T10:00:00Z")
    first_snapshot = Path(first["snapshot"])

    campaign_path.write_text(json.dumps(envelope("<html>new</html>")), encoding="utf-8")
    second = module.ingest(staging, out, observed_at="2026-10-20T11:00:00Z")
    second_snapshot = Path(second["snapshot"])

    assert first_snapshot != second_snapshot
    for rendered in (out / "rendered.md", first_snapshot / "rendered.md", second_snapshot / "rendered.md"):
        card_target = rendered.parent / "communications" / "email-guid" / "card.md"
        if rendered.parent.name == "out":
            card_target = out / "communications" / "email-guid" / "card.md"
        assert card_target.exists(), rendered
        card = card_target.read_text(encoding="utf-8")
        raw_link = re.search(r"\]\(([^)]+campaigns/email-guid\.json)\)", card)
        html_link = re.search(r"\]\((email/[^)]+\.html)\)", card)
        assert raw_link and (card_target.parent / raw_link.group(1)).resolve().is_file()
        assert html_link and (card_target.parent / html_link.group(1)).resolve().is_file()

    old_html = first_snapshot / "communications" / "email-guid" / "email" / "variant-guid" / "format-guid-active.html"
    new_html = second_snapshot / "communications" / "email-guid" / "email" / "variant-guid" / "format-guid-active.html"
    assert old_html.read_text(encoding="utf-8") == "<html>old</html>\n"
    assert new_html.read_text(encoding="utf-8") == "<html>new</html>\n"
    assert (out / "communications" / "email-guid" / "email" / "variant-guid" / "format-guid-active.html").read_text(encoding="utf-8") == "<html>new</html>\n"


def seed_complete_snapshot(module, tmp_path):
    staging = tmp_path / "good"
    staging.mkdir()
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow([])), encoding="utf-8")
    out = tmp_path / "out"
    assert module.ingest(staging, out, observed_at="2026-10-20T10:00:00Z")["complete"] is True
    return staging, out, (out / "latest.json").read_bytes()


def test_identity_mismatch_does_not_promote_latest(tmp_path):
    module = load_module()
    staging, out, latest = seed_complete_snapshot(module, tmp_path)
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 111, "activeVersion": 3}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(flow([]) | {"scenarioId": 222}), encoding="utf-8")

    result = module.ingest(staging, out, observed_at="2026-10-20T11:00:00Z")

    assert result["complete"] is False
    assert "flowId differs from scenarioId" in result["errors"]
    assert (out / "latest.json").read_bytes() == latest


def test_missing_scenario_id_does_not_promote_latest(tmp_path):
    module = load_module()
    staging, out, latest = seed_complete_snapshot(module, tmp_path)
    missing_scenario_id = flow([])
    del missing_scenario_id["scenarioId"]
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(missing_scenario_id), encoding="utf-8")

    result = module.ingest(staging, out, observed_at="2026-10-20T11:00:00Z")

    assert result["complete"] is False
    assert "scenarioId absent" in result["errors"]
    assert (out / "latest.json").read_bytes() == latest


def test_missing_settings_does_not_promote_latest(tmp_path):
    module = load_module()
    staging, out, latest = seed_complete_snapshot(module, tmp_path)
    missing_settings = flow([])
    del missing_settings["settings"]
    (staging / "flows_get.json").write_text(json.dumps({"flowId": 1, "activeVersion": 3}), encoding="utf-8")
    (staging / "flows_lookup_full.json").write_text(json.dumps(missing_settings), encoding="utf-8")

    result = module.ingest(staging, out, observed_at="2026-10-20T11:00:00Z")

    assert result["complete"] is False
    assert "settings absent" in result["errors"]
    assert (out / "latest.json").read_bytes() == latest
