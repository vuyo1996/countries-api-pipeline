# Countries API Pipeline

This project extracts country data from the REST Countries API, transforms the JSON responses into a structured Pandas DataFrame, performs data quality checks, and loads the data into PostgreSQL for analysis.

The pipeline captures geographic, demographic, language, and currency information for countries around the world and demonstrates a complete ETL workflow using Python, Pandas, PostgreSQL, and SQL.

## Pipeline Flow

REST Countries API  
→ JSON Response  
→ Python Requests  
→ Pandas DataFrame  
→ Data Validation  
→ PostgreSQL

## Project Structure

```text
countries-api-pipeline/
├── src/
│   └── main.py
├── countries_sql_problems.txt
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

## Technologies Used

- Python
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- python-dotenv
- Python Logging

## Data Collected

The pipeline captures:

- Country Name
- Country Code (CCA3)
- Capital City
- Region
- Subregion
- Population
- Area
- Official Languages
- Official Currencies

## Data Transformation

The API returns nested JSON structures for languages and currencies.

Example:

```json
{
  "languages": {
    "eng": "English",
    "sna": "Shona"
  }
}
```

These values are flattened into comma-separated strings for loading into PostgreSQL and later analysis.

Examples:

```text
English, Shona, Northern Ndebele
```

```text
United States Dollar, Zimbabwe Gold
```

## Data Quality Checks

The pipeline performs:

- Null value checks
- Duplicate row checks
- Record count validation
- DataFrame shape validation
- Data type inspection

## Pipeline Features

- REST API integration using Requests
- JSON transformation and flattening
- Structured logging using Python's `logging` module
- Environment variable management using `python-dotenv`
- PostgreSQL integration using SQLAlchemy
- Automated data validation before loading
- Handling of missing capitals, languages, and currencies

## Database Table

Country data is loaded into the following PostgreSQL table:

```sql
countries
```

### Table Schema

```sql
CREATE TABLE countries (
                        country_code VARCHAR(3) PRIMARY KEY,
                        name VARCHAR(100),
                        capital VARCHAR(100),
                        region VARCHAR(50),
                        subregion VARCHAR(100),
                        population BIGINT,
                        area NUMERIC,
                        languages TEXT,
                        currencies TEXT
                       );
```

## Environment Variables

The project uses a `.env` file to store database credentials.

Required variables:

```text
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```

The `.env` file is excluded from version control and should never be committed to GitHub.

## Example Analysis Questions

The project includes SQL analysis questions such as:

- Which countries have the largest population?
- Which countries have the largest area?
- What is the total population by region?
- Which subregions have the highest average population?
- Which countries have more than one official language?
- Which languages are spoken in the most different countries?
- How many countries are in each region?
- Which countries have the smallest area?
- Which countries have more than one currency?
- Which currencies are used by multiple countries?

## SQL Concepts Demonstrated

- Aggregations
- GROUP BY
- HAVING
- ORDER BY
- String manipulation
- PostgreSQL array functions
- `string_to_array()`
- `unnest()`
- `array_length()`

## Future Improvements

- Normalize languages into a separate table
- Normalize currencies into a separate table
- Create country-language bridge tables
- Create country-currency bridge tables
- Containerize the pipeline with Docker
- Schedule automated runs using Apache Airflow
- Add data quality testing using dbt

## Author

Vuyo M.