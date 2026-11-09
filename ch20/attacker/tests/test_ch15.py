# 第15章: HTML のアップロードが拒否されることを確かめる
import httpx

BASE = "http://app:8000"


def test_html_upload_is_rejected():
    r = httpx.post(BASE + "/upload", timeout=30,
                   files={"file": ("evil.html", "<script>1</script>", "text/html")})
    assert r.status_code == 400


def test_image_is_served_as_download():
    up = httpx.post(BASE + "/upload", timeout=30,
                    files={"file": ("photo.png", b"x", "image/png")})
    assert up.status_code == 200
    r = httpx.get(BASE + up.json()["url"], timeout=30)
    assert "attachment" in r.headers.get("content-disposition", "")
