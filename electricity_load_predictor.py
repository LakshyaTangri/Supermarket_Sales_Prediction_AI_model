import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import datetime
import matplotlib.pyplot as plt

class ElectricityLoadPredictor:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=42
        )
        self.feature_columns = None

    def preprocess_data(self, df):
        print("Preprocessing data...")
        # Create copy to avoid modifying original data
        df_processed = df.copy()
        
        # Convert Date and Time to datetime features
        df_processed['DateTime'] = pd.to_datetime(df_processed['Date'] + ' ' + df_processed['Time'])
        df_processed['Hour'] = df_processed['DateTime'].dt.hour
        df_processed['DayOfWeek'] = df_processed['DateTime'].dt.dayofweek
        df_processed['Month'] = df_processed['DateTime'].dt.month
        
        # Encode categorical variables
        categorical_columns = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
        for column in categorical_columns:
            if column in df_processed.columns:
                self.label_encoders[column] = LabelEncoder()
                df_processed[column] = self.label_encoders[column].fit_transform(df_processed[column])
        
        # Select features for modeling
        feature_columns = [
            'Branch', 'City', 'Customer type', 'Gender', 'Product line',
            'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Payment',
            'cogs', 'gross margin percentage', 'gross income',
            'Hour', 'DayOfWeek', 'Month'
        ]
        
        # Scale numerical features
        X = self.scaler.fit_transform(df_processed[feature_columns])
        y = df_processed['Rating']
        
        print("Preprocessing complete.")
        self.feature_columns = feature_columns
        return X, y, feature_columns

    def train(self, X, y):
        print("Training model...")
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print("Training complete.")
        return {
            'mse': mse,
            'rmse': np.sqrt(mse),
            'r2': r2,
            'feature_importance': dict(zip(self.feature_columns, self.model.feature_importances_))
        }

    def predict(self, filepath):
        df = pd.read_csv(filepath)
        X, _, _ = self.preprocess_data(df)
        return self.model.predict(X)

if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv('data/supermarket_sales.csv')

    # Create instance of ElectricityLoadPredictor
    predictor = ElectricityLoadPredictor()

    # Preprocess data
    X, y, feature_columns = predictor.preprocess_data(df)

    # Train model
    results = predictor.train(X, y)

    # Print results
    print("Training results:", results)

    # Make predictions on new data
    new_predictions = predictor.predict('data/supermarket_sales.csv')
    print("New predictions:", new_predictions)

    # Plot feature importance
    feature_importance = results['feature_importance']
    sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
    labels, values = zip(*sorted_features)
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.xlabel('Feature')
    plt.ylabel('Importance')
    plt.title('Feature Importance')
    plt.show()
    