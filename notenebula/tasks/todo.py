import os, json
from datetime import datetime
from typing import List, Optional, Dict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
TASKS = os.path.join(BASE, "tasks")

def ensure(): os.makedirs(TASKS, exist_ok=True)

def add(title: str, due: Optional[str]=None, tags: Optional[List[str]]=None) -> str:
    ensure()
    day = datetime.now().strftime("%Y-%m-%d")
    p = os.path.join(TASKS, f"{day}.json")
    data: Dict[str, list] = {"tasks": []}
    if os.path.exists(p): data = json.load(open(p,"r",encoding="utf-8"))
    data["tasks"].append({"ts": datetime.now().isoformat(),"title":title,"due":due or "","tags":tags or []})
    json.dump(data, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    return p

# autosave 2025-12-11T12:14:34.201337+00:00

# autosave 2025-12-22T11:44:41.365981+00:00
# tweak 2026-02-19T18:07:36.223332+00:00
