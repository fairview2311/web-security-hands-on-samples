# 第6章: SQL インジェクションが直っていることを確かめる
import httpx

BASE = "http://app:8000"


def test_sqli_blocked():
    q = "' UNION SELECT 1, value, 1 FROM secrets--"
    r = httpx.get(BASE + "/search", params={"q": q}, timeout=30)
    assert "FLAG{" not in r.text
