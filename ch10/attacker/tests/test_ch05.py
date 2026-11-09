# 第5章: 権限の項目を送っても拒否されることを確かめる
import httpx

BASE = "http://app:8000"


def test_is_admin_is_rejected():
    c = httpx.Client(base_url=BASE, timeout=30)
    data = {"username": "yamada-taro", "password": "password1"}
    c.post("/login", data=data)
    r = c.put("/me", json={"is_admin": 1})
    assert r.status_code == 422
    assert c.get("/admin").status_code == 403
