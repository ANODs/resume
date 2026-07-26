from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from resume_base import (
    BOTTOM,
    MARGIN_X,
    OUTPUT_DIR,
    PAGE_H,
    PAGE_W,
    TOP,
    register_fonts,
)


OUTPUT_PDF = OUTPUT_DIR / "Timofey_Timoshkin_Resume_Dark.pdf"

BLACK = colors.HexColor("#000000")
WHITE = colors.HexColor("#FFFFFF")
PANEL = BLACK
SOFT = WHITE
MUTED_DARK = WHITE
ACCENT = colors.HexColor("#FF4FBF")
ACCENT_HEX = "#FF4FBF"
CONTENT_W = PAGE_W - 2 * MARGIN_X
DATE_W = 35 * mm


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "DarkName",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=22.5,
            leading=23.5,
            textColor=WHITE,
            tracking=0.1,
        ),
        "role": ParagraphStyle(
            "DarkRole",
            parent=base["Normal"],
            fontName="Segoe-Semibold",
            fontSize=9.1,
            leading=10.5,
            textColor=WHITE,
            tracking=0.8,
        ),
        "header_badge": ParagraphStyle(
            "HeaderBadge",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=10.3,
            leading=10.8,
            textColor=BLACK,
            tracking=0.2,
        ),
        "contact": ParagraphStyle(
            "DarkContact",
            parent=base["Normal"],
            fontName="Segoe-Semibold",
            fontSize=7.15,
            leading=8.4,
            textColor=WHITE,
            alignment=1,
            linkUnderline=False,
        ),
        "section": ParagraphStyle(
            "DarkSection",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=8.35,
            leading=9.2,
            textColor=BLACK,
            tracking=0.7,
        ),
        "body": ParagraphStyle(
            "DarkBody",
            parent=base["Normal"],
            fontName="Segoe",
            fontSize=8.25,
            leading=10.65,
            textColor=WHITE,
            spaceAfter=1,
        ),
        "body_small": ParagraphStyle(
            "DarkBodySmall",
            parent=base["Normal"],
            fontName="Segoe",
            fontSize=7.8,
            leading=9.8,
            textColor=WHITE,
        ),
        "job": ParagraphStyle(
            "DarkJob",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=8.85,
            leading=10.7,
            textColor=WHITE,
        ),
        "date": ParagraphStyle(
            "DarkDate",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=7.25,
            leading=9,
            textColor=BLACK,
            alignment=TA_RIGHT,
        ),
        "subtitle": ParagraphStyle(
            "DarkSubtitle",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=8.15,
            leading=9.8,
            textColor=ACCENT,
            spaceBefore=0.5,
            spaceAfter=1,
        ),
        "bullet": ParagraphStyle(
            "DarkBullet",
            parent=base["Normal"],
            fontName="Segoe",
            fontSize=7.8,
            leading=9.9,
            textColor=SOFT,
            leftIndent=9,
            firstLineIndent=-6,
            bulletIndent=0,
            spaceAfter=1.15,
        ),
        "skill_label": ParagraphStyle(
            "DarkSkillLabel",
            parent=base["Normal"],
            fontName="Segoe-Bold",
            fontSize=7.5,
            leading=9.3,
            textColor=BLACK,
        ),
        "skill_text": ParagraphStyle(
            "DarkSkillText",
            parent=base["Normal"],
            fontName="Segoe",
            fontSize=7.45,
            leading=9.35,
            textColor=WHITE,
        ),
    }


def brand_header_en(st):
    left = Table(
        [
            [Paragraph("TIMOFEY TIMOSHKIN", st["name"])],
            [Paragraph("FRONTEND ENGINEER / PRODUCT DEVELOPER", st["role"])],
        ],
        colWidths=[CONTENT_W - 58 * mm],
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
    header = Table(
        [[left, Paragraph("WEB PRODUCTS<br/>SINCE 2018", st["header_badge"])]],
        colWidths=[CONTENT_W - 58 * mm, 58 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 0), (0, 0), BLACK),
                ("BACKGROUND", (1, 0), (1, 0), WHITE),
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
    return header


def contact_strip_en(st):
    contacts = [
        ("TELEGRAM / @TTIMOSHKIN", "https://t.me/ttimoshkin"),
        ("GITHUB / ANODS", "https://github.com/ANODs"),
        ("TIMOSHKIN.DEV", "https://timoshkin.dev"),
        ("FAVOR.DEALS", "https://favor.deals"),
    ]
    row = [Paragraph(f'<a href="{url}" color="{ACCENT_HEX}">{label}</a>', st["contact"]) for label, url in contacts]
    table = Table([row], colWidths=[CONTENT_W / 4] * 4)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PANEL),
                ("TOPPADDING", (0, 0), (-1, -1), 1.1 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1 * mm),
                ("LEFTPADDING", (0, 0), (-1, -1), 1 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 1 * mm),
            ]
        )
    )
    return table


def section_heading(text: str, st):
    table = Table([[Paragraph(text.upper(), st["section"])]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                ("LEFTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 0.55 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.55 * mm),
            ]
        )
    )
    return table


def text_panel_en(text: str, st):
    table = Table([[Paragraph(text, st["body"])]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PANEL),
                ("LEFTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 1.2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
            ]
        )
    )
    return table


def bullet(text: str, st) -> Paragraph:
    return Paragraph(f"<bullet>+</bullet>{text}", st["bullet"])


def job_header(left: str, right: str, st, widths=None):
    widths = widths or (CONTENT_W - DATE_W, DATE_W)
    table = Table([[Paragraph(left, st["job"]), Paragraph(right, st["date"])]], colWidths=list(widths))
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 0), (0, 0), BLACK),
                ("BACKGROUND", (1, 0), (1, 0), WHITE),
                ("LEFTPADDING", (0, 0), (0, 0), 1.8 * mm),
                ("RIGHTPADDING", (0, 0), (0, 0), 1.5 * mm),
                ("LEFTPADDING", (1, 0), (1, 0), 1.5 * mm),
                ("RIGHTPADDING", (1, 0), (1, 0), 1.5 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 0.55 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.55 * mm),
            ]
        )
    )
    return table


def skill_table_en(st):
    rows = [
        (
            "Core frontend",
            "TypeScript, React 18 / 19, Next.js 15 / 16, App Router, SSR / ISR, HTML5, CSS, Tailwind CSS, Vite",
        ),
        (
            "Frontend architecture",
            "Feature-Sliced Design (FSD), TanStack Query, Zustand, Zod, React Hook Form, component systems, responsive UI / UX",
        ),
        (
            "UI and integrations",
            "Framer Motion, Three.js / R3F, Recharts, Lottie, REST / OpenAPI, SSE, LiveKit / WebRTC, Telegram Mini Apps, TON / TonConnect",
        ),
        (
            "Supporting backend",
            "Node.js, Go, Prisma / GORM, PostgreSQL, Redis, JWT, cron",
        ),
        (
            "Delivery and quality",
            "Git / GitLab, merge requests, code review, Jira, Playwright E2E, GitLab CI / CD, Docker / Compose, Dokploy",
        ),
        (
            "AI-assisted workflow",
            "Gemini / Antigravity plan -> refine the MD plan -> Codex implementation -> review and fix the git diff -> "
            "independent Codex agent review -> validate its findings and fix confirmed issues -> open MR",
        ),
    ]
    data = [[Paragraph(label, st["skill_label"]), Paragraph(text, st["skill_text"])] for label, text in rows]
    table = Table(data, colWidths=[42 * mm, PAGE_W - 2 * MARGIN_X - 42 * mm])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (0, -1), WHITE),
                ("BACKGROUND", (1, 0), (1, -1), PANEL),
                ("LEFTPADDING", (0, 0), (0, -1), 2.8 * mm),
                ("RIGHTPADDING", (0, 0), (0, -1), 2 * mm),
                ("LEFTPADDING", (1, 0), (1, -1), 3 * mm),
                ("RIGHTPADDING", (1, 0), (1, -1), 1 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 1.15 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.15 * mm),
            ]
        )
    )
    return table


def on_page_en(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(BLACK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setFont("Segoe-Semibold", 6.8)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN_X, 6.2 * mm, "TIMOFEY TIMOSHKIN / RESUME")
    canvas.drawRightString(PAGE_W - MARGIN_X, 6.2 * mm, f"2026 / {doc.page:02d}")
    canvas.restoreState()


def build_en() -> None:
    register_fonts()
    st = styles()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Timofey Timoshkin - Frontend / Product Engineer",
        author="Timofey Timoshkin",
        subject="Resume",
        creator="ReportLab",
    )

    story = [
        brand_header_en(st),
        Spacer(1, 1.3 * mm),
        contact_strip_en(st),
        Spacer(1, 1.7 * mm),
        section_heading("Profile", st),
        Spacer(1, 0.8 * mm),
        text_panel_en(
            "Frontend engineer and product developer with commercial experience. Building web products since 2018, "
            "taking them from zero to MVP and an operating business. Core expertise in React, Next.js, TypeScript "
            "and frontend architecture. Worked in sprint-based product teams, managed Jira tasks, reviewed merge "
            "requests in GitLab and shipped products end-to-end.",
            st,
        ),
        Spacer(1, 1.6 * mm),
        section_heading("Experience and products", st),
        Spacer(1, 0.9 * mm),
    ]

    story.append(
        KeepTogether(
            [
                job_header(
                    "TEXSOFT / product startup - Lead Product Developer -> Web Information Systems Developer",
                    "07.2025 - 07.2026",
                    st,
                ),
                bullet(
                    "Joined at the startup stage as lead product developer, owning zero-to-one launch, architecture, "
                    "prioritization and delivery. After launch, the startup became a standalone company; formal role: "
                    "Web Information Systems Developer.",
                    st,
                ),
                bullet(
                    "Built a commercial real-time messaging frontend with Feature-Sliced Design: Next.js 15, React 18, "
                    "TypeScript, TanStack Query and Zustand; WebSocket messaging, LiveKit audio / video calls, file "
                    "previews and responsive chat and group flows.",
                    st,
                ),
                bullet(
                    "Worked in a commercial sprint cycle: planning and tracking in Jira, merge requests and code "
                    "reviews in GitLab, Playwright E2E tests, GitLab CI / CD, multi-stage Docker builds and release "
                    "coordination.",
                    st,
                ),
                bullet(
                    "Took the product from an early stage to a repeatable team delivery process and concluded the "
                    "engagement after the startup became a standalone company.",
                    st,
                ),
                Spacer(1, 1.2 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                job_header("Independent products - Founder / Product Engineer", "2024 - Present", st),
                Paragraph(
                    f'<a href="https://favor.deals" color="{ACCENT_HEX}"><b>Favor</b></a> '
                    "(favor.lol -> favor.deals)",
                    st["subtitle"],
                ),
                bullet(
                    "Evolved a Web3 referral mini app into a live marketplace for contracts and deals inside Telegram: "
                    "Next.js, Telegram integration, contract cards, direct and escrow deals, SEO pages, Telegram content "
                    "import and hybrid monetization.",
                    st,
                ),
                bullet(
                    "The graduation project was selected among the top six projects at the final demo day of the "
                    "Startup as a Thesis track at ROSBIOTECH (June 2025).",
                    st,
                ),
                Paragraph(f'<a href="https://loot.gifts" color="{ACCENT_HEX}"><b>loot.gifts</b></a>', st["subtitle"]),
                bullet(
                    "Co-built an ad-supported Telegram product with a backend partner, owning the Next.js / TypeScript "
                    "frontend; reached up to 3,822 monthly users and 2,000 completed target actions.",
                    st,
                ),
                bullet(
                    "Integrated the frontend with a Go API backed by PostgreSQL / Redis and shipped through Docker / "
                    "Dokploy; generated 44.3K search impressions and 4.5K visits in one month.",
                    st,
                ),
                bullet(
                    "Validated acquisition, ad monetization and unit economics with real traffic and my own budget.",
                    st,
                ),
                Paragraph("<b>@pilemidabot</b>", st["subtitle"]),
                bullet(
                    "Built the Telegram Mini App frontend with a partner; the team moved from concept to a working "
                    "release in 3 days.",
                    st,
                ),
                Paragraph(
                    f'<a href="https://hostfi.app" color="{ACCENT_HEX}"><b>hostfi.app - realtime video</b></a>',
                    st["subtitle"],
                ),
                bullet(
                    "Built video conferencing with LiveKit client/server SDK: Next.js frontend and a separate LiveKit "
                    "service in Docker Compose, with automated deployment through Dokploy.",
                    st,
                ),
                Spacer(1, 0.9 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                job_header("Big Balls Birds - Lead Frontend Developer, Telegram Mini App", "Summer 2024", st),
                bullet(
                    "Led frontend and DevOps in a four-person team, coordinating with backend and support; shipped the "
                    "first mini app version in 2 months, with approximately $5,000 in project revenue.",
                    st,
                ),
                Spacer(1, 1.1 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                job_header(
                    f'<a href="https://www.youtube.com/watch?v=U0r0Dp_0pFo" color="{ACCENT_HEX}">PNG Bazaar</a>'
                    " - Frontend Developer / Product Designer, Web3",
                    "2023 - 2024",
                    st,
                ),
                bullet(
                    "Co-built an NFT creation platform on Mantle with two partners, owning product structure, UI / UX "
                    "and frontend delivery. The product placed 30th in Mantle Journey and received a $25,000 project "
                    "payout; personal share was approximately $4,300.",
                    st,
                ),
                Spacer(1, 1.1 * mm),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                job_header("ROSBIOTECH - engineering lab and teaching", "2023 - 2026", st),
                bullet(
                    "Laboratory assistant in engineering, prototyping and additive technologies; taught programming "
                    "at the university technopark (10.2023 - 07.2024).",
                    st,
                ),
                bullet(
                    "Part-time instructor at the International College of Technology (02.2026 - 03.2026).",
                    st,
                ),
                Spacer(1, 0.8 * mm),
            ]
        )
    )

    story.extend(
        [
            Paragraph(
                "<b>Additional experience:</b> web studio - first commercial team experience, 2 months in summer 2019.",
                st["body_small"],
            ),
            Spacer(1, 1.4 * mm),
            section_heading("Technical skills", st),
            skill_table_en(st),
            Spacer(1, 1.6 * mm),
            section_heading("Education", st),
        ]
    )

    education = Table(
        [
            [
                Paragraph("<b>Russian Biotechnological University (ROSBIOTECH)</b> - university studies; Favor graduation project", st["body_small"]),
                Paragraph("2020 - 2025", st["date"]),
            ],
            [
                Paragraph(
                    f'<b>School of Programmers</b> (<a href="https://informatics.ru" color="{ACCENT_HEX}">informatics.ru</a>) - foundational training',
                    st["body_small"],
                ),
                Paragraph("2018", st["date"]),
            ],
        ],
        colWidths=[CONTENT_W - DATE_W, DATE_W],
    )
    education.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (0, -1), PANEL),
                ("BACKGROUND", (1, 0), (1, -1), WHITE),
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

    doc.build(story, onFirstPage=on_page_en, onLaterPages=on_page_en)
    print(OUTPUT_PDF)


if __name__ == "__main__":
    build_en()
