# 演習用・わざと脆弱・本番で使わない
import os
from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

router = APIRouter()
UPLOADS = Path("app/uploads")


@router.post("/upload")
def upload(file: UploadFile = File(...)):
    UPLOADS.mkdir(parents=True, exist_ok=True)
    name = os.path.basename(file.filename or "upload.bin")
    if name in ("", ".", ".."):
        raise HTTPException(400, "ファイル名が必要です")
    # 中身・拡張子を確認せず保存し、HTML も同じオリジンで実行可能にする。
    with (UPLOADS / name).open("wb") as destination:
        import shutil
        shutil.copyfileobj(file.file, destination)
    return {"name": name, "url": "/uploads/" + name}


@router.get("/uploads/{name}")
def uploaded(name: str):
    path = UPLOADS / name
    if not path.is_file():
        raise HTTPException(404, "ファイルがありません")
    return FileResponse(path)
