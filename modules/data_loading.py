import pandas as pd

def load_data():
    path = 'data/insurance.csv'
    return pd.read_csv(path)
