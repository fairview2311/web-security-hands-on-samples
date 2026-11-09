# 演習用・わざと脆弱・本番で使わない
import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download")
def download(name: str = "manual.txt"):
    path = os.path.join("app/files", name)
    if not os.path.isfile(path):
        raise HTTPException(404, "ファイルがありません")
    return FileResponse(path, media_type="text/plain")
