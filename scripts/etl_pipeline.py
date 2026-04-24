import pandas as pd
import numpy as np
import os


def extract_data(path):
    """Extract data from CSV file."""
    return pd.read_csv(path, encoding="latin-1")


def transform_data(df):
    """Clean and transform the dataset."""

    # Drop unnecessary columns
    df = df.drop(
        ['url', 'phone', 'address', 'reviews_list', 'menu_item', 'dish_liked'],
        axis=1
    )

    # Clean 'rate' column
    df['rate'] = df['rate'].replace(['NEW', '-'], np.nan)
    df['rate'] = df['rate'].str.replace('/5', '', regex=False)
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

    # Clean 'approx_cost(for two people)' column
    df['approx_cost(for two people)'] = df['approx_cost(for two people)'] \
        .str.replace(',', '', regex=False)
    df['approx_cost(for two people)'] = pd.to_numeric(
        df['approx_cost(for two people)'], errors='coerce'
    )

    # Handle missing values
    df['rate'] = df['rate'].fillna(df['rate'].mean())
    df['location'] = df['location'].fillna(df['location'].mode()[0])
    df['cuisines'] = df['cuisines'].fillna('Unknown')
    df['rest_type'] = df['rest_type'].fillna('Unknown')
    df['approx_cost(for two people)'] = df['approx_cost(for two people)'] \
        .fillna(df['approx_cost(for two people)'].median())

    # Clean column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('(', '', regex=False)
    df.columns = df.columns.str.replace(')', '', regex=False)
    df.columns = df.columns.str.lower()

    # Encode categorical variables
    df['online_order'] = df['online_order'].map({'Yes': 1, 'No': 0})
    df['book_table'] = df['book_table'].map({'Yes': 1, 'No': 0})

    # Simplify categorical text columns
    df['rest_type'] = df['rest_type'].apply(
        lambda x: x.split(',')[0] if isinstance(x, str) else x
    )
    df['cuisines'] = df['cuisines'].apply(
        lambda x: x.split(',')[0] if isinstance(x, str) else x
    )

    return df


def load_data(df, output_path):
    """Save cleaned data to CSV."""
    df.to_csv(output_path, index=False)


def run_pipeline():
    """Run full ETL pipeline."""

    current_dir = os.path.dirname(__file__)

    input_path = os.path.join(
        current_dir, "..", "data", "raw", "zomato.csv"
    )

    output_path = os.path.join(
        current_dir, "..", "data", "processed", "cleaned_data.csv"
    )

    # Execute pipeline steps
    df = extract_data(input_path)
    df_cleaned = transform_data(df)
    load_data(df_cleaned, output_path)

    print("ETL pipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()
