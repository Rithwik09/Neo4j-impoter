import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Excel file path
FILE = BASE_DIR / "data" / "Topology Master_updated.xlsx"

print(f"\nReading file: {FILE}")

# Load workbook
xls = pd.ExcelFile(FILE)

print("\nSheets:")
print(xls.sheet_names)

print("\n" + "=" * 80)

for sheet in xls.sheet_names:

    print(f"\nSHEET: {sheet}")

    df = pd.read_excel(FILE, sheet_name=sheet)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\n" + "=" * 80)
