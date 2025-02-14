import pandas as pd
import torch
from torch.utils.data import Dataset
from sklearn.preprocessing import StandardScaler, LabelEncoder

class SupermarketDataset(Dataset):
    def __init__(self, csv_path, seq_length=7, train=True):
        """
        Initialize dataset from CSV file
        
        Args:
            csv_path (str): Path to the CSV file
            seq_length (int): Number of time steps to use for sequence
            train (bool): If True, use 80% of data for training, else use 20% for validation
        """
        self.seq_length = seq_length
        
        # Load and preprocess data
        self.df = self._load_and_preprocess('data\supermarket_sales.csv')
        
        # Split data into train/val
        split_idx = int(len(self.df) * 0.8)
        if train:
            self.df = self.df[:split_idx]
        else:
            self.df = self.df[split_idx:]
        
        # Prepare features and target
        self.features = self.df[self.feature_cols].values
        self.target = self.df['gross income'].values
        
    def __len__(self):
        return len(self.df) - self.seq_length
        
    def __getitem__(self, idx):
        x = self.features[idx:idx + self.seq_length]
        y = self.target[idx + self.seq_length]
        return torch.FloatTensor(x), torch.FloatTensor([y])
    
    def _load_and_preprocess(self, csv_path):
        """Load and preprocess the CSV data"""
        df = pd.read_csv(csv_path)
        
        # Convert date and time to datetime
        df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df = df.sort_values('datetime').reset_index(drop=True)
        
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
        
        # Define feature columns
        self.feature_cols = ['hour', 'day_of_week', 'day_of_month', 'month',
                           'Branch_encoded', 'City_encoded', 'Customer type_encoded',
                           'Gender_encoded', 'Product line_encoded', 'Payment_encoded',
                           'Unit price', 'Quantity', 'Tax 5%', 'cogs', 'Rating']
        
        # Scale numerical features
        scaler = StandardScaler()
        df[self.feature_cols] = scaler.fit_transform(df[self.feature_cols])
        df['gross income'] = scaler.fit_transform(df[['gross income']])
        
        return df
    
    def get_feature_dim(self):
        """Return the number of input features"""
        return len(self.feature_cols)