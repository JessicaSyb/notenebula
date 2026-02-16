import re
HDR = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
def headings(md: str): return [(m.group(1), m.group(2).strip()) for m in HDR.finditer(md or "")]

# autosave 2025-10-13T19:17:03.737093+00:00

# autosave 2025-10-20T12:16:55.144381+00:00

# autosave 2025-12-08T20:46:18.393039+00:00

# autosave 2026-01-26T16:27:25.355786+00:00
# tweak 2026-02-16T13:42:23.996040+00:00
