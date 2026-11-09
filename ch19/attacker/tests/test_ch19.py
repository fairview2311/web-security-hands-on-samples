# 第19章: 要約の表示で | safe を使っていないことを確かめる
import pathlib

TEMPLATE = pathlib.Path("app/templates/summary.html")


def test_summary_template_has_no_safe_filter():
    text = TEMPLATE.read_text(encoding="utf-8")
    assert "answer | safe" not in text
    assert "{{ answer }}" in text
