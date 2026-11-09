# 第11章: 弱い鍵の偽造と期限切れが拒否されることを確かめる
import time

import jwt
import httpx

BASE = "http://app:8000"


def test_forged_token_is_rejected():
    forged = jwt.encode({"sub": "1", "is_admin": 1}, "secret", algorithm="HS256")
    r = httpx.get(BASE + "/jwt-me", params={"token": forged}, timeout=30)
    assert r.status_code == 401
    assert "FLAG{" not in r.text


def test_expired_token_is_rejected():
    forged = jwt.encode({"sub": "1", "is_admin": 1, "exp": int(time.time()) - 3600},
                        "secret", algorithm="HS256")
    r = httpx.get(BASE + "/jwt-me", params={"token": forged}, timeout=30)
    assert r.status_code == 401
