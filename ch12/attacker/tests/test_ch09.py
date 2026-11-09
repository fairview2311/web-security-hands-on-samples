# 第9章: 総当たりが止まることを確かめる
import httpx

BASE = "http://app:8000"


def test_bruteforce_is_blocked():
    words = open("attacker/wordlist.txt").read().split()
    codes = []
    for word in words:
        c = httpx.Client(base_url=BASE, follow_redirects=False, timeout=30)
        r = c.post("/login", data={"username": "yamada-taro", "password": word})
        codes.append(r.status_code)
    assert 429 in codes
    assert 303 not in codes
