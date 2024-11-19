import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

def train_holtwinters(data, seasonal_periods=7):
    """
    Train Holt-Winters model for sales forecasting.
    
    Args:
        data: Time series data with date index
        seasonal_periods: Number of periods in a season (default: 7 for weekly seasonality)
    """
    model = ExponentialSmoothing(
        data,
        seasonal_periods=seasonal_periods,
        trend='add',
        seasonal='add',
    )
    fitted_model = model.fit()
    return fitted_model

def make_forecast(model, periods):
    """Generate forecast for specified number of periods."""
    forecast = model.forecast(periods)
    return forecast

def evaluate_forecast(actual, predicted):
    """Calculate forecast accuracy metrics."""
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape
    }

def create_future_dates(last_date, periods):
    """Create future dates for forecasting."""
    date_range = pd.date_range(
        start=last_date + pd.Timedelta(days=1),
        periods=periods,
        freq='D'
    )
    return date_range

if __name__ == "__main__":
    # Example usage
    from data_processing import load_data, clean_data, prepare_time_series
    
    # Load and prepare data
    raw_data = load_data("data/supermarket_sales.csv")
    cleaned_data = clean_data(raw_data)
    time_series_data = prepare_time_series(cleaned_data)
    
    # Train model
    model = train_holtwinters(time_series_data['total'])
    
    # Make forecast
    forecast_periods = 30
    forecast = make_forecast(model, forecast_periods)
    
    # Create future dates
    future_dates = create_future_dates(time_series_data.index[-1], forecast_periods)
    
    # Create forecast DataFrame
    forecast_df = pd.DataFrame({
        'date': future_dates,
        'forecast': forecast
    }).set_index('date')
    
    print("Forecast for next 30 days:")
    print(forecast_df)
