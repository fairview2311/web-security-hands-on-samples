from fastapi import HTTPException, Request
from app.db import connect


def current_user(request: Request):
    sid = request.cookies.get("sid")
    if not sid:
        return None
    with connect() as conn:
        row = conn.execute(
            "SELECT users.* FROM users JOIN sessions ON users.id=sessions.user_id WHERE sid=?",
            (sid,),
        ).fetchone()
    return dict(row) if row else None


def require_user(request: Request):
    user = current_user(request)
    if user is None:
        raise HTTPException(401, "ログインしてください")
    return user
