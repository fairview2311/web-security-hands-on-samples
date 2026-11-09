# 第13章: コマンド注入でファイルを読めないことを確かめる
import httpx

BASE = "http://app:8000"


def test_command_injection_is_blocked():
    c = httpx.Client(base_url=BASE, timeout=30)
    c.post("/login", data={"username": "yamada-taro", "password": "password1"})
    r = c.get("/ping", params={"host": "127.0.0.1; cat /opt/flags/ch13.txt"})
    assert "FLAG{" not in r.text
