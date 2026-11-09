# 演習用・わざと脆弱・本番で使わない
import os
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import APIRouter, HTTPException, Request
from app.session import require_user

router = APIRouter()
KEY = os.environ.get("JWT_SECRET", "")


@router.get("/token")
def token(request: Request):
    user = require_user(request)
    encoded = jwt.encode({"sub": str(user["id"]), "username": user["username"],
                          "is_admin": user["is_admin"],
                          "exp": datetime.now(timezone.utc) + timedelta(seconds=30)}, KEY, algorithm="HS256")
    return {"token": encoded}


@router.get("/jwt-me")
def jwt_me(token: str):
    try:
        claims = jwt.decode(token, KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError as exc:
        raise HTTPException(401, "トークンが正しくありません") from exc
    return {"claims": claims, "flag": "FLAG{jwt}" if claims.get("is_admin") else None}
