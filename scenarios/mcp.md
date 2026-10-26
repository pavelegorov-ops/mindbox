# MCP-first scenario snapshot contract

This is the generic, tenant-free entry point for current live scenario
configuration. Tenant business data belongs only under
`private/<tenant>/scenarios/mcp/`.

1. A read-only native Mindbox MCP collector calls `flows_get` to pin an active
   version, or an explicitly requested draft; it never selects the maximum
   version by inference.
2. It calls `flows_lookup(detail=Full, structure=Full, includeExecutions=false)`
   for that exact version and stores both raw envelopes in `staging/`.
3. `scripts/render_mcp_scenarios.py` accepts only a complete, coherent pair.
   It requires matching `flows_get.flowId` and Full `scenarioId`, an object
   `settings`, active/version equality, `rowVersion`, graph targets,
   reachability and orphan starts. Failed or partial input never advances
   `latest.json`.
4. `campaign_get` envelopes are optional provenance for bindings. For a requested
   communication pass, fetch every unique bound Email with
   `includeBodyForVariants="*"` and each unique MobilePush once. The renderer
   makes a campaign card per GUID, keeps every bound step (a campaign can be
   shared), separates Active/Draft formats, and saves raw HTML only when MCP
   returns it; visual-editor source is labelled as such, never as HTML. Cards
   link to their raw envelope and email sources. Push title/body/image/deeplink
   are documented only when returned; otherwise the card says **«содержимое не
   получено»** and names the absent API fields. Readable docs must not embed
   signed preview URLs. Campaign state/readiness and Active format do not
   establish approval, launch, delivery or recipient rendering.
5. Every coherent input is canonicalized into a versioned snapshot. The
   renderer preserves raw block properties/predicates and emits a deterministic
   readable diff against the preceding coherent snapshot across version/status,
   settings, block properties/connections and bindings.

`src/`, `rendered/`, `schema.md`, `template.yaml`, and
`scripts/render_scenarios.py` remain an archival YAML/DOM route. They are not a
fallback for an incomplete MCP capture and cannot establish current live state.
