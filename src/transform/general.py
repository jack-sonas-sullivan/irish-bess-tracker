import pandas as pd
from pydantic import BaseModel

def pydantic_to_df(pydantic_l: list[BaseModel]) -> pd.DataFrame:
    return pd.DataFrame([record.model_dump() for record in pydantic_l])

def csv_to_df(csv):
    return pd.read_csv(csv)

def xlsx_to_df(csv):
    return pd.read_excel(csv)
