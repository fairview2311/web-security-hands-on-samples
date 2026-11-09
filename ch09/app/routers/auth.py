# 演習用・わざと脆弱・本番で使わない
from time import monotonic
from uuid import uuid4
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from app.db import connect, hash_password, verify_password
from app.web import render

router = APIRouter()
FAIL_LIMIT = 5
FAIL_WINDOW = 60
_fails = {}  # IP アドレス -> [失敗の時刻, ...]


def too_many(ip):
    now = monotonic()
    times = [t for t in _fails.get(ip, []) if now - t < FAIL_WINDOW]
    _fails[ip] = times
    return len(times) >= FAIL_LIMIT


@router.get("/login")
def login_page(request: Request):
    response = render(request, "login.html")
    if not request.cookies.get("sid"):
        response.set_cookie("sid", uuid4().hex, httponly=True)
    return response


@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    ip = request.client.host if request.client else "unknown"
    if too_many(ip):
        return render(request, "login.html",
                      {"error": "試行が多すぎます。しばらく待ってください"}, 429)
    with connect() as conn:
        user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if user is None or not verify_password(password, user["password_hash"]):
            _fails.setdefault(ip, []).append(monotonic())
            return render(request, "login.html", {"error": "ユーザー名かパスワードが違います"}, 401)
        _fails.pop(ip, None)
        sid = request.cookies.get("sid") or uuid4().hex
        conn.execute("INSERT OR REPLACE INTO sessions VALUES (?, ?)", (sid, user["id"]))
    response = RedirectResponse("/", status_code=303)
    response.set_cookie("sid", sid, httponly=True)
    return response


@router.post("/logout")
def logout(request: Request):
    with connect() as conn:
        conn.execute("DELETE FROM sessions WHERE sid=?", (request.cookies.get("sid"),))
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("sid")
    return response
