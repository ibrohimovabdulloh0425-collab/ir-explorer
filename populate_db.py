"""Davlatlar bazasini lokal countries.json + IR intel qatlami orqali to'ldiradi."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from country_intel import enrich

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "countries.db"
JSON_PATH = BASE_DIR / "countries.json"

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cca2 TEXT,
    cca3 TEXT,
    capital TEXT,
    region TEXT,
    subregion TEXT,
    population INTEGER,
    area REAL,
    flag_png TEXT,
    lat REAL,
    lng REAL
)
"""

EXTRA_COLS = [
    ("gdp_usd", "REAL"),
    ("gdp_per_capita", "REAL"),
    ("government", "TEXT"),
    ("leader", "TEXT"),
    ("visa_type", "TEXT"),
    ("rel_uz", "TEXT"),
    ("rel_us", "TEXT"),
    ("rel_eu", "TEXT"),
    ("stability_score", "INTEGER"),
    ("stability_note", "TEXT"),
]


def load_countries() -> list[dict]:
    if not JSON_PATH.exists():
        raise FileNotFoundError(
            f"{JSON_PATH.name} topilmadi. Avval generate_countries_json.py ni ishga tushiring."
        )
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("countries.json bo'sh yoki noto'g'ri formatda.")
    return data


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.execute(SCHEMA_SQL)
    conn.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS idx_countries_cca3 ON countries(cca3)"
    )
    existing = {row[1] for row in conn.execute("PRAGMA table_info(countries)")}
    for name, typ in EXTRA_COLS:
        if name not in existing:
            conn.execute(f"ALTER TABLE countries ADD COLUMN {name} {typ}")
    conn.commit()


def upsert_countries(conn: sqlite3.Connection, countries: list[dict]) -> None:
    sql = """
        INSERT INTO countries (
            name, cca2, cca3, capital, region, subregion,
            population, area, flag_png, lat, lng,
            gdp_usd, gdp_per_capita, government, leader, visa_type,
            rel_uz, rel_us, rel_eu, stability_score, stability_note
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(cca3) DO UPDATE SET
            name=excluded.name,
            cca2=excluded.cca2,
            capital=excluded.capital,
            region=excluded.region,
            subregion=excluded.subregion,
            population=excluded.population,
            area=excluded.area,
            flag_png=excluded.flag_png,
            lat=excluded.lat,
            lng=excluded.lng,
            gdp_usd=excluded.gdp_usd,
            gdp_per_capita=excluded.gdp_per_capita,
            government=excluded.government,
            leader=excluded.leader,
            visa_type=excluded.visa_type,
            rel_uz=excluded.rel_uz,
            rel_us=excluded.rel_us,
            rel_eu=excluded.rel_eu,
            stability_score=excluded.stability_score,
            stability_note=excluded.stability_note
    """
    rows = []
    for c in countries:
        if not c.get("cca3"):
            continue
        info = enrich(c)
        rows.append(
            (
                c.get("name"),
                c.get("cca2"),
                c.get("cca3"),
                c.get("capital"),
                c.get("region"),
                c.get("subregion"),
                c.get("population"),
                c.get("area"),
                c.get("flag_png"),
                c.get("lat"),
                c.get("lng"),
                info["gdp_usd"],
                info["gdp_per_capita"],
                info["government"],
                info["leader"],
                info["visa_type"],
                info["rel_uz"],
                info["rel_us"],
                info["rel_eu"],
                info["stability_score"],
                info["stability_note"],
            )
        )
    conn.executemany(sql, rows)
    conn.commit()


def main() -> None:
    countries = load_countries()
    conn = sqlite3.connect(DB_PATH)
    try:
        ensure_schema(conn)
        upsert_countries(conn, countries)
        total = conn.execute("SELECT COUNT(*) FROM countries").fetchone()[0]
    finally:
        conn.close()

    print("=" * 60)
    print(f"Lokal {JSON_PATH.name} dan {len(countries)} ta yozuv o'qildi.")
    print(f"'{DB_PATH.name}' bazasida jami {total} ta davlat bor (IR maydonlari yangilandi).")
    print("=" * 60)


if __name__ == "__main__":
    main()
