# 第4章: 他人のメモを読めないことを確かめる
import httpx

BASE = "http://app:8000"


def login():
    c = httpx.Client(base_url=BASE, timeout=30)
    data = {"username": "yamada-taro", "password": "password1"}
    c.post("/login", data=data)
    return c


def test_other_users_note_is_not_found():
    c = login()
    r = c.get("/notes/3")
    assert r.status_code == 404
    assert "FLAG{" not in r.text


def test_own_note_is_readable():
    assert login().get("/notes/1").status_code == 200
