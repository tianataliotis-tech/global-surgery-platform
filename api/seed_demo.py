import sqlite3, datetime, pathlib

DB_PATH = pathlib.Path("global_surgery.db")
now = datetime.datetime.utcnow().isoformat()

rows = [
    # indicator_id, iso3, year, value, unit, source, source_url, license
    ("surgical_access_pct", "KEN", 2022, 47.0, "percent", "DEMO", "https://example.org", "CC-BY"),
    ("sao_density",         "KEN", 2022, 0.8,  "per 100k", "DEMO", "https://example.org", "CC-BY"),
    ("surgical_access_pct", "NPL", 2022, 62.0, "percent", "DEMO", "https://example.org", "CC-BY"),
    ("sao_density",         "NPL", 2022, 1.3,  "per 100k", "DEMO", "https://example.org", "CC-BY"),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
for ind, iso3, year, value, unit, source, url, lic in rows:
    cur.execute("""
        INSERT INTO indicator_value (refresh_id, indicator_id, iso3, year, value, unit, source, source_url, license, retrieved_at, method_version)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ("demo-refresh-1", ind, iso3, year, value, unit, source, url, lic, now, "demo-v1"))
conn.commit()
conn.close()
print("Seeded demo rows.")
