"""
Visualization module for Supermarket Sales Analytics.
This module provides functions to create interactive visualizations using Plotly.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
from typing import Tuple, Dict, Any

# Define color schemes
COLOR_SCHEMES = {
    'primary': 'rgb(55, 83, 109)',
    'secondary': 'rgb(26, 118, 255)',
    'accent': 'rgb(255, 127, 14)',
    'grid': 'lightgray',
    'background': 'white'
}

def create_sales_trend(data: pd.DataFrame) -> go.Figure:
    """Create interactive sales trend visualization.
    
    Args:
        data: DataFrame containing date and total sales columns
        
    Returns:
        Plotly figure object containing the sales trend visualization
    """
    try:
        fig = px.line(data, x='date', y='total',
                    title='Daily Sales Trend Analysis',
                    labels={'total': 'Total Sales ($)', 'date': 'Date'})
        
        fig.update_layout(
            plot_bgcolor=COLOR_SCHEMES['background'],
            paper_bgcolor=COLOR_SCHEMES['background'],
            xaxis=dict(showgrid=True, gridcolor=COLOR_SCHEMES['grid']),
            yaxis=dict(showgrid=True, gridcolor=COLOR_SCHEMES['grid'],
                      tickprefix='$')
        )
        return fig
    except Exception as e:
        print(f"Error creating sales trend visualization: {str(e)}")
        raise

def create_product_performance(data: pd.DataFrame) -> go.Figure:
    """Create product performance visualization with sales and ratings.
    
    Args:
        data: DataFrame containing product performance metrics
        
    Returns:
        Plotly figure object containing the product performance dashboard
    """
    try:
        fig = make_subplots(rows=2, cols=1,
                           subplot_titles=('Product Line Sales', 'Product Line Ratings'),
                           vertical_spacing=0.15)
        
        # Sales by product line
        sales_bar = go.Bar(x=data['product_line'], y=data['total'],
                          name='Total Sales',
                          marker_color=COLOR_SCHEMES['primary'])
        fig.add_trace(sales_bar, row=1, col=1)
        
        # Ratings by product line
        rating_bar = go.Bar(x=data['product_line'], y=data['rating'],
                           name='Average Rating',
                           marker_color=COLOR_SCHEMES['secondary'])
        fig.add_trace(rating_bar, row=2, col=1)
        
        fig.update_layout(
            height=800,
            title_text="Product Line Performance Analysis",
            showlegend=True,
            plot_bgcolor=COLOR_SCHEMES['background'],
            paper_bgcolor=COLOR_SCHEMES['background']
        )
        
        # Update axes
        fig.update_xaxes(showgrid=True, gridcolor=COLOR_SCHEMES['grid'])
        fig.update_yaxes(showgrid=True, gridcolor=COLOR_SCHEMES['grid'])
        
        return fig
    except Exception as e:
        print(f"Error creating product performance visualization: {str(e)}")
        raise

def create_branch_performance(data: pd.DataFrame) -> Tuple[go.Figure, go.Figure]:
    """Create branch performance visualizations.
    
    Args:
        data: DataFrame containing branch performance metrics
        
    Returns:
        Tuple of two Plotly figures: (sales distribution, ratings comparison)
    """
    try:
        # Branch sales distribution
        sales_fig = go.Figure(data=[go.Pie(labels=data['branch'],
                                          values=data['total'],
                                          name='Total Sales',
                                          hole=0.4)])
        sales_fig.update_layout(
            title_text="Branch Sales Distribution",
            showlegend=True,
            paper_bgcolor=COLOR_SCHEMES['background']
        )
        
        # Branch ratings
        ratings_fig = go.Figure(data=[go.Bar(x=data['branch'],
                                            y=data['rating'],
                                            name='Average Rating',
                                            marker_color=COLOR_SCHEMES['secondary'])])
        ratings_fig.update_layout(
            title_text="Branch Customer Ratings",
            showlegend=True,
            plot_bgcolor=COLOR_SCHEMES['background'],
            paper_bgcolor=COLOR_SCHEMES['background'],
            yaxis=dict(title='Average Rating',
                      showgrid=True,
                      gridcolor=COLOR_SCHEMES['grid'])
        )
        
        return sales_fig, ratings_fig
    except Exception as e:
        print(f"Error creating branch performance visualization: {str(e)}")
        raise

def create_customer_insights(data: pd.DataFrame) -> go.Figure:
    """Create customer insights dashboard.
    
    Args:
        data: DataFrame containing customer metrics
        
    Returns:
        Plotly figure object containing the customer insights dashboard
    """
    try:
        fig = make_subplots(rows=1, cols=2,
                           subplot_titles=('Average Transaction by Customer Type',
                                         'Total Sales by Customer Type'))
        
        # Average transaction
        avg_bar = go.Bar(x=data['customer_type'],
                        y=data[('total', 'mean')],
                        name='Average Transaction',
                        marker_color=COLOR_SCHEMES['primary'])
        fig.add_trace(avg_bar, row=1, col=1)
        
        # Total sales
        total_bar = go.Bar(x=data['customer_type'],
                          y=data[('total', 'sum')],
                          name='Total Sales',
                          marker_color=COLOR_SCHEMES['secondary'])
        fig.add_trace(total_bar, row=1, col=2)
        
        fig.update_layout(
            height=500,
            title_text="Customer Segment Analysis",
            showlegend=True,
            plot_bgcolor=COLOR_SCHEMES['background'],
            paper_bgcolor=COLOR_SCHEMES['background']
        )
        
        # Update axes
        fig.update_xaxes(showgrid=True, gridcolor=COLOR_SCHEMES['grid'])
        fig.update_yaxes(showgrid=True, gridcolor=COLOR_SCHEMES['grid'],
                        tickprefix='$')
        
        return fig
    except Exception as e:
        print(f"Error creating customer insights visualization: {str(e)}")
        raise

def create_forecast_plot(actual: pd.Series, forecast: pd.Series) -> go.Figure:
    """Create sales forecast visualization with scatterplot and trend line.
    
    Args:
        actual: Series containing actual sales data
        forecast: Series containing forecasted sales data
        
    Returns:
        Plotly figure object containing the forecast visualization
    """
    try:
        fig = go.Figure()
        
        # Convert datetime index to numeric values for trend calculation
        x_numeric = np.arange(len(actual))
        
        # Calculate trend line using polynomial fit
        z = np.polyfit(x_numeric, actual.values, 2)
        p = np.poly1d(z)
        trend_line = p(x_numeric)
        
        # Calculate R-squared
        correlation_matrix = np.corrcoef(actual.values, trend_line)
        r_squared = correlation_matrix[0,1]**2
        
        # Actual sales as scatter plot
        fig.add_trace(go.Scatter(
            x=actual.index,
            y=actual,
            mode='markers',
            name='Actual Sales',
            marker=dict(
                size=8,
                color=COLOR_SCHEMES['primary'],
                symbol='circle'
            ),
            hovertemplate='Date: %{x}<br>Sales: $%{y:.2f}<br>'
        ))
        
        # Add trend line
        fig.add_trace(go.Scatter(
            x=actual.index,
            y=trend_line,
            mode='lines',
            name=f'Trend Line (R² = {r_squared:.3f})',
            line=dict(
                color=COLOR_SCHEMES['accent'],
                width=2
            ),
            hovertemplate='Date: %{x}<br>Trend: $%{y:.2f}<br>'
        ))
        
        # Forecasted sales as line
        fig.add_trace(go.Scatter(
            x=forecast.index,
            y=forecast,
            mode='lines',
            name='Forecast',
            line=dict(
                color=COLOR_SCHEMES['secondary'],
                width=2,
                dash='dash'
            ),
            hovertemplate='Date: %{x}<br>Forecast: $%{y:.2f}<br>'
        ))
        
        fig.update_layout(
            title={
                'text': 'Sales Forecast Analysis with Trend',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title='Date',
            yaxis_title='Sales ($)',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            ),
            plot_bgcolor=COLOR_SCHEMES['background'],
            paper_bgcolor=COLOR_SCHEMES['background'],
            xaxis=dict(
                showgrid=True,
                gridwidth=1,
                gridcolor=COLOR_SCHEMES['grid']
            ),
            yaxis=dict(
                showgrid=True,
                gridwidth=1,
                gridcolor=COLOR_SCHEMES['grid'],
                tickprefix='$'
            )
        )
        
        return fig
    except Exception as e:
        print(f"Error creating forecast visualization: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    from data_processing import load_data, clean_data, aggregate_sales, customer_segmentation, prepare_time_series
    from forecasting import train_holtwinters, make_forecast, create_future_dates
    
    # Load and process data
    raw_data = load_data("data/supermarket_sales.csv")
    cleaned_data = clean_data(raw_data)
    
    # Generate visualizations
    daily_sales, product_perf, branch_perf = aggregate_sales(cleaned_data)
    customer_metrics = customer_segmentation(cleaned_data)
    time_series_data = prepare_time_series(cleaned_data)
    
    # Create and display plots
    sales_trend = create_sales_trend(daily_sales)
    product_dashboard = create_product_performance(product_perf)
    branch_sales, branch_ratings = create_branch_performance(branch_perf)
    customer_dashboard = create_customer_insights(customer_metrics)
    
    # Create forecast
    model = train_holtwinters(time_series_data['total'])
    forecast = make_forecast(model, 30)
    future_dates = create_future_dates(time_series_data.index[-1], 30)
    forecast_df = pd.DataFrame(forecast, index=future_dates)
    
    forecast_plot = create_forecast_plot(time_series_data['total'], forecast_df)
    
    # Save plots to HTML
    sales_trend.write_html("sales_trend.html")
    product_dashboard.write_html("product_performance.html")
    branch_sales.write_html("branch_sales.html")
    branch_ratings.write_html("branch_ratings.html")
    customer_dashboard.write_html("customer_insights.html")
    forecast_plot.write_html("sales_forecast.html")
