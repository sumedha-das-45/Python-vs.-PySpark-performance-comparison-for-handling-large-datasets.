import pandas as pd
import numpy as np

def generate_csv(file_path="large_dataset.csv", num_rows=1_000_000):
    np.random.seed(42)
    data = {
        "id": np.arange(num_rows),
        "age": np.random.randint(18, 70, size=num_rows),
        "salary": np.random.randint(30000, 150000, size=num_rows),
        "department": np.random.choice(['HR', 'Engineering', 'Sales', 'Marketing'], size=num_rows)
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Dataset of {num_rows} rows saved to {file_path}")

generate_csv()
