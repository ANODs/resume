from reportlab.lib import colors

import build_resume_en as resume


resume.OUTPUT_PDF = resume.OUTPUT_DIR / "Timofey_Timoshkin_Resume_Light.pdf"

# Preserve the exact layout while inverting the black/white surfaces.
resume.BLACK = colors.HexColor("#FFFFFF")
resume.WHITE = colors.HexColor("#000000")
resume.PANEL = resume.BLACK
resume.SOFT = resume.WHITE
resume.MUTED_DARK = resume.WHITE
resume.ACCENT = colors.HexColor("#FF4FBF")
resume.ACCENT_HEX = "#FF4FBF"


if __name__ == "__main__":
    resume.build_en()
