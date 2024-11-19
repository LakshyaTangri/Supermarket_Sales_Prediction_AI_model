import os
import pandas as pd
from data_processing import load_data, clean_data, aggregate_sales, customer_segmentation, prepare_time_series
from forecasting import train_holtwinters, make_forecast, create_future_dates, evaluate_forecast
from visualization import (create_sales_trend, create_product_performance,
                         create_branch_performance, create_customer_insights,
                         create_forecast_plot)

def main():
    # Create output directory for visualizations
    output_dir = "visualizations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load and process data
    print("Loading and processing data...")
    file_path = os.path.join(os.path.dirname(__file__), "data", "supermarket_sales.csv")
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    
    # Generate analytics
    print("Generating analytics...")
    daily_sales, product_perf, branch_perf = aggregate_sales(cleaned_data)
    customer_metrics = customer_segmentation(cleaned_data)
    time_series_data = prepare_time_series(cleaned_data)
    
    # Create forecast
    print("Generating sales forecast...")
    model = train_holtwinters(time_series_data['total'])
    forecast_periods = 30
    forecast = make_forecast(model, forecast_periods)
    future_dates = create_future_dates(time_series_data.index[-1], forecast_periods)
    forecast_df = pd.DataFrame(forecast, index=future_dates)
    
    # Create visualizations
    print("Creating visualizations...")
    sales_trend = create_sales_trend(daily_sales)
    product_dashboard = create_product_performance(product_perf)
    branch_sales, branch_ratings = create_branch_performance(branch_perf)
    customer_dashboard = create_customer_insights(customer_metrics)
    forecast_plot = create_forecast_plot(time_series_data['total'], forecast_df)
    
    # Save visualizations
    print("Saving visualizations...")
    sales_trend.write_html(os.path.join(output_dir, "sales_trend.html"))
    product_dashboard.write_html(os.path.join(output_dir, "product_performance.html"))
    branch_sales.write_html(os.path.join(output_dir, "branch_sales.html"))
    branch_ratings.write_html(os.path.join(output_dir, "branch_ratings.html"))
    customer_dashboard.write_html(os.path.join(output_dir, "customer_insights.html"))
    forecast_plot.write_html(os.path.join(output_dir, "sales_forecast.html"))
    
    print("\nAnalysis complete! Visualization files have been created in the 'visualizations' directory:")
    print("1. sales_trend.html - Daily sales trends")
    print("2. product_performance.html - Product line performance analysis")
    print("3. branch_sales.html - Branch sales distribution")
    print("4. branch_ratings.html - Branch ratings comparison")
    print("5. customer_insights.html - Customer segmentation analysis")
    print("6. sales_forecast.html - 30-day sales forecast")

if __name__ == "__main__":
    main()
