from data_loader import load_table, load_supplier_summary
from supplier_risk_engine import calculate_risk_score


def main():
    # Load supplier quality data
    supplier_quality = load_table("supplier_quality")

    # Calculate supplier risk score
    supplier_quality = calculate_risk_score(supplier_quality)

    print("=" * 60)
    print("SUPPLIER QUALITY DATA")
    print("=" * 60)
    print(supplier_quality.head())

    print("\nTotal Records:", len(supplier_quality))

    print("\nRisk Category Distribution")
    print("-" * 60)
    print(supplier_quality["RiskCategory"].value_counts())

    print("\nSupplier Summary by Region")
    print("-" * 60)

    summary = load_supplier_summary()
    print(summary)


if __name__ == "__main__":
    main()