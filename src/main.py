import logging
import os
from datetime import datetime
from urllib.parse import quote_plus

import pandas as pd
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", None)

logging.basicConfig(
                      level=logging.INFO,
                      format="%(asctime)s - %(levelname)s - %(message)s"
                   ) 

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
                         f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
                      )

url = (
         "https://restcountries.com/v3.1/all"
         "?fields=name,cca3,capital,region,subregion,"
         "population,area,languages,currencies"
      )

response = requests.get(url)
response.raise_for_status()

data = response.json()

print("\n")

countries_info = []

for country in data:

    languages = country.get("languages", {})
    language_names = ", ".join(languages.values()) if languages else None

    currencies = country.get("currencies", {})
    currency_names = ", ".join(currency["name"].title() for currency in currencies.values()) if currencies else None

    country_info = {
                      "name": country["name"]["common"],
                      "country_code": country["cca3"],
                      "capital": country["capital"][0] if "capital" in country and country["capital"] else None,
                      "region": country["region"],
                      "subregion": country["subregion"],
                      "population": country["population"],
                      "area": country["area"],
                      "languages": language_names,
                      "currencies": currency_names                       
                   }
                       
    countries_info.append(country_info)

countries_df = pd.DataFrame(countries_info)

logging.info(f"Countries DataFrame created with {len(countries_df)} countries.")

print("\n")

logging.info(f"DataFrame shape: {countries_df.shape}")

print("\n")

null_counts = countries_df.isnull().sum()
logging.info(f"Null values in each column:\n{null_counts}")

print("\n")

duplicate_counts = countries_df.duplicated().sum()
logging.info(f"Duplicate rows:\n{duplicate_counts}")

print("\n")

logging.info("First 5 rows of the DataFrame:")
print(countries_df.head())

print("\n")

countries_df.info()

print("\n")

logging.info(f"\n{countries_df.describe()}")

countries_df.to_sql("countries", 
                    engine, 
                    if_exists="append", 
                    index=False)

print("\n")

logging.info("Data successfully inserted into the 'countries' table in the database.")