import json
import re
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "countries.db"
INDEX_PATH = BASE_DIR / "index.html"
NEWS_PATH = BASE_DIR / "news_analysis.json"

COUNTRY_COLS = """
    id, name, cca2, cca3, capital, region, subregion,
    population, area, flag_png, lat, lng,
    gdp_usd, gdp_per_capita, government, leader, visa_type,
    rel_uz, rel_us, rel_eu, stability_score, stability_note
"""

TOPIC_RULES = [
    ("sanksiya", "Sanksiyalar"),
    ("sud", "Huquq / sud"),
    ("prezident", "Siyosat"),
    ("hukumat", "Siyosat"),
    ("diplom", "Diplomatiya"),
    ("iqtisod", "Iqtisod"),
    ("dollar", "Valyuta"),
    ("bank", "Moliya"),
    ("tadbirkor", "Biznes"),
    ("urush", "Xavfsizlik"),
    ("qotillik", "Xavfsizlik"),
    ("openai", "Texnologiya"),
    ("chatgpt", "Texnologiya"),
]

app = FastAPI(title="IR Explorer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_connection() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise HTTPException(
            status_code=503,
            detail="countries.db topilmadi. Avval populate_db.py ni ishga tushiring.",
        )
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def analyze_article(title: str, text: str) -> dict:
    raw = text or ""
    parts = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    body_parts = [
        p
        for p in parts
        if "kun.uz" not in p.lower() and "Guvohnoma" not in p and len(p) > 80
    ]
    if not body_parts:
        body_parts = parts[1:] if len(parts) > 1 else parts
    summary = " ".join(body_parts[:2])[:520]
    if len(summary) == 520:
        summary = summary.rsplit(" ", 1)[0] + "…"
    blob = f"{title} {summary}".lower()
    tags = []
    for key, label in TOPIC_RULES:
        if key in blob and label not in tags:
            tags.append(label)
    if not tags:
        tags = ["Xalqaro yangilik"]
    if any(k in blob for k in ("sanksiya", "urush", "qotillik", "tergov", "qiynoq")):
        impact = "Yuqori"
        tone = "Geosiyosiy taranglik / huquqiy bosim"
    elif any(k in blob for k in ("iqtisod", "dollar", "tadbirkor", "invest")):
        impact = "O'rta"
        tone = "Iqtisodiy va ishbilarmonlik oqibatlari"
    else:
        impact = "O'rta"
        tone = "Axborot muhiti va tashqi siyosat konteksti"
    return {"summary": summary or (title or ""), "tags": tags[:3], "impact": impact, "tone": tone}


@app.get("/api/health")
def check_health():
    count = 0
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        try:
            count = conn.execute("SELECT COUNT(*) FROM countries").fetchone()[0]
        except sqlite3.Error:
            count = -1
        finally:
            conn.close()
    return {
        "status": "ok",
        "message": "IR Explorer FastAPI Backend tayyor!",
        "countries": count,
    }


@app.get("/api/countries")
def get_countries(region: str | None = None, visa: str | None = None, q: str | None = None):
    conn = get_db_connection()
    try:
        sql = f"SELECT {COUNTRY_COLS} FROM countries WHERE 1=1"
        params: list = []
        if region:
            sql += " AND region = ?"
            params.append(region)
        if visa:
            sql += " AND visa_type = ?"
            params.append(visa)
        if q:
            sql += " AND (name LIKE ? OR capital LIKE ? OR cca3 LIKE ?)"
            like = f"%{q}%"
            params.extend([like, like, like])
        sql += " ORDER BY name"
        rows = conn.execute(sql, params).fetchall()
    except sqlite3.Error as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        conn.close()

    countries = [dict(row) for row in rows]
    return {"status": "success", "count": len(countries), "data": countries}


@app.get("/api/countries/{cca3}")
def get_country(cca3: str):
    conn = get_db_connection()
    try:
        row = conn.execute(
            f"SELECT {COUNTRY_COLS} FROM countries WHERE cca3 = ? COLLATE NOCASE",
            (cca3,),
        ).fetchone()
    finally:
        conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Davlat topilmadi")
    return {"status": "success", "data": dict(row)}


@app.get("/api/news")
def get_news():
    if not NEWS_PATH.exists():
        return {"generated_at": None, "results": []}
    payload = json.loads(NEWS_PATH.read_text(encoding="utf-8"))
    results = []
    for item in payload.get("results") or []:
        analysis = analyze_article(item.get("title") or "", item.get("text") or "")
        results.append({**item, "analysis": analysis})
    return {"generated_at": payload.get("generated_at"), "results": results}


@app.get("/")
def serve_index():
    if not INDEX_PATH.exists():
        raise HTTPException(status_code=404, detail="index.html topilmadi")
    return FileResponse(INDEX_PATH)
