import pandas as pd
import os

def extract_data(path):
    data = pd.read_csv(path)
    return data


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "..", "data", "raw", "zomato.csv")

data = extract_data(file_path)

cleaned_data = data.head()

print(cleaned_data)