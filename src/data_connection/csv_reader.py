import pandas as pd

def get_csv_data(path):
    df = pd.read_csv(path)
    return df

