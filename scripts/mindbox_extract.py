#!/usr/bin/env python3
"""
mindbox_extract.py — снять граф сценария из живой вкладки MindBox через CDP.

Транспорт: Chrome должен быть запущен с remote-debugging (порт 9222),
пользователь залогинен в MindBox и вкладку не закрывал (см. скилл
mindbox-browser-extraction). Скрипт сам находит нужный page-target в
`http://127.0.0.1:9222/json/list`, подключается к его WebSocket и гоняет
Runtime.evaluate — читает nodes/edges из React fiber и тексты фильтров
condition-блоков из открытой панели (?blockId=).

Использование:
    python mindbox_extract.py <scenario_url> [--filters] [--wait N]

  <scenario_url>   полный URL сценария, напр.
                   https://usmall.mindbox.ru/scenarios/250838/edit?version=draft
  --filters        дополнительно открыть каждый condition-блок (?blockId=)
                   и прочитать текст его фильтра (медленнее: по ~N сек на блок).
  --wait N         пауза после навигации, сек (по умолчанию 15).

Вывод — JSON на stdout. Скрипт НЕ пишет файлов и НЕ интерпретирует
семантику: только снимает сырые данные с графа, как они лежат в UI.

Зависимость: websockets (есть в venv hermes). Запускать тем же python.
"""
import sys, json, time, asyncio, urllib.request
import websockets

CDP_HTTP = "http://127.0.0.1:9222"


# --- JS-выражения (чистый ASCII — см. питфолл в скилле) ---

# Извлечь nodes/edges из React fiber, поднимаясь от первой .react-flow__node.
GET_GRAPH_JS = r"""
(() => {
  const el = document.querySelector('.react-flow__node');
  if (!el) return {error: 'no .react-flow__node in DOM'};
  const key = Object.keys(el).filter(k => k.startsWith('__reactInternalInstance'))[0];
  if (!key) return {error: 'no fiber key on node'};
  let f = el[key], depth = 0, nodes = null, edges = null;
  while (f && depth < 40 && (nodes === null || edges === null)) {
    const p = f.memoizedProps;
    if (nodes === null && p && Array.isArray(p.nodes) && p.nodes.length > 0) nodes = p.nodes;
    if (edges === null && p && Array.isArray(p.edges)) edges = p.edges;
    f = f.return; depth++;
  }
  if (!nodes) return {error: 'nodes not found in fiber (depth<40)'};
  const nodeSummary = nodes.map(x => {
    const d = x.data && x.data.node ? x.data.node : null;
    const out = {
      id: x.id,
      type: d ? d.type : (x.type || null),
      name: d ? d.name : null,
    };
    if (d && d.data && d.data.conditionPreview) {
      out.condition_id = d.data.conditionPreview.id;
      out.condition_entity = d.data.conditionPreview.entityDataPartType;
    }
    if (d && d.event) out.event = d.event;
    if (d && d.attributes) out.attributes = d.attributes;
    if (d && d.data && !d.data.conditionPreview) out.data = d.data;
    return out;
  });
  const edgeSummary = (edges || []).map(e => ({
    id: e.id, source: e.source, target: e.target,
    label: e.label, sourceHandle: e.sourceHandle, targetHandle: e.targetHandle,
  }));
  return {
    node_count: nodeSummary.length,
    edge_count: edgeSummary.length,
    nodes: nodeSummary,
    edges: edgeSummary,
  };
})()
"""

# Прочитать текст фильтра открытого condition-блока из DOM.
GET_FILTER_JS = r"""
(() => {
  const t = document.body.innerText;
  const end = t.indexOf('Добавить фильтр');
  if (end < 0) return {error: 'no "Добавить фильтр" marker'};
  const before = t.slice(0, end);
  const s = before.lastIndexOf('Eще');
  const start = s >= 0 ? s : before.lastIndexOf('Еще');
  if (start < 0) return {error: 'no "Eще" marker'};
  const lines = t.slice(start, end).split('\n').map(l => l.trim()).filter(Boolean);
  // lines[0] = "Eще"/"Еще", остальное — строки фильтра
  return {filter_lines: lines.slice(1)};
})()
"""


async def rpc(ws, expr, wait_ms=0):
    """Послать Runtime.evaluate и вернуть value."""
    await ws.send(json.dumps({
        "id": 1, "method": "Runtime.evaluate",
        "params": {"expression": expr, "returnByValue": True},
    }))
    while True:
        msg = json.loads(await ws.recv())
        if msg.get("id") == 1:
            r = msg.get("result", {}).get("result", {})
            if "value" in r:
                return r["value"]
            if r.get("type") == "undefined":
                return None
            return {"_cdp_desc": r.get("description")}


async def navigate(ws, url):
    await ws.send(json.dumps({
        "id": 2, "method": "Page.navigate", "params": {"url": url},
    }))
    while True:
        msg = json.loads(await ws.recv())
        if msg.get("id") == 2:
            return msg.get("result", {})


def list_targets():
    with urllib.request.urlopen(CDP_HTTP + "/json/list", timeout=10) as r:
        return json.load(r)


def find_mindbox_page(targets):
    pages = [t for t in targets
             if t.get("type") == "page" and "mindbox.ru" in t.get("url", "")]
    return pages[0] if pages else None


async def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0].startswith("-"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    url = args[0]
    do_filters = "--filters" in args
    wait = 15
    if "--wait" in args:
        wait = int(args[args.index("--wait") + 1])

    targets = list_targets()
    page = find_mindbox_page(targets)
    if not page:
        print(json.dumps({"error": "no mindbox page target; open a MindBox tab first"}),
              ensure_ascii=False)
        sys.exit(1)
    ws_url = page["webSocketDebuggerUrl"]

    out = {"scenario_url": url, "page_title": page.get("title")}

    async with websockets.connect(ws_url, max_size=200 * 1024 * 1024) as ws:
        # навигируем на нужный URL, если вкладка ещё не там
        cur = page.get("url", "")
        if url.split("?")[0] != cur.split("?")[0]:
            await navigate(ws, url)
            time.sleep(wait)

        graph = await rpc(ws, GET_GRAPH_JS)
        if isinstance(graph, dict) and graph.get("error"):
            out["error"] = graph["error"]
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return
        out.update(graph)

        if do_filters:
            conditions = [n for n in graph.get("nodes", []) if n.get("type") == "condition"]
            out["filters"] = []
            base = url.split("?")[0]
            for c in conditions:
                # открыть панель condition-блока через ?blockId=<node id>
                nav = f"{base}?blockId={c['id']}&version=draft"
                await navigate(ws, nav)
                time.sleep(wait)
                f = await rpc(ws, GET_FILTER_JS)
                out["filters"].append({
                    "node_id": c["id"],
                    "node_name": c.get("name"),
                    **({"filter_lines": f.get("filter_lines", [])}
                       if isinstance(f, dict) and "filter_lines" in f
                       else {"filter_error": f}),
                })

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:  # noqa
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}, ensure_ascii=False))
        sys.exit(1)
