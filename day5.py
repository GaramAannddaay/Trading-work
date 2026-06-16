# 1 ceating a dictionary
stocks = {
    "AAPL" : 175.50,
    "MSFT" : 425.30,
    "TSLA" : 245.80,
    "NVDA" : 788.10
}
print(stocks)

# 2 getting a value
print(stocks["AAPL"])  # 175.50
print(stocks["NVDA"])  # 788.10

# 3  adding and updating
stocks["GOOG"] = 195.40  # add a new ticker
stocks["AAPL"] = 180.00  # update an exisitng price
print(stocks)

# 4 looing through
for ticker, price in stocks.items():
    print(f"{ticker}:${price:.2f}")

# 5 real trading use - store full stock data
portfolio = {
    "AAPL" : {"price": 175.50, "qty":100, "side":"BUY"},
    "MSFT" : {"price": 245.80, "qty":50, "side":"SELL"},
    "TSLA" : {"price": 425.30, "qty":8, "side":"BUY"}
}

for ticker, data in portfolio. items():
    total = data["price"] * data["qty"]
    print(f"{ticker} | {data['side']} | qty: {data['qty']} | total: ${total:.2f}")