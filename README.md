# Supermarket Sales Analytics Platform

A Model to Forecast Seaonality trends in SuperMarket Sales

Clone the repository

Install requirement.txt
Run main.py

## Features

### Time Series Data Analysis & Forcasting 
- **Sales Trend Analysis**: Interactive visualization of daily sales performance
- **Product Performance**: Comprehensive analysis of product line sales and ratings
- **Branch Analytics**: Sales distribution and customer ratings across branches
- **Customer Insights**: Deep dive into customer segments and behavior
- **Sales Forecasting**: 30-day sales predictions with trend analysis
- **Interactive Dashboard**: Web-based interface with responsive design


## Project Structure
```
Supermarket_Sales_Analytics/
├── main.py                
├── data/                  # Data csv storage
├── data_processing.py     

# sales_forecasting/
# ├── data/                      # Data preprocessing
# │   ├── __init__.py
# │   ├── dataset.py
# │   ├── supermarket_sales.csv    #dataset
# │   └── preprocessing.py
# ├── models/                 # adding Neural Network Models 
# │   ├── __init__.py
# │   └── rnn_model.py
# ├── training/
# │   ├── __init__.py
# │   └── trainer.py
# ├── requirements.txt       # Project dependencies
# ├── utils/
# │   ├── __init__.py
# │   └── metrics.py
# └── main.py              # run file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LakshyaTangri/TimeSeries_Forcasting_Supermarket_Sales.git
cd TimeSeries_Forcasting_Supermarket_Sales
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
4. Update the csv file to your data
 
5. Run Main.py

## License
[MIT License](LICENSE)
