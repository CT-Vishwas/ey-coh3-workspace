# generate a function to clean the data
import pandas as pd

def clean_data(df):
    # drop the rows with missing values
    df = df.dropna()
    return df