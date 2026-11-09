# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from app.db import connect
from app.session import require_user
from app.web import render

router = APIRouter()


@router.get("/board")
def board(request: Request):
    with connect() as conn:
        rows = conn.execute("SELECT notes.*, users.display_name FROM notes JOIN users ON notes.owner_id=users.id WHERE is_public=1 ORDER BY notes.id DESC").fetchall()
    response = render(request, "board.html", {"notes": rows})
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; style-src 'unsafe-inline'"
    )
    return response


@router.post("/board")
def post(request: Request, body: str = Form(...), title: str = Form("掲示板への投稿")):
    user = require_user(request)
    with connect() as conn:
        conn.execute("INSERT INTO notes(owner_id,title,body,is_public) VALUES (?,?,?,1)",
                     (user["id"], title, body))
    return RedirectResponse("/board", status_code=303)
