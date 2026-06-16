# 1 Basic if/else
price = 150.00
if price > 100:
    print("BUY signal")
else:
    print("WAIT")

# 2 if / elif / else (multiple conditions)
price = 95
if price > 200:
    print("Strong BUY")
elif price > 100:
    print("BUY")
elif price > 50:
    print("HOLD")
else:
    print("SELL")

# 3 combining conditions with and / or
price = 180
volume = 5000

if price > 100 and volume > 1000:
    print("Strong BUY")
else:
    print("No Signal")

# 4 checking ticker + price together
ticker = "TSLA"
price = 245.80

if ticker == "TSLA" and price < 250:
    print(f"BUY {ticker} - undervalued")
elif ticker == "TSLA" and price >= 250:
    print(f"WAIT on {ticker} - too expensive")

# 5 looping with if - scan a list of stocks
stocks = {"AAPL" : 175.50, "TSLA" : 245.80, "MSFT" : 90.00, "NVDA": 788.10}
for ticker, price in stocks.items():
    if price < 100:
        print(f"{ticker}: CHEAP - consider BUY")
    elif price > 500:
        print(f"{ticker}: EXPENSIVE - consider WAIT")
    else:
        print(f"{ticker}: NORMAL range")