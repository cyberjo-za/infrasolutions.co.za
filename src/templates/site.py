from pathlib import Path

TEMPLATE = (Path(__file__).parent / "infracore.html").read_text(encoding="utf-8")
