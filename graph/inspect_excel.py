import pandas as pd

FILE = "data/Topology Master_updated(3).xlsx"

xls = pd.ExcelFile(FILE)

print("\nSheets:")
print(xls.sheet_names)

print("\n" + "="*80)

for sheet in xls.sheet_names:

    print(f"\nSHEET: {sheet}")

    df = pd.read_excel(FILE, sheet_name=sheet)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\n" + "="*80)
