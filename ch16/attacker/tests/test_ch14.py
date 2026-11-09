# 第14章: パストラバーサルで設定ファイルを読めないことを確かめる
import httpx

BASE = "http://app:8000"


def test_path_traversal_is_blocked():
    r = httpx.get(BASE + "/download", params={"name": "../../.env"}, timeout=30)
    assert "FLAG{" not in r.text


def test_normal_file_is_downloadable():
    r = httpx.get(BASE + "/download", params={"name": "manual.txt"}, timeout=30)
    assert r.status_code == 200
