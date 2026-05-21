# generate a function to read the raw data from the csv file and return a pandas dataframe
import pandas as pd
def read_raw_data(file_path):
    print(f"Reading raw data from {file_path}...")
    df = pd.read_csv(file_path)
    return df