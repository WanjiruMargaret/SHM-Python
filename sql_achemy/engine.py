from sqlalchemy import create_engine
from sqlalchemy.engine import URL

db_credentials={
    "drivername":"postgresql+psycopg",
    "host":"aws-1-ca-central-1.pooler.supabase.com",
    "username":"postgres.lpwoghnqcukxvfrmckpi",
    "password":"E5pbzMbhbazxbsTx",
    "port":5432,
    "database":"postgres"
}

#Build DB URL
DATABASE_URL=URL.create(**db_credentials)

#create engine
engine=create_engine(DATABASE_URL,echo=True,future=True)

with engine.connect() as conn:
    result = conn.execute("SELECT *FROM employee")
    rows=result.fetchone()
