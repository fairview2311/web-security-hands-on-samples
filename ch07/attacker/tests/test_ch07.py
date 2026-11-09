# 第7章: 投稿がエスケープされ、Cookie を読めないことを確かめる
import httpx

BASE = "http://app:8000"


def login():
    c = httpx.Client(base_url=BASE, timeout=30, follow_redirects=True)
    data = {"username": "yamada-taro", "password": "password1"}
    c.post("/login", data=data)
    return c


def test_post_is_escaped():
    c = login()
    r = c.post("/board", data={"body": "<b>ch07</b>"})
    assert "&lt;b&gt;ch07&lt;/b&gt;" in r.text
    assert "<b>ch07</b>" not in r.text


def test_board_has_csp():
    r = httpx.get(BASE + "/board", timeout=30)
    assert "default-src 'none'" in r.headers["content-security-policy"]


def test_session_cookie_is_httponly():
    r = httpx.post(BASE + "/login", timeout=30, data={
        "username": "yamada-taro", "password": "password1"})
    assert "httponly" in r.headers["set-cookie"].lower()
