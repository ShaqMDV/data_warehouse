import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost:0800/warehouse')

with engine.connect() as conn:
    conn.execute("""
    CREATE SCHEMA IF NOT EXISTS dw;
    CREATE TABLE IF NOT EXISTS dw.customers (
                 customer_id SERIAL PRIMARY KEY,
                 name VARCHAR(100),
                 email VARCHAR(100),
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)