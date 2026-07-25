from data_loader import load_table


def main():

    supplier_quality = load_table("supplier_quality")

    print("\nSupplier Quality Dataset")
    print("-" * 50)
    print(supplier_quality.head())

    print(f"\nTotal Records: {len(supplier_quality)}")


if __name__ == "__main__":
    main()