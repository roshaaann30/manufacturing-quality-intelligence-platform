from pathlib import Path
import pandas as pd


def validate_missing_values(df):
    missing = df.isnull().sum()

    if missing.sum() > 0:
        print("\nMissing Values Found:")
        print(missing[missing > 0])
    else:
        print("✓ No missing values found.")


def validate_duplicates(df):
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        print(f"⚠ Found {duplicates} duplicate rows.")
    else:
        print("✓ No duplicate rows found.")


def validate_numeric_ranges(df):
    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:

        if (df[col] < 0).any():
            print(f"⚠ Negative values found in '{col}'.")

        if "rate" in col.lower() or "score" in col.lower():

            if (df[col] > 100).any():
                print(f"⚠ Values greater than 100 found in '{col}'.")


def validate_dates(df):
    for col in df.columns:

        if "date" in col.lower():

            converted = pd.to_datetime(df[col], errors="coerce")

            if converted.isnull().any():
                print(f"⚠ Invalid dates found in '{col}'.")
            else:
                print(f"✓ '{col}' contains valid dates.")


def validate_duplicate_ids(df):
    for col in df.columns:

        if col.lower().endswith("id"):

            duplicates = df[col].duplicated().sum()

            if duplicates > 0:
                print(f"⚠ Duplicate IDs found in '{col}'.")
            else:
                print(f"✓ '{col}' contains unique IDs.")


def validate_dataset(df):

    print("=" * 60)
    print("Running Dataset Validation")
    print("=" * 60)

    validate_missing_values(df)
    validate_duplicates(df)
    validate_numeric_ranges(df)
    validate_dates(df)
    validate_duplicate_ids(df)

    print("\n✓ Dataset validation completed successfully.")


if __name__ == "__main__":

    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Change this filename to validate another dataset
    FILE_NAME = "supplier_quality.csv"

    FILE_PATH = BASE_DIR / "outputs" / FILE_NAME

    print(f"Reading: {FILE_PATH}")

    try:
        df = pd.read_csv(FILE_PATH)

        validate_dataset(df)

    except FileNotFoundError:
        print(f"\n❌ File not found:\n{FILE_PATH}")

    except Exception as e:
        print(f"\n❌ Validation failed:\n{e}")