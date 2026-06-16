import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Roshan123@127.0.0.1:5432/quality_management"
)

df = pd.read_sql(
    "SELECT * FROM supplier_quality",
    engine
)

# Risk Score Formula

df["risk_score"] = (
    df["defectrate"] * 0.6
    + (df["defectiveunits"]/1000) * 0.4
)

# Risk Category

df["risk_category"] = "Low"

df.loc[df["risk_score"] > 5, "risk_category"] = "Medium"

df.loc[df["risk_score"] > 8, "risk_category"] = "High"

print(
    df[
        [
            "suppliername",
            "risk_score",
            "risk_category"
        ]
    ].head()
)

df.to_csv("supplier_risk_analysis.csv", index=False)

print("Risk analysis completed")