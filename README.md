# Supermarket Sales Analytics Platform

A comprehensive data analytics solution that transforms supermarket sales data into actionable business insights through advanced preprocessing, forecasting, and interactive visualization techniques.

## Features

### 1. Data Analysis & Visualization
- **Sales Trend Analysis**: Interactive visualization of daily sales performance
- **Product Performance**: Comprehensive analysis of product line sales and ratings
- **Branch Analytics**: Sales distribution and customer ratings across branches
- **Customer Insights**: Deep dive into customer segments and behavior
- **Sales Forecasting**: 30-day sales predictions with trend analysis
- **Interactive Dashboard**: Web-based interface with responsive design

### 2. Technical Features
- Advanced data preprocessing and cleaning
- Time series analysis and forecasting
- Interactive visualizations with Plotly
- Polynomial trend line analysis with R-squared values
- Comprehensive error handling and logging
- Responsive web interface using Flask and Tailwind CSS

## Project Structure
```
Supermarket_Sales_Analytics/
├── app.py                 # Flask web application
├── data_processing.py     # Data preprocessing and analysis
├── visualization.py       # Visualization generation
├── requirements.txt       # Project dependencies
├── logs/                  # Application logs
├── data/                  # Data storage
├── visualizations/        # Generated visualization files
└── templates/            # HTML templates
    ├── index.html        # Dashboard template
    ├── 404.html         # Not found error page
    └── 500.html         # Server error page
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd Supermarket_Sales_Analytics
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python -m flask run
```

2. Access the dashboard at `http://localhost:5000`

## Features in Detail

### Visualization Components
- **Sales Trends**: 
  - Daily sales performance tracking
  - Polynomial trend line analysis
  - R-squared value calculation
  - Interactive hover information

- **Product Analysis**:
  - Product line performance metrics
  - Customer rating analysis
  - Sales distribution patterns

- **Branch Performance**:
  - Comparative branch analysis
  - Geographic sales distribution
  - Customer satisfaction metrics

### Technical Implementation
- **Error Handling**:
  - Comprehensive exception management
  - User-friendly error pages
  - Detailed error logging

- **Data Processing**:
  - Automated data cleaning
  - Missing value handling
  - Time series preprocessing

- **Visualization Engine**:
  - Interactive Plotly graphs
  - Responsive design
  - Consistent color schemes
  - Custom hover templates

## Dependencies
- Flask: Web framework
- Plotly: Interactive visualizations
- Pandas: Data manipulation
- NumPy: Numerical computations
- Scipy: Scientific computations
- Tailwind CSS: Frontend styling

## Error Handling
- Comprehensive logging system with rotation
- User-friendly error pages (404, 500)
- Detailed error tracking and reporting
- Automated error notification system

## Future Improvements
- [ ] Advanced forecasting models
- [ ] Additional interactive features
- [ ] Enhanced data export options
- [ ] Real-time data processing
- [ ] Advanced user authentication
- [ ] Custom visualization themes

## Contributing
Contributions are welcome! Please feel free to submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
