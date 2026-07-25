import pandas as pd
from database import get_engine


def load_table(table_name):
    engine = get_engine()
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)