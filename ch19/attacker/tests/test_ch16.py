# 第16章: 内部サービスに接続できないことを確かめる
import httpx

BASE = "http://app:8000"


def test_ssrf_to_internal_is_blocked():
    r = httpx.get(BASE + "/preview",
                  params={"url": "http://internal-admin:9000/"}, timeout=30)
    assert "FLAG{" not in r.text
    assert r.status_code == 400
