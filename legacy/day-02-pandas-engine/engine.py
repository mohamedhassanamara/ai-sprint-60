import pandas as pd
import numpy as np

def process_data():
    # Read both CSVs
    users = pd.read_csv('users.csv')
    transactions = pd.read_csv('transactions.csv')

    # The Merge: Left Join keeping all transactions
    df = pd.merge(transactions, users, on='user_id', how='left')

    # Missing Value Imputation
    df['region'] = df['region'].fillna("Unknown")
    df['amount'] = df['amount'].fillna(df['amount'].median())

    # Datetime Parsing (The Trap): Convert join_date and tx_date to proper Pandas datetime objects
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
    df['tx_date'] = pd.to_datetime(df['tx_date'], errors='coerce')

    # Vectorized Feature Engineering
    df['discount_eligible'] = (df['amount'] > 200) & (df['status'] == 'completed')

    # Complex Aggregation: Group by region
    regional_metrics = df.groupby('region').agg(
        total_revenue=('amount', 'sum'),
        unique_users=('user_id', 'nunique')
    ).reset_index()

    # Export: Save to JSON
    regional_metrics.to_json('regional_metrics.json', orient='records', indent=4)

if __name__ == '__main__':
    process_data()
