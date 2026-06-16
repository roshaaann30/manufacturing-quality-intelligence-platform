import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL details

host = "127.0.0.1"

database = "quality_management"

user = "postgres"

password = "Roshan123"

port = "5432"

# Connect

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

print("Connected successfully!")

# Read supplier_quality table

query = "SELECT * FROM supplier_quality"

df = pd.read_sql(query, engine)

print(df.head())

# Check missing values

missing_values = df.isnull().sum()

print("\nMissing Values")

print(missing_values)

# Check duplicates

duplicates = df.duplicated().sum()

print("\nDuplicate Rows")

print(duplicates)

# Check negative defect rates

negative_defects = (df["defectrate"] < 0).sum()

print("\nNegative Defect Rates")

print(negative_defects)

# Check blank supplier names

blank_names = (df["suppliername"] == "").sum()

print("\nBlank Supplier Names")

print(blank_names)

quality_report = pd.DataFrame({

    "Metric": [

        "Missing Values",

        "Duplicate Rows",

        "Negative Defect Rates",

        "Blank Supplier Names"

    ],

    "Value": [

        missing_values.sum(),

        duplicates,

        negative_defects,

        blank_names

    ]

})

quality_report.to_csv(

    "quality_report.csv",

    index=False

)

print("\nQuality report created!")