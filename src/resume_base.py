from __future__ import annotations

import os
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "pdf"

PAGE_W, PAGE_H = A4
MARGIN_X = 14 * mm
TOP = 12 * mm
BOTTOM = 13 * mm


def _font_files() -> tuple[Path, Path, Path, Path]:
    windir = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    candidates = [
        (
            windir / "segoeui.ttf",
            windir / "seguisb.ttf",
            windir / "segoeuib.ttf",
            windir / "segoeuii.ttf",
        ),
        (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
        ),
        (
            Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Italic.ttf"),
        ),
    ]
    for files in candidates:
        if all(path.is_file() for path in files):
            return files
    raise RuntimeError("No supported Unicode font set found (Segoe UI, DejaVu Sans or Arial).")


def register_fonts() -> None:
    normal, semibold, bold, italic = _font_files()
    pdfmetrics.registerFont(TTFont("Segoe", str(normal)))
    pdfmetrics.registerFont(TTFont("Segoe-Semibold", str(semibold)))
    pdfmetrics.registerFont(TTFont("Segoe-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("Segoe-Italic", str(italic)))
    pdfmetrics.registerFontFamily(
        "Segoe",
        normal="Segoe",
        bold="Segoe-Bold",
        italic="Segoe-Italic",
        boldItalic="Segoe-Bold",
    )
