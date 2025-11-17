import pandas as pd
from logs.utils import logger

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    if df is None:
        logger.error("No DataFrame provided for transformation")
        return None

    logger.info(f"Starting transformation on {len(df)} rows")

    # 1️⃣ Drop rows with missing values
    initial_rows = len(df)
    df = df.dropna()
    dropped_na = initial_rows - len(df)
    logger.info(f"Dropped {dropped_na} rows with missing values")

    # 2️⃣ Remove duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    dropped_dupes = initial_rows - len(df)
    logger.info(f"Dropped {dropped_dupes} duplicate rows")

    # 3️⃣ Basic validation rules (example for water potability dataset)
    #   - 'pH', 'Hardness', etc. >= 0
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        invalid_rows = df[df[col] < 0].shape[0]
        if invalid_rows > 0:
            df = df[df[col] >= 0]
            logger.info(f"Dropped {invalid_rows} rows with invalid {col} < 0")

    logger.info(f"Transformation complete. {len(df)} rows remaining")
    return df
