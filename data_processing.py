import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load supermarket sales data."""
    data = pd.read_csv(file_path, parse_dates=["Date"])
    return data

def clean_data(data):
    """Clean and preprocess the data."""
    # Clean column names
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Convert date and time columns
    data['datetime'] = pd.to_datetime(data['date'].astype(str) + ' ' + data['time'].astype(str))
    
    # Calculate additional features
    data['month'] = data['date'].dt.month
    data['day_of_week'] = data['date'].dt.dayofweek
    data['hour'] = pd.to_datetime(data['time']).dt.hour
    
    # Calculate profit
    data['profit'] = data['gross_income']
    
    return data

def aggregate_sales(data):
    """Create various sales aggregations."""
    # Daily sales
    daily_sales = data.groupby('date')['total'].sum().reset_index()
    
    # Product line performance
    product_performance = data.groupby('product_line').agg({
        'quantity': 'sum',
        'total': 'sum',
        'profit': 'sum',
        'rating': 'mean'
    }).reset_index()
    
    # Branch performance
    branch_performance = data.groupby('branch').agg({
        'total': 'sum',
        'profit': 'sum',
        'rating': 'mean'
    }).reset_index()
    
    return daily_sales, product_performance, branch_performance

def customer_segmentation(data):
    """Perform customer segmentation based on spending patterns."""
    customer_metrics = data.groupby('customer_type').agg({
        'total': ['mean', 'sum'],
        'quantity': 'mean',
        'rating': 'mean'
    }).reset_index()
    
    return customer_metrics

def prepare_time_series(data):
    """Prepare time series data for forecasting."""
    daily_sales = data.groupby('date')['total'].sum().reset_index()
    daily_sales.set_index('date', inplace=True)
    daily_sales = daily_sales.sort_index()
    
    return daily_sales

if __name__ == "__main__":
    # Example Usage
    file_path = "data/supermarket_sales.csv"
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    daily_sales, product_performance, branch_performance = aggregate_sales(cleaned_data)
    customer_metrics = customer_segmentation(cleaned_data)
    time_series_data = prepare_time_series(cleaned_data)
    print(daily_sales)
    print(product_performance)
    print(branch_performance)
    print(customer_metrics)
    print(time_series_data)
