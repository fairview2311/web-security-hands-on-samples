import hashlib
import hmac
import secrets

from fastapi import HTTPException, Request

SECRET = secrets.token_bytes(32)


def csrf_token(request: Request) -> str:
    sid = request.cookies.get("sid", "")
    return hmac.new(SECRET, sid.encode(), hashlib.sha256).hexdigest()


def check_csrf(request: Request, token: str) -> None:
    if not hmac.compare_digest(token, csrf_token(request)):
        raise HTTPException(403, "CSRF トークンが正しくありません")
