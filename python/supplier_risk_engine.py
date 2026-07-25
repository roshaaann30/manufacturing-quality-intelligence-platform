import pandas as pd


def calculate_risk_score(df):

    df = df.copy()

    score = (
        df["DefectRate"] * 0.5
        + (100 - df["SupplierRating"]) * 0.3
        + (df["DefectiveUnits"] / df["UnitsReceived"] * 100) * 0.2
    )

    df["CalculatedRiskScore"] = score.round(2)

    conditions = [
        df["CalculatedRiskScore"] >= 50,
        df["CalculatedRiskScore"] >= 25
    ]

    categories = [
        "High",
        "Medium"
    ]

    df["RiskCategory"] = "Low"

    df.loc[conditions[1], "RiskCategory"] = "Medium"
    df.loc[conditions[0], "RiskCategory"] = "High"

    return df