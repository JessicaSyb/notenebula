import os, json
from datetime import datetime
from typing import List, Optional, Dict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MARKS = os.path.join(BASE, "bookmarks")

def ensure(): os.makedirs(MARKS, exist_ok=True)

def add(url: str, title: Optional[str]=None, tags: Optional[List[str]]=None, note: str="") -> str:
    ensure()
    day = datetime.now().strftime("%Y-%m-%d")
    p = os.path.join(MARKS, f"{day}.json")
    data: Dict[str, list] = {"bookmarks": []}
    if os.path.exists(p): data = json.load(open(p,"r",encoding="utf-8"))
    data["bookmarks"].append({"ts": datetime.now().isoformat(),"url":url,"title":title or "","tags":tags or [],"note":note})
    json.dump(data, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    return p

# autosave 2025-10-20T12:39:42.979463+00:00
# tweak 2025-11-03T19:44:23.178572+00:00

# autosave 2025-11-24T20:15:53.156889+00:00
