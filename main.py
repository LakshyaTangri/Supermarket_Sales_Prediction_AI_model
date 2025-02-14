import torch
from torch.utils.data import DataLoader
from data.dataset import SupermarketDataset
from models.rnn_model import SupermarketRNN
from training.trainer import ModelTrainer

def main(csv_path='data\supermarket_sales.csv'):
    # Create datasets
    train_dataset = SupermarketDataset(csv_path, seq_length=7, train=True)
    val_dataset = SupermarketDataset(csv_path, seq_length=7, train=False)
    
    # Create dataloaders
    batch_size = 32
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    
    # Initialize model
    input_size = train_dataset.get_feature_dim()
    hidden_size = 128
    model = SupermarketRNN(input_size, hidden_size)
    
    # Train model
    trainer = ModelTrainer(model)
    trained_model = trainer.train(train_loader, val_loader)
    
    return trained_model

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Train sales forecasting model')
    parser.add_argument('--csv_path', type=str, default='data\supermarket_sales.csv',
                      help='Path to the CSV file containing sales data')
    args = parser.parse_args()
    
    model = main(args.csv_path)