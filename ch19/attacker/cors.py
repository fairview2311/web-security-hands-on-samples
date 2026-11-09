# 演習用: CORS のヘッダーを確かめる
import httpx

BASE = "http://app:8000"

c = httpx.Client(base_url=BASE, timeout=30)
c.post("/login", data={"username": "yamada-taro", "password": "password1"})
r = c.get("/me", headers={"Origin": "http://evil.example"})
print("Allow-Origin:", r.headers.get("access-control-allow-origin"))
print("Allow-Credentials:", r.headers.get("access-control-allow-credentials"))
