import pandas as pd

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath, sep=';', low_memory=False, na_values='?')
    df.dropna(inplace=True)
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
    df.drop(columns=['Date', 'Time'], inplace=True)
    df = df.astype(float, errors='ignore')
    df.sort_values('Datetime', inplace=True)
    return df
