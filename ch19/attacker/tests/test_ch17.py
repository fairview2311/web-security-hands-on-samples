# 第17章: 同時のリクエストでも1回だけ成功することを確かめる
import concurrent.futures

import httpx

BASE = "http://app:8000"


def test_coupon_is_used_only_once():
    login = httpx.Client(base_url=BASE, timeout=30)
    login.post("/login", data={"username": "yamada-taro", "password": "password1"})
    sid = login.cookies.get("sid")

    def use():
        c = httpx.Client(base_url=BASE, timeout=30, cookies={"sid": sid})
        return c.post("/coupon", data={"code": "MIDORI100"}).status_code

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        codes = [f.result() for f in [pool.submit(use) for _ in range(10)]]

    assert codes.count(200) == 1
