# 第12章: 別のオリジンに CORS の許可を返さないことを確かめる
import httpx

BASE = "http://app:8000"


def test_other_origin_is_not_allowed():
    c = httpx.Client(base_url=BASE, timeout=30)
    c.post("/login", data={"username": "yamada-taro", "password": "password1"})
    r = c.get("/me", headers={"Origin": "http://evil.example"})
    allow = r.headers.get("access-control-allow-origin")
    assert allow != "http://evil.example"
    assert allow != "*"
