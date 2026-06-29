import pandas as pd

price_data = pd.read_csv("nvda_prices.csv", index_col="Date", parse_dates=True)

# daily return = how much % the price moved since yesterday
price_data["Daily Return"] = price_data["Close"].pct_change()

# cumulative return = how much % you'd be up/down since day 1, compounded
price_data["Cumulative Return"] = (1 + price_data["Daily Return"]).cumprod() - 1

print(price_data[["Close", "Daily Return", "Cumulative Return"]])
