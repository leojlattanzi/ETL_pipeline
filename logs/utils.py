import logging
import os

# Make sure logs folder exists
os.makedirs("logs", exist_ok=True)

# Create a named logger
logger = logging.getLogger("etl_logger")
logger.setLevel(logging.INFO)

# Only add handlers if none exist
if not logger.handlers:
    # File handler
    file_handler = logging.FileHandler("logs/etl.log", mode="a")
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(file_formatter)
    logger.addHandler(console_handler)

logger.info("Logger initialized.")

