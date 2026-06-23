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

# 4 filtering rows
expensive = df[df["price"]>300]
print(expensive)

cheap_and_many = df[(df["price"] < 300) & (df["qty"] > 5)]
print(cheap_and_many)

# 5 basic statistics
df["total"] = df["price"] * df["qty"]
print(df)

print(df["price"].mean())       # avergae price
print(df["price"].max())        # highest price
print(df["price"].min())        # lowest price
print(df["total"].sum())        # total value of all holdings
print(df.describe())            # count, mean, min, max, etc all at once
