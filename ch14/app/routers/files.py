# 演習用・わざと脆弱・本番で使わない
import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()
BASE_DIR = os.path.realpath("app/files")


@router.get("/download")
def download(name: str = "manual.txt"):
    path = os.path.realpath(os.path.join(BASE_DIR, name))
    if os.path.commonpath([BASE_DIR, path]) != BASE_DIR or not os.path.isfile(path):
        raise HTTPException(404, "ファイルがありません")
    return FileResponse(path, media_type="text/plain")
