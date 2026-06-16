import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)

query = """
SELECT
suppliername,
supplierregion,
supplierrating,
componenttype,
month,
defectrate,
defectiveunits,
unitsreceived
FROM supplier_quality
"""

df = pd.read_sql(query, engine)

df.to_csv("supplier_performance.csv", index=False)

print("CSV file created successfully!")