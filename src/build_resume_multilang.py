from __future__ import annotations

import sys

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

import build_resume_en as design


DATA = {
    "ru": {
        "name": "ТИМОФЕЙ ТИМОШКИН",
        "role": "ФРОНТЕНД-РАЗРАБОТЧИК / ПРОДУКТОВЫЙ РАЗРАБОТЧИК",
        "badge": "ВЕБ-ПРОДУКТЫ<br/>С 2018 ГОДА",
        "profile_h": "Профиль",
        "profile": (
            "Фронтенд-разработчик и продуктовый разработчик с коммерческим опытом. Создаю веб-продукты с 2018 года: "
            "от идеи и MVP до работающего бизнеса. Основная экспертиза - React, Next.js, TypeScript и архитектура "
            "фронтенда. Работал в продуктовых командах по спринтам, вёл задачи в Jira, проводил ревью merge request "
            "в GitLab и выпускал продукты end-to-end."
        ),
        "experience_h": "Опыт и продукты",
        "tex_title": "TEXSOFT / продуктовый стартап - ведущий продуктовый разработчик -> разработчик веб-информационных систем",
        "tex_date": "07.2026 - н.в.",
        "tex_bullets": [
            "Пришёл на стадии стартапа как ведущий продуктовый разработчик: отвечал за запуск с нуля, архитектуру, "
            "приоритеты и delivery. После запуска стартап стал самостоятельной компанией; официальная должность - "
            "разработчик веб-информационных систем.",
            "Разработал коммерческий фронтенд мессенджера в реальном времени по Feature-Sliced Design: Next.js 15, "
            "React 18, TypeScript, TanStack Query и Zustand; сообщения по WebSocket, аудио- и видеозвонки LiveKit, "
            "предпросмотр файлов, адаптивные чаты и группы.",
            "Работал в коммерческом спринтовом цикле: планирование и трекинг в Jira, merge request и code review в "
            "GitLab, E2E-тесты Playwright, GitLab CI / CD, multi-stage Docker-сборки и координация релизов.",
            "Провёл продукт от ранней стадии до повторяемого командного процесса разработки и выпуска.",
        ],
        "ind_title": "Собственные продукты - основатель / продуктовый разработчик",
        "ind_date": "2024 - н.в.",
        "favor_suffix": "(favor.lol -> favor.deals)",
        "favor_bullets": [
            "Развил реферальное Web3-приложение до работающего маркетплейса контрактов и сделок внутри Telegram: "
            "Next.js, интеграция с Telegram, карточки контрактов, прямые и escrow-сделки, SEO-страницы, импорт "
            "Telegram-контента и гибридная монетизация.",
            "Дипломный проект вошёл в шесть лучших на финальном демо-дне программы Стартап как диплом в РОСБИОТЕХе "
            "(июнь 2025 года).",
        ],
        "loot_bullets": [
            "Вместе с backend-партнёром запустил рекламный Telegram-продукт, полностью отвечая за фронтенд на "
            "Next.js / TypeScript; до 3 822 пользователей в месяц и 2 000 выполненных целевых действий.",
            "Интегрировал фронтенд с Go API, PostgreSQL и Redis; развернул через Docker / Dokploy. За один месяц "
            "получено 44,3 тыс. показов в поиске и 4,5 тыс. визитов.",
            "Проверил привлечение, рекламную монетизацию и юнит-экономику на реальном трафике и собственном бюджете.",
        ],
        "pilemida": "Вместе с партнёром разработал фронтенд Telegram Mini App; команда прошла путь от идеи до рабочего релиза за 3 дня.",
        "hostfi_title": "hostfi.app - видеосвязь в реальном времени",
        "hostfi": "Реализовал видеоконференции на LiveKit client/server SDK: фронтенд Next.js и отдельный сервис LiveKit в Docker Compose с автоматическим развёртыванием через Dokploy.",
        "bbb_title": "Big Balls Birds - ведущий фронтенд-разработчик, Telegram Mini App",
        "bbb_date": "Лето 2024",
        "bbb": "Отвечал за фронтенд и DevOps в команде из четырёх человек, координировался с backend и поддержкой; первая версия mini app выпущена за 2 месяца, выручка проекта - около $5 000.",
        "png_suffix": " - фронтенд-разработчик / продуктовый дизайнер, Web3",
        "png_date": "2023 - 2024",
        "png": "Вместе с двумя партнёрами создал NFT-платформу на Mantle, отвечая за структуру продукта, UI / UX и фронтенд. Проект занял 30-е место в Mantle Journey и получил $25 000; моя доля составила около $4 300.",
        "ros_title": "РОСБИОТЕХ - инженерная лаборатория и преподавание",
        "ros_date": "2023 - 2026",
        "ros_bullets": [
            "Лаборант в сфере инженерии, прототипирования и аддитивных технологий; преподавал программирование в университетском технопарке (10.2023 - 07.2024).",
            "Преподаватель по совместительству в Международном колледже технологий (02.2026 - 03.2026).",
        ],
        "additional": "<b>Дополнительный опыт:</b> веб-студия - первый коммерческий опыт в команде, 2 месяца летом 2019 года.",
        "skills_h": "Технические навыки",
        "skills": [
            ("Основной фронтенд", "TypeScript, React 18 / 19, Next.js 15 / 16, App Router, SSR / ISR, HTML5, CSS, Tailwind CSS, Vite"),
            ("Архитектура фронтенда", "Feature-Sliced Design (FSD), TanStack Query, Zustand, Zod, React Hook Form, компонентные системы, адаптивный UI / UX"),
            ("UI и интеграции", "Framer Motion, Three.js / R3F, Recharts, Lottie, REST / OpenAPI, SSE, LiveKit / WebRTC, Telegram Mini Apps, TON / TonConnect"),
            ("Смежный backend", "Node.js, Go, Prisma / GORM, PostgreSQL, Redis, JWT, cron"),
            ("Delivery и качество", "Git / GitLab, merge request, code review, Jira, Playwright E2E, GitLab CI / CD, Docker / Compose, Dokploy"),
            ("AI-процесс", "План в Gemini / Antigravity -> ручная проверка и дополнение MD-плана -> реализация в Codex -> ревью и правки git diff -> независимое ревью агентом Codex -> проверка замечаний и исправление подтверждённых проблем -> открытие MR"),
        ],
        "education_h": "Образование",
        "edu_1": "<b>Российский биотехнологический университет (РОСБИОТЕХ)</b> - обучение в университете; Favor как дипломный проект",
        "edu_2_prefix": "<b>Школа программистов</b>",
        "edu_2_suffix": "- фундаментальная подготовка",
        "footer": "ТИМОФЕЙ ТИМОШКИН / РЕЗЮМЕ",
    },
    "it": {
        "name": "TIMOFEY TIMOSHKIN",
        "role": "SVILUPPATORE FRONTEND / SVILUPPATORE DI PRODOTTO",
        "badge": "PRODOTTI WEB<br/>DAL 2018",
        "profile_h": "Profilo",
        "profile": (
            "Sviluppatore frontend e di prodotto con esperienza commerciale. Realizzo prodotti web dal 2018, "
            "dall'idea e dall'MVP fino a un business operativo. Competenze principali in React, Next.js, TypeScript "
            "e architettura frontend. Ho lavorato in team di prodotto organizzati per sprint, gestendo attività in Jira, "
            "facendo code review delle merge request in GitLab e seguendo i rilasci end-to-end."
        ),
        "experience_h": "Esperienza e prodotti",
        "tex_title": "TEXSOFT / startup di prodotto - Lead Product Developer -> Sviluppatore di sistemi informativi web",
        "tex_date": "07.2026 - Presente",
        "tex_bullets": [
            "Entrato nella fase startup come lead product developer, responsabile del lancio zero-to-one, "
            "dell'architettura, delle priorità e della delivery. Dopo il lancio la startup è diventata un'azienda "
            "autonoma; ruolo formale: Sviluppatore di sistemi informativi web.",
            "Realizzato un frontend commerciale di messaggistica real-time con Feature-Sliced Design: Next.js 15, "
            "React 18, TypeScript, TanStack Query e Zustand; messaggi WebSocket, chiamate audio / video LiveKit, "
            "anteprime file e flussi responsive per chat e gruppi.",
            "Lavorato in un ciclo commerciale a sprint: pianificazione e tracciamento in Jira, merge request e code "
            "review in GitLab, test E2E con Playwright, GitLab CI / CD, build Docker multi-stage e coordinamento dei rilasci.",
            "Portato il prodotto da una fase iniziale a un processo di delivery di team ripetibile.",
        ],
        "ind_title": "Prodotti indipendenti - Fondatore / Product Engineer",
        "ind_date": "2024 - Presente",
        "favor_suffix": "(favor.lol -> favor.deals)",
        "favor_bullets": [
            "Trasformata una mini app Web3 di referral in un marketplace attivo per contratti e accordi dentro Telegram: "
            "Next.js, integrazione Telegram, schede contratto, accordi diretti ed escrow, pagine SEO, importazione di "
            "contenuti Telegram e monetizzazione ibrida.",
            "Il progetto di laurea è stato selezionato tra i sei migliori al demo day finale del percorso Startup as a Thesis di ROSBIOTECH (giugno 2025).",
        ],
        "loot_bullets": [
            "Co-realizzato con un partner backend un prodotto Telegram finanziato dalla pubblicità, occupandomi del "
            "frontend Next.js / TypeScript; fino a 3.822 utenti mensili e 2.000 azioni target completate.",
            "Integrato il frontend con un'API Go basata su PostgreSQL / Redis e distribuito tramite Docker / Dokploy; "
            "44,3 mila impressioni di ricerca e 4,5 mila visite in un mese.",
            "Validati acquisizione, monetizzazione pubblicitaria e unit economics con traffico reale e budget personale.",
        ],
        "pilemida": "Sviluppato con un partner il frontend di una Telegram Mini App; il team è passato dall'idea a una release funzionante in 3 giorni.",
        "hostfi_title": "hostfi.app - video in tempo reale",
        "hostfi": "Realizzate videoconferenze con LiveKit client/server SDK: frontend Next.js e servizio LiveKit separato in Docker Compose, con deployment automatico tramite Dokploy.",
        "bbb_title": "Big Balls Birds - Lead Frontend Developer, Telegram Mini App",
        "bbb_date": "Estate 2024",
        "bbb": "Guidato frontend e DevOps in un team di quattro persone, coordinandomi con backend e supporto; prima versione della mini app rilasciata in 2 mesi, con circa $5.000 di ricavi.",
        "png_suffix": " - Sviluppatore frontend / Product Designer, Web3",
        "png_date": "2023 - 2024",
        "png": "Co-realizzata con due partner una piattaforma NFT su Mantle, occupandomi di struttura del prodotto, UI / UX e frontend. Il progetto si è classificato 30° in Mantle Journey e ha ricevuto $25.000; la mia quota è stata di circa $4.300.",
        "ros_title": "ROSBIOTECH - laboratorio di ingegneria e docenza",
        "ros_date": "2023 - 2026",
        "ros_bullets": [
            "Assistente di laboratorio in ingegneria, prototipazione e tecnologie additive; docente di programmazione nel technopark universitario (10.2023 - 07.2024).",
            "Docente part-time presso l'International College of Technology (02.2026 - 03.2026).",
        ],
        "additional": "<b>Esperienza aggiuntiva:</b> web studio - prima esperienza commerciale in team, 2 mesi nell'estate 2019.",
        "skills_h": "Competenze tecniche",
        "skills": [
            ("Frontend principale", "TypeScript, React 18 / 19, Next.js 15 / 16, App Router, SSR / ISR, HTML5, CSS, Tailwind CSS, Vite"),
            ("Architettura frontend", "Feature-Sliced Design (FSD), TanStack Query, Zustand, Zod, React Hook Form, sistemi di componenti, UI / UX responsive"),
            ("UI e integrazioni", "Framer Motion, Three.js / R3F, Recharts, Lottie, REST / OpenAPI, SSE, LiveKit / WebRTC, Telegram Mini Apps, TON / TonConnect"),
            ("Backend di supporto", "Node.js, Go, Prisma / GORM, PostgreSQL, Redis, JWT, cron"),
            ("Delivery e qualità", "Git / GitLab, merge request, code review, Jira, Playwright E2E, GitLab CI / CD, Docker / Compose, Dokploy"),
            ("Workflow con AI", "Piano con Gemini / Antigravity -> revisione e integrazione manuale del piano MD -> implementazione con Codex -> revisione e correzione del git diff -> review indipendente di un agente Codex -> validazione dei rilievi e correzione dei problemi confermati -> apertura della MR"),
        ],
        "education_h": "Formazione",
        "edu_1": "<b>Università Russa di Biotecnologia (ROSBIOTECH)</b> - studi universitari; Favor come progetto di laurea",
        "edu_2_prefix": "<b>Scuola di Programmazione</b>",
        "edu_2_suffix": "- formazione di base",
        "footer": "TIMOFEY TIMOSHKIN / CURRICULUM",
    },
}

OUTPUT_NAMES = {
    ("ru", "dark"): "Тимофей_Тимошкин_Резюме_Тёмное.pdf",
    ("ru", "light"): "Тимофей_Тимошкин_Резюме_Светлое.pdf",
    ("it", "dark"): "Timofey_Timoshkin_Curriculum_Scuro.pdf",
    ("it", "light"): "Timofey_Timoshkin_Curriculum_Chiaro.pdf",
}


def apply_theme(theme: str) -> None:
    if theme == "dark":
        design.BLACK = colors.HexColor("#000000")
        design.WHITE = colors.HexColor("#FFFFFF")
        design.PANEL = design.BLACK
        design.SOFT = design.WHITE
        design.MUTED_DARK = design.WHITE
    elif theme == "light":
        design.BLACK = colors.HexColor("#FFFFFF")
        design.WHITE = colors.HexColor("#000000")
        design.PANEL = design.BLACK
        design.SOFT = design.WHITE
        design.MUTED_DARK = design.WHITE
    else:
        raise ValueError(f"Unknown theme: {theme}")
    design.ACCENT = colors.HexColor("#FF4FBF")
    design.ACCENT_HEX = "#FF4FBF"


def tune_styles(st, lang: str) -> None:
    if lang == "ru":
        st["name"].fontSize = 20.7
        st["name"].leading = 22
        st["role"].fontSize = 7.7
        st["role"].leading = 9.3
        st["header_badge"].fontSize = 8.8
        st["header_badge"].leading = 9.8
        st["body"].fontSize = 7.8
        st["body"].leading = 10.1
        st["body_small"].fontSize = 7.45
        st["body_small"].leading = 9.25
        st["job"].fontSize = 8.2
        st["job"].leading = 10
        st["date"].fontSize = 6.9
        st["subtitle"].fontSize = 7.85
        st["bullet"].fontSize = 7.35
        st["bullet"].leading = 9.25
        st["bullet"].spaceAfter = 0.8
        st["skill_label"].fontSize = 7.05
        st["skill_label"].leading = 8.7
        st["skill_text"].fontSize = 7.05
        st["skill_text"].leading = 8.75
    else:
        st["role"].fontSize = 7.8
        st["role"].leading = 9.3
        st["header_badge"].fontSize = 9.2
        st["header_badge"].leading = 9.9
        st["body"].fontSize = 7.8
        st["body"].leading = 10
        st["body_small"].fontSize = 7.4
        st["body_small"].leading = 9.2
        st["job"].fontSize = 8.15
        st["job"].leading = 9.9
        st["date"].fontSize = 6.8
        st["subtitle"].fontSize = 7.8
        st["bullet"].fontSize = 7.3
        st["bullet"].leading = 9.2
        st["bullet"].spaceAfter = 0.75
        st["skill_label"].fontSize = 6.95
        st["skill_label"].leading = 8.6
        st["skill_text"].fontSize = 6.95
        st["skill_text"].leading = 8.65

def brand_header(st, d):
    left = Table(
        [[Paragraph(d["name"], st["name"])], [Paragraph(d["role"], st["role"])]],
        colWidths=[design.CONTENT_W - 58 * mm],
    )
    left.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 2.2 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 0.5 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5 * mm),
            ]
        )
    )
    table = Table(
        [[left, Paragraph(d["badge"], st["header_badge"])]],
        colWidths=[design.CONTENT_W - 58 * mm, 58 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 0), (0, 0), design.BLACK),
                ("BACKGROUND", (1, 0), (1, 0), design.WHITE),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 0),
                ("TOPPADDING", (0, 0), (0, 0), 0),
                ("BOTTOMPADDING", (0, 0), (0, 0), 0),
                ("LEFTPADDING", (1, 0), (1, 0), 3 * mm),
                ("RIGHTPADDING", (1, 0), (1, 0), 2 * mm),
                ("TOPPADDING", (1, 0), (1, 0), 1.5 * mm),
                ("BOTTOMPADDING", (1, 0), (1, 0), 1.5 * mm),
            ]
        )
    )
    return table


def skill_table(st, rows):
    data = [[Paragraph(label, st["skill_label"]), Paragraph(text, st["skill_text"])] for label, text in rows]
    table = Table(data, colWidths=[42 * mm, design.CONTENT_W - 42 * mm])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (0, -1), design.WHITE),
                ("BACKGROUND", (1, 0), (1, -1), design.PANEL),
                ("LEFTPADDING", (0, 0), (0, -1), 2.8 * mm),
                ("RIGHTPADDING", (0, 0), (0, -1), 2 * mm),
                ("LEFTPADDING", (1, 0), (1, -1), 3 * mm),
                ("RIGHTPADDING", (1, 0), (1, -1), 1 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 1.0 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.0 * mm),
            ]
        )
    )
    return table


def page_callback(footer: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(design.BLACK)
        canvas.rect(0, 0, design.PAGE_W, design.PAGE_H, stroke=0, fill=1)
        canvas.setFont("Segoe-Semibold", 6.8)
        canvas.setFillColor(design.WHITE)
        canvas.drawString(design.MARGIN_X, 6.2 * mm, footer)
        canvas.drawRightString(design.PAGE_W - design.MARGIN_X, 6.2 * mm, f"2026 / {doc.page:02d}")
        canvas.restoreState()

    return draw


def build(lang: str, theme: str) -> None:
    d = DATA[lang]
    apply_theme(theme)
    design.register_fonts()
    st = design.styles()
    tune_styles(st, lang)
    out = design.OUTPUT_DIR / OUTPUT_NAMES[(lang, theme)]
    design.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(out),
        pagesize=(design.PAGE_W, design.PAGE_H),
        leftMargin=design.MARGIN_X,
        rightMargin=design.MARGIN_X,
        topMargin=design.TOP,
        bottomMargin=design.BOTTOM,
        title=f"{d['name']} - {d['role']}",
        author=d["name"],
        subject="Resume",
        creator="ReportLab",
    )

    story = [
        brand_header(st, d),
        Spacer(1, 1.3 * mm),
        design.contact_strip_en(st),
        Spacer(1, 1.7 * mm),
        design.section_heading(d["profile_h"], st),
        Spacer(1, 0.8 * mm),
        design.text_panel_en(d["profile"], st),
        Spacer(1, 1.6 * mm),
        design.section_heading(d["experience_h"], st),
        Spacer(1, 0.9 * mm),
    ]

    story.append(
        KeepTogether(
            [design.job_header(d["tex_title"], d["tex_date"], st)]
            + [design.bullet(text, st) for text in d["tex_bullets"]]
            + [Spacer(1, 1.2 * mm)]
        )
    )

    story.append(
        KeepTogether(
            [
                design.job_header(d["ind_title"], d["ind_date"], st),
                Paragraph(
                    f'<a href="https://favor.deals" color="{design.ACCENT_HEX}"><b>Favor</b></a> {d["favor_suffix"]}',
                    st["subtitle"],
                ),
                *[design.bullet(text, st) for text in d["favor_bullets"]],
                Paragraph(
                    f'<a href="https://loot.gifts" color="{design.ACCENT_HEX}"><b>loot.gifts</b></a>',
                    st["subtitle"],
                ),
                *[design.bullet(text, st) for text in d["loot_bullets"]],
                Paragraph(
                    f'<a href="https://t.me/pilemidabot" color="{design.ACCENT_HEX}"><b>@pilemidabot</b></a>',
                    st["subtitle"],
                ),
                design.bullet(d["pilemida"], st),
                Paragraph(
                    f'<a href="https://hostfi.app" color="{design.ACCENT_HEX}"><b>{d["hostfi_title"]}</b></a>',
                    st["subtitle"],
                ),
                design.bullet(d["hostfi"], st),
                Spacer(1, 0.9 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                design.job_header(d["bbb_title"], d["bbb_date"], st),
                design.bullet(d["bbb"], st),
                Spacer(1, 1.1 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                design.job_header(
                    f'<a href="https://www.youtube.com/watch?v=U0r0Dp_0pFo" color="{design.ACCENT_HEX}">PNG Bazaar</a>{d["png_suffix"]}',
                    d["png_date"],
                    st,
                ),
                design.bullet(d["png"], st),
                Spacer(1, 1.1 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [design.job_header(d["ros_title"], d["ros_date"], st)]
            + [design.bullet(text, st) for text in d["ros_bullets"]]
            + [Spacer(1, 0.8 * mm)]
        )
    )

    story.extend(
        [
            Paragraph(d["additional"], st["body_small"]),
            Spacer(1, 1.4 * mm),
            design.section_heading(d["skills_h"], st),
            skill_table(st, d["skills"]),
            Spacer(1, 1.6 * mm),
            design.section_heading(d["education_h"], st),
        ]
    )

    education = Table(
        [
            [Paragraph(d["edu_1"], st["body_small"]), Paragraph("2020 - 2025", st["date"])],
            [
                Paragraph(
                    f'{d["edu_2_prefix"]} (<a href="https://informatics.ru" color="{design.ACCENT_HEX}">informatics.ru</a>) {d["edu_2_suffix"]}',
                    st["body_small"],
                ),
                Paragraph("2018", st["date"]),
            ],
        ],
        colWidths=[design.CONTENT_W - design.DATE_W, design.DATE_W],
    )
    education.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (0, -1), design.PANEL),
                ("BACKGROUND", (1, 0), (1, -1), design.WHITE),
                ("LEFTPADDING", (0, 0), (0, -1), 2 * mm),
                ("RIGHTPADDING", (0, 0), (0, -1), 1.5 * mm),
                ("LEFTPADDING", (1, 0), (1, -1), 1.5 * mm),
                ("RIGHTPADDING", (1, 0), (1, -1), 1.5 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 0.8 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.8 * mm),
            ]
        )
    )
    story.append(education)

    callback = page_callback(d["footer"])
    doc.build(story, onFirstPage=callback, onLaterPages=callback)
    print(out)


def main() -> None:
    if len(sys.argv) == 3:
        build(sys.argv[1].lower(), sys.argv[2].lower())
        return
    for lang in ("ru", "it"):
        for theme in ("dark", "light"):
            build(lang, theme)


if __name__ == "__main__":
    main()
