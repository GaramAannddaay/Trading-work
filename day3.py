# 1 creating strings - stock ticker and tradi info
ticker = "AAPL"
side = "BUY"
price = 182.50
qty = 100
print(ticker, side, price, qty)

# 2 combining strings (concatenation & f-strings)
message = "order: " + ticker + " " + side
print(message)

# f-strings (cleaner)
message = f"order: {ticker} {side} {qty} @ ${price}"
print(message)

# 3 string formatting - clean price display
price = 1234.5678
print(f"price: ${price:.2f}") # price: $1234.57
print(f"ticker: {ticker:<10}|") # left align in 10 chars
print(f"ticker: {ticker:>10}|") # right aling in 10 chars

# 4 string methods - cleaning and checking ticker input
raw = " aapl "
clean = raw.strip().upper()
print(clean)       # AAPL
print(clean.startswith("A"))  # True
print(len(clean))     #4

tickers = "AAPL, TSLA, MSFT, NVDA"
print(tickers.split(","))   # ['AAPL', 'TSLA', 'MSFT', 'NVDA']

# 5 finding characters - parsing a trade signal string
signal = "signal:BUY:TSLA:qty=50:price=250.00"

print(signal.find("TSLA"))    # index where TSLA starts
print("BUY" in signal)     # True
print("SELL" in signal)    #False

parts = signal.split(".")
print(parts)
# ["signal', "BUY', 'TSLA', 'QTY=50', 'price=250.00']

action =  parts[1]
stock = parts[2]
print(f"action: {action}, stock: {stock}")   # action: BUY, stock: TSLA