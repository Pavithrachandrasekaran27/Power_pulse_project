def add_time_features(df):
    df['hour'] = df['Datetime'].dt.hour
    df['day'] = df['Datetime'].dt.day
    df['month'] = df['Datetime'].dt.month
    df['year'] = df['Datetime'].dt.year
    df['weekday'] = df['Datetime'].dt.weekday
    return df
