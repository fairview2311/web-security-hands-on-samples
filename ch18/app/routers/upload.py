# 演習用・わざと脆弱・本番で使わない
import secrets
import shutil
from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

router = APIRouter()
UPLOADS = Path("app/uploads")


ALLOWED = {".png", ".jpg", ".jpeg", ".gif", ".txt", ".pdf"}


@router.post("/upload")
def upload(file: UploadFile = File(...)):
    UPLOADS.mkdir(parents=True, exist_ok=True)
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in ALLOWED:
        raise HTTPException(400, "許可されていない種類のファイルです")
    name = secrets.token_hex(8) + suffix
    with (UPLOADS / name).open("wb") as destination:
        shutil.copyfileobj(file.file, destination)
    return {"name": name, "url": "/uploads/" + name}


@router.get("/uploads/{name}")
def uploaded(name: str):
    path = UPLOADS / name
    if not path.is_file():
        raise HTTPException(404, "ファイルがありません")
    return FileResponse(path, media_type="application/octet-stream",
                        filename=name, content_disposition_type="attachment")
