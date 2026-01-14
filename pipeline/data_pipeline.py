import pandas as pd
import sys

month = sys.argv[1]

df = pd.DataFrame({"Day": [1, 2], "Num_passengers": [3, 4]})
df["Reservation Month"] = month

print(df.head())
df.to_parquet(f"output_month_{sys.argv[1]}.parquet")