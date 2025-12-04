import os, json
from ..graph.build import build_graph, load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
REPORTS = os.path.join(BASE, "reports")

def export_json() -> str:
    os.makedirs(REPORTS, exist_ok=True)
    data = {"index": load_index(), "graph": build_graph()}
    p = os.path.join(REPORTS, "export.json")
    json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return p
# tweak 2025-10-06T10:57:48.203625+00:00

# autosave 2025-10-23T18:47:13.700481+00:00
# tweak 2025-12-04T15:53:07.421295+00:00
