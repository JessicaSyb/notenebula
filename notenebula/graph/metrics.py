from typing import Dict, List, Tuple

def out_degree(g: Dict[str, List[str]]): return {k: len(v) for k,v in g.items()}

def in_degree(g: Dict[str, List[str]]):
    inc = {k:0 for k in g}
    for vs in g.values():
        for t in vs:
            if t in inc: inc[t]+=1
    return inc

def top_by_out(g: Dict[str, List[str]], n:int=5) -> List[Tuple[str,int]]:
    return sorted(((k,len(v)) for k,v in g.items()), key=lambda x:-x[1])[:n]
# tweak 2025-11-17T20:40:32.090587+00:00

# autosave 2025-11-20T19:57:27.073665+00:00
