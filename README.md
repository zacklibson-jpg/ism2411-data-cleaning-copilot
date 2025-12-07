# ism2411 data cleaning copilot

This project is for ISM 2411 at the University of South Florida. The goal is to clean a small sales data set and save a cleaner version that is easier to use.

## Project structure

* data/raw contains the original messy CSV file from Canvas named sales_data_raw.csv
* data/processed will contain the cleaned CSV file named sales_data_clean.csv after you run the script
* src/data_cleaning.py contains the Python code that does the cleaning
* reflection.md contains a short written reflection 

## Cleaning steps

The script does the following:

1. Loads the raw CSV file into a pandas DataFrame  
2. Standardizes column names to use lower case and underscores  
3. Strips extra spaces from text fields such as product names and categories  
4. Drops rows that are missing price or quantity values  
5. Converts price and quantity columns to numeric types and removes rows that have negative values  

## How to run

From the project root folder run this command in a terminal:

```bash
python src/data_cleaning.py
