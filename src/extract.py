import pandas as pd
import os
from logs.utils import logger

def extract_csv(file_path="data/water_potability.csv"):
    abs_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        logger.error(f"CSV file not found: {abs_path}")
        return None

    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns from {abs_path}")
        return df
    except Exception as e:
        logger.error(f"Failed to read CSV {abs_path}: {e}")
        return None