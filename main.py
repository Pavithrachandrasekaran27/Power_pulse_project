from src.data_preprocessing import load_and_preprocess_data
from src.feature_engineering import add_time_features
from src.model_training import train_model
from src.visualize import plot_correlations

def main():
    filepath = 'data/household_power_consumption.txt'
    df = load_and_preprocess_data(filepath)
    df = add_time_features(df)
    plot_correlations(df)
    model, metrics = train_model(df)
    print("Model Evaluation Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

if __name__ == "__main__":
    main()
