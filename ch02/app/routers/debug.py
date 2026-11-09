# 演習用・わざと脆弱・本番で使わない
import os
import platform
from fastapi import APIRouter

router = APIRouter()


@router.get("/debug")
def debug():
    return {"environment": dict(os.environ), "python": platform.python_version(),
            "cwd": os.getcwd(), "flag": "FLAG{debug-info}"}
