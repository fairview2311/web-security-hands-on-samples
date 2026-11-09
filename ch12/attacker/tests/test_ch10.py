# 第10章: ログインでセッション ID が変わることを確かめる
import httpx

BASE = "http://app:8000"
FIXED = "attacker-fixed-session-0001"


def test_session_id_changes_on_login():
    header = {"Cookie": f"sid={FIXED}"}
    c = httpx.Client(base_url=BASE, timeout=30, follow_redirects=False)
    login = c.post("/login", headers=header,
                   data={"username": "yamada-taro", "password": "password1"})
    assert login.status_code == 303
    assert login.cookies.get("sid") != FIXED
    attacker = httpx.Client(base_url=BASE, timeout=30)
    assert "山田 太郎 /" not in attacker.get("/", headers=header).text
