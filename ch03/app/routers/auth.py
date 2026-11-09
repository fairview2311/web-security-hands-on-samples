# 演習用・わざと脆弱・本番で使わない
from hashlib import md5
from uuid import uuid4
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from app.db import connect
from app.web import render

router = APIRouter()


@router.get("/login")
def login_page(request: Request):
    response = render(request, "login.html")
    if not request.cookies.get("sid"):
        response.set_cookie("sid", uuid4().hex, httponly=False)
    return response


@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    with connect() as conn:
        user = conn.execute("SELECT * FROM users WHERE username=? AND password_hash=?",
                            (username, md5(password.encode()).hexdigest())).fetchone()
        if user is None:
            return render(request, "login.html", {"error": "ユーザー名かパスワードが違います"}, 401)
        # 回数制限なし。攻撃者が設定した既存 sid も、そのままログインに使う。
        sid = request.cookies.get("sid") or uuid4().hex
        conn.execute("INSERT OR REPLACE INTO sessions VALUES (?, ?)", (sid, user["id"]))
    response = RedirectResponse("/", status_code=303)
    response.set_cookie("sid", sid, httponly=False)
    return response


@router.post("/logout")
def logout(request: Request):
    with connect() as conn:
        conn.execute("DELETE FROM sessions WHERE sid=?", (request.cookies.get("sid"),))
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("sid")
    return response
