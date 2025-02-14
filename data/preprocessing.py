import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
    def prepare_data(self, df):
        # Convert date and time to datetime
        df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df = df.sort_values('datetime')
        
        # Create time-based features
        df['hour'] = df['datetime'].dt.hour
        df['day_of_week'] = df['datetime'].dt.dayofweek
        df['day_of_month'] = df['datetime'].dt.day
        df['month'] = df['datetime'].dt.month
        
        # Encode categorical variables
        categorical_cols = ['Branch', 'City', 'Customer type', 'Gender', 
                          'Product line', 'Payment']
        
        for col in categorical_cols:
            le = LabelEncoder()
            df[col + '_encoded'] = le.fit_transform(df[col])
            self.label_encoders[col] = le
        
        # Select features for model
        feature_cols = ['hour', 'day_of_week', 'day_of_month', 'month',
                       'Branch_encoded', 'City_encoded', 'Customer type_encoded',
                       'Gender_encoded', 'Product line_encoded', 'Payment_encoded',
                       'Unit price', 'Quantity', 'Tax 5%', 'cogs', 'rating']
        
        # Scale features
        features_scaled = self.scaler.fit_transform(df[feature_cols])
        target_scaled = self.scaler.fit_transform(df[['gross income']])
        
        return features_scaled, target_scaled