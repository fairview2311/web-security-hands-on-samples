# 演習用: 同時にクーポンを使ってレースコンディションを試す
import concurrent.futures
import httpx

BASE = "http://app:8000"
login = httpx.Client(base_url=BASE, timeout=30)
login.post("/login", data={"username": "yamada-taro", "password": "password1"})
sid = login.cookies.get("sid")


def use():
    c = httpx.Client(base_url=BASE, timeout=30, cookies={"sid": sid})
    return c.post("/coupon", data={"code": "MIDORI100"}).json()


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    results = [f.result() for f in [pool.submit(use) for _ in range(10)]]

success = [r for r in results if isinstance(r.get("points"), int)]
print("成功した回数:", len(success), "/ 10")
print("最終ポイント:", max((r["points"] for r in success), default=0))
