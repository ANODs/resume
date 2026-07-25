from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    ROOT / "src" / "build_resume_en.py",
    ROOT / "src" / "build_resume_en_light.py",
    ROOT / "src" / "build_resume_multilang.py",
)
EXPECTED = (
    "Timofey_Timoshkin_Resume_Dark.pdf",
    "Timofey_Timoshkin_Resume_Light.pdf",
    "Тимофей_Тимошкин_Резюме_Тёмное.pdf",
    "Тимофей_Тимошкин_Резюме_Светлое.pdf",
    "Timofey_Timoshkin_Curriculum_Scuro.pdf",
    "Timofey_Timoshkin_Curriculum_Chiaro.pdf",
)


def main() -> None:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)

    output_dir = ROOT / "output" / "pdf"
    missing = [name for name in EXPECTED if not (output_dir / name).is_file()]
    if missing:
        raise RuntimeError(f"Missing generated PDFs: {missing}")
    print(f"Built {len(EXPECTED)} PDFs in {output_dir}")


if __name__ == "__main__":
    main()
