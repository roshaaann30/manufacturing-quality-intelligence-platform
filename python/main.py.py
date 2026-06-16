import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)

query = "SELECT * FROM supplier_quality"

df = pd.read_sql(query, engine)

print(df.head())