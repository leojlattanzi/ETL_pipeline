# Water Potability ETL Pipeline

This project is an **ETL (Extract, Transform, Load) pipeline** for cleaning, validating, and loading water potability data into a PostgreSQL database. It also saves both cleaned and rejected rows as CSV files for auditing purposes.

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup](#setup)  
- [Usage](#usage)  
- [ETL Flow](#etl-flow)  
- [Database Schema](#database-schema)  
- [Logging](#logging)  
- [Output](#output)  
- [Future Improvements](#future-improvements)  

---

## Project Structure

ETL_pipeline/
├── src/
│ ├── extract.py # Extracts CSV data
│ ├── transform.py # Cleans and validates data
│ ├── load.py # Loads cleaned & rejected data into PostgreSQL
├── logs/
│ └── utils.py # Logging utility
├── data/
│ └── water_potability.csv
├── output/
│ ├── cleaned_rows.csv
│ └── rejected_rows.csv
├── main.py # Runs the ETL pipeline
├── README.md
├── requirements.txt


