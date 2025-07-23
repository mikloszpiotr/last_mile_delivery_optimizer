
import pandas as pd

def optimize_route(df: pd.DataFrame):
    return df.sort_values(by="distance_km").reset_index(drop=True)
