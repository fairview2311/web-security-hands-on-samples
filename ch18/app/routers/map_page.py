# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, Request
from app.web import render

router = APIRouter()


@router.get("/map")
def map_page(request: Request):
    return render(request, "map.html")
