# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.db import connect
from app.session import require_user

router = APIRouter()


class ProfileUpdate(BaseModel):
    display_name: str | None = None
    bio: str | None = None
    is_admin: int | None = None
    points: int | None = None


@router.get("/me")
def my_profile(request: Request):
    user = require_user(request)
    return {"id": user["id"], "username": user["username"],
            "display_name": user["display_name"], "bio": user["bio"],
            "secret_memo": "FLAG{cors}"}


@router.put("/me")
def update_profile(request: Request, profile: ProfileUpdate):
    user = require_user(request)
    values = profile.model_dump(exclude_unset=True, exclude_none=True)
    with connect() as conn:
        if values:
            fields = ", ".join(f"{key}=?" for key in values)
            conn.execute(f"UPDATE users SET {fields} WHERE id=?", (*values.values(), user["id"]))
        row = conn.execute("SELECT id, username, display_name, bio, is_admin, points FROM users WHERE id=?", (user["id"],)).fetchone()
    return dict(row)
