# 演習用・わざと脆弱・本番で使わない
import sqlite3
from fastapi import APIRouter, Request
from app.db import connect
from app.peek import peek
from app.web import render

router = APIRouter()


@router.get("/search")
def search(request: Request, q: str = ""):
    sql = "SELECT id, title, body FROM notes WHERE is_public=1 AND title LIKE ?"
    pattern = "%" + q + "%"
    rows, error = [], None
    try:
        with connect() as conn:
            rows = conn.execute(sql, (pattern,)).fetchall()
    except sqlite3.Error as exc:
        error = str(exc)
    response = render(request, "search.html", {"q": q, "notes": rows, "sql": sql, "error": error})
    return peek(response, "sql", sql)
