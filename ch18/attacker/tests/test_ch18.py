# 第18章: 秘密情報が漏れないことを確かめる
import httpx

BASE = "http://app:8000"


def test_api_key_not_in_page():
    c = httpx.Client(base_url=BASE, timeout=30)
    c.post("/login", data={"username": "yamada-taro", "password": "password1"})
    assert "FLAG{secret-in-page}" not in c.get("/map").text


def test_debug_page_is_gone():
    assert httpx.get(BASE + "/debug", timeout=30).status_code == 404
