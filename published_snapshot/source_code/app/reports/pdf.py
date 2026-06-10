from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas


def write_pdf(path: Path, title: str, lines: list[str]) -> None:
    canvas = Canvas(str(path), pagesize=letter)
    canvas.setTitle(title)
    y = 760
    for line in [title, ""] + lines:
        canvas.drawString(40, y, line[:110])
        y -= 16
        if y < 40:
            canvas.showPage()
            y = 760
    canvas.save()
