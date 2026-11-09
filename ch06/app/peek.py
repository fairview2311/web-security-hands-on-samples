"""演習用の「のぞき窓」。内部情報を公開するため、本番では付けない。

x-peek は URL デコードすると JSON になる。日本語や改行もヘッダに格納できる。
画面には SQL・コマンドをエスケープして表示し、HTML 自体はヘッダで観察する。
"""
import json
from urllib.parse import quote


def peek(response, kind: str, value: str):
    response.headers["x-peek"] = quote(
        json.dumps({"kind": kind, "value": value}, ensure_ascii=False), safe=""
    )
    return response
