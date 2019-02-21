import pandas as pd
from pathlib import Path
from functools import lru_cache
from countrynames import to_code_3

root = Path(__file__).parents[1]

@lru_cache(maxsize=200)
def to_code(countryname):
    return to_code_3(countryname)


# CAIT data
cait = pd.read_excel(
    root / "archive/CW_NDC_Content_26062018.xlsx",
    sheet_name=1
)

cait.to_csv(root / "data/ndc-content-cait.csv", index=False)
