# 演習用・わざと脆弱・本番で使わない
from fastapi.middleware.cors import CORSMiddleware


def add_cors(app):
    app.add_middleware(
        CORSMiddleware, allow_origins=["http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"], allow_headers=["*"], expose_headers=["x-peek"],
    )
