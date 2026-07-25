from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)


def get_engine():
    return create_engine(DATABASE_URL)