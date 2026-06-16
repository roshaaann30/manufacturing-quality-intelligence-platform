import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)

df = pd.read_sql(
    "SELECT * FROM supplier_quality",
    engine
)

print("Total Suppliers:", len(df))

print("Average Defect Rate:", round(df["defectrate"].mean(),2))

print("Average Supplier Rating:", df["supplierrating"].mode()[0])

print("Total Defective Units:", df["defectiveunits"].sum())

print("Total Units Received:", df["unitsreceived"].sum())