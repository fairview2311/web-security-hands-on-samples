# 演習用・わざと脆弱・本番で使わない
from urllib.parse import urlparse
import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

router = APIRouter()


ALLOWED_HOSTS = {"example.com", "www.example.com"}


@router.get("/preview")
def preview(url: str):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or parsed.hostname not in ALLOWED_HOSTS:
        raise HTTPException(400, "許可されていない URL です")
    try:
        result = httpx.get(url, timeout=5, follow_redirects=False, trust_env=False)
    except httpx.HTTPError as exc:
        raise HTTPException(502, str(exc)) from exc
    return Response(content=result.content, status_code=result.status_code,
                    media_type=result.headers.get("content-type", "text/plain"))
