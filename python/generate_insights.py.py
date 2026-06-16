import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)

df = pd.read_sql(
    "SELECT * FROM supplier_quality",
    engine
)

print("=== BUSINESS INSIGHTS ===")

# Top 5 risky suppliers

top_risk = df.sort_values(
    by="defectrate",
    ascending=False
).head(5)

print("\nTop 5 Risky Suppliers")

print(
    top_risk[
        ["suppliername","defectrate"]
    ]
)

# Best supplier region

best_region = df.groupby(
    "supplierregion"
)["defectrate"].mean().idxmin()

print("\nBest Region:")

print(best_region)

# Worst supplier region

worst_region = df.groupby(
    "supplierregion"
)["defectrate"].mean().idxmax()

print("\nWorst Region:")

print(worst_region)

# Highest defect supplier

highest_supplier = df.loc[
    df["defectrate"].idxmax(),
    "suppliername"
]

print("\nHighest Defect Supplier:")

print(highest_supplier)

# Supplier with most units received

top_delivery = df.loc[
    df["unitsreceived"].idxmax(),
    "suppliername"
]

print("\nHighest Delivery Supplier:")

print(top_delivery)


insights = pd.DataFrame({

    "Insight": [

        "Best Region",

        "Worst Region",

        "Highest Defect Supplier",

        "Highest Delivery Supplier"

    ],

    "Value": [

        best_region,

        worst_region,

        highest_supplier,

        top_delivery

    ]

})

insights.to_csv(

    "business_insights.csv",

    index=False

)

print("Business insights created!")