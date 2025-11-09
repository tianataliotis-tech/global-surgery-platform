from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd
import sqlalchemy as sa
import os

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///global_surgery.db")
engine = sa.create_engine(DATABASE_URL)

# Initialize API
app = FastAPI(title="Global Surgery Intelligence API")

@app.get("/v1/indicators")
def indicators(
    iso3: str | None = None,
    year: int | None = None,
    indicator_id: str | None = None
):
    """Return indicator values filtered by country, year, or indicator ID."""
    q = """
    SELECT indicator_id, iso3, year, value, unit, source, source_url, license, retrieved_at
    FROM indicator_value
    WHERE 1=1
    """
    params = {}
    if iso3:
        q += " AND iso3 = :iso3"
        params["iso3"] = iso3.upper()
    if year:
        q += " AND year = :year"
        params["year"] = year
    if indicator_id:
        q += " AND indicator_id = :indicator_id"
        params["indicator_id"] = indicator_id

    df = pd.read_sql(q, engine, params=params)
    return JSONResponse(df.to_dict(orient="records"))
