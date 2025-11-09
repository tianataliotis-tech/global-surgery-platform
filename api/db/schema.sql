-- Minimal schema for a working demo

CREATE TABLE IF NOT EXISTS dataset_refresh (
  id TEXT PRIMARY KEY,
  source TEXT,
  started_at TEXT,
  finished_at TEXT,
  status TEXT,
  note TEXT
);

CREATE TABLE IF NOT EXISTS indicator_value (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  refresh_id TEXT,
  indicator_id TEXT,
  iso3 CHAR(3),
  year INTEGER,
  value REAL,
  unit TEXT,
  source TEXT,
  source_url TEXT,
  license TEXT,
  retrieved_at TEXT,
  method_version TEXT
);
