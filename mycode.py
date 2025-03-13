import pandas as pd
import os

people = {
    "Name": ["John Doe", "Alice Smith", "Bob Johnson"],
    "Age": [30, 25, 40],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(people)

data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")

