"""
Flask application for serving Supermarket Sales Analytics visualizations.
"""

import os
import logging
from flask import Flask, render_template, send_from_directory, abort
from logging.handlers import RotatingFileHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger.addHandler(handler)

app = Flask(__name__)

# Configure the static folder to serve visualization files
app.static_folder = 'visualizations'

# Define visualization metadata
VISUALIZATIONS = [
    {
        'title': 'Daily Sales Trends',
        'description': 'Interactive visualization of daily sales performance over time',
        'url': '/viz/sales_trend.html',
        'icon': '📈'
    },
    {
        'title': 'Product Performance',
        'description': 'Comprehensive analysis of product line sales and customer ratings',
        'url': '/viz/product_performance.html',
        'icon': '📊'
    },
    {
        'title': 'Branch Sales Distribution',
        'description': 'Distribution of sales across different branch locations',
        'url': '/viz/branch_sales.html',
        'icon': '🏪'
    },
    {
        'title': 'Branch Ratings',
        'description': 'Customer satisfaction ratings comparison across branches',
        'url': '/viz/branch_ratings.html',
        'icon': '⭐'
    },
    {
        'title': 'Customer Insights',
        'description': 'Deep dive into customer segments and purchasing behavior',
        'url': '/viz/customer_insights.html',
        'icon': '👥'
    },
    {
        'title': 'Sales Forecast',
        'description': '30-day sales forecast with trend analysis and predictions',
        'url': '/viz/sales_forecast.html',
        'icon': '🔮'
    }
]

@app.route('/')
def index():
    """Render the main dashboard page."""
    try:
        logger.info("Rendering main dashboard")
        return render_template('index.html', visualizations=VISUALIZATIONS)
    except Exception as e:
        logger.error(f"Error rendering dashboard: {str(e)}")
        return "An error occurred while loading the dashboard", 500

@app.route('/viz/<path:filename>')
def serve_visualization(filename):
    """Serve visualization files."""
    try:
        if not os.path.exists(os.path.join('visualizations', filename)):
            logger.warning(f"Visualization file not found: {filename}")
            abort(404)
        
        logger.info(f"Serving visualization: {filename}")
        return send_from_directory('visualizations', filename)
    except Exception as e:
        logger.error(f"Error serving visualization {filename}: {str(e)}")
        return "An error occurred while loading the visualization", 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ensure the visualizations directory exists
    os.makedirs('visualizations', exist_ok=True)
    
    # Create log directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logger.info("Starting Supermarket Sales Analytics web server")
    app.run(debug=True, port=5000)
