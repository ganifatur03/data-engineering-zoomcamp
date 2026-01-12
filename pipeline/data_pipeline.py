import pandas as pd
import sys

mode = sys.argv[1]

if mode == "web":
    print("Process web data")
elif mode == "youtube":
    print("Process youtube data")

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())