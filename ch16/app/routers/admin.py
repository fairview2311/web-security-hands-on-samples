# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, HTTPException, Request
from app.session import require_user
from app.web import render

router = APIRouter()


@router.get("/admin")
def admin_page(request: Request):
    user = require_user(request)
    if not user["is_admin"]:
        raise HTTPException(403, "管理者だけが開けます")
    return render(request, "admin.html", {"flag": "FLAG{mass-assignment}"})
