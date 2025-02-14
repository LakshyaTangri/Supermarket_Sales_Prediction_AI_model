
import pandas as pd
from electricity_load_predictor import ElectricityLoadPredictor
# Load your data
df = pd.read_csv('data\supermarket_sales.csv')

# Initialize the predictor
predictor = ElectricityLoadPredictor()

# Preprocess data
X, y, feature_columns = predictor.preprocess_data(df)

# Train the model and get evaluation metrics
results = predictor.train(X, y)

# Make predictions on new data
new_predictions = predictor.predict('data\supermarket_sales.csv')