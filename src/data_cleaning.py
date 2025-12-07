"""
data_cleaning.py

This script loads a raw sales data CSV, applies several cleaning steps,
and writes a cleaned version to data/processed/sales_data_clean.csv.
"""

import os
import pandas as pd


# This function loads the raw sales data from the given file path
# into a pandas DataFrame and checks that the file exists.
def load_data(file_path: str) -> pd.DataFrame:
    """Load raw sales data from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find file at {file_path}")
    df = pd.read_csv(file_path)
    return df


# This function standardizes column names so that they are easier
# to work with in code. It uses lower case, strips spaces, and
# replaces spaces and dashes with underscores.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names."""
    df_copy = df.copy()
    df_copy.columns = (
        df_copy.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df_copy


# This function removes extra spaces from text fields so that
# product names and categories are consistent.
def strip_text_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading and trailing whitespace from text columns."""
    df_clean = df.copy()
    text_columns = df_clean.select_dtypes(include=["object"]).columns
    for col in text_columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()
    return df_clean


# This function handles missing prices and quantities.
# In this example, it drops any row that is missing either value.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with missing price or quantity values."""
    df_clean = df.copy()

    possible_price_columns = ["price", "unit_price", "sale_price"]
    possible_quantity_columns = ["quantity", "qty", "units_sold"]

    price_column = next((c for c in possible_price_columns if c in df_clean.columns), None)
    quantity_column = next((c for c in possible_quantity_columns if c in df_clean.columns), None)

    if price_column is None or quantity_column is None:
        raise KeyError("Could not find expected price or quantity columns in the data.")

    df_clean = df_clean.dropna(subset=[price_column, quantity_column])
    return df_clean


# This function removes rows with clearly invalid numeric values.
# It drops rows that cannot be converted to numbers and removes
# any rows with negative prices or quantities.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with negative or non numeric prices or quantities."""
    df_clean = df.copy()

    possible_price_columns = ["price", "unit_price", "sale_price"]
    possible_quantity_columns = ["quantity", "qty", "units_sold"]

    price_column = next((c for c in possible_price_columns if c in df_clean.columns), None)
    quantity_column = next((c for c in possible_quantity_columns if c in df_clean.columns), None)

    if price_column is None or quantity_column is None:
        raise KeyError("Could not find expected price or quantity columns in the data.")

    # Convert to numeric and drop rows that cannot be converted
    df_clean[price_column] = pd.to_numeric(df_clean[price_column], errors="coerce")
    df_clean[quantity_column] = pd.to_numeric(df_clean[quantity_column], errors="coerce")
    df_clean = df_clean.dropna(subset=[price_column, quantity_column])

    # Remove negative values that do not make sense for sales
    df_clean = df_clean[(df_clean[price_column] >= 0) & (df_clean[quantity_column] >= 0)]

    return df_clean


if __name__ == "__main__":
    # Set paths relative to the project root
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Run the full cleaning pipeline step by step
    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_text_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    # Make sure the output folder exists
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    # Save cleaned data and show a quick preview
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
