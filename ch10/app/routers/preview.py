# 演習用・わざと脆弱・本番で使わない
import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

router = APIRouter()


@router.get("/preview")
def preview(url: str):
    try:
        result = httpx.get(url, timeout=5, follow_redirects=True, trust_env=False)
    except httpx.HTTPError as exc:
        raise HTTPException(502, str(exc)) from exc
    return Response(content=result.content, status_code=result.status_code,
                    media_type=result.headers.get("content-type", "text/plain"))
