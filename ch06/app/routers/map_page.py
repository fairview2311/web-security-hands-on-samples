# 演習用・わざと脆弱・本番で使わない
import os
from fastapi import APIRouter, Request
from app.web import render

router = APIRouter()


@router.get("/map")
def map_page(request: Request):
    return render(request, "map.html", {"maps_api_key": os.environ.get("MAPS_API_KEY", "")})
