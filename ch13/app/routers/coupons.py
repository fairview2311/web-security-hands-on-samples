# 演習用・わざと脆弱・本番で使わない
import time
from fastapi import APIRouter, Form, HTTPException, Request
from app.db import connect
from app.session import require_user

router = APIRouter()


@router.post("/coupon")
def coupon(request: Request, code: str = Form(...)):
    user = require_user(request)
    with connect() as conn:
        row = conn.execute("SELECT * FROM coupons WHERE code=?", (code,)).fetchone()
    if row is None or row["used"]:
        raise HTTPException(400, "使えないクーポンです")
    # 確認と更新を分離し、複数のリクエストが確認を通過できる隙間を作る。
    time.sleep(0.3)
    with connect() as conn:
        conn.execute("UPDATE coupons SET used=1 WHERE code=?", (code,))
        conn.execute("UPDATE users SET points=points+? WHERE id=?", (row["points"], user["id"]))
        points = conn.execute("SELECT points FROM users WHERE id=?", (user["id"],)).fetchone()[0]
    return {"points": points, "flag": "FLAG{race-condition}" if points > row["points"] else None}
