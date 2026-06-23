import pandas as pd

df = pd.read_csv("stocks.csv")

# 1 filtering rows
print(df[df["price"] > 300])

# 2 filtering with multiple conditions
print(df[(df["price"] < 500) & (df["qty"] >=5 )])

# 3 sorting by a column
print(df.sort_values("price"))                      # lowest to highest
print(df.sort_values("price", ascending=False))     # highest to lowest

# 4 adding a new column (total value)
df["total_value"] = df["price"] * df["qty"]
print(df)

# 5 calcualting % return from buy price to current price
df["buy_price"] = [150.00, 200.00, 400.00, 500.00]
df["pct_return"] = (df["price"] - df["buy_price"]) / df["buy_price"] * 100
print(df)

# 6 finding the average
print(df["price"].mean())       # average price
print(df["pct_return"].mean())  # average return across all stocks

# 7 grouping data - average return by sector
df["sector"] = ["tech", "auto", "tech", "tech"]
print(df.groupby("sector")["pct_return"].mean())

# 8 grouping with multiple stats at once
print(df.groupby("sector")["total_value"].sum())
print(df.groupby("sector").agg({"price": "mean", "qty": "sum"}))

# 9 finding the best and worst performer
best = df.loc[df["pct_return"].idxmax()]
worst = df.loc[df["pct_return"].idxmin()]
print("best:\n", best)
print("worst:\n", worst)

# 10 ranking everything from biggest winner to biggest loser
print(df.sort_values("pct_return", ascending=False)[["ticker", "pct_return"]])