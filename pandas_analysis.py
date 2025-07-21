import pandas as pd
import time

start = time.time()
df = pd.read_csv("large_dataset.csv")

#Simple processing: filter and group
filtered = df[df["age"] > 30]
agg = filtered.groupby("department")["salary"].mean()

print("Pandas Result:")
print(agg)

print(f"Pandas processing time: {time.time() - start:.2f} seconds")
