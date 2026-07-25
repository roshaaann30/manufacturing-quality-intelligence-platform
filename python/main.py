from data_loader import load_table
from supplier_risk_engine import calculate_risk_score


def main():

    supplier_quality = load_table("supplier_quality")

    supplier_quality = calculate_risk_score(supplier_quality)

    print(supplier_quality.head())

    print("\nRisk Category Distribution")
    print(supplier_quality["RiskCategory"].value_counts())


if __name__ == "__main__":
    main()