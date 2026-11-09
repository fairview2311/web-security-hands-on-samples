# 演習用・わざと脆弱・本番で使わない
from fastapi import APIRouter, Form, HTTPException, Request
from app.db import connect
from app.session import require_user

router = APIRouter()


@router.post("/coupon")
def coupon(request: Request, code: str = Form(...)):
    user = require_user(request)
    with connect() as conn:
        # 使用済みでない行だけを、1つの UPDATE で使用済みにする
        cursor = conn.execute(
            "UPDATE coupons SET used=1 WHERE code=? AND used=0", (code,))
        if cursor.rowcount == 0:
            raise HTTPException(400, "使えないクーポンです")
        row = conn.execute("SELECT points FROM coupons WHERE code=?", (code,)).fetchone()
        conn.execute("UPDATE users SET points=points+? WHERE id=?", (row["points"], user["id"]))
        points = conn.execute("SELECT points FROM users WHERE id=?", (user["id"],)).fetchone()[0]
    return {"points": points, "flag": "FLAG{race-condition}" if points > row["points"] else None}
