# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, HTTPException, Request
from app.db import connect
from app.session import require_user
from app.web import render

router = APIRouter()


@router.get("/notes/{id}")
def note(request: Request, id: int):
    user = require_user(request)
    with connect() as conn:
        row = conn.execute(
            "SELECT * FROM notes WHERE id=? AND (owner_id=? OR is_public=1)",
            (id, user["id"]),
        ).fetchone()
    if row is None:
        raise HTTPException(404, "メモがありません")
    return render(request, "note.html", {"note": row})
