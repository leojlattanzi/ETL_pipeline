from src.extract import extract_csv
from src.transform import transform_data
from logs.utils import logger
logger.info("ETL pipeline Started")

extracted = extract_csv()
print(extracted.head())
transform_data(extracted)