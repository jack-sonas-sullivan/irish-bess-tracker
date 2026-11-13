import pandas as pd

def save_parquet(df, filepath):
    df.to_parquet(filepath, index=False)

def load_parquet(filepath):
    return pd.read_parquet(filepath)