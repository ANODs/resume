# Timofey Timoshkin - Resume

Source and generated PDF versions of my resume in Russian, English and Italian. Each language is available in dark and light themes inspired by [timoshkin.dev](https://timoshkin.dev).

## Ready-to-use PDFs

| Language | Dark | Light |
| --- | --- | --- |
| Русский | [Тёмная версия](output/pdf/Тимофей_Тимошкин_Резюме_Тёмное.pdf) | [Светлая версия](output/pdf/Тимофей_Тимошкин_Резюме_Светлое.pdf) |
| English | [Dark version](output/pdf/Timofey_Timoshkin_Resume_Dark.pdf) | [Light version](output/pdf/Timofey_Timoshkin_Resume_Light.pdf) |
| Italiano | [Versione scura](output/pdf/Timofey_Timoshkin_Curriculum_Scuro.pdf) | [Versione chiara](output/pdf/Timofey_Timoshkin_Curriculum_Chiaro.pdf) |

## Build locally

Requires Python 3.10+.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python build_all.py
```

Generated files are written to `output/pdf/`. The builder uses Segoe UI on Windows and falls back to DejaVu Sans or Arial on other systems.

## Project structure

```text
.
|-- build_all.py
|-- src/
|   |-- resume_base.py
|   |-- build_resume_en.py
|   |-- build_resume_en_light.py
|   `-- build_resume_multilang.py
`-- output/pdf/
    `-- six generated resume PDFs
```

## Contacts

- Telegram: [@ttimoshkin](https://t.me/ttimoshkin)
- GitHub: [ANODs](https://github.com/ANODs)
- Portfolio: [timoshkin.dev](https://timoshkin.dev)
- Product: [favor.deals](https://favor.deals)
