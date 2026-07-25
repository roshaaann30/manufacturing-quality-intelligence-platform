import pandas as pd
from database import get_engine


def load_table(table_name, columns=None):
    engine = get_engine()

    if columns:
        query = f"""
        SELECT {', '.join(columns)}
        FROM {table_name}
        """
    else:
        query = f"SELECT * FROM {table_name}"

    return pd.read_sql(query, engine)


def load_supplier_summary():
    engine = get_engine()

    query = """
    SELECT
        SupplierRegion,
        COUNT(*) AS Suppliers,
        AVG(DefectRate) AS AvgDefectRate,
        AVG(SupplierRating) AS AvgSupplierRating
    FROM supplier_quality
    GROUP BY SupplierRegion
    ORDER BY AvgDefectRate DESC;
    """

    return pd.read_sql(query, engine)