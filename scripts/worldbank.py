import pandas as pd
from pathlib import Path
from functools import lru_cache
from countrynames import to_code_3

root = Path(__file__).parents[1]

@lru_cache(maxsize=200)
def to_code(countryname):
    return to_code_3(countryname)

# Worldbank analysis
wb = pd.read_excel(
    root / "archive/CW_NDC_Content_26062018.xlsx",
    sheet_name=2
)

# Fix missing country name.
wb.loc[wb.CountryCode == "NI", "CountryName"] = "Nicaragua"

# Convert to 3-letter codes from names.
wb.CountryCode = wb.CountryName.apply(to_code)

assert wb.CountryCode.isnull().sum() == 0

wb.to_csv(root / "data/ndc-content-world-bank.csv", index=False)
