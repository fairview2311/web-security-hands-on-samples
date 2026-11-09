# 演習用・わざと脆弱・本番で使わない
import subprocess
from fastapi import APIRouter, Request
from app.peek import peek
from app.web import render

router = APIRouter()


@router.get("/ping")
def ping(request: Request, host: str = "127.0.0.1"):
    command = "ping -c 1 " + host
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "コマンドが時間切れになりました"
    response = render(request, "tools.html", {"host": host, "command": command, "output": output})
    return peek(response, "command", command)
