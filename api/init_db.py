import sqlite3, pathlib

DB_PATH = pathlib.Path("global_surgery.db")
SCHEMA = pathlib.Path("db/schema.sql")

if not SCHEMA.exists():
    raise SystemExit("db/schema.sql not found")

conn = sqlite3.connect(DB_PATH)
with open(SCHEMA, "r") as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print(f"Initialized {DB_PATH.resolve()} from {SCHEMA}")
