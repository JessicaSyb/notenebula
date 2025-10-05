import os, re, json
from typing import List, Dict, Optional

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
NOTES = os.path.join(BASE, "notes")
META  = os.path.join(BASE, "data", "meta")

RX_LINK = re.compile(r"\[\[([^\[\]]+)\]\]")
RX_TAG  = re.compile(r"(?<!\w)#([a-zA-Z0-9_\-]+)")

def ensure():
    os.makedirs(NOTES, exist_ok=True)
    os.makedirs(META,  exist_ok=True)

def slug(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-_]+", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "note"

def list_notes() -> List[str]:
    ensure()
    return sorted([f for f in os.listdir(NOTES) if f.endswith(".md")])

def read_note(fn: str) -> Optional[str]:
    p = os.path.join(NOTES, fn)
    return open(p, "r", encoding="utf-8").read() if os.path.exists(p) else None

def write_note(title: str, body: str) -> str:
    ensure()
    fn = slug(title) + ".md"
    p = os.path.join(NOTES, fn)
    with open(p, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body.strip()}\n")
    return p

def parse(text: str) -> Dict[str, List[str]]:
    return {
        "links": sorted(set(RX_LINK.findall(text or ""))),
        "tags":  sorted(set(RX_TAG.findall(text or ""))),
    }

def build_index() -> str:
    ensure()
    idx = {}
    for fn in list_notes():
        idx[fn] = parse(read_note(fn) or "")
    out = os.path.join(META, "index.json")
    json.dump(idx, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return out
