"""みどりメモ：ローカル Docker 専用の脆弱性演習アプリ。"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from app.config import load_env
from app.cors import add_cors
from app.db import connect, reset
from app.routers import (admin, auth, board, coupons, files, jwt_api,
                         map_page, notes, preview, profile, search, summary, tools, upload)
from app.session import current_user
from app.web import render


@asynccontextmanager
async def lifespan(app):
    load_env()
    reset()
    yield


app = FastAPI(title="みどりメモ（脆弱性演習用）", lifespan=lifespan)
add_cors(app)
for module in (auth, notes, profile, admin, search, board, tools, files,
               upload, preview, coupons, jwt_api, map_page, summary):
    app.include_router(module.router)


@app.get("/")
def home(request: Request):
    user = current_user(request)
    with connect() as conn:
        notes = conn.execute(
            "SELECT * FROM notes WHERE is_public=1 OR owner_id=? ORDER BY id",
            (user["id"] if user else -1,),
        ).fetchall()
    return render(request, "home.html", {"notes": notes})
