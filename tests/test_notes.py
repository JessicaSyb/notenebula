from notenebula.core.notes import parse
def test_parse():
    s="Пример [[Связь]] и #tag1 #tag2"
    meta=parse(s)
    assert "Связь" in meta["links"]
    assert "tag1" in meta["tags"] and "tag2" in meta["tags"]
