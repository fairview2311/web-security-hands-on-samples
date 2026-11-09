# 第8章: トークンの無い投稿が拒否されることを確かめる
import httpx

BASE = "http://app:8000"


def test_post_without_token_is_rejected():
    c = httpx.Client(base_url=BASE, timeout=30)
    data = {"username": "yamada-taro", "password": "password1"}
    c.post("/login", data=data)
    r = c.post("/board", data={"body": "トークン無しの投稿"})
    assert r.status_code == 403
