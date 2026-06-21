# 1 create a dataframe
import pandas as pd

data = {
    "ticker": ["AAPL", "TSLA", "MSFT", "NVDA"],
    "price": [180.00, 245.00, 425.30, 788.10],
    "qty": [10, 5, 8, 3]
}

df = pd.DataFrame(data)
print(df)

# 2 viewing it
print(df.head())    # first 5 rows
print(df.shape)     # (rows, columns)
print(df.columns)   # column names
print(df.dtypes)    # data type of each column

# 3 reading you real CSV into a DataFrame
df = pd.read_csv("stocks.csv")
print(df)